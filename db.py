import psycopg

CONN_STRING = "dbname=dvdrental user=postgres password=postgres host=localhost port=5432"

def select(columns, table_name, where=None):
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            column_list = ", ".join(columns)
            #("_id", "in", "(1,2.3)")
            # "_id in (1,2,3)"
            where_string = f'WHERE {where[0]} {where[1]} {where[2]}' if where else ""
            query =f'SELECT {column_list} FROM {table_name} {where_string};'
            cur.execute(query)
            result = cur.fetchall()
    return result


def update(column_value, table_name, where=None):
  with psycopg.connect(CONN_STRING) as conn:
      with conn.cursor() as cur:
          values = [f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {str(value)}"  for key, value in column_value.items()]
          value_list = ', '.join(values) #Can concatenate not str values
          where_string = f'WHERE {where[0]} {where[1]} {where[2]}'
          query =f'UPDATE {table_name} SET {value_list} {where_string};'
          print(query)
          cur.execute(query)
  return f'Parametro Actualizado -> {select("*", table_name, where)}'


def insert(column_value, table_name):
  with psycopg.connect(CONN_STRING) as conn:
      with conn.cursor() as cur:
          columns = [column for column in column_value.keys()]
          values = [f"'{value}'" if isinstance(value, str) else str(value) for value in column_value.values()]
          column_list = ", ".join(columns)
          value_list = ', '.join(values) #Can concatenate not str values
          query =f'INSERT INTO {table_name} ({column_list}) VALUES ({value_list});'
          cur.execute(query)
          result = f"Parametro Creardo -> {column_value}"
  return result



def delete(table_name, where):
  with psycopg.connect(CONN_STRING) as conn:
      with conn.cursor() as cur:
          where_string = f'WHERE {where[0]} {where[1]} {where[2]}'
          print(table_name)
          print(where_string)
          #("_id", "in", "(1,2.3)")
          # "_id in (1,2,3)"
          query =f'DELETE FROM {table_name} {where_string};'
          print(query)
          cur.execute(query)
          result = f"Parametro de la tabla {table_name} Eliminado | ID -> {where[2]}"
  return result