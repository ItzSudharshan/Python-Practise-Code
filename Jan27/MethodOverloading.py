class Demo:
    def disp(self):
        print('Inside disp with 0 Para')
    
    def disp(self, a):
        print('Inside disp with 1 Para')
        
    def disp(self,a , b):
        print('Inside disp with 2 para')
        
d = Demo()
#d.disp()
#d.disp(10)
d.disp(10, 20)

#Python doesnt Support Method Overloading. Only the last invoked method is Usefull rest all previous Methods are Useless