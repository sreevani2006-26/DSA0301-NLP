# Simple Earley Parser Implementation

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["I"], ["You"]],
    "VP": [["V", "N"]],
    "V": [["like"], ["love"]],
    "N": [["Python"], ["NLP"]]
}

sentence = "I like Python".split()

# Earley chart
chart = [set() for _ in range(len(sentence) + 1)]

# State format: (LHS, RHS, dot_position, start_position)
chart[0].add(("S'", ("S",), 0, 0))


def predictor(state, position):
    lhs, rhs, dot, start = state
    next_symbol = rhs[dot]

    if next_symbol in grammar:
        for production in grammar[next_symbol]:
            chart[position].add((next_symbol, tuple(production), 0, position))


def scanner(state, position):
    lhs, rhs, dot, start = state
    next_symbol = rhs[dot]

    if position < len(sentence) and next_symbol == sentence[position]:
        chart[position + 1].add((lhs, rhs, dot + 1, start))


def completer(state, position):
    lhs, rhs, dot, start = state

    for st in list(chart[start]):
        l, r, d, s = st

        if d < len(r) and r[d] == lhs:
            chart[position].add((l, r, d + 1, s))


# Earley Algorithm
for i in range(len(chart)):
    changed = True

    while changed:
        changed = False
        states = list(chart[i])

        for state in states:
            lhs, rhs, dot, start = state

            if dot < len(rhs):
                next_symbol = rhs[dot]

                before = len(chart[i])

                if next_symbol in grammar:
                    predictor(state, i)
                else:
                    scanner(state, i)

                if len(chart[i]) > before:
                    changed = True

            else:
                before = len(chart[i])
                completer(state, i)

                if len(chart[i]) > before:
                    changed = True

# Check acceptance
accepted = ("S'", ("S",), 1, 0) in chart[len(sentence)]

if accepted:
    print("Sentence Accepted")
else:
    print("Sentence Rejected")
