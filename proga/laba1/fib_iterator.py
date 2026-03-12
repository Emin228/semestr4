from math import sqrt

class FibonacchiLst():
    """Класс возвращающий каждый элемент, который входит в список Фибоначи"""
    def __init__(self, range:list):
        self.range = range
        self.idx = 0
        self.count0 = 0
        self.count1 = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                res = self.range[self.idx]
            
            except IndexError:
                raise StopIteration
            
            if res == 0:
                self.count0+=1
                if self.count0<=1:
                    self.idx +=1
                    return res
            elif res == 1:
                self.count1+=1
                if self.count1 <=2:
                    self.idx +=1
                    return res
            else:
                A1 = 5 * res**2 + 4
                A2 = 5 * res**2 - 4

                B1 = int(sqrt(A1))
                B2 = int(sqrt(A2))
                if (B1**2 == A1) or (B2**2 == A2):
                    self.idx +=1
                    return res
            self.idx +=1

print(list(FibonacchiLst([1,1,1,1,11,0,0,0,0,3,2])))
            
             

    