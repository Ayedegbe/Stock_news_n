#create function to iter
def array_diff(a,b):
#iterate through list b and check if characters are in a and return what is left
    for i in b:
        while i in a:
            a.remove(i)
    return a
print(array_diff([1, 2, 2], [1, 3, 4]))
