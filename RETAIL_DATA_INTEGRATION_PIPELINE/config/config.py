from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"
LOG_DIR = BASE_DIR / "logs"

BASE_URL = "https://jsonplaceholder.typicode.com"

ENDPOINTS = {
    "users": f"{BASE_URL}/users",
    "posts": f"{BASE_URL}/posts",
    "comments": f"{BASE_URL}/comments",
}

TIMEOUT = 30