class Animal():
    def __init__(self, sound=None, name=None, age=None, breed=None):
        self.sound = sound
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} live {self.age} years {self.breed} {self.sound}"

    def speak(self, sound):
        self.sound = sound
        return f"{self.name} say {self.sound}"