import json, prettytable

data = open('yelp_academic_dataset_checkin.json','r')

business_id_counts = {}

i = 0
for line in data:
    checkin = json.loads(line.strip())
    business_id = checkin['business_id']
    if business_id is not None:
        if business_id not in business_id_counts.keys():
            business_id_counts[business_id] = len(checkin['time'])
        else:
            business_id_counts[business_id] += len(checkin['time'])
    #print json.dumps(business, indent=2)
    i +=1
    #if i >10000:
    #    break
    print str(i), 'counted.\r',

#Get the top ten most frequent categories
business_counts = business_id_counts.items()
sorted_counts = sorted(business_counts, key=lambda x: x[1], reverse=True)
table = prettytable.PrettyTable(['Business ID','Count'])
out_counts = {}
for row in sorted_counts[0:10]:
    table.add_row(row)
    out_counts[row[0]] = row[1]

with open('checkin_table.txt', 'w') as outfile:
    outfile.write(str(table))

with open('checkin_table.json', 'w') as outfile:
    outfile.write(json.dumps(out_counts, indent=2))




