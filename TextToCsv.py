import json
import pandas as pd

# the file to be converted to
# json format
filename = 'play_store.txt'

# dictionary where the lines from
# text will be stored
dict1 = {}

# creating dictionary
with open(filename) as fh:

    for line in fh:
        print(line)
        temp = json.loads(line)
        for i in temp:
            if i in dict1:
                dict1[i].append(temp[i])
            else:
                dict1[i] = [temp[i]]

df = pd.DataFrame(dict1)
df.to_csv('play_store.csv')


