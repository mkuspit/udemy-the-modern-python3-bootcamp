set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

sets_union = set_1 | set_2
print(sets_union)

sets_intersection = set_1 & set_2
print(sets_intersection)

set_1_diff_set_2 = set_1 - set_2
print(set_1_diff_set_2)

set_2_diff_set_1 = set_2 - set_1
print(set_2_diff_set_1)