# import myfunction as m
#
# print(m.add(2,3))
# print(m.multiply(5,54))

class parent:
    def __init__(self,name):
        print('parent __init__',name)

class parent2:
    def __init__(self,name):
        print('parent2 __init__',name)

class child(parent,parent2):
    def __init__(self):
        print('child __init__')
        super().__init__('max')

ch=child()
print(child.__mro__)