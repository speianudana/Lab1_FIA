from production import IF, AND, THEN

RULES = (

    IF(AND('(?y) has red clothes',  # rule 3
           '(?y) has blue eyes',
           '(?y) has black skin color',
           '(?y) has more than 50 kg',
           '(?y) has more than 30 years'),
       THEN('(?y) is a Quasarian')),

    IF(AND('(?y) has red clothes',  # rule 5
           '(?y) has brown eyes',
           '(?y) has Moldavian accent',
           '(?y) has white skin color'),
       THEN('(?y) is an Earthian')),

    IF(AND('(?y) has red clothes',  # rule 6
           '(?y) has more than 4 legs', ),
       THEN('(?y) is a Marsian')),

    IF(AND('(?y) has white clothes',  # rule 7
           '(?y) has less than 7 fingers'),
       THEN('(?y) is an Orionian')),

    IF(AND('(?y) has white clothes',  # rule 8
           '(?y) has white skin color',
           '(?y) has more than 80 kg'),
       THEN('(?y) is a Siriusian')),

    IF(AND('(?y) has red clothes',  # rule 9
           '(?y) has green eyes',
           '(?y) black skin color'),
       THEN('(?y) is a Loonie'))
)

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


tree = Tree('{0} has red clothes',
            Tree('{0} has blue eyes', Tree('{0} has black skin color',
                                           Tree('{0} has more than 50 kg', Tree('{0} has more than 30 years'))),

                 Tree('{0} has brown eyes', Tree('{0} has Moldavian accent', Tree('{0} has white skin color')),
                      Tree('{0} has green eyes', Tree('{0} has black skin color'),
                           Tree('{0} has more than 4 legs')))),

            Tree('{0} has white clothes', Tree('{0} has white skin color',
                                               Tree('{0} has more than 80 kg'),
                                               Tree('{0} has less than 7 fingers'))))
