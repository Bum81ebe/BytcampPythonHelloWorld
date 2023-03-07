#asking a question and greeting version3 different Names

name = input("What is your name? ").title().strip()
language = input("Which of the following language do you speak - English, German, French or Georgian? ").title().strip()


if language == "English":
    print(f"Hello, {name}, nice to meet you!")
elif language == "German":
    print(f"Hallo, {name}, schön, Sie kennenzulernen!")
elif language == "French":
    print(f"Bonjour, {name}, enchanté de vous rencontrer!")
elif language == "Georgian":
    print(f"გამარჯობა, {name}, სასიამოვნოა შენი გაცნობა!")
else:
    print(f"Hello, {name}, Since i do not know your language i will say Hello in English!")