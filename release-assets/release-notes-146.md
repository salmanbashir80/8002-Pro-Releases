Four tools per row, readable light/dark Home themes, compact cards, crisp native text and subtle animations.

- Improved tool search with aliases, common misspellings and a separate web-search action.
- Pin or drag search results into a chosen Home position; layouts persist after reopening.
- Fixed hidden-shortcut restoration and narrow-screen framing in Calculator, Battery, Note Pad and utility forms.
- Catalog remains exactly 100 tools.

Validation: 200 Node tests and 73 Android JVM tests passed. Home layouts checked at 320/360/390/430px in both themes; 100 tool destinations captured in each theme with no cropped visible controls or JavaScript page errors. APK/AAB signatures and all 122 final web assets verified.

Beta verification limit: physical-device, TalkBack and emulator acceptance were not performed. GitHub Actions was blocked by account billing/spending settings, so these artifacts were built and verified locally.

Install the APK over the existing installation to retain app data. AAB uses the existing Play manifest. Signing certificate is unchanged.

Source commit: 6e1859dbde4f72e2c041723b100627304b7989f4
APK SHA-256: 0d3caaef49f49b8fc74399e7886eebd96e92b594cc68ea3c88d025dacdbe81da
AAB SHA-256: 9e53f55c6932b4a8043d5e823df8e080742f808f6062de2c086ac960e27c44b5
Signing certificate SHA-256: 92cbdb92ec298f841523d065fb0008d455fc823a1f72054602af47d15c740706
