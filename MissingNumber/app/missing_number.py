def find_missing(list_1, list_2):
    if isinstance(list_1, list) and isinstance(list_2, list):
        if all(isinstance(i, int) for i in list_1) and all(isinstance(i, int) for i in list_2):
            if all(i>0 for i in list_1) and all(i>0 for i in list_2):
                values = list(set(list_1) ^ set(list_2))
                if len(values) is 0:
                    return 0
                elif len(values) is 1:
                    return values[0]
                else:
                    return values
            else:
                raise ValueError
        else:
            raise TypeError
    else:
        raise TypeError