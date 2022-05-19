# Programmed on 19.5.2022

import pandas as pd
import json

full_df = pd.read_json('LegacyAtomic.json')

return_dict = {}

for i in range(2,len(full_df)):
    try:
        dict = full_df.iloc[i]['data'][0]
        if len(dict['subtypes']) > 1 and 'Creature' in dict['types']:
            return_dict[dict['name']] = [dict['subtypes'], dict['colorIdentity']]
    except Exception:
        pass

with open("CreatureSubtypes.json", "w") as outfile:
    json.dump(return_dict, outfile)