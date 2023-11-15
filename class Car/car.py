class Car():
    def __init__(self, name, model, speed, color, nitro_speed, engine_power, number):
        self.name = name
        self.model = model
        self.speed = speed
        self.color = color
        self.nitro_speed = nitro_speed
        self.engine_power = engine_power
        self.number = number

    def info(self):
        print(f"    Car {self.number}: \nName: {self.name} \nModel: {self.model} \nSpeed: \
{self.speed}km/h \nEngine power: {self.engine_power}hp \nColor: \
{self.color} \nNitro Speed: {self.nitro_speed}" )


Car1 = Car("Ford Mustang", "GT", 250, "Black", "Yes", 450, 1)

Car2 = Car("AUDI Q7", "Q7", 250, "Navarra Blue", "No", 335, 2)

Car2.info()
