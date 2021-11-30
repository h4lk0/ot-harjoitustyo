table_insert = {}
table_select = {}

def add_table(table_name):
    table_insert[table_name] = f'"INSERT INTO {table_name} (eng, kor) VALUES (?, ?)"'
    table_select[table_name] = f'"SELECT eng, kor FROM {table_name})"'

def table_getter(table_name):
    return table_select[table_name]

def insert_into_table(table_name):
    return table_insert[table_name]

add_table("Nouns")