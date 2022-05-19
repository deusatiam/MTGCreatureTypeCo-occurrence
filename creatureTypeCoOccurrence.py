# Programmed on 19.5.2022
import pandas as pd
import json

types_df = pd.read_json('SubtypeSimilarities.json').T
types_df.columns = ['Co-occurrences', 'Count']
types_df = types_df.sort_values(by=['Count'], ascending=False)

return_dict = {}

for i in range(len(types_df)):
    temp_dict = types_df.iloc[i]['Co-occurrences']
    sorted_dict = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
    return_dict[types_df.iloc[i].name] = [dict(sorted_dict), types_df.iloc[i]['Count']]

with open("CreatureTypeCoOccurrences.json", "w") as outfile:
    json.dump(return_dict, outfile)

