import pandas as pd
import os
from typing import List, Dict

def parse_daily_reports(folder_path: str) -> Dict[str, List[Dict]]:
    result = {}
    for filename in os.listdir(folder_path):
        if filename.startswith("Daily report_") and filename.endswith(".xlsx"):
            parts = filename.replace(".xlsx", "").split("_")
            team_member = f"{parts[-2]} {parts[-1]}"
            df = pd.read_excel(os.path.join(folder_path, filename))
            df.columns = df.columns.str.strip()

            for _, row in df.iterrows():
                if str(row["Interview"]).strip().lower() == "yes" and str(row["Status"]).strip().lower() == "pass":
                    candidate = str(row["Candidate Name"]).strip()
                    role = str(row["Role"]).strip()
                    result[candidate] = {
                        "role": role,
                        "team_member": team_member
                    }
    return result

def parse_new_employees(file_path: str) -> List[Dict]:
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip()
    data = []
    for _, row in df.iterrows():
        name = str(row["Employee Name"]).strip()
        join_date = pd.to_datetime(row["Join Date"]).strftime("%d-%b-%Y")
        role = str(row["Role"]).strip()
        data.append({
            "name": name,
            "join_date": join_date,
            "role": role
        })
    return data

def merge_data(new_employees: List[Dict], interview_results: Dict[str, Dict]) -> List[Dict]:
    final = []
    for emp in new_employees:
        name = emp["name"]
        role = emp["role"]
        join_date = emp["join_date"]
        team_member = interview_results.get(name, {}).get("team_member", "N/A")
        final.append({
            "name": name,
            "role": role,
            "join_date": join_date,
            "team_member": team_member
        })
    return final