from collections import Counter

corpus = [
    "I love NLP",
    "I love Python",
    "I study NLP",
    "We study Python",
    "You love NLP",
    "I study Python"
]

tokens = []
for sentence in corpus:
    tokens.extend(sentence.split())

print("Tokens:")
print(tokens)

unigram_counts = Counter(tokens)

print("\nUnigram Frequency:")
for word, count in unigram_counts.items():
    print(f"{word}: {count}")

bigrams = []

for sentence in corpus:
    words = sentence.split()
    for i in range(len(words) - 1):
        bigrams.append((words[i], words[i + 1]))

bigram_counts = Counter(bigrams)

print("\nBigram Frequency:")
for bg, count in bigram_counts.items():
    print(f"{bg}: {count}")

total_words = len(tokens)

print("\nUnigram Probabilities:")
for word, count in unigram_counts.items():
    print(f"P({word}) = {count}/{total_words} = {count/total_words:.4f}")

print("\nBigram Probabilities (MLE):")

for (w1, w2), count in bigram_counts.items():
    probability = count / unigram_counts[w1]
    print(f"P({w2}|{w1}) = {count}/{unigram_counts[w1]} = {probability:.4f}")

first = input("\nEnter first word of bigram: ")
second = input("Enter second word of bigram: ")

bigram = (first, second)

if bigram in bigram_counts:
    probability = bigram_counts[bigram] / unigram_counts[first]
    print("\nBigram exists in the corpus.")
    print("Frequency:", bigram_counts[bigram])
    print("Probability:", round(probability, 4))
else:
    print("\nBigram does NOT exist in the corpus.")
    print("Frequency: 0")
    print("Probability: 0")
