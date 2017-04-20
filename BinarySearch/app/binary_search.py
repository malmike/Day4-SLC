class BinarySearch(list):
    def __init__(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            self.binary_list =  [x*b for x in range(1,a+1)] 
            #self.binary_list = [x for x in range(b,(a*b)+1,b)]
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
    def binary_search(self, a_list, item):
        first = 0
        last = len(a_list)-1
        found = False
        midpoint = 0
        count = 0
        while first<=last and found is False:
            count += 1
            midpoint = (first+last)//2
            if a_list[midpoint] == item:
                found = True
                break
            else:
                if item < a_list[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        if a_list[midpoint] == item:
            return {'count':count, 'index':midpoint}
        else:
            return {'count':count, 'index': -1}







