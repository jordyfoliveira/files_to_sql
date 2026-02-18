PROFILES = {
    "csv_users": {
        "input": {
            "file": "input/users.csv",
            "sheet_name": None,
            "encoding": "utf-8"
        },
        "output": {
            "file": "output/users.sql",
            "dialect": "postgres",
            "if_not_exists": True
        },
        "table": {
            "name": "users",
            "selected_columns": None,
            "primary_key": "user_id"
        }
    },

    "json_users": {
        "input": {
            "file": "input/sample.json",
            "sheet_name": None
        },
        "output": {
            "file": "output/users_from_json.sql"
        },
        "table": {
            "name": "users_json",
            "selected_columns": None
        }
    }
}

ACTIVE_PROFILE = "json_users"

CONFIG = PROFILES[ACTIVE_PROFILE]