def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique
sample_list = [1, 2, 3, 3, 4, 4, 5, 3, 7, 5]
print("The Sample List is:", sample_list)
print(" Unique List:", unique_list(sample_list))
