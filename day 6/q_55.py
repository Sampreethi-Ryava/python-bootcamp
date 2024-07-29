class Father:
    def father_speak():
        return"father class"
class Mother:
    def mother_speak():
        return"mother class"
class Kid(Father,Mother):
    def kid_speak():
        return"iam kid i am having properties of mother and father"
obj1=Kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())

