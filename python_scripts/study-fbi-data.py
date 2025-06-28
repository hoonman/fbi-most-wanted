import requests
import json
import time

response = requests.get('https://api.fbi.gov/wanted/v1/list')
data = json.loads(response.content) 

page_num = 1
current_total = 0
actual_total = data['total']
most_wanted_list = []

while current_total < actual_total:
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page':page_num})
    if response.status_code != 200 or not response.content:
        print(f"Error or empty response at page {page_num}, stopping. status code was: {response.status_code}")
        break
    try:
        data = json.loads(response.content)
        if 'items' not in data or not data['items']:
            print(f"No items found at page {page_num}, stopping")
            break
        most_wanted_list.extend(data['items'])
        data_items_num = len(data['items'])
        current_total += data_items_num
        print("finished page num: ", page_num, "\t total: ", current_total)
        page_num += 1
        if page_num % 10 == 0:
            print("sleeping...")
            time.sleep(5)
    except json.JSONDecodeError:
        print(f"Invalid JSON response at page {page_num}, stopping")
        break

print("total: ", current_total)

# after getting all the criminals into a list, let's write that into a giant file
with open('fbi-data-all.json', 'w') as f:
    json.dump(most_wanted_list, f, indent=4)
