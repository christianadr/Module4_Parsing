import json 
import yaml

# example of json
x = '{"name": "John", "age": "30", "city": "New York City"}'

# parse json
y = json.loads(x)
print(f"The output of json file is {y}")
print(f"Age: {y['age']}")
print(f"Name: {y['name']}")
print(f"City: {y['city']}")