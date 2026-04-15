# a = [1, 2, 3, 2]
# a.append(5)
# print(a)
# a.pop()
# print(a)
# a.remove(2)
# print(a)


# a.insert(1, 5)
# print(a)

# print(a[-3])
# a.pop(1)
# print(a)


# a.remove(2)
# print(a)
# b = [8, 9, 10]
# print(a+b)
# print(a*2)

# for i in a:
#     print(i)
# a = [1, 2, 3, 4, 5]
# print(a[1:5:2])


# for i in range(1,16):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)


# es=[100,120,130,110]
# print(sum(es)/len(es))


# import itertools
# word = "abc"
# print(list(itertools.permutations(word)))
# a = [1, 2, 3]
# print(a[::2])
# a = [1, 2, 3]
# a.pop(1)
# print(a)
# for i in range(2):
#     for j in range(2):
#         print(i+j)


# a=[1,2,3]
# b=a
# b.append(4)
# print(a==b)
# print(a)
# print(b)

# import itertools

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for perm in permutations(nums):
#     if check_magic(perm):
#         print(perm)


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# common = set1 & set2
# print(common)


# import random
# n=23

# birthdays=[random.randint(1,365) for _ in range(n)]


# print(birthdays)


# if len(birthdays)!=len(set(birthdays)):
#     print("At least two people share a birthday.")

# movie="avater"
# guess="_v_t_r"
# for i in range(len(movie)):
#     if(movie[i]==guess[i]):
#         print(movie[i],end="")
# import random
# print(random.randint(1, 3))

# d={"name":"Pradip","age":20}
# # for key in d:
# #     print(key, d[key])
# print(d.items())

# arr = [3, 2, 1]
# print(sorted(arr))


# for i in {"x": 1, "y": 2}:
#     print(i)


# d = {"a": 1, "b": 2, "a": 3}
# print(d["a"])
# d = {"a": 1, "b": 2}
# d["b"] = 5
# print(d)


# d = {"x": 1}
# print(d["y"])


# d = {1: "a", True: "b"}
# print(d)
# attendance = {}

# attendance["Mon"] = ["A", "B"]
# attendance["Tue"] = ["A"]

# print(attendance)
# f=open("file.txt","w")
# f.write("Hello")
# f.close()


f = open("a.txt", "w")
f.write("Hello")
f.write("World")
f.close()
