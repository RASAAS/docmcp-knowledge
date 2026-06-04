# Install Plugin

Reguverse Assistant is delivered as a Microsoft Word Add-in, supporting Windows, macOS, and Web.

## System Requirements

| Platform | Minimum Requirements |
|----------|---------------------|
| Windows | Windows 10+, Microsoft 365 or Office 2019+ |
| macOS | macOS 12+, Microsoft 365 for Mac |
| Web | Word Online (Microsoft 365 browser version) |

## Installation Methods

### Method 1: Automated Install (Recommended)

Download the installer for your platform from the official website:

**Windows:**
1. Download `ReguverseAssistant-Windows.zip`
2. Extract and run `install.bat`
3. Restart Microsoft Word

**macOS:**
1. Download `ReguverseAssistant-macOS.zip`
2. Extract and run `install.command` (right-click > Open for first time)
3. Restart Microsoft Word

### Method 2: Manual Install

**Windows:**
1. Open File Explorer, navigate to: `%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\`
2. Copy `manifest.xml` to that directory
3. Restart Word

**macOS:**
1. Open Finder, press Cmd+Shift+G, enter: `~/Library/Containers/com.microsoft.Word/Data/Documents/wef/`
2. Copy `manifest.xml` to that directory
3. Restart Word

### Method 3: Word Online

1. Open Word Online (https://www.office.com)
2. Create or open a document
3. Click Insert > Add-ins > Upload My Add-in
4. Select the `manifest.xml` file
5. The add-in appears in the Home tab

## Verify Installation

After successful installation, look for the "Reguverse" icon in Word's ribbon (Home tab, right side). Click it to open the task pane.

## Next Steps

- [Register & Login](./register)
