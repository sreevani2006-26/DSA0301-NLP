# Context-Free Grammar (CFG)
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["I"], ["You"]],
    "VP": [["V", "N"]],
    "V": [["like"], ["love"]],
    "N": [["Python"], ["NLP"]]
}

# Recursive Top-Down Parser
def parse(symbol, words):
    # If symbol is a terminal
    if symbol not in grammar:
        if words and words[0] == symbol:
            return words[1:]
        return None

    # Try each production rule
    for production in grammar[symbol]:
        remaining = words
        success = True

        for sym in production:
            remaining = parse(sym, remaining)
            if remaining is None:
                success = False
                break

        if success:
            return remaining

    return None


# Input sentence
sentence = "I like Python"
words = sentence.split()

# Parse from start symbol S
result = parse("S", words)

if result == []:
    print("Sentence Accepted")
else:
    print("Sentence Rejected")
