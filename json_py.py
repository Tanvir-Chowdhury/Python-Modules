import json
"""people_string = '''
{
    "people" : [
        {
            "name" : "Tanvir Chowdhury",
            "phone" : "01644916069",
            "age" : 18,
            "college" : true
        },
        {
            "name" : "Tanim Chowdhury",
            "phone" : "01727615289",
            "age" : "12",
            "college" : false
        }
    ]
}
'''

data = json.loads(people_string)

for person in data["people"]:
    #print(person["name"]+" - "+ person["phone"])
    del person["age"]

new_string = json.dumps(data, indent=4, sort_keys=True)
print(new_string)"""

with open("states.json") as f:
    data = json.load(f)
    for state in data["states"]:
        '''state_sym = state["abbreviation"]
        state_name = state["name"]
        print(state_name+" - "+state_sym)'''
        del state["area_codes"]

with open("new_states.json", 'w') as f:
    json.dump(data, f, indent= 4)