from backchain import backchain_to_goal_tree
from production import forward_chain
import rules

possible_results = ["Marsian", "Siriusian", "Quasarian", "Earthian", "Loonie", "Orionian"]


def yes(ques):
    ans = raw_input(ques).lower()
    return ans[0] == 'y'


answers = []


def ask_questions(tree, name):
    if tree is None:
        return
    result = yes(tree.cargo.format(name) + '? y/n ')
    if result:
        answers.append(tree.cargo.format(name).encode('utf8'))
        ask_questions(tree.left, name)
    else:
        ask_questions(tree.right, name)


run_client = True

while run_client:
    answers = []
    print('Give name')
    name = raw_input('Name: ')
    type_of_chain = raw_input('Forward or Backward chain?(F/B):')
    if type_of_chain == "F":
        ask_questions(rules.tree, name)
        result = forward_chain(rules.RULES, answers)
        if len(result) != 0:
            nationality = result[-1].split()[-1]
            if nationality in possible_results:
                print(result[-1])
            else:
                print "Unknown"
        else:
            print "Unknown"
    else:
        nationality = raw_input('Enter nationality:')
        print backchain_to_goal_tree(rules.RULES, name + ' is a ' + nationality)


HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''