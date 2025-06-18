import random
print('''
         .---.
        /    |\________________
        ()  | ________   _   _)
         \    |/        | | | |
          `---'         "-" |_|
                               
''')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
for n in range(1,nr_letters+1):
    random_index = random.randint(0, len(letters)-1)
    password_list+=letters[random_index]
nr_symbols = int(input(f"How many symbols would you like?\n"))
for n in range(1,nr_symbols+1):
    random_index = random.randint(0, len(symbols)-1)
    password_list+=symbols[random_index]
nr_numbers = int(input(f"How many numbers would you like?\n"))
for n in range(1,nr_numbers+1):
    random_index = random.randint(0, len(numbers)-1)
    password_list+=numbers[random_index]

random.shuffle(password_list)

password = ''.join(password_list)
print(password)
