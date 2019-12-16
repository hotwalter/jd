#可迭代对象： 必须要有 __iter__ 方法

class Human:
    def __init__(self,name):
        self.name = name
    def __iter__(self):
        return iter("abc")

    def __next__(self):
        return self.name




h1=Human("xiaoming")
print(h1.__next__())
print(next(h1))
# for x in h1:
#     print(x)