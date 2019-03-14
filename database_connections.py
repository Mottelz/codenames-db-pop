import sqlite3
from sqlite3 import Error

# Code from http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# Edited by Mottel Zirkind on March 8, 2019

import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_path):
        self.db_file = db_path
        self.conn = self.create_connection(self.db_file)

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None

    def get_all_words(self):
        """
        Query all rows from the given table
        :return: An array of all the words
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Word")

        rows = cur.fetchall()
        words = []
        for row in rows:
            for word in row:
                words.append(word)
        return words

    def add_codename(self, word):
        """
        Add a codename
        :param word: the word to add
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Codenames(codename) VALUES(?)", (word,))
        self.conn.commit()

    def add_clue(self, word):
        """
        Add a codename
        :param word: the word to add
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Clues(clue) VALUES(?)", (word,))
        self.conn.commit()

    def add_reference(self, clue, codename):
        """
        Add a record to the suggest
        :param clue: The clue word
        :param codename: The codename
        :return:
        """
        # Verify that the clue and codename already exist
        if not self.codename_exists(codename):
            self.add_codename(codename)
        if not self.clue_exists(clue):
            self.add_clue(clue)

        # If this doesn't exist
        if not self.reference_exists(clue, codename):
            cur = self.conn.cursor()
            cur.execute("INSERT INTO Suggest(clue, codename) VALUES(?, ?)", (clue, codename))
            self.conn.commit()

    def codename_exists(self, codename):
        """
        Verify that the codename already exists
        :param codename: the codename to be checked
        :return: true if it's there, otherwise false
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Codenames WHERE codename=?", (codename, ))
        row = cur.fetchone()
        if row is not None:
            return True
        else:
            return False

    def clue_exists(self, clue):
        """
        Verify that the codename already exists
        :param clue: the clue to be checked
        :return: true if it's there, otherwise false
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Clues WHERE clue=?", (clue, ))
        row = cur.fetchone()
        if row is not None:
            return True
        else:
            return False

    def reference_exists(self, clue, codename):
        """
        Verify that the codename already exists
        :param clue: the clue to be checked
        :param codename: the codename to be checked
        :return: true if it's there, otherwise false
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Suggest WHERE clue=? AND codename=?", (clue, codename))
        row = cur.fetchone()
        if row is not None:
            return True
        else:
            return False

    def get_all_codenames(self):
        """
        Query all rows from the given table
        :return: An array of all the codenames
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Codenames")

        rows = cur.fetchall()
        codenames = []
        for row in rows:
            for codename in row:
                codenames.append(codename)
        return codenames

    def add_board_layout(self, first, layout):
        """
        Add a board layout
        :param first: red || blue. The team that goes first.
        :param layout: string of chars CARB that defines the board layout.
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("INSERT INTO BoardLayouts(firstTeam, layout) VALUES(?, ?)", (first, layout))
        self.conn.commit()
