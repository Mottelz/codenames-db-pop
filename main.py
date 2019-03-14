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


codenames = new_db.get_all_codenames()
all_da_clues = get_all_da_clues(codenames)
counter = Counter(all_da_clues)
new_codenames = set()

for pair in counter.most_common(100):
    if pair[1] > 2:
        new_codenames.add(pair[0])

for codename in codenames:
    clues = spinup_data.get_related_words(codename)
    if any(True for clue in clues if clue in new_codenames):
        new_codenames.add(codename)

all_da_clues = get_all_da_clues(list(new_codenames))

c2 = Counter(all_da_clues)
print(counter.most_common(100))
