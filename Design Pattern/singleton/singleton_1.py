class SingleTon():
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance


o1 = SingleTon()
print("object - 1 ==>",o1)
o1.data = 10

o2 = SingleTon()
print("object - 2 ==>",o2)
print("object - 2  data ==>",o2.data)
o2.data = 5

print("object - 1 data ==>",o1.data)