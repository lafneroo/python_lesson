from animal import Animal

class cat(Animal):
    def __init__(self, name, sound, age):
        super().__init__(name, sound, age)


cat1 = cat("kusya", "miau", 5)
print(cat1.speak(cat1.sound))