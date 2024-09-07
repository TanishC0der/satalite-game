#creating tuple
house=(61,"Broadwood" ,"Drive")
house=61,"Broadwood" ,"Drive"

print (house)

print(house[1])

# itterating through a tuple
for element in house:
    print(element)

#packing
address=("12","Redwing Drive","Preston","England")

#unpacking
house_number,street_name,city,country=address

print(house_number)

print(country)
#nested tuple
book=("Harry potter","Chamber of Secrets" ,[1,2,3],[4,5,6])
print(book[2])
print(book[3][1])

book[3][0]=9
print(book)

#access tuple element using slicing
my_Tuple=("a","b","c",1,2,3,4,5,6,7,8,9)
#elemnt2nd to 4th
print(my_Tuple[1:4])
print(my_Tuple[5:])
print(my_Tuple[2:10])