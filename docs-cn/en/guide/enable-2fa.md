# Enable two-factor authentication

Paid plans and team members must turn on two-factor authentication (2FA) after sign-in. Install **Microsoft Authenticator** on your phone, then scan the QR code on your computer screen.

The QR code is in the Reguverse window titled "Enable two-factor authentication". Leave that window open and scan the computer screen with your phone.

::: info Phone only, no computer screen
A phone cannot scan a QR code shown on its own screen. In the authenticator app, enter the setup key manually. Copy the characters shown under "Or enter the secret manually" in the Reguverse window.
:::

## Step 1: Install Microsoft Authenticator

In your phone's app store, search for **authenticator**. Install the official Microsoft app. Ads and other apps with similar names cannot turn on Reguverse 2FA.

### iPhone / iPad (App Store)

1. Open the App Store and search for **authenticator**.
2. Skip the sponsored result at the top (it is marked as an ad).
3. Install **Microsoft Authenticator**. The developer must be **Microsoft Corporation**.
4. Tap Get or Open. The button label follows your store language (Get, 获取, 開啟, and so on).

<img class="phone-shot" src="/guide/2fa/ios-app-store.png" alt="App Store search for authenticator. The boxed result is Microsoft Authenticator by Microsoft Corporation." />

### Android

**Huawei / Honor (AppGallery)**

1. Open AppGallery and search for **authenticator**.
2. Skip the ad at the top.
3. Install the boxed **Authenticator**. Its description is "使用应用轻松登录微软账户" (Use the app to sign in to your Microsoft account easily), and the icon is a blue lock. Tap Install or Open.
4. Leave the other results (身份验证器2FA, token apps, QR Authenticator, and similar names) uninstalled.

<img class="phone-shot" src="/guide/2fa/android-appgallery.png" alt="Huawei AppGallery search for authenticator. The boxed result is Microsoft Authenticator." />

**Other Android phones (Google Play and similar stores)**

Search for **Microsoft Authenticator** and confirm the publisher is **Microsoft Corporation** before you install it.

## Step 2: Add Reguverse in the authenticator

1. Open Microsoft Authenticator.
2. If the app asks you to sign in with a Microsoft account, skip that step. Reguverse does not use a Microsoft account.
3. Tap **+** at the top right. On a first launch this may be labeled Add account.
4. Choose **Other account** (the option that mentions Google, Facebook, and similar services). Personal account and Work or school account are for Microsoft sign-in, so they will not accept this QR code.
5. Allow camera access.
6. Point the camera at the QR code in the Reguverse window until the app says the account was added.
7. The account list shows Reguverse (or your email) with a 6-digit code that changes about every 30 seconds.

If the scan does not complete, choose manual entry on the scan screen and type the secret from the Reguverse window. You can name the account Reguverse.

## Step 3: Confirm in Reguverse

1. Write down the **recovery codes** in the window, or store them in a password manager, then check "I have saved my recovery codes". Each code works once. You need them if you change phones or remove the authenticator app.
2. Tap Continue.
3. Enter the 6-digit code **currently shown** in the app, with no spaces, then tap Confirm and enable.
4. If the code is rejected, wait until the digits refresh and enter the new code.

## Later sign-ins

After your email and password, enter the 6-digit code from the authenticator. You can check "Trust this device for 7 days" so this device skips the code for a week.

## If setup still fails

| What you see | What to do |
|---|---|
| Many apps named Authenticator | On iPhone, the developer must be **Microsoft Corporation**. On Huawei AppGallery, the description must be "使用应用轻松登录微软账户". |
| The QR code does nothing | Scan the computer screen, with the whole code inside the frame and the screen brightness turned up. If that still fails, enter the secret manually. |
| The code is always rejected | Set the phone clock to automatic time. Use the 6 digits on screen now, not the previous set. |
| New phone | Sign in with a saved recovery code, then turn on 2FA again. |
