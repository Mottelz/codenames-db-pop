import database_connections as db
import spinup_data

database = db.Database("codenames.db")

codenames = database.get_all_codenames()

for codename in codenames:
    clues = spinup_data.get_related_words(codename)
    for clue in clues:
        database.add_reference(clue, codename)
