# meta-test
## Stack
Backend:
* python3
* flask
* peewee (with psycopg2)
* PostgreSQL

Frontend:
* Vue.js
* Vue-router

## Before start
Installing requirements
```
$: pip install -r api/requirements.txt
```
```
$: npm i
```

## Backend
### Database
Project requires database config file 'api/db/db_settings.json':
```
{
  "user": "test",
  "password": "test",
  "host": "localhost",
  "port": 5432,
  "dbname": "test"
}
```
Creating tables:
```
$: cd api
$: python
>>> from db.db import *
>>> db.create_tables([Psychotherapists, ScriptExecutionResults])
>>> exit
```

### Running dev server:
1. Make 'start_dev_server.sh' executable:
```
$: chmod +x start_dev_server.sh
```
1. Run 'start_dev_server.sh':
```
$: ./start_dev_server.sh
```

## Update script
### Usage
Update script requires config file 'api/request_settings.json':
```
{
  "url": API_URL,           // "https://api.airtable.com/v0"
  "db_id": DATABASE_ID,
  "table_name": TABLE_NAME, // "Psychotherapists"
  "query_params": {         // Any number of params
     KEY: VALUE             // "api_key": API_KEY
   }
}
```
1. Make 'start_update.sh' executable:
```
$: chmod +x start_update.sh
```
1. Script execution:
```
$: ./start_update.sh
```

## Frontend
### Build
```
npm run build
```
