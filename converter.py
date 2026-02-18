import pandas as pd
from sql_generator import generate_create_table, generate_inserts

def convert_to_sql(config):
    input_file = config["input"]["file"]
    sheet_name = config["input"]["sheet_name"]
    table_name = config["table"]["name"]
    selected_columns = config["table"]["selected_columns"]
    output_file = config["output"]["file"]

    # Ler ficheiro
    if input_file.endswith(".csv"):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file, sheet_name=sheet_name)

    # Selecionar colunas se definido
    if selected_columns:
        df = df[selected_columns]

    create_stmt = generate_create_table(df, table_name)
    insert_stmts = generate_inserts(df, table_name)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(create_stmt + "\n\n")
        for stmt in insert_stmts:
            f.write(stmt + "\n")

    print("SQL gerado com sucesso.")