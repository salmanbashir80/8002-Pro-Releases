# Privacy Policy & Security Declaration — 8002 CleanUp Pro

**Effective Date:** November 7, 2026  
**Developer:** Salman Bashir (`salmanbashir80`)  
**Package Name:** `com.salmanbashir.cleanup8002`  
**Application Name:** 8002 CleanUp Pro

---

## 1. Overview & Commitment to User Privacy

**8002 CleanUp Pro** is designed with a strict **Privacy-First and Offline-First** philosophy. We believe that utilities, system clean-up tools, file managers, and calculation worksheets should serve the user without tracking, logging, or harvesting user data. 

8002 CleanUp Pro does **not** sell, rent, monetize, or transmit any user information to third-party advertisers, data brokers, or external analytics servers.

---

## 2. Permitted Capabilities & Usage Declarations

### A. Storage Access (`MANAGE_EXTERNAL_STORAGE`, `READ_MEDIA_*`)
- **Purpose**: Used strictly for user-initiated device storage analysis, temporary cache cleanup, large file inspection, WhatsApp media categorization, and EX Downloader file saving.
- **Data Handling**: File inspection occurs entirely on-device. No filenames, media, photos, or documents are ever uploaded to remote servers.

### B. Network & Diagnostics (`INTERNET`, `ACCESS_NETWORK_STATE`, `ACCESS_WIFI_STATE`)
- **Purpose**: Used for:
  1. Ping, DNS latency, and internet speed test diagnostics requested by the user.
  2. Currency exchange rate updates.
  3. EX Downloader streaming from user-entered URLs.
  4. Local network subnet discovery (identifying devices on the user's private Wi-Fi).
- **Security**: All external communications default to encrypted HTTPS via `network_security_config`. Cleartext traffic is prohibited except for user-requested LAN router admin diagnostics (`192.168.x.x`).

### C. Local VPN Service (`BIND_VPN_SERVICE`)
- **Purpose**: Used solely to provide on-device DNS filtering and an app-specific firewall.
- **Data Handling**: All filtering happens locally on the Android device via a virtual loopback interface. User network packets are **never** proxied, inspected, or recorded on remote servers.

### D. App Protection & Privacy Gate (`BIND_ACCESSIBILITY_SERVICE`)
- **Purpose**: Used optionally and strictly for the **App Locker** feature to detect when a user-selected protected application (such as WhatsApp or Gallery) is launched, displaying the local PIN / Biometric verification prompt.
- **Safety**: Window contents are explicitly **not readable** (`android:canRetrieveWindowContent="false"`). Keystrokes, text inputs, and on-screen content are never recorded, transmitted, or monitored.

### E. Camera & OCR (`CAMERA`)
- **Purpose**: Used on-demand for Document Studio scanner and offline Tesseract OCR text recognition. Camera streams are processed in memory and never transmitted externally.

---

## 3. Play Protect & Safety Compliance

8002 CleanUp Pro adheres to Google Play Protect Device and Network Abuse policies:
- **No Stalkerware / Spyware**: The application does not monitor user location in the background, does not access contacts, and does not monitor private calls or text messages.
- **No Unauthorized Modifications**: The application does not download executable binary code or bypass Android sandbox security.
- **User Control & Transparency**: All cleanup, locking, and diagnostic operations require explicit user interaction and can be paused or uninstalled at any time through standard Android settings.

---

## 4. Developer Contact & Verification

For security audits, Play Protect verification inquiries, or vulnerability reports:
- **GitHub Repository**: [salmanbashir80/8002CleanUp-Android-source](https://github.com/salmanbashir80/8002CleanUp-Android-source)
- **Releases Portal**: [salmanbashir80/8002-Pro-Releases](https://github.com/salmanbashir80/8002-Pro-Releases)
- **Email Contact**: `salmanbashir80@users.noreply.github.com`
