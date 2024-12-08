class Animal:
    pass


class Mamifero(Animal):
    pass


class Ave(Animal):
    pass


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Onitorrinco(Mamifero, Ave):
    pass


class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()
