from config_loader import load_config
from converter import convert_to_sql

if __name__ == "__main__":
    CONFIG = load_config("config.yml")
    convert_to_sql(CONFIG)