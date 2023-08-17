import db

'''ADDRESS SECTION'''
#address_id |                address                 | address2 |       district       | city_id | postal_code |    phone     |     last_update
def get_all_address():
    columns = ["address", "address2", "district", "city_id", "postal_code", "phone"]
    return db.select(columns, "address")


def get_addresses(ids):
    columns = ["address", "address2", "district", "city_id", "postal_code", "phone"]
    where = "address_id", "in", str(tuple(ids))
    return db.select(columns, "address", (where))

def get_address(customer_id):
    columns = ["address", "address2", "district", "city_id", "postal_code", "phone"]
    where = ("address_id", "=", customer_id)
    return db.select(columns, "address", (where))


def modify_address(id, column_values):
    dict_vals  = column_values
    where = "address_id", "=", int(id)
    return db.update(dict_vals, "address", (where))

def create_address(column_values):
    dict_vals  = column_values
    return db.insert(dict_vals, "address")

def delete_address(id):
  where = "address_id", "=", int(id)
  return db.delete("address", (where))




dict_val_add = {"address":"Begonias 250 santa maria", "address2":".", "district": "azcapotzalco", "city_id":10, "postal_code": "02990", "phone":"62678394"}
#print(create_customer(dict_val_add))
#print(get_all_address())
#print(get_addresses([1,2,3]))
#print(get_address(10))
#print(create_address(dict_val_add))
#print(delete_address(606))
#print(modify_address(606,dict_val_add))
