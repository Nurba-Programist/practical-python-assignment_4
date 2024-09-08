def rock_paper_scissors():

    player = int(input("1 - камень, 2 - ножница, 3 - бумага. Введите ваш выбор: "))
    computer = 1

    if player == computer:
        print("Ничья!")

    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 2):
        print("Вы выиграли!")

    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("Вы проиграли!")
    else:
        print("Неверная команда. Попробуйте снова.")


def guess_the_number():
   number = 7 

   while True:
       guess_num = int(input("Введите число: "))

       if guess_num > number:
          print("Число больше сем нужно. Попробуйте ещё раз!")
       elif guess_num < number:
           print("Число меньше чем нужно. Попробуйте ещё раз!")
       else:
           print("Поздравляю вы угодали! Возврат в главное меню.")
           break
       
def main_menu():

    while True:
        print("Во что хотите поиграть?")
        game = int(input("1 - Камень, ножница, бумага; 2 - Угадай число; 3 - Выйти: "))

        if game == 1:
            rock_paper_scissors()
        elif game == 2:
            guess_the_number()
        elif game == 3:
            print("Выход из программы. ")
            break
        else:
            print("Неверная команда. Попробуйте снова. ")

main_menu()