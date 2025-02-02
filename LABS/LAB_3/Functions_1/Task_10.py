#Write a Python function that takes a list and returns a new list 
#with unique elements of the first list. Note: don't use collection set

def unique_list(list_1):
    list_2=[]
    for x in list_1:
        if x not in list_2:
            list_2.append(x)
    return list_2

list_1=[3, 3, 3, 5, 7, 3, 4]
print(unique_list(list_1))