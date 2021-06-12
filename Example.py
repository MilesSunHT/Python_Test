'''------------- Python Exmaple -------------'''
'''
    constructor
    paramter
    arguments
    2) principles: Encapsulation; Inheritance, Polymorphism.
        Encapsulation: only share certain details in the class for user to use(33:00)
        Inheritance: Customer & Teacher are all inheritad from User (cutomer will have all things defined in user)
        Polymorphism: Treate Customer & Teacher as the same thing when approcah User, but Cutomer and Teacher can do different things
'''
class User:                             #Inheritance
    def log(self):
        print("---------Parent Testing")
        print(self)
class Teacher(User):                    #Polymorphism
    def log(self):
        print("This is the polymorphism testing")


class Test (User):                      #Adding "User" here, then everything defined in User will get inharited by Test Class
    def log(self):
        print("this overwirte the log in User")
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print("Created2")

    #2) ------ Create a property ------
    @property
    def name (self):
        return self._name  # sufix "_" means private

    @name.setter
    def name (self,name):
        self._name = name
    #2) ------ Create a property ------

    @name.deleter
    def name (self):
        del self._name

    def gender_change (self,gender_update):
        self.gender = gender_update
        print("Gender changed")

    def name_change(self,name_change):
        self.name = name_change
        print("name changed")

    def read():
        print("static function")

    def __str__(self) -> str:
        #print("convert to string")
        return "Name: "+ self.name + "," + "Gender: " + self.gender
        
    def print_all (all):
        for all in all:
            print(all)

    def __eq__(self, second) -> bool:
        if self.name==second and self.gender==second:
            return True
        return False

    #over writing mehod
    __repr__ =__str__

''' ------------- Output Section ------------- '''
c= Test("Miles", "M")
print(c.name,c.gender)

c2 = [Test("a","b"), Test("a2", "b2")]
print(c2[0].name)

c2[0].gender_change("Female")
c2[0].name_change("Helen")
print(c2[0].name, c2[0].gender)

c2[1].name = "Duncan"
c2[1].gender = "Male"
print(c2[1].name, c2[1].gender)

Test.read()

print(c2[0],c2[1])

Test.print_all(c2)
print(c2[0]==c2[1])

print(c2)

del c2[0] 

print(c2)

c2[0].log()


users = [Test("a","b"), Test("a2", "b2"), Teacher()]
for user in users:
    user.log() 
''' 
    This log method is defined in User Class, which can be inheritated into the child Test class, 
    Tho, the teacher has it's own function which will overwrite the log in User (Polymorphism)
'''