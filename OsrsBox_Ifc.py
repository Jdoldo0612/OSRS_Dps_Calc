from osrsbox import items_api

all_db_items = items_api.load()

for item in all_db_items:
    if(item.name.lower() == "dragon scimitar"):
        print(item.name)
