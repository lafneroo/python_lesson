from animal import Animal

class dog(Animal):
    def __init__(self, name, sound, age):
        super().__init__(name, sound, age)

dog1 = dog('muhtar',"gavgav", 10)
print(dog1.speak(dog1.sound))