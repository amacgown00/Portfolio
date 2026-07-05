import os
import pandas as pd

# ============================================================
# CONFIG
# ============================================================

# Create new folder for each department and add path.     
OUTPUT_DIR = r"C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\sflms_redux\affinity"

# Run SFLMS saved report "Combine_data_item" and add path.
CURRICULUM_DATA_FILE = r"C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\sflms_redux\affinity\Affinity_Curriculum_Data_05May2026.csv"

# Run SFLMS saved report "Combine_item status by user" and add path.
USER_CURRICULUM_ITEM_STATUS_FILE = r"C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\sflms_redux\affinity\Affinity_Item_Status_05May2026.csv"


OUTPUT_FILE_NAME = "combined_data_05May2026_Affinity.csv"

# ============================================================
# COLUMN INDEX MAPS
# ============================================================

CD_COLUMNS = {
    0: "curriculum_id",
    1: "curriculum_title",
    2: "security_domain_id",
    3: "security_domain_description",
    4: "active",
    5: "date_created",
    6: "curriculum_description",
    7: "subsequent_failures_reset_curriculum_status",
    8: "item_type",
    9: "item_id",
    10: "item_revision_date",
    11: "revision_number",
    12: "item_title",
    13: "assignment_type",
    14: "initial_period_item",
    15: "initial_number_item",
    16: "initial_basis_item",
    17: "retraining_period_item",
    18: "retraining_number_item",
    19: "retraining_basis_item",
    20: "effective_date",
    21: "job_classification_id",
    22: "job_description",
    23: "requirement_requirements",
    24: "initial_period_requirement",
    25: "initial_number_requirement",
    26: "initial_basis_requirement",
    27: "retraining_period_requirement",
    28: "retraining_number_requirement",
    29: "retraining_basis_requirement",
    30: "requirement_group",
    31: "initial_period_requirement_group",
    32: "initial_number_requirement_group",
    33: "initial_basis_requirement_group",
    34: "retraining_period_requirement_group",
    35: "retraining_number_requirement_group",
    36: "retraining_basis_requirement_group",
    37: "group_requirements",
    38: "description",
    39: "document_link_id",
    40: "document_link_title",
    41: "review_flag",
    42: "sub_curriculum_id",
    43: "sub_curriculum_title",
    44: "sub_curriculum_parent_id",
    45: "sub_curriculum_level",
}

CIS_COLUMNS = {
    0: "user",
    1: "active_user",
    2: "first_name",
    3: "last_name",
    4: "middle_name",
    5: "curriculum_id",
    6: "curriculum_title",
    7: "completed",
    8: "assignment_date",
    9: "days_remaining",
    10: "item_id",
    11: "item_type",
    12: "item_revision_date",
    13: "revision_number",
    14: "item_title",
    15: "completion_date",
    16: "completion_status_id",
    17: "completion_status",
    18: "required_date",
}

# ============================================================
# HELPERS
# ============================================================

def ensure_output_dir(path):
    os.makedirs(path, exist_ok=True)

def read_report(path, rename_map):
    ext = os.path.splitext(path)[1].lower()

    if ext in [".xlsx", ".xls"]:
        df = pd.read_excel(path, header=0, dtype=str)
    else:
        df = pd.read_csv(path, header=0, dtype=str, encoding="utf-8-sig")

    if len(df.columns) < len(rename_map):
        raise ValueError(
            f"{os.path.basename(path)} has only {len(df.columns)} columns, "
            f"but expected at least {len(rename_map)}."
        )

    df = df.iloc[:, :len(rename_map)].copy()
    df.columns = [rename_map[i] for i in range(len(rename_map))]

    for col in df.columns:
        df[col] = df[col].fillna("").astype(str).str.strip()

    return df

def unique_nonblank(series):
    return sorted({str(x).strip() for x in series if str(x).strip() != ""})

def to_number(value):
    text = str(value).strip()
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

def get_item_due_days(number_value, period_value):
    number = to_number(number_value)
    period = str(period_value).strip().lower()

    if number is None or period == "":
        return ""

    day_multipliers = {
        "day": 1, "days": 1,
        "week": 7, "weeks": 7,
        "month": 30, "months": 30,
        "year": 365, "years": 365,
    }

    multiplier = day_multipliers.get(period)
    if multiplier is None:
        return ""

    return format_number(number * multiplier)

def get_item_due_label(number_value, period_value):
    due_days = get_item_due_days(number_value, period_value)
    if due_days == "":
        return ""
    day_word = "day" if due_days == "1" else "days"
    return f"Due {due_days} {day_word} after assignment"

def save_output(df, output_dir, file_name):
    primary_path = os.path.join(output_dir, file_name)
    try:
        df.to_csv(primary_path, index=False)
        return primary_path
    except PermissionError as exc:
        fallback_path = os.path.join(os.getcwd(), file_name)
        if os.path.abspath(fallback_path) == os.path.abspath(primary_path):
            raise PermissionError(
                f"Could not write to {primary_path}. "
                "Close the file if it is open, or change OUTPUT_DIR."
            ) from exc
        df.to_csv(fallback_path, index=False)
        print(
            f"Could not write to configured output path: {primary_path}\n"
            f"Saved to fallback path instead: {fallback_path}"
        )
        return fallback_path

# ============================================================
# MAIN
# ============================================================

