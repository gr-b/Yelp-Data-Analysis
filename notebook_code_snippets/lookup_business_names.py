import json, prettytable

# The file to decode each business id
with open('business_lookup.json','r') as lookup_file:
    read = lookup_file.read().strip()
    lookup_table = json.loads(read)

# The file with the top ten business ids and counts
with open('checkin_table.json','r') as checkin_file:
    read = checkin_file.read().strip()
    checkin_table = json.loads(read)

final_table = {}

for business_id in checkin_table.keys():
    business_name = lookup_table[business_id]
    business_count = checkin_table[business_id]

    final_table[business_name] = business_count

table = prettytable.PrettyTable(['Business Name','Checkin Count'])
sorted_items = sorted(final_table.items(), key=lambda x: x[1], reverse=True)
for row in sorted_items:
    table.add_row(row)

with open('business_count_table.txt', 'w') as outfile:
    outfile.write(str(table))
