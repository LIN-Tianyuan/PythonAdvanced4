import json

with open("America.txt", 'r') as f:
    us_data = f.read()

# print(us_data)
us_data = us_data.replace("jsonp_1629344292311_69436(", "")

us_data = us_data[:-2]
print(type(us_data))
us_python_data = json.loads(us_data)
print(us_python_data['data'])