def prog1():
    class Restaurant:
        def __init__(self, name, cuisine_type):
            self.name = name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print("Restaurant name:", self.name)
            print("Cuisine type:", self.cuisine_type)
    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine_type,flavors):
            super().__init__(name, cuisine_type)
            self.flavors = flavors

        def describe_flavors(self):
            print(f"Доступные вкусы в {self.name}:")
            for flavor in self.flavors:
                print(f"- {flavor}")

    my_ice_cream_stand = IceCreamStand("Ванилла", "Кафе-Мороженое", ["Ваниль", "Шоколад", "Клубника"])
    my_ice_cream_stand.describe_restaurant()
    my_ice_cream_stand.describe_flavors()
def prog2():
    class Restaurant:
        def __init__(self, name, cuisine_type, location, hours):
            self.name = name
            self.cuisine_type = cuisine_type
            self.location = location
            self.hours = hours
        def describe_restaurant(self):
            print("Restaurant name:", self.name)
            print("Cuisine type:", self.cuisine_type)
            print("Location:", self.location)
            print("Hours:", self.hours)
    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine_type, location, hours, flavors):
            super().__init__(name, cuisine_type, location, hours)
            self.flavors = flavors

        def describe_flavors(self):
            print(f"Доступные вкусы в {self.name}:")
            for flavor in self.flavors:
                print(f"- {flavor}")
        def delete(self,flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"Сорт {flavor} удален из меню!")
            else:
                print(f"Сорт {flavor} не найден в меню!")
        def add(self, flavor):
            self.flavors.append(flavor)
            print(f"Сорт {flavor} добавлен в меню!")
        def check(self, flavor):
            if flavor in self.flavors:
                print('Есть в наличии')
            else:
                print('Нет в наличии')

    class Stick(IceCreamStand):
        def __init__(self, name, cuisine_type, location, hours, flavors, sticks):
            super().__init__(name, cuisine_type, location, hours, flavors)
            self.sticks = sticks

        def describe_flavors(self):
            print(f"Доступные вкусы {self.sticks} в {self.name}:")
            for flavor in self.flavors:
                print(f"- {flavor}")

        def delete(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"Сорт {flavor} удален из меню!")
            else:
                print(f"Сорт {flavor} не найден в меню!")

        def add(self, flavor):
            self.flavors.append(flavor)
            print(f"Сорт {flavor} добавлен в меню!")

        def check(self, flavor):
            if flavor in self.flavors:
                print('Есть в наличии')
            else:
                print('Нет в наличии')

    class Soft(IceCreamStand):
        def __init__(self, name, cuisine_type, location, hours, flavors,soft):
            super().__init__(name, cuisine_type, location, hours, flavors)
            self.soft = soft
        def describe_flavors(self):
            print(f"Доступные вкусы {self.soft} в {self.name}:")
            for flavor in self.flavors:
                print(f"- {flavor}")

        def delete(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"Сорт {flavor} удален из меню!")
            else:
                print(f"Сорт {flavor} не найден в меню!")

        def add(self, flavor):
            self.flavors.append(flavor)
            print(f"Сорт {flavor} добавлен в меню!")

        def check(self, flavor):
            if flavor in self.flavors:
                print('Есть в наличии')
            else:
                print('Нет в наличии')

    def prog1():
        s = IceCreamStand("Ванилла", "Кафе-Мороженое", "Плошадь", "10:00-17:00", ["Ваниль", "Шоколад", "Клубника"])
        s.describe_restaurant()
        s.describe_flavors()
        s.delete('Ваниль')
        s.describe_flavors()
        s.add('Ваниль')
        s.describe_flavors()
        s.check("Ваниль")
    def prog2():
        sticks = Stick("Ванилла", "Кафе-Мороженое", "Плошадь", "10:00-17:00", ["Ваниль", "Шоколад", "Клубника"], "Мороженое на палочке")
        sticks.describe_restaurant()
        sticks.describe_flavors()
        sticks.delete('Ваниль')
        sticks.describe_flavors()
        sticks.add('Ваниль')
        sticks.describe_flavors()
        sticks.check("Ваниль")
    def prog3():
        soft = Soft("Ванилла", "Кафе-Мороженое", "Плошадь", "10:00-17:00", ["Ваниль", "Шоколад", "Клубника"], "Мягкое мороженое")
        soft.describe_restaurant()
        soft.describe_flavors()
        soft.delete('Ваниль')
        soft.describe_flavors()
        soft.add('Ваниль')
        soft.describe_flavors()
        soft.check("Ваниль")
    prog1()

def prog3():
    import tkinter as tk

    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors

        def display_flavors(self):
            print("Available flavors:")
            for flavor in self.flavors:
                print(flavor)

    class IceCreamApp:
        def __init__(self, ice_cream_stand):
            self.ice_cream_stand = ice_cream_stand

            self.root = tk.Tk()
            self.root.title(self.ice_cream_stand.name)

            self.flavors_label = tk.Label(self.root, text="Available flavors:")
            self.flavors_label.pack()

            for flavor in self.ice_cream_stand.flavors:
                flavor_label = tk.Label(self.root, text=flavor)
                flavor_label.pack()

            self.root.mainloop()

    ice_cream_stand = IceCreamStand("Cool Treats", ["Vanilla", "Chocolate", "Strawberry", "Mint"])
    ice_cream_stand.display_flavors()
    app = IceCreamApp(ice_cream_stand)
prog3()