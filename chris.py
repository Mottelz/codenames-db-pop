import database_connections as db
import spinup_data
from collections import Counter

new_db = db.Database("new.db")


def get_all_clues(words: []):
    to_ret = []
    for word in words:
        to_ret += spinup_data.get_related_words(word)
    return to_ret


def count_valid(counter):
    valid = 0
    for pair in counter.most_common():
        if pair[1] > 2:
            valid = valid + 1
    return valid


def sanitize_codenames(old_codenames):
    counter = Counter(old_codenames)
    new_codenames = set()

    for pair in counter.most_common(100):
        if pair[1] > 2:
            new_codenames.add(pair[0])
            if len(new_codenames) == 60:
                break

    for codename in old_codenames:
        clues = spinup_data.get_related_words(codename)
        if any(True for clue in clues if clue in new_codenames):
            new_codenames.add(codename)

    return list(new_codenames)


codenames = new_db.get_all_codenames()
counter = Counter(get_all_clues(codenames))
n = count_valid(counter)

while n < 200:
    print(n)
    codenames = sanitize_codenames(codenames)
    counter = Counter(get_all_clues(codenames))
    n = count_valid(counter)

print(counter)
