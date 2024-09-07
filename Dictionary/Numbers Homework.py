Numbers={}

user_number=input("Write some numbers please \n Numbers:")

for character in user_number:
    if character.isdigit():
        if character in Numbers:
            Numbers[character]+=1
        else:
            Numbers[character]=1
    else:
        print("Invalid set of numbers! Please try again!")
       
print(Numbers)
