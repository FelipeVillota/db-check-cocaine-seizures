# config.py
import os

BASE_DIR = os.getcwd()

SERVICE_ACCOUNT_FILE = os.path.join(
    BASE_DIR, "nyckelring/brelok/summer-sector-439022-v6-2eafffbbfb90.json"
)

ORIGINAL_SPREADSHEET_ID = "1t61MafCmnRe2QN082Bk1V0IxBSIW8UUqH1g5mULgb2o"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Kernel and environment names
VENV_NAME = "venv-db-check"
KERNEL_NAME = "db-check"
