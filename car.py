class Car:
    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        print(self.speed)

        
def main():
    car1 = Car(2001, "Honda")
    for i in range(5):
        car1.accelerate()
        car1.get_speed()
    for i in range(5):
        car1.brake()
        car1.get_speed()

main()
