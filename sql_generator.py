def map_dtype(dtype):
    dtype = str(dtype)

    if "int" in dtype:
        return "INTEGER"
    if "float" in dtype:
        return "FLOAT"
    if "datetime" in dtype:
        return "TIMESTAMP"
    return "VARCHAR(255)"

def sanitize_column(name):
    return name.strip().replace(" ", "_").lower()

def generate_create_table(df, table_name):
    columns_sql = []

    for col in df.columns:
        col_name = sanitize_column(col)
        sql_type = map_dtype(df[col].dtype)
        columns_sql.append(f"{col_name} {sql_type}")

    columns_block = ",\n  ".join(columns_sql)

    return f"CREATE TABLE {table_name} (\n  {columns_block}\n);"

def generate_inserts(df, table_name):
    statements = []

    for _, row in df.iterrows():
        values = []
        for value in row:
            if value is None:
                values.append("NULL")
            elif isinstance(value, str):
                escaped = value.replace("'", "''")
                values.append(f"'{escaped}'")
            else:
                values.append(str(value))

        values_sql = ", ".join(values)
        statements.append(f"INSERT INTO {table_name} VALUES ({values_sql});")

    return statements