DROP TABLE IF EXISTS country;

CREATE TABLE country (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  area INTEGER NOT NULL,
  capitalName TEXT NOT NULL,
  countryName TEXT NOT NULL,
);
