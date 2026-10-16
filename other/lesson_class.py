import time


class cat:
    def __init__(self, breed=None, gender=str, age=int, timer=int):
        self.breed = breed
        self.gender = gender
        self.age = age
        self.live = timer

    def __str__(self):
        return f'{self.breed} {self.gender} {self.age} {self.live}'

    def live(self):
        if self.live < 0:
            self.is_alive = False
        else:
            self.live -= 1

    def talk(self):
        print("afafaf")

cat1 = cat(breed='cat', gender="male", age=1, timer=10)
print(cat1)
for i in range(15):
    cat1.live()
    time.sleep(1)
    if cat1.is_alive:
        cat1.talk()
    else:
        print("вот такая фигня собачка")