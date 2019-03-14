CREATE TABLE Codenames(
  codename string unique not null,
  primary key(codename)
);

CREATE TABLE Clues(
  clue string unique not null,
  primary key(clue)
);

CREATE TABLE Suggest(
  clue string not null,
  codename string not null,
  primary key(clue, codename),
  foreign key(clue) references Clues(clue),
  foreign key(codename) references Codenames(codename)
);

CREATE TABLE GameHistory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    blueTeamName VARCHAR(60),
    redTeamName VARCHAR(60),
    numberOfRounds INT NOT NULL,
    winner VARCHAR(60),
    assassinRevealed BIT,
    civilianRevealed INT,
    redTilesRevealed INT,
    blueTilesRevealed INT
);

CREATE TABLE BoardLayouts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstTeam string NOT NULL,
  layout string NOT NULL
);

-- How many of a given word's clues are also codenames
