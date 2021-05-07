import json
import pandas as pd

def gen_json(index, person):
    person = person.to_json(force_ascii=False)
    person = json.loads(person)
    fixture = {
        "model": "accounts.person",
        "pk": index + 1,
        "fields": person
    }
    return fixture

with open("people_data.json", "w") as file:
    people_df = pd.read_csv("people_data.csv")
    people_iter = people_df.iterrows()
    people_json = [gen_json(i, d) for i, d in people_iter]
    json.dump(people_json, file)
