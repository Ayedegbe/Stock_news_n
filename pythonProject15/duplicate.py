def duplicate_count(text): # function to count number of re-occuring letters
    text = text.lower() # convert text to lower case
    see = [] # create empty list
    for char in text: # loop through text
        count = text.count(char) # count each character
        if count > 1 and char not in see: # if the count of each characrer is more than one and is not yet counted
            see.append(char) # append said character into empty list created above
            c = len(see)# count of items in see
        elif count < 1:
            return 0
    return c



text = "Indivisibilities"
print(duplicate_count(text))