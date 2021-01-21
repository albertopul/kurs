from faker import Faker
faker = Faker()

class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'
    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"       
    def __eq__(self, other):
        return (
            self.make == other.make and
            self.model_name == other.model_name and
            self.top_speed == other.top_speed and
            self.color == other.color)

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_one == car_two

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
print(car)
mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)


print(mustang)



class Contacts:
    def __init__(self, name, surname, company_name, occupation, email):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.occupation = occupation
        self.email = email
    def __str__(self)




def people():
    for i in range(1):
        person1 = Contacts(name="Marta",surname="Perez",company_name="Deluxe",occupation="Joker",email="costam@cos.pl")
        print(person1.name, person1.surname, person1.email)
        print("-----------------")
        person2 = Contacts(name="Agata",surname="Pulińska",company_name="Deluxe",occupation="Joker",email="dfdsdvs@cos.pl")
        print(person2.name, person2.surname, person2.email)
        print("-----------------")
        person3 = Contacts(name="Fran",surname="Perez",company_name="Deluxe",occupation="Joker",email="dfxfe@cos.pl")
        print(person3.name, person3.surname, person3.email)
        print("-----------------")
        person4 = Contacts(name="Anka",surname="Skakanka",company_name="Deluxe",occupation="Joker",email="dfx df@cos.pl")
        print(person4.name, person4.surname, person4.email)
        print("-----------------")
        person5 = Contacts(name="Kasia",surname="Suchar",company_name="Deluxe",occupation="Joker",email="dfxv @cos.pl")
        print(person5.name, person5.surname, person5.email)
        print("-----------------")
people()


list = [] 
def fake_people():
    for person in range(7):
        person = Contacts(name=faker.first_name(), surname=faker.last_name(), company_name=faker.company(), occupation=faker.job(), email=faker.email())
        print(faker.first_name(), faker.last_name())
        print(faker.company())
        print(faker.job())
        print(faker.email())
        print("--------------")
        list.append(person)
    for obj in list:
        print(obj.name, obj.surname, obj.company_name, obj.occupation, obj.email, sep ='  /  ')
fake_people()



