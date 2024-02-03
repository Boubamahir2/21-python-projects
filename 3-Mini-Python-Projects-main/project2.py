with open("story.txt", "r") as f:
    story = f.read()
# print(story)
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)


'''
Here's a breakdown of the code:

1. Reading the Story:

with open("story.txt", "r") as f:: Opens the file "story.txt" in read mode ("r") and assigns the file object to f.
story = f.read(): Reads the entire content of the file into the variable story.
2. Finding Words to Replace:

words = set(): Creates an empty set named words to store unique words to be replaced.
target_start = "<", target_end = ">": Defines markers for words to be replaced (words enclosed in <>).
for i, char in enumerate(story):: Iterates through each character in story along with its index (i).
If char == target_start: Sets start_of_word to i, indicating the start of a potential word to replace.
If char == target_end and start_of_word != -1: Found the end of a word (both start and end markers are present).
word = story[start_of_word: i + 1]: Extracts the word (including markers).
words.add(word): Adds the word to the words set.
start_of_word = -1: Resets start_of_word for the next word.
3. Getting User Input:

answers = {}: Creates an empty dictionary answers to store user-provided replacements.
for word in words:: Iterates through each word in the words set.
answer = input("Enter a word for " + word + ": "): Prompts the user for a replacement for the word.
answers[word] = answer: Stores the user's input as the value for the corresponding key word in the answers dictionary.
4. Replacing Words:

for word in words:: Iterates through each word in the words set again.
story = story.replace(word, answers[word]): Replaces each occurrence of the word in the story string with the corresponding replacement from the answers dictionary.
5. Printing the Modified Story:

print(story): Prints the final modified story with the user-provided replacements.'''