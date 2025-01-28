import random

# Функция для симуляции броска кубика
def roll():
    min_value = 1  # Минимальное значение на кубике
    max_value = 6  # Максимальное значение на кубике
    roll = random.randint(min_value, max_value)  # Генерация случайного числа от 1 до 6
    return roll  # Возвращаем результат броска

# Бесконечный цикл для получения корректного количества игроков
while True:
    players = input("Enter the number of players( 2 - 4 ): ")  # Запрашиваем количество игроков
    if players.isdigit():  # Проверяем, является ли ввод числом
        players = int(players)  # Преобразуем ввод в целое число
        if 2 <= players <= 4:  # Проверяем, что количество игроков в диапазоне от 2 до 4
            break  # Выходим из цикла, если условия выполнены
        else:
            print("Must be between (2 - 4)")  # Сообщаем о некорректном вводе
    else:
        print("Invalid number of players, try again:")  # Сообщаем о некорректном вводе

max_score = 50  # Максимальное количество очков для победы
player_scores = [0 for _ in range(players)]  # Список для хранения очков всех игроков

# Основной игровой цикл
while max(player_scores) < max_score:  # Игра продолжается, пока никто не достиг максимального количества очков
    for player_index in range(players):  # Проходим по всем игрокам
        print(f"\nPlayer: {player_index + 1} turn has just started!\n")  # Уведомляем о начале хода игрока
        print(f"Your total score is {player_scores[player_index]}")  # Выводим текущий общий счет игрока
        current_score = 0  # Счет за текущий ход

        # Цикл для выполнения бросков текущего игрока
        while True:
            should_roll = input("Would you like to take a roll? Press 'y' ")  # Запрос на бросок кубика
            if should_roll.lower() != "y":  # Если игрок отказывается бросать
                current_score = 0  # Счет за ход обнуляется
                break  # Выход из цикла бросков

            value = roll()  # Бросок кубика
            if value == 1:  # Если выпадает 1
                print("you rolled a 1. Turn done")  # Сообщаем, что ход завершен
                break  # Выход из цикла бросков
            else:
                current_score += value  # Добавляем выпавшее значение к счету за ход
                print(f"You rolled a: {value}")  # Сообщаем о значении броска
            print(f"Your current score is: {current_score}")  # Выводим текущий счет за ход

        player_scores[player_index] += current_score  # Добавляем счет за ход к общему счету игрока
        print(f"Your total score is: {player_scores[player_index]}")  # Выводим общий счет игрока

# После завершения игры определяем победителя
max_score = max(player_scores)  # Определяем максимальный счет среди всех игроков
winning_idx = player_scores.index(max_score)  # Находим индекс игрока с максимальным счетом
print(f"Player number {winning_idx + 1} is winning with the score of: {max_score}")  # Сообщаем о победителе


# def roll():
#     """Simulates rolling a die."""
#     return random.randint(1, 6)


# def get_player_count():
#     """Prompts the user to input a valid number of players."""
#     while True:
#         players = input("Enter the number of players (2-4): ")
#         if players.isdigit():
#             players = int(players)
#             if 2 <= players <= 4:
#                 return players
#             else:
#                 print("Number of players must be between 2 and 4.")
#         else:
#             print("Invalid input. Please enter a number between 2 and 4.")


# def take_turn(player_index, current_score):
#     """Handles a single player's turn."""
#     print(f"\nPlayer {player_index + 1}, it's your turn!")
#     print(f"Your current total score is {current_score}")
#     turn_score = 0

#     while True:
#         should_roll = input("Would you like to roll the die? (y to roll): ").strip().lower()
#         if should_roll != 'y':
#             print("You chose to end your turn.")
#             break

#         rolled_value = roll()
#         if rolled_value == 1:
#             print("You rolled a 1! Your turn is over, and you lose all turn points.")
#             turn_score = 0
#             break
#         else:
#             turn_score += rolled_value
#             print(f"You rolled a {rolled_value}.")
#             print(f"Your turn score is now {turn_score}.")

#     return turn_score


# def display_scores(player_scores):
#     """Displays the current scores of all players."""
#     print("\nCurrent Scores:")
#     for i, score in enumerate(player_scores):
#         print(f"Player {i + 1}: {score}")


# def play_game():
#     """Main function to play the dice game."""
#     max_score = 50
#     player_count = get_player_count()
#     player_scores = [0] * player_count

#     while max(player_scores) < max_score:
#         for player_index in range(player_count):
#             turn_score = take_turn(player_index, player_scores[player_index])
#             player_scores[player_index] += turn_score
#             print(f"Player {player_index + 1}'s total score is now {player_scores[player_index]}.")

#             if player_scores[player_index] >= max_score:
#                 break  # End game early if a player reaches the max score.

#         display_scores(player_scores)

#     # Determine the winner
#     winning_score = max(player_scores)
#     winning_player = player_scores.index(winning_score) + 1
#     print(f"\nCongratulations Player {winning_player}! You win with a score of {winning_score}.")


# if __name__ == "__main__":
#     play_game()
