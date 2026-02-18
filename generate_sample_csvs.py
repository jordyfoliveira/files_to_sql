import random
import string
from datetime import datetime, timedelta

import pandas as pd


def rand_name():
    first = ["Ana", "Bruno", "Carla", "Diogo", "Eva", "Filipe", "Gina", "Hugo", "Ines", "Joao", "Luis", "Marta"]
    last = ["Silva", "Santos", "Ferreira", "Pereira", "Costa", "Oliveira", "Rodrigues", "Martins", "Almeida"]
    return f"{random.choice(first)} {random.choice(last)}"


def rand_email(name: str):
    domains = ["gmail.com", "outlook.com", "empresa.pt", "proton.me"]
    base = (
        name.lower()
        .replace(" ", ".")
        .replace("ã", "a")
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ç", "c")
    )
    return f"{base}{random.randint(1, 999)}@{random.choice(domains)}"


def rand_phone():
    # estilo PT (sem garantir validade real)
    return f"9{random.randint(10, 99)}{random.randint(100000, 999999)}"


def rand_date(days_back=365):
    d = datetime.now() - timedelta(days=random.randint(0, days_back))
    return d.date().isoformat()


def rand_sku():
    return "SKU-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=8))


def main():
    random.seed(42)

    # -------------------------
    # USERS
    # -------------------------
    n_users = 50
    users = []
    for user_id in range(1, n_users + 1):
        name = rand_name()
        users.append(
            {
                "user_id": user_id,
                "name": name,
                "email": rand_email(name),
                "phone": rand_phone(),
                "created_at": rand_date(730),
                "is_active": random.choice([True, True, True, False]),
            }
        )
    df_users = pd.DataFrame(users)

    # -------------------------
    # PRODUCTS
    # -------------------------
    product_names = [
        "Teclado Mecânico",
        "Rato Gaming",
        "Monitor 27",
        "SSD 1TB",
        "Headphones",
        "Webcam 1080p",
        "Dock USB-C",
        "Cadeira Escritório",
        "Microfone USB",
        "Router Wi-Fi",
    ]

    n_products = 20
    products = []
    for product_id in range(1, n_products + 1):
        products.append(
            {
                "product_id": product_id,
                "sku": rand_sku(),
                "product_name": random.choice(product_names),
                "price": round(random.uniform(9.99, 399.99), 2),
                "in_stock": random.randint(0, 250),
            }
        )
    df_products = pd.DataFrame(products)

    # -------------------------
    # ORDERS (relaciona users e products)
    # -------------------------
    n_orders = 120
    orders = []
    for order_id in range(1, n_orders + 1):
        user_id = random.randint(1, n_users)
        product_id = random.randint(1, n_products)
        qty = random.randint(1, 5)
        unit_price = float(df_products.loc[df_products["product_id"] == product_id, "price"].iloc[0])
        total = round(qty * unit_price, 2)

        orders.append(
            {
                "order_id": order_id,
                "user_id": user_id,
                "product_id": product_id,
                "quantity": qty,
                "unit_price": unit_price,
                "total_price": total,
                "order_date": rand_date(365),
                "status": random.choice(["paid", "pending", "shipped", "cancelled"]),
            }
        )
    df_orders = pd.DataFrame(orders)

    # -------------------------
    # Save CSVs
    # -------------------------
    df_users.to_csv("users.csv", index=False, encoding="utf-8")
    df_products.to_csv("products.csv", index=False, encoding="utf-8")
    df_orders.to_csv("orders.csv", index=False, encoding="utf-8")

    print("CSVs gerados: users.csv, products.csv, orders.csv")


if __name__ == "__main__":
    main()