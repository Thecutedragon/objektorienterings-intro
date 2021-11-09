class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand

    def get_color(self):
        print(self.color)

    def set_color(self, new_color):
        self.color = new_color

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, new_mileage):
        self.mileage = new_mileage


# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587)
b_car = Car("Ferrari", "Red", 2014)
c_car = Car("Tesla", "White", 1531)
d_car = Car("BMW", "Silver", 105)

my_cars = [a_car, b_car, c_car, d_car]
for car in my_cars:
    car.get_brand()
