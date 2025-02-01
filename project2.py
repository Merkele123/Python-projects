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

# Open the file and read the entire text
with open("story.txt", "r") as f:
    story = f.read()

# Use a set to extract words between < and >
# Find the index of the ">" character starting from the current "<" character
words = {story[i:j+1] for i, char in enumerate(story) if char == "<" and (j := story.find(">", i)) != -1}

# Collect user responses for each word
answers = {word: input(f"Enter a word for {word}: ") for word in words}

# Replace each word with the user-provided input
story = ''.join(answers.get(word, word) for word in (story.split('<')[0], *words))

# Print the final string after replacements
print(story)
