Alphabet={}

User_sentence=input("enter a sentence : ").lower()

for character in User_sentence:
    if character .isalpha():
        if character in Alphabet:
            Alphabet[character]+=1
        else:
            Alphabet[character]=1
print(Alphabet)
