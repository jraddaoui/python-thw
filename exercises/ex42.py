## Animal is-a class
class Animal(object):
    pass

## Dog is-a class (inherits from Animal)
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a class (inherits from Animal)
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a class
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet
        self.pet = None

## Employee is-a class (inherits from Person)
class Employee(Person):

    def __init__(self, name, salary):
        ## Use super class to set the name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a class
class Fish(object):
    pass

## Salmon is-a class (inherits from Fish)
class Salmon(Fish):
    pass

## Halibut is-a class (inherits from Fish)
class Halibut(Fish):
    pass


## rover is-a object of Dog
rover = Dog("Rover")

## satan is-a object of Cat
satan = Cat("Satan")

## mary is-a object of Person
mary = Person("Mary")

## mary has-a pet, which is satan
mary.pet = satan

## frank is-a object of Employee
frank = Employee("Frank", 120000)

## frank has-a pet, which is rover
frank.pet = rover

## flipper is-a object of Fish
flipper = Fish()

## crouse is-a object of Salmon
crouse = Salmon()

## harry is-a object of Halibut
harry = Halibut()
