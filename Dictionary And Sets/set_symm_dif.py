"""
    set symmetric difference:
        -> Opposite of intersection
        -> Produces the set of items that are in one set or the other, but not in both.
        -> If `A` and `B` are two sets, then symmetric dif = (A | B) - (A & B)

"""
morning = ["Java", "Ruby", "C", "Lisp", "C#"]
afternoon = ["Python", "C#", "Java", "C", "Ruby"]

# possible_courses = set(morning) ^ set(afternoon) # '6' operator not defined for lists
possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)

