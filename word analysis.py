def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count = count + 1
    return count
def find_longest(words):
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest
def find_shortest(words):
    shortest = words[0]
    for w in words:
        if len(w) < len(shortest):
            shortest = w
    return shortest
sentence = input("Enter a sentence: ")
words = sentence.split()
total_words = len(words)
total_chars = len(sentence)
longest_word = find_longest(words)
shortest_word = find_shortest(words)
vowel_count = count_vowels(sentence)
unique_words = set(words)
sorted_words = sorted(unique_words)
print("Total words:", total_words)
print("Total characters:", total_chars)
print("Longest word:", longest_word)
print("Shortest word:", shortest_word)
print("Number of vowels:", vowel_count)
print("Unique words:", unique_words)
print("Words in alphabetical order:")
for w in sorted_words:
    print(w)
file = open("word_analysis.txt", "w")
file.write("Sentence: " + sentence + "\n")
file.write("Total words: " + str(total_words) + "\n")
file.write("Total characters: " + str(total_chars) + "\n")
file.write("Longest word: " + longest_word + "\n")
file.write("Shortest word: " + shortest_word + "\n")
file.write("Number of vowels: " + str(vowel_count) + "\n")
file.write("Unique words: " + str(unique_words) + "\n")
file.write("Words in alphabetical order: " + str(sorted_words) + "\n")
file.close()
print("Analysis saved in word_analysis.txt")
