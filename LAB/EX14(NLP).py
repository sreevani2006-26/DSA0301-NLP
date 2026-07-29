# Subject-Verb Agreement Checker using CFG Rules

grammar = {
    "Singular_Subject": ["He", "She", "Ram"],
    "Plural_Subject": ["They", "We", "Students"],
    "Singular_Verb": ["likes", "plays", "runs"],
    "Plural_Verb": ["like", "play", "run"]
}

# Input sentence
sentence = input("Enter a sentence: ").split()

# Check agreement
if len(sentence) >= 2:
    subject = sentence[0]
    verb = sentence[1]

    if subject in grammar["Singular_Subject"] and verb in grammar["Singular_Verb"]:
        print("Sentence is Grammatically Correct.")

    elif subject in grammar["Plural_Subject"] and verb in grammar["Plural_Verb"]:
        print("Sentence is Grammatically Correct.")

    else:
        print("Sentence is Grammatically Incorrect.")

else:
    print("Invalid Sentence.")
