
class FibonacchiList():
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0
        self.ones_count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                res = self.instance[self.idx]
            except IndexError:
                raise StopIteration
            
            self.idx +=1

            if res == 0:
                return 0
            
            a1 = 5*res**2+4
            a2 = 5*res**2-4

            b1 = int(a1**0.5)
            b2 = int(a2**0.5)

            if b1*b1 == a1 or b2*b2 == a2:
                if res == 1:
                    self.ones_count+=1
                    if self.ones_count>2:
                        continue
                    else:
                        return res
                else:
                    return res  


            

lst = [0,1,1,1,3,4,5]
g = FibonacchiList(lst)
for x in g:
    print(x)



            

        

            
        