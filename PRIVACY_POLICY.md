# 8002 CleanUp Pro — Privacy Policy

**Effective date:** November 8, 2026  
**App:** 8002 CleanUp Pro (`com.salmanbashir.cleanup8002`)  
**Developer:** Salman Bashir

This policy describes permissions and data flows in the current Android beta application. Some functions run entirely on the device; others contact external services or user-selected servers. **Using a VPN, browser, downloader, weather service, or update checker involves network traffic**. This policy is a disclosure, not a certificate of Google Play Protect approval.

## 1. Device permissions and local processing

- **Files and media:** Storage analysis, media scanning, OCR, cleanup, downloads, file exploration, and private media functions use file/media access. Device file metadata and selected content may be processed locally. Sharing, FTP, cloud-picker, or download features can transfer files to or from destinations deliberately selected by the user. Review each operation before deleting or sharing data.
- **Installed apps and usage:** App Manager, App Locker, Shield, and Boost may use package visibility, app-usage access, and optional Shizuku authorization to identify apps or carry out user-requested operations. The app cannot override Android security restrictions without platform authorization.
- **Accessibility:** The optional App Locker accessibility service responds to window-state and notification-state events to identify transitions into protected apps. The service declares `canRetrieveWindowContent="false"`; accessibility does not grant the app permission to read typed text or chat contents. Disable the service in Android Accessibility settings when not needed.
- **Location:** If location access is granted, location-dependent utilities may use it; external weather or other network lookups can involve location-derived queries. Permission can be revoked in Android Settings.
- **Camera and OCR:** Camera access is used for user-initiated scanning, including on-device OCR. Files or results shared through other features may leave the device only when those functions are used.
- **Other system permissions:** Notifications, network state, background/foreground services, VPN, and installation permissions support the app's optional features. Android controls access to these capabilities.

## 2. Internet connections and third parties

The app can contact outside hosts for requested features. Depending on the feature, destination servers can observe your public IP address, request timing, and data sent to them under their own policies.

- **Updates:** GitHub's public release API and GitHub-hosted download infrastructure are contacted to check or download updates.
- **Full VPN:** The optional WireGuard feature connects to a VPN gateway whose configuration is imported by the user. **Traffic routed over that tunnel reaches the chosen gateway; it is not exclusively processed on-device.** The gateway operator may be able to observe connection metadata or unencrypted traffic. The app also performs exit-IP/country checks using `api4.ipify.org` and `ipapi.co` and a DNS connectivity check. The app does not bundle free VPN server credentials.
- **Local VPN / DNS protection:** Local DNS filtering and per-app firewall operation are distinct from the Full VPN mode. DNS queries or network traffic may still reach upstream resolvers and destination services; a local filter is not a guarantee of anonymity.
- **Browser, downloader, weather, currency, diagnostics:** User-entered sites, media servers, and external information/diagnostic providers can receive requests and their associated network information. Browser pages and linked services have their own privacy practices.
- **Local sharing:** FTP/FTPS and LAN file sharing transfer user-selected information to destinations on the relevant network. Review the network and recipient before enabling them.

The Android network security configuration blocks cleartext HTTP by default and defines limited exceptions for specified loopback/local-router hosts. This is **not** a blanket guarantee that all external providers, websites, or end-to-end VPN traffic are private or encrypted at every hop.

## 3. Data stored on the device

Application settings, protected-app selections, local histories, download records, and credentials or imported VPN configurations may be stored on the device for the corresponding feature. Security-sensitive settings should use Android-backed protected storage where implemented. Uninstalling the app or clearing its data removes app-managed local data subject to Android storage behavior, but does not recall files already exported, downloaded, backed up, or sent to third parties.

This policy does not assert that no network requests, diagnostics, or third-party data processing ever occur. External service operators control their own retention, logging, and privacy practices.

## 4. Your choices

You can decline optional permissions, switch off App Locker accessibility access, disconnect VPN modes, remove imported VPN endpoints, stop local sharing, or uninstall the app. Some utility features will not operate without the relevant permission. For Android installations from GitHub, keep Play Protect enabled and independently assess security warnings.

## 5. Contact and updates

For app information or to report a privacy/security issue, use the developer's [GitHub profile](https://github.com/salmanbashir80) and the [official release repository](https://github.com/salmanbashir80/8002-Pro-Releases). The source repository is private; its URL is not a public support channel.

This policy may be updated as features and network integrations change. The effective date above identifies the current version.
