from nltk.corpus import wordnet as wn


def get_related_words(word: str):
    related_words = []  # The list of words to return

    for syn in wn.synsets(word):  # For each sense of the word.
        for l in syn.lemmas():  # For each related word
            new_word = l.name().lower()
            # Make sure it's a single word and not the word given
            if all_good(word, new_word, related_words):
                related_words.append(l.name())
    return related_words


def all_good(core_word, new_word, words):
    if core_word in new_word or new_word in core_word:
        return False
    if new_word in words:
        return False
    if '_' in new_word:
        return False

    for rword in words:
        if same(rword, new_word):
            return False

    return True


def same(word1, word2):
    sense1 = wn.synsets(word1)[0]
    sense2 = wn.synsets(word2)[0]

    if sense1.wup_similarity(sense2) == 1.0:
        return True
    else:
        return False
