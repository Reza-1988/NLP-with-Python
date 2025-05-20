
def create_set(input_ls):
    """Convert the input list to a set without duplicate elements."""
    return set(input_ls)

def union(first_set, second_set):
    """Perform union operation between two sets."""
    return first_set.union(second_set)

def intersection(first_set, second_set):
    """Perform intersection operation between two sets."""
    return first_set.intersection(second_set)

def difference(first_set, second_set):
    """Perform difference operation between two sets (first_set - second_set)."""
    return first_set.difference(second_set)

def complement(universal_set, first_set):
    """Calculate the complement of first_set with respect to the universal_set."""
    return universal_set.difference(first_set)

def is_empty(the_set):
    """Check if a set is empty."""
    return len(the_set) == 0

def is_subset(first_set, second_set):
    """Check if first_set is a subset of second_set."""
    return first_set.issubset(second_set)

def is_member(the_set, element):
    """Check if the element is a member of the set."""
    return element in the_set

def power_set_number(the_set):
    """Calculate the number of elements in the power set of the given set."""
    return 2 ** len(the_set)

def probability_of_event(event_set, sample_space) -> float:
    """Calculate the probability of an event_set within the sample_space."""
    if len(sample_space) == 0:
        raise ValueError("Sample space must not be empty.")
    return len(event_set) / len(sample_space)

def conditional_probability(event_A, event_B) -> float:
    """Calculate the conditional probability P(A|B) using the intersection of A and B."""
    if len(event_B) == 0:
        raise ValueError("Set B must not be empty.")
    intersection_set = event_A.intersection(event_B)
    return len(intersection_set) / len(event_B)

def are_independent(event_A, event_B, sample_space) -> bool:
    """Check if events A and B are independent within the sample_space."""
    prob_A = probability_of_event(event_A, sample_space)
    prob_B = probability_of_event(event_B, sample_space)
    intersection_set = event_A.intersection(event_B)
    prob_intersection = len(intersection_set) / len(sample_space)
    return abs(prob_intersection - (prob_A * prob_B)) < 1e-9  # Approximate equality check

def bayes_theorem(event_A, event_B, sample_space) -> float:
    """Apply Bayes' theorem to compute P(B|A)."""
    if len(event_A) == 0:
        raise ValueError("Set A must not be empty.")
    prob_A = probability_of_event(event_A, sample_space)
    prob_B = probability_of_event(event_B, sample_space)
    intersection_set = event_A.intersection(event_B)
    prob_intersection = len(intersection_set) / len(sample_space)
    return (prob_intersection / prob_A) if prob_A != 0 else 0