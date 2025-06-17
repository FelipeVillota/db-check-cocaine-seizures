# db-check-cocaine-seizures
This is a lightweight database management strategy for monitoring entries by the IC team in the shared Google Sheet "incautaciones cocaina 01-02".

It is designed to support weekly governance workflows by checking for formatting errors, invalid values, data quality issues and more. 

## Why?
The spreadsheet is where the data lives. It remains a collaborative work in progress, shaped by multiple investigators. This tool acts like a back-end quality checkpoint:

- Helps us keep the data and process trustworthy
- Saves time
- Complements Google Sheets basic validation
- Facilitates team monitoring, analysis and reporting

### How does it work?

This tool is multifunctional and can be adapted according to the database's goal or to specific tasks. It is based on the create-read-update-delete logic.

Three simple approaches:

1. Define ALL the rules for columns -> Create custom functions per rule blocks -> Apply them row-wise, collect "violations"

2. Just verify -> rules are handled in the spreadsheet

3. A hybrid management

In all the approaches we can flag or intervene directly as needed. 


### Columns by theme: 

| **Topic**                 | **Variables**                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 📌 **Event Metadata**     | Type, Time unit, Date, Date 2, Year, Month, Day, Duration, Description, Source links, Tags                                             |
| 🚨 **Drugs & Quantities** | Type Drugs, Quantity, Weight unit, seizure\_kgs                                                                                        |
| 🚚 **Modus Operandi**     | Modus Operandi/place of seizure, Sub MO                                                                                                |
| 📍 **Seizure Location**   | Region, Country, Department/State, Municipality/Port                                                                                   |
| 🌱 **Origin**             | Origin country, Origin Area, Origin municipality                                                                                       |
| 🔄 **Transit**            | Transit 1/Region, Transit 1/Country, Transit 1/Department, Transit 1/Municipality, Transit 2/Region *(note: fix casing inconsistency)* |

### Basic rules:
 

### Walkthrough on how it was set up:
 _***Enabling the Google Sheets API and Creating a Service Account***_

To allow external programs (like Python or R scripts) to access the Google Sheet for validation and reporting:

1. **Go to the [Google Cloud Console](https://console.cloud.google.com/).**

2. **Create a new project** or select an existing one.

3. **Enable APIs**:
   - Navigate to **APIs & Services > Library**.
   - Search for **Google Sheets API** and click **Enable**.
   - Also enable **Google Drive API** (required for some file operations).

4. **Create a Service Account**:
   - Go to **APIs & Services > Credentials**.
   - Click **Create Credentials > Service Account**.
   - Provide a name (`db-watch`) and click **Create**.
   - Skip the permissions step, then click **Done**.

5. **Generate JSON Credentials**:
   - In the Service Accounts list, find your new account.
   - Click the three dots on the right → **Manage keys**.
   - Click **Add Key > Create New Key**.
   - Choose **JSON** format and download the file (Kept safe).

6. **Share Your Google Sheet with the Service Account**:
   - Open your Google Sheet.
   - Click **Share**.
   - Add the Service Account’s email address (db-watch@summer-sector-439022-v6.iam.gserviceaccount.com).
   - Give it **Editor** access.