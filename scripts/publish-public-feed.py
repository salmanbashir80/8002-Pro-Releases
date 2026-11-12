"""Publish public release metadata to the CDN; credentials stay in the publishing environment."""
import argparse
import base64
import json
import pathlib
import re
import subprocess

REPO = 'salmanbashir80/8002-Pro-Releases'
TAG = re.compile(r'v\d+\.\d+\.\d+(?:[-+][A-Za-z0-9._-]+)?')
NAME = re.compile(r'8002CleanUp-Pro(?:-[A-Za-z0-9._-]+)?\.apk')
DIGEST = re.compile(r'sha256:[a-fA-F0-9]{64}')

def snapshot(rows):
    if not isinstance(rows, list):
        raise ValueError('Expected the public GitHub release list')
    result = []
    for row in rows:
        if not isinstance(row, dict) or row.get('draft') is not False:
            continue
        tag = row.get('tag_name', '')
        if not isinstance(tag, str) or not TAG.fullmatch(tag):
            continue
        assets = []
        for asset in row.get('assets', []):
            if not isinstance(asset, dict):
                continue
            name, size = asset.get('name', ''), asset.get('size')
            if (not isinstance(name, str) or not NAME.fullmatch(name)
                or asset.get('state') != 'uploaded' or not isinstance(size, int)
                or not 1_000_000 < size < 150_000_000
                or not isinstance(asset.get('digest'), str) or not DIGEST.fullmatch(asset['digest'])
                or asset.get('browser_download_url') != f'https://github.com/{REPO}/releases/download/{tag}/{name}'):
                continue
            assets.append({k: asset[k] for k in ('name', 'state', 'size', 'digest', 'browser_download_url')})
        if not assets:
            continue
        result.append({'tag_name': tag, 'draft': False, 'prerelease': row.get('prerelease') is True,
                       'name': str(row.get('name') or tag)[:150], 'body': str(row.get('body') or '')[:6000],
                       'published_at': str(row.get('published_at') or ''), 'assets': assets})
    if len(json.dumps(result).encode()) > 1_000_000:
        raise ValueError('Public feed exceeds the client metadata limit')
    return result

def gh_api(route, method='GET', data=None, allow_missing=False):
    command = ['gh', 'api', '--method', method, route]
    if data is not None:
        command += ['--input', '-']
    response = subprocess.run(command, input=json.dumps(data) if data is not None else None,
                              text=True, capture_output=True)
    if response.returncode:
        if allow_missing and '404' in response.stderr:
            return None
        raise RuntimeError(response.stderr.strip())
    return json.loads(response.stdout)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=pathlib.Path, help='Previously fetched public release array')
    parser.add_argument('--output', type=pathlib.Path, help='Write a local snapshot for deployment/testing')
    parser.add_argument('--publish', action='store_true', help='Commit releases.json to the public channel main branch')
    args = parser.parse_args()
    rows = json.loads(args.input.read_text()) if args.input else gh_api(f'repos/{REPO}/releases?per_page=30')
    content = (json.dumps(snapshot(rows), ensure_ascii=False, indent=2) + '\n').encode()
    if len(content) > 1_000_000:
        raise ValueError('Public feed exceeds the client metadata limit')
    if args.output:
        args.output.write_bytes(content)
    if args.publish:
        if gh_api(f'repos/{REPO}')['private']:
            raise ValueError('The update channel must be public')
        route = f'repos/{REPO}/contents/releases.json'
        current = gh_api(route+'?ref=main', allow_missing=True)
        if current and base64.b64decode(current.get('content', '')) == content:
            print('PUBLIC_FEED_UNCHANGED')
            return
        payload = {'message': 'chore: refresh verified public update feed', 'branch': 'main',
                   'content': base64.b64encode(content).decode(),
                   'committer': {'name': '8002 LLC', 'email': '8002salman@gmail.com'}}
        if current:
            payload['sha'] = current['sha']
        published = gh_api(route, 'PUT', payload)
        print('PUBLIC_FEED_PUBLISHED', published['commit']['sha'])
    print('PUBLIC_FEED_VALIDATED', len(snapshot(rows)), 'published releases')

if __name__ == '__main__':
    main()
