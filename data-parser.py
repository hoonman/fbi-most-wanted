import requests
import json



# 53 is the maximum number of pages. but this can probably change...

# response = requests.get('https://api.fbi.gov/wanted/v1/list')
# response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
#     'page': 53
# })

# for i in range(0, 54):
#     print(i)
#     response = requests.get('https://api.fbi.gov/wanted/v1/list', params = {
#         'page': i
#     })
#     data = json.loads(response.content)

#     # load the data into a file
#     with open(f"fbi-data-{i}.json", "w") as f:
#         json.dump(data, f, indent=4)



# some questions we can answer with this data
# out of the fbi's most wanted list, how many have unknown name? unknown height? 




# let us design this parser.
# this parser will have the following methods

# function that will load json data into a dictionary so we can easily use it
# input: maximum page number, 
# output: dicionary of fbi's most wanted criminals

class Parser:

    def __init__(self):
        self.total_count = 0
        self.most_wanted = {}

    def get_fbi_data(self, max_page_num):
        # we are going to try except here i think

        for i in range(1, max_page_num):
            response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page':i})
            new_map = json.loads(response.content)


parser = Parser()
parser.get_fbi_data(5)
print('most wanted: ', parser.most_wanted)
