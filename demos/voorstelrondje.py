import random
import time

names = ["Peter-Paul", "Rick M.", "Roland", "Marianne",
         "Thomas", "Peter", "Jeske", "Kolja", "Rick H.",
         "Robin"]

random.shuffle(names)

print("\nIntroductie:\n")
print(
    """
    1. Wie ben je?
    2. Wat is je achtergrond?
    3. Wat wil je leren?
    4. Welke programmeertalen ken je al?
    5. Fun Fact
    """
)
print("Volgorde:\n")

time.sleep(1.5)
for index, participant in enumerate(names, start=1):
    print(f"{index}. {participant}")
    time.sleep(1.5)
