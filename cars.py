class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

        # Variables
        self._current_speed = 0

    def accelerate(self, step=10):
        self.current_speed += step

    def decelerate(self, step=10):
        self.current_speed -= step
    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")





"""
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'
    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"       
    def __eq__(self, other):
        return (
            self.make == other.make and
            self.model_name == other.model_name and
            self.top_speed == other.top_speed and
            self.color == other.color
        )
    def __gt__(self, other):
        return self.top_speed > other.top_speed
"""


car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_three = Car(make="Ford", model_name="Mustang", top_speed=350, color="Yellow")

car_one.current_speed 
print(car_one.current_speed)



"""
print(car_one < car_three)

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]
by_speed = sorted(cars, key=lambda car: car.top_speed)
by_make = sorted(cars, key=lambda car: car.make)
print(by_make)
"""



"""
class Contacts:
    def __init__(self, name, surname, company_name, occupation, email):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.occupation = occupation
        self.email = email
    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'



person1 = Contacts(name="Marta",surname="Perez",company_name="Deluxe",occupation="Joker",email="costam@cos.pl")
person2 = Contacts(name="Agata",surname="Pulińska",company_name="Deluxe",occupation="Joker",email="dfdsdvs@cos.pl")
person3 = Contacts(name="Fran",surname="Perez",company_name="Deluxe",occupation="Joker",email="dfxfe@cos.pl")
person4 = Contacts(name="Anka",surname="Skakanka",company_name="Deluxe",occupation="Joker",email="dfx df@cos.pl")
person5 = Contacts(name="Kasia",surname="Suchar",company_name="Deluxe",occupation="Joker",email="dfxv @cos.pl")

print(person1)
print(person2)
print(person3)
print(person4)
print(person5)
"""