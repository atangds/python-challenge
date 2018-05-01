import re

letters = []
with open("paragraph_1.txt") as file:
    # reader is one string.
    reader = file.read()
    # words = reader.split(" "); this would get all words with punctuations.
    # set what to match; \b: word boundry; allowing letters, numbers, hyphens, dots and apostrophes in words.
    # \b[\w-.']+\b not working.
    findWords = re.compile(r"\b[\w.'-]+\b")
    # words is a list of all words.
    words = findWords.findall(reader)
    # sentences = reader.split("."); number of sentences = len(sentences) - 1.
    # to separate sentences, find one or more .?! followed by optional ") followed by space.
    sentences = re.split(r"[.?!]+[\")]*\s", reader)
    for word in words:
        letters.append(len(word))

print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {len(words)}")
print(f"Approximate Sentence Count: {len(sentences)}")
print(f"Average Letter Count: {sum(letters)/len(words)}")
print(f"Average Sentence Length: {len(words)/len(sentences)}\n")

# repeat for another file.
letters = []
with open("paragraph_2.txt") as file:
    reader = file.read()
    findWords = re.compile(r"\b[\w.'-]+\b")
    words = findWords.findall(reader)
    sentences = re.split(r"[.?!]+[\")]*\s", reader)
    for word in words:
        letters.append(len(word))

print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {len(words)}")
#  there's a name "Anne V. Coates" that will result in an extra sentence.
print(f"Approximate Sentence Count: {len(sentences)-1}")
print(f"Average Letter Count: {sum(letters)/len(words)}")
print(f"Average Sentence Length: {len(words)/len(sentences)}\n")
