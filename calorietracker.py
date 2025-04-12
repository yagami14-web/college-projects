class User:
    def __init__(self, name, height, weight, goal, diet):
        self.name = name
        self.height = height
        self.weight = weight
        self.goal = goal
        self.diet = diet.lower()


class DietPlan:
    def __init__(self, diet):
        self.diet = diet.lower()
        self.meals = {
            "vegan": {
                "morning": ["Oats with almond milk", "Banana smoothie"],
                "afternoon": ["Chickpea salad", "Lentil soup"],
                "evening": ["Tofu stir fry", "Veg wrap"]
            },
            "vegetarian": {
                "morning": ["Cornflakes with milk", "Poha"],
                "afternoon": ["Paneer curry", "Dal rice"],
                "evening": ["Veg soup", "Roti sabzi"]
            },
            "omnivore": {
                "morning": ["Eggs and toast", "Yogurt"],
                "afternoon": ["Chicken salad", "Fish curry with rice"],
                "evening": ["Grilled chicken", "Soup"]
            },
            "carnivore": {
                "morning": ["Bacon and eggs", "Chicken sausage"],
                "afternoon": ["Steak and eggs", "Roast chicken"],
                "evening": ["Beef stir fry", "Chicken wings"]
            }
        }

    def show(self):
        if self.diet not in self.meals:
            print("Diet type not recognized.")
            return

        print(f"\nDiet plan for {self.diet}:")

        print("\nMorning:")
        for item in self.meals[self.diet]["morning"]:
            print("-", item)

        print("\nAfternoon:")
        for item in self.meals[self.diet]["afternoon"]:
            print("-", item)

        print("\nEvening:")
        for item in self.meals[self.diet]["evening"]:
            print("-", item)


class Tracker:
    def __init__(self, user):
        self.user = user
        self.total = 0
        self.food_log = []

    def add_food(self, food, cal):
        self.food_log.append((food, cal))
        self.total += cal
        print(f"Added: {food} ({cal} kcal). Total so far: {self.total} kcal.")

    def summary(self):
        print(f"\nCalorie Summary for {self.user.name}:")
        print(f"Goal: {self.user.goal} kcal")
        print(f"calories consumed: {self.total} kcal")

        if self.total < self.user.goal:
            print("You are under your calorie goal.")
        elif self.total > self.user.goal:
            print("You are over your calorie goal.")
        else:
            print("You hit your calorie goal exactly!")

        print("\nFood log:")
        for item in self.food_log:
            print(f"- {item[0]}: {item[1]} kcal")


# -------- Main Program --------

name = input("Your name: ")
height = float(input("Your height (cm): "))
weight = float(input("Your weight (kg): "))
goal = int(input("Daily calorie goal: "))
diet = input("Diet type (vegan / vegetarian / omnivore / carnivore): ")

user = User(name, height, weight, goal, diet)
plan = DietPlan(user.diet)
tracker = Tracker(user)

plan.show()

while True:
    more = input("\nAdd food? (yes/no): ").lower()
    if more != "yes":
        break

    food = input("Food name: ")
    cal = int(input("Calories: "))
    tracker.add_food(food, cal)

tracker.summary()
print("thank you for using my app")
