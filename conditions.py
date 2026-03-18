import random


number_to_guess= random.randint(1, 1000)
guess = -1
abandon = False


while guess != number_to_guess:  
    instruction = input("Entrez un nombre entre 1 et 1000 [q: quitter]")
    
    if not instruction.isnumeric():
        if instruction == 'q':
            abandon = True
            break
        else:
            print("instruction is invalid")
            continue
    guess = int(instruction)  
    if guess < number_to_guess:
        print("C'est plus")
    elif guess > number_to_guess:
        print("C'est moin")
if abandon:
    print(f"Dommage, le nombre était {number_to_guess}")
else:
    print(f"Bravo, vous avez trouvé le nombre {number_to_guess}")


