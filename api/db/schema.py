import os
import json
from playhouse.postgres_ext import *

with open(os.path.dirname(__file__) + '/db_settings.json') as f:
    db_settings = json.load(f)

db = PostgresqlExtDatabase(
    db_settings.get('dbname'),
    user=db_settings.get('user'),
    password=db_settings.get('password'),
    host=db_settings.get('host', 'localhost'),
    port=db_settings.get('port', 5432)
)

class BaseModel(Model):
    class Meta:
        database = db

class Psychotherapists(BaseModel):
    store_id = TextField(unique=True)
    name = TextField()
    photo_url_small = TextField()
    photo_url_full = TextField()
    methods = ArrayField(TextField)
    created_time = TextField()

    def toDict(self):
        return {
            'id': self.id,
            'store_id': self.store_id,
            'name': self.name,
            'photo_url_small': self.photo_url_small,
            'photo_url_full': self.photo_url_full,
            'methods': self.methods,
            'created_time': self.created_time
        }

    def toTuple(self):
        d = self.toDict()
        del d['id']
        d['methods'] = tuple(d['methods'])
        return tuple(
            sorted(d.items())
        )

class ScriptExecutionResults(BaseModel):
    start_date = DateTimeField()
    data = TextField()
