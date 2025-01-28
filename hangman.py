import random

# Список возможных слов для игры
words = ["apple", "window", "forest", "pencil", "journey", "coffee", "island", "garden", "rainbow", "mountain"]

# Выбираем случайное слово из списка
chosen_word = random.choice(words)

# Создаем список, который будет показывать подчеркивания для каждой буквы в выбранном слове
word_display = ['_' for _ in chosen_word]

# Количество попыток
attempts = 8

print("Welcome to Hangman!")  # Приветственное сообщение

# Пока игроки не исчерпали все попытки и в слове есть подчеркивания
while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))  # Показываем текущее состояние слова
    guess = input("Guess a letter: ").lower()  # Запрос ввода буквы и приведение к нижнему регистру
    
    # Проверяем, если буква есть в слове
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Разгадываем букву
    else:
        attempts -= 1  # Уменьшаем количество попыток
        print(f"That's a wrong letter! Try again! You have {attempts} attempts left.")

# После завершения цикла, проверяем, было ли найдено слово
if '_' not in word_display:
    print("You guessed the word!") 
    print(' '.join(word_display))  # Показываем полностью разгаданное слово
    print("You survived!")
else:
    print(f"You ran out of attempts. The word was: {chosen_word}")  # Сообщаем игроку, что он проиграл
    print("You died!")



# # List of possible words for the game
# words = ["apple", "window", "forest", "pencil", "journey", "coffee", "island", "garden", "rainbow", "mountain"]

# chosen_word = random.choice(words)  # Choose a random word
# word_display = ['_'] * len(chosen_word)  # Display underscores for each letter in the word
# attempts = 8  # Number of attempts

# print("Welcome to Hangman!")

# while attempts > 0 and '_' in word_display:
#     print("\n" + ' '.join(word_display))  # Display current word state
#     guess = input("Guess a letter: ").lower()  # Get input and convert to lowercase
    
#     if guess in chosen_word:
#         word_display = [guess if chosen_word[i] == guess else word_display[i] for i in range(len(chosen_word))]
#     else:
#         attempts -= 1
#         print(f"Wrong guess! You have {attempts} attempts left.")

# if '_' not in word_display:
#     print(f"Congratulations! The word was: {chosen_word}. You survived!")
# else:
#     print(f"Game Over! The word was: {chosen_word}. You ran out of attempts.")
