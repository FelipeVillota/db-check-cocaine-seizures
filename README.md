# db-check-cocaine-seizures
This is a lightweight data validation tool for monitoring entries by the IC team in the shared Google Sheets "incautaciones cocaina 01-02". It is designed to support weekly governance workflows by checking for formatting errors, invalid values, and data quality issues. Highlights problematic rows directly in the sheet and generates structured audit reports for review.

### Why?
- Good practice for reproducibility, transparency and scalability (can be applied to other relevant dbs: e.g., homicide data, etc).  
- Google Sheets validation is basic -> we can enforce custom rules (e.g., logical dates, quantities, relationships, normalize names, etc).
- Facilitates reporting and knowledge sharing.
- Overall: provides quality data ready to be analyzed

### Who?
MAD Unit


### Walkthrough on how it was set up:
#### Step 1: Enable the Google Sheets API and Create a Service Account

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