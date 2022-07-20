def move_zeros(list): # returns [1, 1, 2, 1, 3, 0, 0]
    for n in list:
        if n == 0 :
           list.remove(n)
           list.append(n)
    return list
trial = [1, 0, 1, 2, 0, 1, 3]
print(move_zeros(trial))