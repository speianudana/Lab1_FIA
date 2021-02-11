from production import AND, OR, match, populate, simplify


def backchain_to_goal_tree(rules, hypothesis):
    # find rules that produces this hypothesis
    rules_con = [hypothesis]

    for rule in rules:
        for con in rule.consequent():
            bindings = match(con, hypothesis)

            if bindings is not None:
                ant = rule.antecedent()

                if isinstance(ant, AND):
                    rules_con.append(AND([backchain_to_goal_tree(rules, populate(branch, bindings)) for branch in ant]))
                elif isinstance(ant, OR):
                    rules_con.append(OR([backchain_to_goal_tree(rules, populate(branch, bindings)) for branch in ant]))
                else:
                    rules_con.append(backchain_to_goal_tree(rules, populate(ant, bindings)))

    return simplify(OR(rules_con))