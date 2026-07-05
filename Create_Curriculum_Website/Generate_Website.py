import json
import pandas as pd
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]

ITEM_TYPE_FILTER = ""   # Example: "OJT" or leave blank
# Column constants — match combined curriculum CSV format (1_CHELMSFORD_MFG_combined_*.csv)
PARENT_ID_COL = "curriculum_id"
PARENT_TITLE_COL = "curriculum_title"
SUB_ID_COL = "sub_curriculum_id"
SUB_TITLE_COL = "sub_curriculum_title"
SUB_PARENT_ID_COL = "sub_curriculum_parent_id"
ITEM_ID_COL = "item_id"
ITEM_TITLE_COL = "item_title"
ITEM_TYPE_COL = "item_type"
ROW_TYPE_COL = ""
DUE_DAYS_COL = "initial_due_days_item"


# =========================================================
# HELPERS
# =========================================================

def normalize(value):
    if pd.isna(value):
        return ""
    return str(value).strip()

def normalize_upper(value):
    return normalize(value).upper()

def to_number(value):
    text = normalize(value)
    if text == "":
        return None
    try:
        return float(text)
    except ValueError:
        return None

def format_number(value):
    if value is None:
        return ""
    if float(value).is_integer():
        return str(int(value))
    return f"{value:g}"

def build_due_label(day_values):
    numeric_values = sorted({
        to_number(value) for value in day_values
        if to_number(value) is not None
    })
    if not numeric_values:
        return ""
    if len(numeric_values) == 1:
        day_count = format_number(numeric_values[0])
        day_word = "day" if day_count == "1" else "days"
        return f"Initial due: {day_count} {day_word}"
    min_days = format_number(numeric_values[0])
    max_days = format_number(numeric_values[-1])
    return f"Initial due: {min_days}-{max_days} days"

def resolve_csv_file():
    candidates = [
        Path(PRIMARY_CSV_FILE),
        Path(FALLBACK_CSV_FILE),
    ]
    existing = [path for path in candidates if path.exists()]
    if not existing:
        raise FileNotFoundError(
            "Could not find a combined CSV file in the configured locations."
        )
    return str(max(existing, key=lambda path: path.stat().st_mtime))

def resolve_output_html_file():
    output_folder = Path(OUTPUT_FOLDER)
    if not output_folder.is_absolute():
        output_folder = PROJECT_ROOT / output_folder
    output_folder.mkdir(parents=True, exist_ok=True)
    return output_folder / OUTPUT_FILENAME


# =========================================================
# PARSE CSV INTO UI DATA
# =========================================================

