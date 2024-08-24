import json
split_size = 960 
with open('book_info.json', 'r') as json_file:
    original_data = json.load(json_file)

current_part = 1
current_part_data = []

for index, entry in original_data.items():
    current_part_data.append({index: entry})

    if len(current_part_data) >= split_size:
        with open(f'part_{current_part}.json', 'w') as part_json_file:
            json.dump(current_part_data, part_json_file, indent=4)

        current_part += 1
        current_part_data = []

if current_part_data:
    with open(f'part_{current_part}.json', 'w') as part_json_file:
        json.dump(current_part_data, part_json_file, indent=4)

print(f'Split into {current_part} parts.')
