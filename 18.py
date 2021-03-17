import json

print(dir(json))

employee = {
    "first_name": "Solam",
    "age": 28,
    "address": "Butwal"
}
json_data = json.dumps(employee, indent=2)
print(json_data)
print(json.loads(json_data))
