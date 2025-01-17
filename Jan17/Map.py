#Map is a built in method . this method accepts 2 parameters . (function and iterable Object )
def double(x) :
        return x*2
    
li = [1,2,3,4]
double_li = map(double, li)
print(double_li) #Iterable Object convert it to list
print(list(double_li))



tup = ('10','20', '30')
tup = tuple(map(int, tup))  #[2, 4, 6, 8]


li2 = [1,5,66]
floatList = list(map(float,li2))
print(floatList, type(floatList))
