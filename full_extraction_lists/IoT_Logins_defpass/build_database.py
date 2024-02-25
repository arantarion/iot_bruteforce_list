import json


def create_blocks(text, index):
    blocks = []
    for i in range(len(index)-1):
        start_idx = index[i]
        stop_idx = index[i+1]
        blocks.append(text[start_idx:stop_idx])
        
    return blocks

def create_block(block):
    data = {}
    for item in block:      
        try:
            key, value = item.split(": ")
            data.update({key:value})
        except:
            print(item)
        
    return data

with open("defpass_full_dump_raw.txt", "r") as f:
    text = f.readlines()

text = [x.replace("\n", "") for x in text]
indices = [i for i, x in enumerate(text) if "Vendor" in x]

blocks = create_blocks(text, indices)

results = []
for block in blocks:
    x = create_block(block)
    results.append(x)

with open('defpass_database.json', 'w') as outfile:
    json.dump(results, outfile)