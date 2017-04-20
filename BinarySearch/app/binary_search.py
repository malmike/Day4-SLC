class BinarySearch(list):
    def __init__(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            self.binary_list =  [x*b for x in range(1,a+1)] 
            self.length = len(self.binary_list)
        else:
            raise TypeError
    def __getitem__(self,key):
        return  self.binary_list[key]  
    def search(self, search_item):
        if isinstance(search_item, int):
            return self.binary_search(self.binary_list, search_item)
        else:
            raise TypeError
    