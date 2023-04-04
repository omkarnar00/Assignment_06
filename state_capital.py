import json

state_capital=[{"Andhra Pradesh":"Amaravati"},
                {"ArunachalPrades":	"Itanagar"},
                {"Assam"	:"Dispur"},
                {"Bihar":"Patna"},
                {"Chhattisgarh":"Raipur"},
                {"Goa":	"Panaji"},
                {"Gujarat":	"Gandhinagar"}]

with open("state_capital.json","w") as f:
    json.dump(state_capital,f)