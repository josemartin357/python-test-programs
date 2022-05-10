# Implement a program that computes the approximate grade level needed to comprehend some text.
from cs50 import get_string

# asking user input and stripping blank spaces at beginning and end
text = get_string("Enter text: ").strip()

# initiate values 
letter = 0
# words starts at 1 because logic calls to increase words for every blank space. In sentences, words will be 1 higher than empty spaces
words = 1
sentences = 0

# looping to count letter, words and sentences
for i in range(len(text)):
    # for every blank, add words +1
    if text[i] == ' ':
        words += 1
    # for every value from isalpha(), add letter +1
    elif text[i].isalpha():
        letter += 1
    # for every dot, question or exclamation mark, add sentences + 1
    elif text[i] == '.' or text[i] =='?' or text[i] =='!':
        sentences += 1

# L is average number of letters per 100 words
L = letter / words * 100
# S is average number of sentences per 100 words
S = sentences / words * 100
# Coleman-Liau formula
index = 0.0588 * L - 0.296 * S - 15.8
# print(index)

# conditionals to print
if index >= 16:
    print("Grade is 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade: {index}")


# NOTES:
# Program first asks the user to type in some text, and then outputs the grade level for the text, according to the Coleman-Liau formula.
# Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.