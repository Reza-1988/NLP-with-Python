def create_set(input_ls):
    """تبدیل لیست ورودی به یک مجموعه بدون عناصر تکراری."""
    return set(input_ls)

def union(first_set, second_set):
    """انجام عملیات اجتماع بین دو مجموعه."""
    return first_set.union(second_set)

def intersection(first_set, second_set):
    """انجام عملیات اشتراک بین دو مجموعه."""
    return first_set.intersection(second_set)

def difference(first_set, second_set):
    """انجام عملیات تفاضل بین دو مجموعه (first_set - second_set)."""
    return first_set.difference(second_set)

def complement(universal_set, first_set):
    """محاسبه متمم مجموعه first_set نسبت به مجموعه جهانی universal_set."""
    return universal_set.difference(first_set)

def is_empty(the_set):
    """بررسی خالی بودن یک مجموعه."""
    return len(the_set) == 0

def is_subset(first_set, second_set):
    """بررسی اینکه first_set زیرمجموعه second_set است یا خیر."""
    return first_set.issubset(second_set)

def is_member(the_set, element):
    """بررسی عضویت عنصر element در مجموعه the_set."""
    return element in the_set

def power_set_number(the_set):
    """محاسبه تعداد اعضای مجموعه توانی یک مجموعه."""
    return 2 ** len(the_set)

def probability_of_event(event_set, sample_space) -> float:
    """محاسبه احتمال یک پیشامد event_set در فضای نمونه sample_space."""
    if len(sample_space) == 0:
        raise ValueError("فضای نمونه نباید خالی باشد.")
    return len(event_set) / len(sample_space)

def conditional_probability(event_A, event_B) -> float:
    """محاسبه احتمال شرطی P(A|B) با استفاده از اشتراک دو مجموعه A و B."""
    if len(event_B) == 0:
        raise ValueError("مجموعه B نباید خالی باشد.")
    intersection_set = event_A.intersection(event_B)
    return len(intersection_set) / len(event_B)

def are_independent(event_A, event_B, sample_space) -> bool:
    """بررسی استقلال دو پیشامد A و B در فضای نمونه sample_space."""
    prob_A = probability_of_event(event_A, sample_space)
    prob_B = probability_of_event(event_B, sample_space)
    intersection_set = event_A.intersection(event_B)
    prob_intersection = len(intersection_set) / len(sample_space)
    return abs(prob_intersection - (prob_A * prob_B)) < 1e-9  # بررسی تقریبی برابری

def bayes_theorem(event_A, event_B, sample_space) -> float:
    """اعمال قضیه بیز برای محاسبه P(B|A)."""
    if len(event_A) == 0:
        raise ValueError("مجموعه A نباید خالی باشد.")
    prob_A = probability_of_event(event_A, sample_space)
    prob_B = probability_of_event(event_B, sample_space)
    intersection_set = event_A.intersection(event_B)
    prob_intersection = len(intersection_set) / len(sample_space)
    return (prob_intersection / prob_A) if prob_A != 0 else 0
