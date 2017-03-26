import json, prettytable

data = open('yelp_academic_dataset_business.json','r')

categ = {}

#i = 0
for line in data:
    business = json.loads(line.strip())
    categories = business['categories']
    if categories is None:
        continue
    for category in categories:
        if category not in categ.keys():
            categ[category] = 1
        else:
            categ[category] += 1
    #print json.dumps(business, indent=2)
    #i +=1
    #if i >100:
    #    break

#Get the top ten most frequent categories
categories = categ.items()
sorted_categories = sorted(categories, key=lambda x: x[1], reverse=True)
#print sorted_categories[0:10]
table = prettytable.PrettyTable(['Category','Count of businesses in category'])
for row in sorted_categories[0:10]:
    table.add_row(row)
print table




