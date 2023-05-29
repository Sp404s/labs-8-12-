def prog1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print("Restaurant name:", self.restaurant_name)
            print("Cuisine type:", self.cuisine_type)

        def open_restaurant(self):
            print("Ресторан открыт")

    newRestaurant = Restaurant("Вкусно и точка", "Фаст-Фуд")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
def prog2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print("Restaurant name:", self.restaurant_name)
            print("Cuisine type:", self.cuisine_type)

        def open_restaurant(self):
            print("The restaurant", self.restaurant_name, "is now open.")

    fast = Restaurant("Вкусно и точка", "Фаст-Фуд")
    euro = Restaurant("Евразия", "Еврояпон")
    coff = Restaurant("Cofix", "Кофейня")

    fast.describe_restaurant()
    euro.describe_restaurant()
    coff.describe_restaurant()
def prog3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print("Restaurant name:", self.restaurant_name)
            print("Cuisine type:", self.cuisine_type)
            print("Rating:", self.rating)
        def update_rating(self, new_rating):
            self.rating = new_rating
    restaurant = Restaurant("Вкусно и точка", "Фаст-Фуд", 4.3)
    restaurant.describe_restaurant()
    restaurant.update_rating(4.8)
    restaurant.describe_restaurant()
prog3()