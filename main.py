import database_connections as db
import spinup_data

# The databases
old_db = db.Database("old.db")
new_db = db.Database("new.db")

old_words = old_db.get_all_words()

for word in old_words:
    related_words = spinup_data.get_related_words(word)
    if related_words.__len__() > 1:
        for clue in related_words:
            print("Adding " + word + " and " + clue)
            new_db.add_reference(clue, word)


