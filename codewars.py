# def fun(s):
#     d = {"A": "T", "C": "G"}
#     n = ""
#     for x in s:
#         if x in d.keys():
#             n += d[x]
#         elif x in d.values():
#             n+= d
#         else:
#             n += x
#     return n
#
#
# print(fun("AAAA"))

l = [0, 1, 2, 3, 4]
l[1:2] = []
print(l)
