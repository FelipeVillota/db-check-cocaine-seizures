# db-check-cocaine-seizures
This is a lightweight database management strategy for monitoring entries by the IC team in the shared Google Sheet "incautaciones cocaina 01-02".

It is designed to support weekly governance workflows by checking for formatting errors, invalid values, and data quality issues. It is multifunctional: it can flag problematic cells directly within the Google Sheet, make corrections and generate validation reports as needed.

### Why?
- Assures reproducibility, transparency and scalability
- Complements Google Sheets basic validation -> we can enforce custom rules (e.g., logical dates, quantities, relationships, normalizations, etc).
- Facilitates supervision, analysis and reporting.

### How does it work?

It is essential to recognize both, the database's goal and the fact that it remains a collaborative work in progress, made by multiple team members.

So, as a catalyst for data quality, this script intends to be a back-end check:

1. Define rules per column

2. Create a function per rule block

3. Apply them row-wise, collecting "violations"

4. Mark validation status per row

6. (Optional) Direct color highlighting

7. (Optional) Direct correction

Columns by theme: 

| **Topic**                 | **Variables**                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 📌 **Event Metadata**     | Type, Time unit, Date, Date 2, Year, Month, Day, Duration, Description, Source links, Tags                                             |
| 🚨 **Drugs & Quantities** | Type Drugs, Quantity, Weight unit, seizure\_kgs                                                                                        |
| 🚚 **Modus Operandi**     | Modus Operandi/place of seizure, Sub MO                                                                                                |
| 📍 **Seizure Location**   | Region, Country, Department/State, Municipality/Port                                                                                   |
| 🌱 **Origin**             | Origin country, Origin Area, Origin municipality                                                                                       |
| 🔄 **Transit**            | Transit 1/Region, Transit 1/Country, Transit 1/Department, Transit 1/Municipality, Transit 2/Region *(note: fix casing inconsistency)* |


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