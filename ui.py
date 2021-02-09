from production import IF, AND, OR, NOT, THEN, forward_chain
import rules

run_client = True

given_rules = []
while run_client:
    TEST_RESULTS_1 = ""
    print("Give being's name?")
    name = raw_input("Name: ")

    print("Has the being more than 50 kg?")
    message = raw_input("Yes/No: ")
    if message == "Yes":
        given_rules.append(name + " has more than 50 kg")
    else:
        given_rules.append(name + " has less than 50 kg")

    print("Has the being more than 30 years?")
    message = raw_input("Yes/No: ")
    if message == 'Yes':
        given_rules.append(name + " has more than 30 years")
    else:
        given_rules.append(name + " has less than 30 years")

    print("Has white skin color?")
    message = raw_input("Yes/No: ")
    if message == 'Yes':
        given_rules.append(name + " has white skin color")

    print("How many fingers does " + name + " have?")
    message = raw_input("Number of fingers on a hand: ")
    print (int(message))
    if int(message) > 5:
        given_rules.append(name + " has more than 5 fingers")

    print("How many legs does " + name + " have?")
    message = raw_input("Number of legs: ")
    if int(message) > 4:
        given_rules.append(name + " has more than 4 legs")

    TEST_RESULTS_1 = forward_chain([rules.rule1, rules.rule4, rules.rule2], given_rules)
    print TEST_RESULTS_1[-1]

