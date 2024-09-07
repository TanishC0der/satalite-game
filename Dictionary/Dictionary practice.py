Vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

User_sentence=input("Type in a scentence : ").lower()

for character in User_sentence:
    if character in Vowels:
        Vowels[character]+=1
print("Vowels occurrences")
for vowel in Vowels.items():
    print(vowel)



