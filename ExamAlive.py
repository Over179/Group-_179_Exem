# 1. Лиса ест кролика. Кролик ест растения.
# Растение поглощает солнечный свет. Представитель каждого класса может умереть,
# если достигнет определенного возраста или для него не будет еды.
# Напишите виртуальные методы поедания и определения состояния живого существа
# (живой или нет, в зависимости от достижения предельного возраста и наличия еды (входной параметр)).

class Alive:
    def __init__(self, count):
        self.count = count

    def info(self):
        print("count:", self.count)


class Plants(Alive):
    def __init__(self, koef_repr, count):
        super().__init__(count)
        self.koef_repr = koef_repr

    def grown(self):
        self.count *= self.koef_repr

    def info(self):
        print("count plants:", self.count)

    def rabbits_food(self,count_rabbits):
        self.count -= count_rabbits * 10

    def add_plants(self,count_plants):
        self.count += count_plants

class Rabbits(Alive):
    def __init__(self, koef_repr,koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("count rabbits:", self.count)

    def foxes_food(self,count_foxes):
        self.count -= count_foxes * 4

    def take_away(self,count_rabbits):
        self.count -= count_rabbits

class Foxes(Alive):
    def __init__(self, koef_repr, koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("count foxes:", self.count)

    def hunters_food(self, count_hunters):
        self.count -= count_hunters * 3

    def destroy_off(self, count_foxes):
        self.count -= count_foxes

class Hunters(Alive):
    def __init__(self, koef_repr, koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def info(self):
        print("count hunters:", self.count)

plants = Plants(10, 200)
rabbits = Rabbits(5,0.2,180)
foxes = Foxes(7,0.25,60)
hunters = Hunters(10,0.01,1)


year = 1
print("begin:")
plants.info()
rabbits.info()
foxes.info()
hunters.info()

while year <= 10:

    if plants.count // 10  <= rabbits.count:
        print("warning!!!!!!!")
        print("plants is very low")
    if rabbits.count // 10 <= foxes.count:
        print("warning!!!!!!!")
        print("rabbits is very few")
    if foxes.count <= hunters.count:
        print("warning!!!!!!!")
        print("foxes is very few")

        rabbits.info()
        plants.info()
        foxes.info()
        hunters.info()
        choise = int(input("enter 1 - add plants 2 - take away rabbits 3 - take away foxes 4 - take away hunters"))
        if choise == 1:
            count = int(input("enter count plants:"))
            plants.add_plants(count)
        elif choise == 2:
            count = int(input("enter count rabbits:"))
            rabbits.take_away(count)
        if choise == 3:
            count = int(input("enter count foxes:"))
            foxes.take_away(count)
        elif choise == 4:
            count = int(input("enter count hunters:"))
            hunters.take_away(count)




    if plants.count <= 0 or rabbits.count <= 0 or foxes.count <= 0 or hunters.count<=0:
        print("Fatality on year:",year)
        print("All our alive will disappear")
        break

    plants.grown()
    plants.rabbits_food(rabbits.count)

    rabbits.death()
    rabbits.reproduction()

    foxes.death()
    foxes.reproduction()

    foxes.hunters_food(hunters.count)

    print("year: ", year)

    plants.info()
    rabbits.info()
    foxes.info()
    hunters.info()


    year += 1


