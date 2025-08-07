list_names = ["Adam", "Ewa", "Wojtek", "alberta", "Robert", "Marcin", "Michal"]


list_name_females = [firstname for firstname in list_names if firstname[-1] == "a"]
list_name_males = [firstname for firstname in list_names if firstname[-1] != "a"]
print(list_name_females)
print(list_name_males)




import requests
url = "https://api.agify.io"
params = {"name": "John"}

response = requests.get(url, params)

if response.status_code == 200:
    data = response.json()
    print(data["count"])
    print(data["name"])
    print(data["age"])

else:
    print(f"Error:{response:status_code}")