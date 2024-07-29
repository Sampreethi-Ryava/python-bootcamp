#to print  non repeating or unique charaters in a string
vowels="aeiou"
consonants="bcdfghjklmnpqrstuvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)