def main():
    ensure_output_dir(OUTPUT_DIR)

    print("Loading reports...")
    cd = read_report(CURRICULUM_DATA_FILE, CD_COLUMNS)
    cis = read_report(USER_CURRICULUM_ITEM_STATUS_FILE, CIS_COLUMNS)

    if cd.empty and cis.empty:
        print("Both input files are empty.")
        return

    # --------------------------------------------------------
    # STEP 1: Curriculum Data — primary structure source
    # --------------------------------------------------------
    cd_structure = cd.copy()

    cd_structure["initial_due_days_item"] = cd_structure.apply(
        lambda row: get_item_due_days(
            row["initial_number_item"],
            row["initial_period_item"],
        ),
        axis=1,
    )
    cd_structure["initial_due_label_item"] = cd_structure.apply(
        lambda row: get_item_due_label(
            row["initial_number_item"],
            row["initial_period_item"],
        ),
        axis=1,
    )
    cd_structure["source"] = "curriculum_data"

    cd_output = cd_structure[
        [
            "curriculum_id",
            "curriculum_title",
            "sub_curriculum_id",
            "sub_curriculum_title",
            "sub_curriculum_parent_id",
            "sub_curriculum_level",
            "item_id",
            "item_title",
            "item_type",
            "item_revision_date",
            "revision_number",
            "assignment_type",
            "initial_due_days_item",
            "initial_due_label_item",
            "requirement_requirements",
            "requirement_group",
            "group_requirements",
            "active",
            "effective_date",
            "source",
        ]
    ].drop_duplicates().copy()

    # --------------------------------------------------------
    # STEP 2: Curriculum Item Status — fills item gaps
    # Scoped to one representative user per site
    # Only keeps items tied to curricula found in Curriculum Data
    # --------------------------------------------------------
    curriculum_ids_from_cd = set(unique_nonblank(cd["curriculum_id"]))

    cis_structure = cis[cis["curriculum_id"].isin(curriculum_ids_from_cd)].copy()

    cis_structure = cis_structure[
        [
            "curriculum_id",
            "curriculum_title",
            "item_id",
            "item_title",
            "item_type",
            "item_revision_date",
            "revision_number",
        ]
    ].drop_duplicates().copy()

    # CIS does not have subcurriculum or hierarchy fields
    cis_structure["sub_curriculum_id"] = ""
    cis_structure["sub_curriculum_title"] = ""
    cis_structure["sub_curriculum_parent_id"] = ""
    cis_structure["sub_curriculum_level"] = ""
    cis_structure["assignment_type"] = ""
    cis_structure["initial_due_days_item"] = ""
    cis_structure["initial_due_label_item"] = ""
    cis_structure["requirement_requirements"] = ""
    cis_structure["requirement_group"] = ""
    cis_structure["group_requirements"] = ""
    cis_structure["active"] = ""
    cis_structure["effective_date"] = ""
    cis_structure["source"] = "curriculum_item_status"

    cis_output = cis_structure[
        [
            "curriculum_id",
            "curriculum_title",
            "sub_curriculum_id",
            "sub_curriculum_title",
            "sub_curriculum_parent_id",
            "sub_curriculum_level",
            "item_id",
            "item_title",
            "item_type",
            "item_revision_date",
            "revision_number",
            "assignment_type",
            "initial_due_days_item",
            "initial_due_label_item",
            "requirement_requirements",
            "requirement_group",
            "group_requirements",
            "active",
            "effective_date",
            "source",
        ]
    ].drop_duplicates().copy()

    # --------------------------------------------------------
    # STEP 3: Combine — prefer Curriculum Data over CIS
    # --------------------------------------------------------
    combined = pd.concat([cd_output, cis_output], ignore_index=True)

    combined["source_rank"] = combined["source"].map({
        "curriculum_data": 1,
        "curriculum_item_status": 2,
    })

    combined = combined.sort_values(
        by=["curriculum_id", "sub_curriculum_id", "item_id", "source_rank"],
        na_position="last"
    ).copy()

    combined = combined.drop_duplicates(
        subset=[
            "curriculum_id",
            "sub_curriculum_id",
            "item_id",
            "item_revision_date",
            "revision_number",
        ],
        keep="first"
    ).copy()

    combined = combined.drop(columns=["source_rank"])

    # --------------------------------------------------------
    # STEP 4: Row type labels
    # --------------------------------------------------------
    def get_row_type(row):
        has_sub = str(row["sub_curriculum_id"]).strip() != ""
        has_item = str(row["item_id"]).strip() != ""
        if has_sub and has_item:
            return "subcurriculum_item"
        if has_sub:
            return "subcurriculum"
        if has_item:
            return "curriculum_item"
        return "curriculum"

    combined["row_type"] = combined.apply(get_row_type, axis=1)

    # --------------------------------------------------------
    # STEP 5: Sort
    # --------------------------------------------------------
    combined["sub_curriculum_level_num"] = pd.to_numeric(
        combined["sub_curriculum_level"], errors="coerce"
    )

    combined = combined.sort_values(
        by=[
            "curriculum_id",
            "sub_curriculum_level_num",
            "sub_curriculum_id",
            "item_id",
            "item_revision_date",
            "revision_number",
        ],
        na_position="last"
    ).copy()

    combined = combined.drop(columns=["sub_curriculum_level_num"])

    # --------------------------------------------------------
    # STEP 6: Export
    # --------------------------------------------------------
    output_path = save_output(combined, OUTPUT_DIR, OUTPUT_FILE_NAME)

    print("\nDone.")
    print(f"Saved file: {output_path}")
    print(f"Rows: {len(combined)}")
    print(f"Curricula: {len(unique_nonblank(combined['curriculum_id']))}")
    print(f"Subcurricula: {len(unique_nonblank(combined['sub_curriculum_id']))}")
    print(f"Items: {len(unique_nonblank(combined['item_id']))}")

if __name__ == "__main__":
    main()