
def dict_deep_copy(d: dict) -> dict:
    """Returns a deep copy of the dict `d` passed as argument"""
    new_dict = {}
    # for item, value in d.items():
    #     l = []
    #     for i in value:
    #         l.append(i)
    #     new_dict[item] = l
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict
