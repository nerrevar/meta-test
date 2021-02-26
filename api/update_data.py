import os
import json
import requests

# Read config from JSON file
with open(os.path.dirname(__file__) + '/request_settings.json') as f:
    request_settings = json.load(f)

# Construct query
query_url = '{0}/{1}/{2}?{3}'.format(
    request_settings.get('url'),
    request_settings.get('db_id'),
    request_settings.get('table_name'),
    ';'.join(
        [
            k + '=' + v
            for (k,v) in request_settings.get('query_params', {}).items()
        ]
    )
)

# Perform request to api
response = requests.get(query_url)

if response.status_code == 200:
    data = response.json()
else:
    print('Error while retrieving data. Status code: ', response.status_code)
    exit(2)

# Check database connection
from db.db import *
try:
    db.connect()
except:
    print('Error connecting to DB')
    exit(1)

# Write raw results to database
write_raw_data(response.text)

# Check existing of records and create/update/delete if necassary
new_array = []
new_ids_set = set()
for ps in data.get('records'):
    fields = ps.get('fields')
    if fields.get('Фотография'):
        photo_url_small = fields.get('Фотография')[0].get('thumbnails').get('small').get('url')
        photo_url_full = fields.get('Фотография')[0].get('thumbnails').get('full').get('url')
    else:
        photo_url_small = 'undefined'
        photo_url_full = 'undefined'
    new_ids_set.add(ps.get('id'))
    new_array.append({
        'store_id': ps.get('id'),
        'name': ps.get('fields').get('Имя'),
        'photo_url_small': photo_url_small,
        'photo_url_full': photo_url_full,
        'methods': tuple(fields.get('Методы', [])),
        'created_time': ps.get('createdTime')
    })
check_psychoterapists(
    set(
        tuple(sorted(item.items())) for item in new_array
    ),
    new_ids_set
)

db.close()
