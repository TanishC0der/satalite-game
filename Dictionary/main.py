ages={
    "Tanish":11,
    "Max":12,
    "Priyal":44
}
#accesing elements inside a dictionary
print(ages["Tanish"])
#getting keys
ages2=ages.keys()
print(ages2)
#getting values
ages3=ages.values()
print(ages3)
#getting key value
ages4=ages.items()
print(ages)
#checking if a key exists
if "Tanish" in ages:
    print("Tanish is in the dictionary")
else:
    print("Tanish is not in the dictionary")
#changing value
ages["Max"]=15
print(ages)
#changing a key value
ages.pop("Max")
ages["Pratham"]=18
print(ages)
#looping through the dictionarry
for ages5 in ages:
    print(ages5)
    
#looping through the vakues
for ages5 in ages.values():
    print(ages5)
#nested dictionary
school={
    "5A":{
        "John":{
            "Maths":90,
            "English":40,

        }
    },
    "5B":{
        "Tanish":{
            "Science":150,
            "Maths":100,

        }
    }
}