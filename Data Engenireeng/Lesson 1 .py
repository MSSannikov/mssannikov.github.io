import json
#file = open("text.txt", "r", encoding = "UTF-8")
with open("text.json", "r", encoding = "UTF-8") as f:
    content = json.load(f)



    new_user = { "id": 6, "name": "Massimo", "email": "Massimo.russo@example.com", "role": "Data Scientist" }
    content['Users'].append(new_user)
    #for row in content['Users']:
print(content)

with open("text1.txt", "w", encoding = "UTF-8") as f:
    json.dump(content, f, indent = 4)


    #print(content['Users'])

    #.split(",")

#cleared = [int(i) for i in content]

#print(sum(cleared))
