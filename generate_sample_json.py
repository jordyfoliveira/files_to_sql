import json
import random
from datetime import datetime, timedelta

def rand_name():
    first = ["Ana", "Bruno", "Carla", "Diogo", "Eva", "Filipe"]
    last = ["Silva", "Santos", "Ferreira", "Costa", "Oliveira"]
    return f"{random.choice(first)} {random.choice(last)}"

def rand_email(name):
    base = name.lower().replace(" ", ".")
    return f"{base}{random.randint(1,99)}@gmail.com"

def rand_date():
    d = datetime.now() - timedelta(days=random.randint(0, 365))
    return d.date().isoformat()

def generate_json():
    data = []
    for i in range(1, 51):
        name = rand_name()
        data.append({
            "user_id": i,
            "name": name,
            "email": rand_email(name),
            "age": random.randint(18, 65),
            "created_at": rand_date(),
            "is_active": random.choice([True, False])
        })

    with open("input/sample.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("sample.json gerado com sucesso.")

if __name__ == "__main__":
    generate_json()