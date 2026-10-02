# s1 = {1,2,3,4}
# print(type(s1))
# s1.add(9)
# print(s1)
# s1.pop()
# print(s1)
# s1.remove(9)
# print(s1)
# del s1
# s2={3,4,5,6,7}
# print(s2)
# new = 3 in s2
# print(new)

# for i in s2:
#     print(i,end="  ")

# d1={"name":"aditi","gender":"female"}
# print(d1)
# d1["gender"]="male"
# print(d1)
# d1["name"]="aditya"
# print(d1)

# for i in d1:
#     print(i,d1[i])

# g="gender" in d1
# print(g)

def even_num(num):
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")


for i in range(1, 10):
    print(even_num(i))
