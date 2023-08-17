import db


'''CUSTOMER SECTION'''
def get_all_customers():
    columns = ["customer_id", "first_name", "last_name", "email", "activebool"]
    return db.select(columns, "customer")


def get_customers(ids):
    columns = ["customer_id", "first_name", "last_name", "email", "activebool"]
    where = "customer_id", "in", str(tuple(ids))
    return db.select(columns, "customer", (where))

def get_customer(customer_id):
    columns = ["customer_id", "first_name", "last_name", "email", "activebool"]
    where = ("customer_id", "=", customer_id)
    return db.select(columns, "customer", (where))

def get_customer_by_status(status=True):
    columns = ["customer_id", "first_name", "last_name", "email", "active"]
    where = ("active", "=", int(status))
    return db.select(columns, "customer", (where))

def modify_customer(id, column_values):
    dict_vals  = column_values
    where = "customer_id", "=", int(id)
    return db.update(dict_vals, "customer", (where))

def create_customer(column_values):
    dict_vals  = column_values
    return db.insert(dict_vals, "customer")

def delete_customer(id):
  where = "customer_id", "=", int(id)
  return db.delete("customer", (where))

def deactivate_customer(id):
  where = "customer_id", "=", int(id)
  return db.update({"active":0}, "customer", (where))



dict_val = {"first_name":"rockdrigo", "last_name":"zavala", "store_id": 1, "address_id":14, "activebool": False}
#print(create_customer(dict_val))
#print(get_all_customers())
#print(get_customers([1,2,3]))
#print(get_customer(10))
#print(get_customer_by_status(True))
#print(create_customer(dict_val))
#print(delete_customer(605))
#print(modify_customer(611,dict_val))
#print(deactivate_customer(611))