INSERT INTO User (
	user_id, user_name, age, weight, activity
) VALUES (
	001, 'Sunny', 19, 69, 10
);

INSERT INTO User (
	user_id, user_name, age, weight, activity
) VALUES (
	002, 'Bunny', 21, 100, 4
);

INSERT INTO User (
	user_id, user_name, age, weight, activity
) VALUES (
	003, 'Garry', 25, 88, 3
);

SELECT user_id, user_name, age, weight, activity
FROM User;

INSERT INTO Messanger (
	user_id, messanger_name, address
) VALUES (
	001, 'gmail', 'SunnySuper@gmail.com'
);

INSERT INTO Messanger (
	user_id, messanger_name, address
) VALUES (
	002, 'telegram', '@Bunnyboy'
);

INSERT INTO Messanger (
	user_id, messanger_name, address
) VALUES (
	003, 'ukr.net', '@GarryPotter@ukr.net'
);

SELECT user_id, messanger_name, address
FROM Messanger;

INSERT INTO Complex (
	user_id, day, complex_name, time_start, type
) VALUES (
	001, 20, 'morning fresh', {hours: 8, minutes: 30, second: 0}, 'fulfilled'
);

INSERT INTO Complex (
	user_id, day, complex_name, time_start, type
) VALUES (
	002, 20, 'litl free', {hours: 10, minutes: 15, second: 0}, 'unfulfilled'
);

INSERT INTO Complex (
	user_id, day, complex_name, time_start, type
) VALUES (
	003, 20, 'big hard', {hours: 15, minutes: 55, second: 0}, 'awaiting'
);

SELECT user_id, day, complex_name, time_start, type
FROM Complex;

INSERT INTO Exercise (
	complex_name, exercise_name, time_length, kcal, repeats
) VALUES (
	'big hard', 'squat', {hours: 0, minutes: 0, second: 10}, 4, 100
);

INSERT INTO Exercise (
	complex_name, exercise_name, time_length, kcal, repeats
) VALUES (
	'big hard', 'push ups', {hours: 0, minutes: 0, second: 15}, 6, 100
);

INSERT INTO Exercise (
	complex_name, exercise_name, time_length, kcal, repeats
) VALUES (
	'morning fresh', 'squat', {hours: 0, minutes: 0, second: 10}, 4, 1
);

SELECT complex_name, exercise_name, time_length, kcal, repeats
FROM Exercise ;

UPDATE User 
SET weight = 68
WHERE user_id = 001;

UPDATE User 
SET activity = 12
WHERE user_id = 002;

UPDATE User 
SET age = 20
WHERE user_id = 003;

SELECT user_id, user_name, age, weight, activity
FROM User;

UPDATE Messanger
SET address = 'new form address'
WHERE user_id = 001 and messanger_name = 'ukr.net';

UPDATE Messanger
SET address = 'new form address'
WHERE user_id = 002 and messanger_name = 'ukr.net';

UPDATE Messanger
SET address = 'old '
WHERE user_id = 003 and messanger_name = 'ukr.net';

SELECT user_id, messanger_name, address
FROM Messanger;

UPDATE Complex
SET complex_name = 'old boy '
WHERE user_id = 001 and day = 20;

UPDATE Complex
SET time_start = {hours: 16, minutes: 55, second: 0}
WHERE user_id = 002 and day = 20;

UPDATE Complex
SET type = 'unfulfilled'
WHERE user_id = 003 and day = 20;

SELECT user_id, day, complex_name, time_start, type
FROM Complex;

UPDATE Exercise
SET time_length = {hours: 0, minutes: 0, second: 20}
WHERE complex_name = 'old boy '  and exercise_name = 'squat';

UPDATE Exercise
SET repeats = 20
WHERE complex_name = 'Big hard'  and exercise_name = 'squat';

UPDATE Exercise
SET kcal = 25
WHERE complex_name = 'morning fresh'  and exercise_name = 'push ups';

SELECT complex_name, exercise_name, time_length, kcal, repeats
FROM Exercise ;

SELECT complex_name, time_start
FROM Complex 
WHERE User_id = 001 AND day = 2
ALLOW FILTERING;

SELECT age, weight, activity
FROM User
WHERE user_id = 001;

SELECT type
FROM Complex
WHERE day = 20
ALLOW FILTERING;

SELECT exercise_name, repeats
FROM Exercise
WHERE complex_name = 'sit-down';

DELETE user_name, age, weight, activity
FROM User
WHERE user_id = 001;

DELETE  age, weight, activity
FROM User
WHERE user_id = 002; 

DELETE  age, activity
FROM User
WHERE user_id = 003; 

DELETE  address
FROM Messanger
WHERE user_id = 001;

DELETE  address
FROM Messanger
WHERE messanger_name = 'telegram';

DELETE address
FROM Messanger
WHERE user_id = 003;

DELETE complex_name, time_start, type
FROM Complex
WHERE user_id = 003;

DELETE complex_name
FROM Complex
WHERE day = 20;

DELETE type
FROM Complex
WHERE user_id = 001;

DELETE kcal
FROM Exercise
WHERE exercise_name = 'push ups';

DELETE time_length
FROM Exercise
WHERE exercise_name = 'squat';

DELETE time_length, kcal, repeats
FROM Exercise
WHERE complex_name = 'morning fresh';



