# Install Plugin

Reguverse Assistant is delivered as a Microsoft Word Add-in, supporting Windows and macOS. A web browser version is also available.

## System Requirements

| Platform | Minimum Requirements |
|----------|---------------------|
| Windows | Windows 10+, Microsoft 365 or Office 2019+ |
| macOS | macOS 12+, Microsoft 365 for Mac |
| Web | Chrome / Edge / Firefox / Safari |

## Installation Methods

### Method 1: Automated Install (Recommended)

Download the installer from the [product info page](https://app.reguverse.com/info/) and run the install script.

**Windows:**
1. Download `ReguverseAssistant-Intl-Windows.zip`
2. Extract and double-click `install.bat`
3. Restart Microsoft Word

**macOS:**
1. Download `ReguverseAssistant-Intl-macOS.zip`
2. Extract and double-click `install.command` (you may need to right-click > Open the first time)
3. Restart Microsoft Word

Download links and detailed instructions:
- International users: https://app.team-ra.org/info/
- China users: https://app.reguverse.com/info/

<!-- Screenshot placeholder: installer files -->

### Method 2: Manual Install

If automatic installation fails:

**Windows:**
1. Open File Explorer, enter in the address bar: `%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\`
2. Copy `manifest.xml` to this directory
3. Restart Word

**macOS:**
1. Open Finder, press Cmd+Shift+G, enter: `~/Library/Containers/com.microsoft.Word/Data/Documents/wef/`
2. Copy `manifest.xml` to this directory
3. Restart Word

### Method 3: Web Browser Version

No plugin installation required. Access the system directly via browser:

- International users: https://app.team-ra.org/
- China users: https://app.reguverse.com/

The web version supports all features except "Insert to Word". Generated documents can be downloaded as Word files.

## Verify Installation

After successful installation, you should see the "Reguverse" icon in Word:

- **Windows/macOS**: In the "Home" tab, on the right side

Click the icon to open the Reguverse Assistant task pane.

<!-- Screenshot placeholder: Reguverse icon in Word -->

## Update Plugin

The plugin automatically loads the latest version. If you experience issues:

1. Close all Word windows
2. Clear Office cache:
   - Windows: Delete cache files in `%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\`
   - macOS: Delete cache in `~/Library/Containers/com.microsoft.Word/Data/Library/Caches/`
3. Reopen Word

## Troubleshooting

### Plugin icon not visible after install?

- Confirm Office version is 2019 or Microsoft 365 (Office 2016 and earlier not supported)
- Verify manifest file is in the correct directory
- Try fully quitting Word and restarting

### macOS says "cannot verify developer"?

Right-click the install script, select "Open", then click "Open" again in the dialog.

## Next Steps

- [Register & Login](./register) -- Create your account
