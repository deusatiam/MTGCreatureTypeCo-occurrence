# Programmed on 19.5.2022

import pandas as pd
from itertools import permutations
import json

subtype_df = pd.read_json('CreatureSubtypes.json').T
subtype_df.columns = ['Subtypes', 'ColorId']

# The structure of this dictionary is as follows
# dict{string: list[dict{string: int}, int]}
# The overall dictionary combines a creature type with an array that keeps track of co-occurrences with other creature types in another dictionary, as well as a count of total 
# occurrences
dict = {}

# Permutations used for adding all the creature types to each others' dictionaries
perms = {
    2: list(permutations([0,1],2)),
    3: list(permutations([0,1,2],2)),
    4: list(permutations([0,1,2,3],2))
}

for i in range(len(subtype_df)):
    subtypes = subtype_df.iloc[i]['Subtypes']
    for permutation in perms[len(subtypes)]:
        # Check if first creature type is in main dictionary, then if the second creature type is in the first creature type's dictionary
        # If so, add one occurrence
        if subtypes[permutation[0]] in dict.keys() and subtypes[permutation[1]] in dict[subtypes[permutation[0]]][0].keys():
            dict[subtypes[permutation[0]]][0][subtypes[permutation[1]]] += 1
            dict[subtypes[permutation[0]]][1] += 1
        # Check if first creature type is in main dictionary. The previous check has not passed, so the second creature type is not in the first's dictionary
        # If so, add the second creature type to the first's dictionary
        elif subtypes[permutation[0]] in dict.keys():
            dict[subtypes[permutation[0]]][0][subtypes[permutation[1]]] = 1
            dict[subtypes[permutation[0]]][1] += 1
        # If the first creature type is not in the main dictionary, add it and initialize it's subdictionary
        else:
            dict[subtypes[permutation[0]]] = [{subtypes[permutation[1]]: 1}, 1]


with open("SubtypeSimilarities.json", "w") as outfile:
    json.dump(dict, outfile)