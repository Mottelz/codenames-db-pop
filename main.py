import database_connections as db
import spinup_data
from collections import Counter

# The databases
# old_db = db.Database("old.db")
new_db = db.Database("new.db")

# old_words = old_db.get_all_words()
#
# for word in old_words:
#     related_words = spinup_data.get_related_words(word)
#     if len(related_words) > 1:
#         for clue in related_words:
#             print("Adding " + word + " and " + clue)
#             new_db.add_reference(clue, word)


def get_all_da_clues(words: []):
    to_ret = []
    for word in words:
        to_ret += spinup_data.get_related_words(word)
    return to_ret


def get_num_of_good(c: Counter):
    to_ret = 0
    for pair in c.most_common():
        if pair[1] > 2:
            to_ret += 1
    return to_ret


codenames = new_db.get_all_codenames()
all_da_clues = get_all_da_clues(codenames)
c1 = Counter(all_da_clues)
codenames2 = set()

for pair in c1.most_common(100):
    if pair[1] > 2:
        codenames2.add(pair[0])

for codename in codenames:
    clues = spinup_data.get_related_words(codename)
    if any(True for clue in clues if clue in codenames2):
        codenames2.add(codename)

all_da_clues = get_all_da_clues(list(codenames2))

c2 = Counter(all_da_clues)
codenames3 = set()

for pair in c2.most_common(50):
    if pair[1] > 2:
        codenames3.add(pair[0])

for codename in codenames2:
    clues = spinup_data.get_related_words(codename)
    if any(True for clue in clues if clue in codenames3):
        codenames3.add(codename)

all_da_clues = get_all_da_clues(list(codenames3))

c3 = Counter(all_da_clues)
# print(c3.most_common(100))
codenames4 = set()

for pair in c3.most_common(50):
    if pair[1] > 2:
        codenames4.add(pair[0])

for codename in codenames3:
    clues = spinup_data.get_related_words(codename)
    if any(True for clue in clues if clue in codenames4):
        codenames4.add(codename)

all_da_clues = get_all_da_clues(list(codenames4))

c4 = Counter(all_da_clues)
# print(c4.most_common(100))
codenames5 = set()

for pair in c4.most_common(60):
    if pair[1] > 2:
        codenames5.add(pair[0])

for codename in codenames4:
    clues = spinup_data.get_related_words(codename)
    if any(True for clue in clues if clue in codenames5):
        codenames5.add(codename)

all_da_clues = get_all_da_clues(list(codenames5))

c5 = Counter(all_da_clues)
