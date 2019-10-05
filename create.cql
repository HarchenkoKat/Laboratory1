CREATE KEYSPACE Katya
WITH REPLICATION = {'class': 'SimpleStrategy',
	'replication_factor': 3
};

USE Katya;

CREATE TYPE time_format(
	hours int,
	minutes int,
	second int
);

CREATE TABLE User(
	user_id int,
	user_name text,
	age int,
	weight int,
	activity int,
	PRIMARY KEY((user_id))
);

CREATE TABLE Messanger (
	user_id int,
	messanger_name text,
	address text,
	PRIMARY KEY((user_id), messanger_name)
	);

CREATE TABLE Complex (
	user_id int,
	day int,
	complex_name text,
	time_start frozen<time_format>,
	type text,
	PRIMARY KEY((user_id), day)
);

CREATE TABLE Exercise (
	complex_name text,
	exercise_name text,
	time_length frozen<time_format>,
	kcal int,
	repeats int static,
	PRIMARY KEY((complex_name), exercise_name )
);