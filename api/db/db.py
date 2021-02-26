from datetime import datetime

from db.schema import *

def check_psychoterapists(new_set, new_ids_set):
    current_array = Psychotherapists.select(
        Psychotherapists.store_id,
        Psychotherapists.name,
        Psychotherapists.photo_url_small,
        Psychotherapists.photo_url_full,
        Psychotherapists.methods,
        Psychotherapists.created_time
    )

    current_set = set(ps.toTuple() for ps in current_array)

    if new_set == current_set:
        return
    else:
        new_or_updated_records = [dict(item) for item in new_set.difference(current_set)]
        deleted_ids = set()
        if current_set.difference(new_set):
            current_ids = set(ps.store_id for ps in current_array)
            deleted_ids = current_ids.difference(new_ids_set)

    if new_or_updated_records:
        for row in db.batch_commit(new_or_updated_records, 100):
            Psychotherapists.insert(**row).on_conflict(
                conflict_target=[Psychotherapists.store_id],
                update={
                    Psychotherapists.name: row.get('name'),
                    Psychotherapists.photo_url_small: row.get('photo_url_small'),
                    Psychotherapists.photo_url_full: row.get('photo_url_full'),
                    Psychotherapists.methods: row.get('methods'),
                    Psychotherapists.created_time: row.get('created_time')
                }
            ).execute()

    if deleted_ids:
        Psychotherapists.delete().where(Psychotherapists.store_id << deleted_ids).execute()

def write_raw_data(data):
    ScriptExecutionResults.create(start_date=datetime.now(), data=data).save()

def get_psychotherapists():
    return [ps.toDict() for ps in Psychotherapists.select().iterator()]

def get_psychotherapist(id):
    return Psychotherapists.get_by_id(id).toDict()
