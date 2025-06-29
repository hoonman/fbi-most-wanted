import requests
import threading
import time

class FBIService:
    def __init__(self):
        self.base_url = 'https://api.fbi.gov/wanted/v1/list'
        self.cache = {'items':[],'last_updated': None}
        self._refresh_data()

    def _refresh_data(self):
        all_items = []
        page = 1
        while True:
            response = requests.get(self.base_url, params={'page': page})
            if response.status_code != 200:
                break
            data = response.json().get('items', [])
            if not data:
                break
            all_items.extend(data)
            # if page % 10 == 0:
            #     time.sleep(5)
            page += 1
            print(f"page num: {page} \t total: {page * 20}")
        self.cache['items'] = all_items
        self.cache['last_updated'] = time.time()

    def schedule_refresh(self, interval_hours=24):
        def loop():
            while True:
                time.sleep(interval_hours * 3600)
                self._refresh_data()
        thread = threading.Thread(target= loop, daemon=True)
        thread.start()

    '''
    this function gets the list with specified pages
    '''
    def get_list(self, page=1, page_size=20, filters=None):
        items = self.cache['items']
        total = len(items)
        start = (page - 1) * page_size
        end = start + page_size
        return items[start:end], total

    '''
    this function retrieves details of a FBI wanted criminal by uid
    '''
    def get_details(self, item_id): 
        for item in self.cache['items']:
            if str(item.get('uid')) == item_id:
                return item
        return None
    
    '''
    this function retrieves the existing 'field offices' from cache
    '''
    def get_field_offices(self):
        field_offices = set()
        items = self.cache['items']
        for item in items:
            if 'field_offices' in item and item['field_offices']:
                if item != None and item['field_offices'] != None and item['field_offices']:
                        new_set = set(item['field_offices'])
                        field_offices = field_offices | new_set

        return list(field_offices)

        

