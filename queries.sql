--  Find out how many Clues exist per clue word.
SELECT count(c) FROM (select Count(clue) as c from Suggest GROUP BY clue) WHERE c=1;

-- Find out how many clues exist per codename.
SELECT count(c) FROM (select Count(codename) as c from Suggest GROUP BY codename) WHERE c=1;

-- Get number of Clues.
SELECT Count(clue) FROM Clues;

-- Get number of Codenames.
SELECT Count(codename) FROM Codenames;

-- Get the clues for a codename
SELECT * FROM Suggest WHERE codename='CODENAME';

-- Get the codenames for a clue
SELECT * FROM Suggest WHERE codename='CODENAME';
