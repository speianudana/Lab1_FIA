from production import IF, AND, OR, NOT, THEN

RULES = (
    IF(AND('(?y) has more than 50 kg',  # rule 1
           '(?y) has more than 30 years', ),
       THEN('(?y) is old')),

    IF(AND('(?y) has more than 5 fingers',  # rule 2
           '(?y) has more than 4 legs', ),
       THEN('(?y) is sick')),

    IF(AND('(?y) has red clothes',  # rule 3
           '(?y) has blue eyes',
           '(?y) has black skin color',
           '(?y) is sick',
           '(?y) is old'),
       THEN('(?y) is a Quasarian')),

    IF(AND('(?y) has less than 30 years',  # rule 4
           '(?y) has white skin color'),
       THEN('(?y) is young')),

    IF(AND('(?y) has white eyes',  # rule 5
           '(?y) has moldavian accent',
           '(?y) is young'),
       THEN('(?y) is an Earthian')),

    IF(AND('(?y) has yellow clothes',  # rule 6
           '(?y) is sick', ),
       THEN('(?y) is a Marsian')),

    IF(AND('(?y) has white clothes',  # rule 7
           '(?y) has blue skin color',
           '(?y) is old'),
       THEN('(?y) is an Orionian')),

    IF(AND('(?y) has green clothes',  # rule 8
           '(?y) has american accent',
           '(?y) is young'),
       THEN('(?y) is a Siriusian')),
    IF(AND('(?y) has red clothes',  # rule 9
           '(?y) has blue eyes',
           '(?y) black skin color'),
       THEN('(?y) is a Loonie'))
)


# tree = {
#    "a": ["b", "c"],
#    "b": ["d", "e"],
#    "c": [None, "f"],
#    "d": [None, None],
#    "e": [None, None],
#    "f": [None, None],
# }

tree = {
   "What color are X's clothes?": ["Red", "Green","White", "Yellow"],
   "Red": ["What color are the eyes?"],
    "Green": ["Has X american accent?"],
    "White":["What color is the skin?"],
    "Yellow":["Has X more than 5 fingers on a hand?"],
    "What color are the eyes?": ["Blue", "Brown"],
   "Blue": ["What color is the skin?"],
   "Brown": ["Has X Moldavian accent?"],
    "Black":["Has X more than 5 fingers on a hand"],
   "f": [None, None],
}