# 开启双因素认证

付费套餐用户和团队成员登录后需要开启双因素认证（2FA）。请在手机上安装 **Microsoft Authenticator**（微软身份验证器），再扫描电脑屏幕上的二维码。

二维码出现在 Reguverse 的「启用双因素认证」窗口中。请保持这个窗口不要关闭，用手机扫描电脑屏幕。

::: info 只有手机、没有电脑屏幕时
不要用手机去扫手机自己的屏幕，扫不出来。打开验证器后选择手动输入密钥，把窗口里「或手动输入密钥」下面的那一串字符原样填入。
:::

## 第 1 步：安装 Microsoft Authenticator

在手机应用商店搜索 **authenticator**。请只安装微软官方应用。名称相近的广告和其他验证器不能用来开启 Reguverse 的 2FA。

### iPhone / iPad（App Store）

1. 打开 App Store，搜索 **authenticator**。
2. 跳过最上方带「广告」标记的结果。
3. 安装 **Microsoft Authenticator**，开发者必须是 **Microsoft Corporation**。
4. 点「获取」或「打开」（不同语言界面可能显示为 Get、获取、開啟）。

<img class="phone-shot" src="/guide/2fa/ios-app-store.png" alt="App Store 搜索 authenticator，红框为 Microsoft Authenticator，开发者 Microsoft Corporation" />

### Android

**华为 / 荣耀（应用市场）**

1. 打开「应用市场」，搜索 **authenticator**。
2. 跳过最上方的广告。
3. 安装红框中的 **Authenticator**：说明文字是「使用应用轻松登录微软账户」，图标是蓝色的锁。点「安装」或「打开」。
4. 不要安装「身份验证器2FA」「Authenticator身份验证器-令牌」「QR Authenticator」等其他结果。

<img class="phone-shot" src="/guide/2fa/android-appgallery.png" alt="华为应用市场搜索 authenticator，红框为微软 Authenticator" />

**其他 Android 手机（Google Play 等）**

搜索 **Microsoft Authenticator**，确认发行商是 **Microsoft Corporation** 后再安装。

## 第 2 步：在验证器里添加 Reguverse

1. 打开刚安装的 Microsoft Authenticator。
2. 如果应用要求登录微软账号，请先跳过。Reguverse 不使用微软账号。
3. 点右上角 **+**（第一次打开时也可能是「添加账户」）。
4. 账户类型选 **其他账户**（Other account。说明里常出现 Google、Facebook 等字样）。不要选「个人账户」或「工作或学校账户」。
5. 允许使用相机。
6. 将取景框对准电脑上 Reguverse 窗口里的二维码，直到提示已添加。
7. 账户列表中会出现 Reguverse（或您的邮箱），旁边是 6 位数字，大约每 30 秒更换一次。

扫不出来时，在扫描界面选择手动输入，把 Reguverse 窗口中的密钥原样填入。账户名可填写 Reguverse。

## 第 3 步：回到 Reguverse 确认开启

1. 先把窗口中的**恢复码**抄下来或存到密码管理器，并勾选「我已保存恢复码」。每个恢复码只能使用一次。换手机或卸载验证器后，要用恢复码登录。
2. 点「继续」。
3. 输入验证器里**当前显示**的 6 位数字，不要加空格，点「确认并启用」。
4. 如果提示验证码错误，等数字刷新后再输入新的一组。

## 之后登录

输入邮箱和密码后，再输入验证器中的 6 位数字。验证时可勾选「信任此设备 7 天」，这 7 天内这台设备不用重复输入。

## 仍然无法开启时

| 现象 | 处理 |
|---|---|
| 商店里有很多 Authenticator | iPhone 只认开发者 **Microsoft Corporation**。华为应用市场只认说明为「使用应用轻松登录微软账户」的那一项。 |
| 二维码没有反应 | 扫的是电脑屏幕，不是手机自己的屏幕。调高屏幕亮度，让整张二维码进入取景框。仍不行就手动输入密钥。 |
| 验证码一直错误 | 把手机时间设为自动。使用当前这 30 秒内显示的 6 位数字，不要用上一组。 |
| 换了新手机 | 用当初保存的恢复码登录，然后重新开启 2FA。 |
