# We use dictionaries to set KEY VALUE PAIRS
# Like infos of a customer (name, phone, etc)

customer = {
    "name": "John Smith",
    "age": "30",
    "is_verified": True
}

print(customer["name"])

# this way with the method "get", we don't receive an error, just a message saying 'None'
print(customer.get("birthdate"))

# Here we set a default value for a 'variable' that doesn't exist
# But it doesn't update the dictionary
print(customer.get("birthdate", 'Jan 1 1998'))

customer["name"] = "Felps"
customer["birthdate"] = "Sep 24 2003"

print(customer)
print(customer["birthdate"])
