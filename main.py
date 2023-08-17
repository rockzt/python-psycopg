import psycopg

#connection string
try:
  conn = psycopg.connect("dbname=dvdrental user=postgres password=postgres host=localhost port=5432")
  cursor = conn.cursor()

  cursor.execute(
      """
      SELECT customer_id, first_name, last_name FROM customer ORDER BY last_name;
      """
  )
  print("Clients List")
  for cust_id, name, last_name in cursor.fetchall():
    print(f"Cliente {cust_id}: {last_name} , {name}")
  #single_row = cursor.fetchone()
  #print(f"Single Row -> {single_row}")
  #many_row = cursor.fetchmany(5)
  #print(f"Many Rows -> {many_row}")
  #all_rows = cursor.fetchall()
  #print(f"All Rows -> {all_rows}")
  cursor.close()
  conn.close()
except psycopg.OperationalError as e:
  print(f"Error connecting to DB  ->{e}")



#CRATE TABLE INSTRUCTION
'''
CONN_STRING = "dbname=dvdrental user=postgres password=postgres host=localhost port=5432"

table_name  = "test"
columns = [
  ("id", "serial", "PRIMARY KEY"),
  ("NUM", "integer", ""),
  ("data", "text",  "")
]

with psycopg.connect(CONN_STRING) as connection:
  print("connection successful")
  col_string = ",".join([" ".join(col) for col in columns])
  print(col_string)
  cursor = connection.execute(f'CREATE TABLE {table_name}({col_string})')
'''

'''
#INSERT INSTRUCTION
CONN_STRING = "dbname=dvdrental user=postgres password=postgres host=localhost port=5432"

table_name  = "test"


with psycopg.connect(CONN_STRING) as connection:
  print("connection successful")
  with connection.cursor() as cursor:
      cursor.execute("insert into test (NUM, data) VALUES (%s, %s)", (100, "cualquier"))
  connection.commit()
  #connection.rollback()
'''


#BASIC CRUD FUNCTIONS
CONN_STRING = "dbname=dvdrental user=postgres password=postgres host=localhost port=5432"

table_name_d  = "customer"

def get_all_customer(): #Lista de clientes
  data = None
  with psycopg.connect(CONN_STRING) as connection:
    print("connection successful")
    with connection.cursor() as cursor:
       cursor.execute(f'SELECT * FROM {table_name_d}')
       data = cursor.fetchall()
  return data


def get_customers(list_customers: list): # [("1","rock","zav"), (otro_usuario)]
  data = None
  customers = str(list_customers).replace('[', '').replace(']', '')
  with psycopg.connect(CONN_STRING) as connection:
    print("connection successful")
    print(customers)
    with connection.cursor() as cursor:
      cursor.execute(f'SELECT * FROM {table_name_d} WHERE customer_id IN ({customers})')
      data = cursor.fetchall()
  return data


def get_customer(num_customer:int): #Datos de un cliente
  data = None
  customer_id = num_customer
  with psycopg.connect(CONN_STRING) as connection:
    print("connection successful")
    with connection.cursor() as cursor:
      cursor.execute(f'SELECT * FROM {table_name_d} WHERE customer_id = {customer_id}')
      data = cursor.fetchall()
  return data


def get_customers_by_status(status: bool): #Clientes activos o inactivos
  data = None
  status_customers = status
  with psycopg.connect(CONN_STRING) as connection:
    print("connection successful")
    with connection.cursor() as cursor:
      cursor.execute(f'SELECT * FROM {table_name_d} WHERE activebool = {status_customers}')
      data = cursor.fetchall()
  return data



#Calling Fuctions
print(get_all_customer())
print(get_customers([1,2,3,4,5,6]))
print(get_customer(10))
print(get_customers_by_status(True))
