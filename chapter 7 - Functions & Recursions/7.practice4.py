# write a function that takes a string and returns the count of 
# vowels and consonants separately . 

def func(userInput):
    vowels="aeiouAEIOU"

    countVowel=0
    countConsonant=0

    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel+=1
            else:
                countConsonant+=1
        
    return countConsonant,countVowel

Consonant,Vowel = func("Akshil Nagani")

print(Consonant,Vowel)