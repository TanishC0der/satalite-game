for i in range(5):
    print(f"\nEnter the details for the group {i+1}")
    group_name=input("Enter the group name")
    size_of_the_group=int(input("Enter the size of the group"))
    date_of_the_comp=int(input("Write the date of the competion"))
    Venue=input("Write the venue")
    Type_of_medal=input("Enter the type of medal:Gold ,Silver or Bronze")
    group_record=(group_name,size_of_the_group,date_of_the_comp,Venue,Type_of_medal)

for i in group_record:
    print(i)