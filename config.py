CONFIG = {
    "input": {
        "file": "input/users.csv",
        "sheet_name": None,
        "encoding": "utf-8"
    },
    "output": {
        "file": "output/users.sql",
        "dialect": "postgres",   # postgres | mysql | sqlite
        "if_not_exists": True
    },
    "table": {
        "name": "users",
        "selected_columns": None,
        "primary_key": "user_id"
    }
}