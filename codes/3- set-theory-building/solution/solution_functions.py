def create_set(input_ls):
    return set(input_ls)

def union(first_set, second_set):
    return first_set.union(second_set)

def intersection(first_set, second_set):
    return first_set.intersection(second_set)

def difference(first_set, second_set):
    return first_set.difference(second_set)

def complenment(universal_set, first_set):
    return universal_set.difference(first_set)

def is_empty(the_set):
    return len(the_set) == 0

def is_subset(first_set, second_set):
    return first_set.issubset(second_set)

def is_member(the_set, element):
    return element in the_set

def power_set_number(the_set):
    return 2 ** len(the_set)
