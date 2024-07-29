.#write a program to find consonents
str=input()
vowel="aeiou"
consonant="bcdfghjklmnpqrstuvwxyz"
ans=""
for i in (str):
    if(i in consonant):
        ans+=i
for i in (str):
    if(i in vowel):
        ans+=i
print(ans)