def build_data(csv_file, item_type_filter=""):
    df = pd.read_csv(csv_file, dtype=str).fillna("")
    df.columns = [str(col).replace("\ufeff", "").strip() for col in df.columns]

    required = [
        PARENT_ID_COL,
        PARENT_TITLE_COL,
        SUB_ID_COL,
        SUB_TITLE_COL,
        ITEM_ID_COL,
        ITEM_TITLE_COL,
        ITEM_TYPE_COL,
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        print("ACTUAL CSV COLUMNS:")
        for col in df.columns:
            print(repr(col))
        raise KeyError(f"Missing required columns: {missing}")

    if item_type_filter:
        df = df[
            df[ITEM_TYPE_COL]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.upper()
            == item_type_filter.strip().upper()
        ].copy()

    parent_map = {}

    for _, row in df.iterrows():
        parent_id = normalize(row[PARENT_ID_COL])
        parent_title = normalize(row[PARENT_TITLE_COL])
        sub_id = normalize(row[SUB_ID_COL])
        sub_title = normalize(row[SUB_TITLE_COL])
        sub_parent_id = normalize(row.get(SUB_PARENT_ID_COL, ""))
        item_id = normalize(row[ITEM_ID_COL])
        item_title = normalize(row[ITEM_TITLE_COL])
        item_type = normalize(row[ITEM_TYPE_COL])

        # Empty item_id → standalone sub with no parent shown in UI
        if not item_id:
            if not sub_id:
                continue
            noparent_key = f"__noparent__{sub_id}"
            if noparent_key not in parent_map:
                parent_map[noparent_key] = {
                    "id": noparent_key,
                    "title": "",
                    "noparent": True,
                    "children": [],
                    "items": [],
                    "_due_days": [],
                }
            noparent_obj = parent_map[noparent_key]
            if not any(s["id"] == sub_id for s in noparent_obj["children"]):
                noparent_obj["children"].append({
                    "id": sub_id,
                    "title": sub_title if sub_title else sub_id,
                    "items": [],
                })
            continue

        effective_parent_id = sub_parent_id if sub_parent_id else parent_id
        effective_parent_title = parent_title if parent_title else effective_parent_id

        if not effective_parent_id:
            continue

        if effective_parent_id not in parent_map:
            parent_map[effective_parent_id] = {
                "id": effective_parent_id,
                "title": effective_parent_title,
                "children": [],
                "items": [],
                "_due_days": [],
            }

        parent_obj = parent_map[effective_parent_id]
        due_days = normalize(row.get(DUE_DAYS_COL, ""))
        if due_days and due_days not in parent_obj["_due_days"]:
            parent_obj["_due_days"].append(due_days)

        if sub_id:
            sub_obj = next((s for s in parent_obj["children"] if s["id"] == sub_id), None)
            if sub_obj is None:
                sub_obj = {
                    "id": sub_id,
                    "title": sub_title if sub_title else sub_id,
                    "items": []
                }
                parent_obj["children"].append(sub_obj)

            if item_id or item_title:
                item_obj = {
                    "id": item_id if item_id else item_title,
                    "title": item_title if item_title else item_id,
                    "type": item_type
                }
                exists = any(
                    x["id"] == item_obj["id"] and x["title"] == item_obj["title"]
                    for x in sub_obj["items"]
                )
                if not exists:
                    sub_obj["items"].append(item_obj)
        else:
            if item_id or item_title:
                item_obj = {
                    "id": item_id if item_id else item_title,
                    "title": item_title if item_title else item_id,
                    "type": item_type
                }
                exists = any(
                    x["id"] == item_obj["id"] and x["title"] == item_obj["title"]
                    for x in parent_obj["items"]
                )
                if not exists:
                    parent_obj["items"].append(item_obj)

    data = []
    for parent in parent_map.values():
        parent["due_label"] = build_due_label(parent.pop("_due_days", []))
        data.append(parent)

    # Parents with subcurricula first, alphabetical within each group
    data.sort(key=lambda x: (0 if x["children"] else 1, (x["title"] or "").lower()))

    for parent in data:
        parent["children"].sort(key=lambda x: (x["title"] or "").lower())
        parent["items"].sort(key=lambda x: (x["title"] or "").lower())
        for sub in parent["children"]:
            sub["items"].sort(key=lambda x: (x["title"] or "").lower())

    return data


# =========================================================
# BUILD HTML FROM TEMPLATE FILE
# =========================================================

def build_html(template_file, data):
    template_text = Path(template_file).read_text(encoding="utf-8")
    data_json = json.dumps(data, ensure_ascii=False)
    return template_text.replace("__TREE_DATA__", data_json)


# =========================================================
# MAIN
# =========================================================

def main():
    csv_file = resolve_csv_file()
    print(f"Using CSV: {csv_file}")
    data = build_data(csv_file, ITEM_TYPE_FILTER)

    final_html = build_html(TEMPLATE_FILE, data)
    output_html = resolve_output_html_file()
    output_html.write_text(final_html, encoding="utf-8")
    print(json.dumps(data[:2], indent=2))
    print(f"Created: {output_html}")


# ─── CONFIGURE PATHS HERE ───


### INSERT COMBINED FILEPATH

PRIMARY_CSV_FILE = SCRIPT_DIR / r"C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\sflms_redux\affinity\combined_data_05May2026_Affinity.csv"


### FOLDER FOR NEW HTML FILE
### Use a folder name like "QC" or paste a full folder path.

OUTPUT_FOLDER = "Affinity"


### NAME OF NEW HTML FILE 
OUTPUT_FILENAME = "1_Affinity.html"

# ───────────────────────────────────────

### DO NOT CHANGE
TEMPLATE_FILE = SCRIPT_DIR / "curriculum_panel_april23.html"


FALLBACK_CSV_FILE = r"C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\sflms_redux\affinity\Backup_Combined_Data_05May2026_Affinity.csv"

####

if __name__ == "__main__":
    main()

'''
Action descriptions from AI

- Replace (item) with (item) containing "title" trigger and a (type of action) with (words). 

- Hover/focus within show logic. 

- Functions not touched

- Add toggle buttons to column header in panel 

- alongside existing content 

- render changes into (x) so panel content stays in sync


- **** Identify formal names of interface elements (buttons, search bars, dropdowns, expand)
'''
