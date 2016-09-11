from collections import Counter
import json

with open('open_data_pharmacy.txt') as f:
    pl = f.read().splitlines()

pc = dict(Counter(pl))

with open('pharmacy_count.txt', 'w') as f:
    f.write(json.dumps(pc))
