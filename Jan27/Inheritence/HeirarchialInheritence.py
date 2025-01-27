class Demo1:
    def disp1(self):
            print('Inside Disp1')

class Demo2(Demo1):
    def disp2(self):
            print('Inside Disp2')

class Demo3(Demo1):
    pass

d2 = Demo2()
d2.disp1()
d3 = Demo3()
d3.disp1()