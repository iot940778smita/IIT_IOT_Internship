def overlapping(list1, list2):
   
    for item in list1:
        if item in list2:
            return True
    return False


list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]
list_c = [10, 11, 12]

print(f"Do list_a and list_b overlap? {overlapping(list_a, list_b)}")
print(f"Do list_a and list_c overlap? {overlapping(list_a, list_c)}")

