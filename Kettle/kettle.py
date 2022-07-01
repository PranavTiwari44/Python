class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 9.99)
print(kenwood.make)
print(kenwood.price)
kenwood.power = 1.5
print(kenwood.power)

hamilton = Kettle("Hamilton", 19.99)
print(hamilton.make)
print(hamilton.price)
hamilton.switch_on()
print(hamilton.on)
