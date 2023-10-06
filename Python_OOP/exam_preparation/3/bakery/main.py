from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

bakery = Bakery("Sun and Moon")
bread1 = Bread("Limec", 20)
bread2 = Bread("Mac", 15)
bread3 = Bread("White", 10)
cake1 = Cake("Borovinka", 20)
cake2 = Cake("Banana", 15)
cake3 = Cake("Avocado", 10)
drink1 = Tea("Ice", 4, "Nestle")
drink2 = Tea("Hot", 3, "Lind")
drink4 = Water("Izvorna", 5, "Bankq")
drink5 = Water("Vitamin", 4, "GornaBanq")
table1 = InsideTable(25, 10)
table2 = OutsideTable(56, 4)

bakery.add_food("Bread", "Limec", 20)
bakery.add_food("Bread", "Mac", 15)
bakery.add_food("Bread", "White", 10)
bakery.add_food("Cake", "Borovinka", 20)
bakery.add_food("Cake", "Banana", 15)
bakery.add_food("Cake", "Avocado", 10)

bakery.add_drink("Tea", "Ice", 4, "Nestle")
bakery.add_drink("Tea", "Hot", 3, "Lind")
bakery.add_drink("Water", "Izvorna", 5, "Bankq")
bakery.add_drink("Water", "Vitamin", 4, "GornaBanq")

bakery.add_table("InsideTable", 25, 10)
bakery.add_table("OutsideTable", 56, 4)

food_names = ["Limec", "Mac", "Banana"]
drink_names = ["Ice", "Vitamin"]
bakery.reserve_table(10)
print(bakery.order_food(25, *food_names))
print(bakery.order_drink(25, *drink_names))

print(bakery.leave_table(25))
print(bakery.get_free_tables_info())
print(bakery.get_total_income())

