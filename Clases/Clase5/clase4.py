class Animals:
    def __init__(self, animalsName):
        print(animalsName, 'is an animal.');


class Mammal(Animals):
    def __init__(self, Name):
        print(Name, 'is a mammal.')
        super().__init__(Name)
    

class donotFly(Mammal):
      def __init__(self, name):
        print(name, "cannot fly.")
        super().__init__(name)


class donotSwim(Mammal):
    def __init__(self, name):
        print(name, "cannot swim.")
        super().__init__(name)


class Cat(donotSwim, donotFly):
    def __init__(self):
        print('A cat.');
        super().__init__('Cat')

cat = Cat()
print('')
bat = donotSwim('Bat')