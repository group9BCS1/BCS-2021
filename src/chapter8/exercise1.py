def chop(lst):
# Removes the first element
    del lst[0]
# Removes the last element
    del lst[-1]
def middle(lst):
# Stores all but the first element
    new = lst[1:]
# Deletes the last element
    del new[-1]
    return new


my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)
print(chop_list)

middle_list = middle(my_list2)
print(my_list2)
print(middle_list)