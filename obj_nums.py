class car:
    obj_num = 0
    def __init__(self , n , p):
        self.name = n
        self.price = p
        
        car.obj_num += 1
    def show(self):
        print(f'{self.name} costs {self.price}')

c1 = car('pride' , 100)
c2 = car('benz' , 200)
c3 = car('toyota' , 300)
c4 = car('honda' , 500)

print(car.obj_num)