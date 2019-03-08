from nltk.corpus import wordnet as wn


def get_related_words(word: str):
    related_words = []  # The list of words to return

    for syn in wn.synsets(word):  # For each sense of the word.
        for l in syn.lemmas():  # For each related word
            new_word = l.name()
            # Make sure it's a single word and not the word given
            if word not in new_word and '_' not in new_word and new_word not in related_words:
                related_words.append(l.name())
    return related_words


