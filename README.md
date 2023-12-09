# Auto-Parade Script

## Overview

This script is designed to automate the update of the parade state on the portal. It utilizes Playwright for automating interactions with the website.

## Configuration
### This step is optional, however it is recommended for security reasons
Before running the script, make sure to configure the following environment variables. You can set these variables based on your operating system:

### Windows

```powershell
$env:RMC_ID="Your_RMC_Username"
$env:RMC_PASS="Your_RMC_Password"
```
### Mac OS / Linux
```bash
export RMC_ID="Your_RMC_Username"
export RMC_PASS="Your_RMC_Password"
```

Replace the placeholder values with your actual RMC username, RMC password, and Twilio authentication token if applicable.

## Running the Script
1. Ensure that you have Python installed on your system.
2. Install dependencies by running `pip install -r requirements.txt`.
3. Execute the script using the command `python auto-parade.py` or in your IDE.

## Operation
The script performs the following steps:
- Logging into the RMC portal.
- Accessing the parade state update page.
- Selecting the desired option for the parade state (currently "Present").
- Saving the changes.

## SMS Notification (Optional)
If you have configured your Twilio account, the script will send an SMS notification to inform you of the successful update of the parade state. You can enable this feature by uncommenting the appropriate lines in the script.

**Note**: Ensure not to share your RMC or Twilio credentials publicly.
