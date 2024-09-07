WCD={
    "France":"Paris",
    "Japan":"Tokyo",
    "Canada":"Ottawa"
}

print(WCD["Canada"])
 
if "Japan"in WCD:
    print("Japan is in the dictionary")
else:
    print("Japan is not in the dictonary")

for WCD2 in WCD:
    print(WCD2)