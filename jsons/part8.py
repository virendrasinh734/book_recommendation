import json

with open("./jsons/part_8.json", "r") as infile:
    data = json.load(infile)

start_index = next((i for i, item in enumerate(data) if int(next(iter(item))) > 7107), len(data))

elements_after_7107 = data[start_index:]

with open("modified.json", "w") as outfile:
    json.dump(elements_after_7107, outfile, indent=4)

print("Elements after '7107' from part_8.json have been written to modified.json")
