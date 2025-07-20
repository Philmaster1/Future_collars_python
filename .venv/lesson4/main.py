list_names = ["Adam", "Ewa", "Wojtek", "alberta", "Robert", "Marcin", "Michal"]


list_name_females = [firstname for firstname in list_names if firstname[-1] == "a"]
list_name_males = [firstname for firstname in list_names if firstname[-1] != "a"]
print(list_name_females)
print(list_name_males)




url = "https://api.agify.io"

params = {
    "name": "Marek"}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['name']}, Age: {data['age']}, Count: {data['count']}")
else:
    print(f"Error: {response.status_code}")