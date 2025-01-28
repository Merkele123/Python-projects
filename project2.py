with open("story.txt", "r") as f:
    story = f.read()

words = set()

strat_of_word = -1
target_start = "<"
target_end = ">"


for i, char in enumerate(story):
    if char == target_start:
        strat_of_word = i

    if char == target_end and strat_of_word != -1:
        word = story[strat_of_word : i + 1]
        words.add(word)
        strat_of_word = -1

answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
print(story)

# Short version

# Открываем файл и считываем весь текст
with open("story.txt", "r") as f:
    story = f.read()

# Используем множество для извлечения слов между < и >
# Ищем индекс символа ">", начиная с текущего символа "<"
words = {story[i:j+1] for i, char in enumerate(story) if char == "<" and (j := story.find(">", i)) != -1}

# Собираем ответы пользователя для каждого слова
answers = {word: input(f"Enter a word for {word}: ") for word in words}

# Заменяем каждое слово на введенное пользователем
story = ''.join(answers.get(word, word) for word in (story.split('<')[0], *words))

# Выводим итоговую строку после замен
print(story)
