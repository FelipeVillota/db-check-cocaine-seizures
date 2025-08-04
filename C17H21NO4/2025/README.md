# db-check-cocaine-seizures

<div style="text-align:center;font-family:sans-serif;margin:20px 0;max-width:600px;margin:auto;font-size:14px;font-weight:300;color:#777">
  <img src="1000+aToNoFcoke+22.jpg" alt="NFT by Camilo Restrepo" style="max-width:100%;border:1px solid #eee">
  <p style="font-style:italic;margin:8px 15px;line-height:1.4;font-weight:300">One-Kilo Package of Cryptococaine #1000. Image taken from the NFT collection <a href="https://camilorestrepo.co/#/a-ton-of-coke/" target="_blank" style="color:#06c;font-weight:400">A Ton of Coke</a> 
by Colombian artist Camilo Restrepo.</p>
</div>

<br><br>

This is a lightweight database management strategy for monitoring entries by the IC team in the shared Google Sheet "incautaciones cocaina 01-02".

It is designed to support data governance workflows with:

📈 Monitoring tools for data quality

🔍 Custom validation rules

📊 KPI-based reporting

🚨 Alert for anomalies

🎛️ Quick filters for targeted analyses

✅ A script for direct edits on the Google Sheet

## Why?
The spreadsheet is where the data lives. It remains a collaborative work in progress, shaped by multiple investigators. This tool acts like a back-end and dedicated quality checkpoint:
![alt text](image-why.png)
- Helps us keep the data and process trustworthy

- Saves time

- Complements Google Sheets basic validation

- Facilitates team monitoring, analysis and reporting

## How does it work?

This tool is multifunctional and can be adapted according to the database's goal or to specific project tasks, following a create-read-update-delete logic. The script and associated material can be placed in IC's Github.

Apart from checking the overall "data health", there are three approaches to validation:

- Manage all the rules here and report <span style="color: red; font-weight: bold;">(impractical)</span>
- Just monitor here and report <span style="color: red; font-weight: bold;">(missed opportunities)</span>
- Hybrid <span style="color: green; font-weight: bold;">(adequate)</span>


<div style="border: 2px solid green; padding: 10px; border-radius: 5px; text-align: center;"> <b>We work with what already exists + leverage back-end functionalities.</b> </div>

## What is the workflow?

[![alt text](image-workflow.png)](https://app.eraser.io/workspace/piMlbKXsypAm5EdTYQHk?origin=share)


## We work by groups of variables

| **Category**                                   | **Variables**                                                                                                                                                                                                                                    | **Status**        |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| <mark style="background-color: #90EE90">**Event Metadata**</mark>     | <mark style="background-color: #90EE90">Type, Time unit, Date, Date 2, Year, Month, Day, Duration, Description, Source link, Project interested</mark>                                                                                             | Done              |
| <mark style="background-color: #90EE90">**Drugs & Quantities**</mark>  | <mark style="background-color: #90EE90">Type Drugs, Quantity, Weight unit, seizure_kgs</mark>                                                                                                               | Finish by 25/07   |
| **Modus Operandi**                            | Modus Operandi/place of seizure, Sub MO                                                                                                                                                                                                           | Finish by 01/08   |
| **Seizure Location**                          | Region, Country, Department/State, Municipality/Port                                                                                                                                                                                              | Finish by 08/08   |
| **Origin**                                    | Origin country, Origin Area, Origin municipality                                                                                                                                                                                                  | Finish by 15/08   |
| **Transit**                                   | Transit 1/Region, Transit 1/Country, Transit 1/Department, Transit 1/Municipality, Transit 2/ region, Transit 2/ country, Transit 2/Department, Transit 2/municipality/port                                                                         | Finish by 22/08   |
| **Destination**                               | Destition - Region, Destition - Country, Destition - department.state, Destition - Municipality/Port, Destition 2 - Country, Destition 2 - Municipality/Port                                                                                       | Finish by 29/08   |
| **Criminal Actors**                           | Criminal group #1, Criminal group #2, Criminal group #3                                                                                                                                                                                            | Finish by 05/09   |

## Walkthrough on how the API was set up
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



