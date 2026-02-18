from pathlib import Path
import yaml

def load_config(path="config.yml"):
    config_path = Path(path)

    if not config_path.exists():
        raise FileNotFoundError(f"Config file '{path}' não encontrado.")

    with open(config_path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    active = raw["active_profile"]
    profiles = raw["profiles"]

    if active not in profiles:
        raise KeyError(f"active_profile '{active}' não existe em profiles")

    return profiles[active]