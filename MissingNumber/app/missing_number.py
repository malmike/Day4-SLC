def find_missing(list_1, list_2):
    if isinstance(list_1, list) and isinstance(list_2, list):
        if all(isinstance(i, int) for i in list_1) and all(isinstance(i, int) for i in list_2):
            if all(i>0 for i in list_1) and all(i>0 for i in list_2):
                pass
            else:
                raise ValueError
        else:
            raise TypeError
    else:
        raise TypeError