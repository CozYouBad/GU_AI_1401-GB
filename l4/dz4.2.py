my_list1 = [10, 20, 4, 45, 441, 18, 111, 1, 1, 5]
my_list2 = [el for el in my_list1 if el > my_list1[my_list1.index(el)-1]]
print(my_list2)