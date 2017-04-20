class BinarySearch(list):
    def __init__(self, a, b):
        #Inherit the methods in list
        super(BinarySearch, self).__init__()
        #Check that the values entered are integers
        if isinstance(a, int) and isinstance(b, int):
            #Loop used to generate values that are appended to the class list
            for x in range(b,(a*b)+1,b):
                self.append(x)
            #Get the length of the generated class list
            self.length = len(self)
        else:
            raise TypeError
    def search(self, search_item):
        #Check that the search item is an integer
        if isinstance(search_item, int) and len(self) > 0:
            #Initialize index to -1 and found to false
            found, index = False, -1
            #Assign to first first index value of the list
            first = 0
            #Assign to last the last index value of the list
            last = len(self)-1
            #Assign 0 to a variable count
            count = 0
            #Check that the first value in the list is not the search item
            if self[first]==search_item:
                found, index = True, first
            #Check that the last value in the list is not the search item
            elif self[last]==search_item:
                found, index = True, last
            #Check that the search item is not greater than the last item in the list or 
            #less than the first item in the list
            elif search_item > self[last] or search_item < self[first]:
                found, index = True, -1
            #Loop through the list until the value is found or 
            #until the value in first is greater than that in last
            while first<=last and not found:
                #Get the index at the midpoint between the index in first and that in last
                midpoint = (first+last)//2
                #Check whether the value is at the midpoint
                if self[midpoint] == search_item:
                    #Set found to true and index to the value in midpoint 
                    found,index = True, midpoint
                else: 
                    count += 1                   
                    #Put the index of midpoint-1 to the last value if search item is less than
                    #value at midpoint
                    if search_item < self[midpoint]:
                        last = midpoint - 1
                        if search_item>self[last]:
                            break
                    #Put the index of midpoint=1 to the last value if search item is greater than
                    #value at midpoint
                    else:
                        first = midpoint + 1
                        if search_item<self[first]:
                            break
                #Increment the count by 1 to show the number of times the loop has occured
            #Return count and index at which the search item is, in a dictionary
            return {'count':count, 'index':index}
        else:
            raise TypeError
   