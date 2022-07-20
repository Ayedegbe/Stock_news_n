L = [1, 2, "af", "b", 2, 14, "C", 234]


def filter_list(L):
    c=[]
    for i in L:
        if type(i) is int:
            c.append(i)
    return c
print(filter_list(L))
