from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster()
session = cluster.connect('katya')
# Inserts
##user
start = session.execute("select * from User")

query = SimpleStatement("INSERT INTO User (user_id, user_name, age, weight, activity) VALUES (001, 'Sunny', 19, 69, 10)", consistency_level=ConsistencyLevel.LOCAL_ONE)
session.execute(query)
query = SimpleStatement("INSERT INTO User (	user_id, user_name, age, weight, activity) VALUES (	002, 'Bunny', 21, 100, 4)", consistency_level=ConsistencyLevel.LOCAL_ONE)
session.execute(query)
query = SimpleStatement("INSERT INTO User (	user_id, user_name, age, weight, activity) VALUES (	003, 'Garry', 25, 88, 3)", consistency_level=ConsistencyLevel.LOCAL_ONE)
session.execute(query)

result = session.execute("select * from User")
print('user table')
print(start.current_rows , result.current_rows)

## messanger
start = session.execute("select * from messanger")

session.execute("INSERT INTO Messanger (user_id, messanger_name, address) VALUES (	001, 'gmail', 'SunnySuper@gmail.com')")
session.execute("INSERT INTO Messanger (user_id, messanger_name, address) VALUES (	002, 'telegram', '@Bunnyboy')")
session.execute("INSERT INTO Messanger (user_id, messanger_name, address) VALUES (	003, 'ukr.net', '@GarryPotter@ukr.net')")

result = session.execute("select * from Messanger")
print('Messanger table')
print(start.current_rows , result.current_rows)

## Complex
start = session.execute("select * from Complex")

session.execute("INSERT INTO Complex (user_id, day, complex_name, time_start, type) VALUES (001, 20, 'morning fresh', {hours: 8, minutes: 30, second: 0}, 'fulfilled')")
session.execute("INSERT INTO Complex (user_id, day, complex_name, time_start, type) VALUES (002, 20, 'litl free', {hours: 10, minutes: 15, second: 0}, 'unfulfilled')")
session.execute("INSERT INTO Complex (user_id, day, complex_name, time_start, type) VALUES (003, 20, 'big hard', {hours: 15, minutes: 55, second: 0}, 'awaiting')")

result = session.execute("select * from Complex")
print('Complex table')
print(start.current_rows , result.current_rows)

## Exercise
start = session.execute("select * from Exercise")

session.execute("INSERT INTO Exercise(complex_name, exercise_name, time_length, kcal, repeats) VALUES ('big hard', 'squat', {hours: 0, minutes: 0, second: 10}, 4, 100)")
session.execute("INSERT INTO Exercise(complex_name, exercise_name, time_length, kcal, repeats) VALUES ('big hard', 'push ups', {hours: 0, minutes: 0, second: 15}, 6, 100)")
session.execute("INSERT INTO Exercise(complex_name, exercise_name, time_length, kcal, repeats) VALUES ('morning fresh', 'squat', {hours: 0, minutes: 0, second: 10}, 4, 1)")

result = session.execute("select * from Exercise")
print('Exercise table')
print(start.current_rows , result.current_rows)

# Updates
## user

session.execute("UPDATE User  SET weight = 68 WHERE user_id = 001")
session.execute("UPDATE User  SET activity = 12 WHERE user_id = 002")
session.execute("UPDATE User  SET age = 20 WHERE user_id = 003")

result = session.execute("select * from User")
print('user after update')
print(result.current_rows)

## Messanger

session.execute("UPDATE Messanger SET address = 'new form address' WHERE user_id = 001 and messanger_name = 'ukr.net'")
session.execute("UPDATE Messanger SET address = 'new form address' WHERE user_id = 002 and messanger_name = 'ukr.net'")
session.execute("UPDATE Messanger SET address = 'old ' WHERE user_id = 003 and messanger_name = 'ukr.net'")

result = session.execute("select * from Messanger")
print('messanger after update')
print(result.current_rows)

## complex

session.execute("UPDATE Complex SET complex_name = 'old boy ' WHERE user_id = 001 and day = 20")
session.execute("UPDATE Complex SET time_start = {hours: 16, minutes: 55, second: 0} WHERE user_id = 002 and day = 20")
session.execute("UPDATE Complex SET type = 'unfulfilled' WHERE user_id = 003 and day = 20")

result = session.execute("select * from Complex")
print('complex after update')
print(result.current_rows)

## Exercise

session.execute("UPDATE Exercise SET time_length = {hours: 0, minutes: 0, second: 20} WHERE complex_name = 'old boy'  and exercise_name = 'squat'")
session.execute("UPDATE Exercise SET repeats = 40 WHERE complex_name = 'old boy' ")
session.execute("UPDATE Exercise SET kcal = 25 WHERE complex_name = 'morning fresh'  and exercise_name = 'push ups'")

result = session.execute("select * from Exercise")
print('exercise after update')
print(result.current_rows)

# Finale selectos

res = session.execute("SELECT complex_name, time_start FROM Complex WHERE User_id = 001 AND day = 2 ALLOW FILTERING")
print(res.current_rows)

res = session.execute("SELECT age, weight, activity FROM User WHERE user_id = 001")
print(res.current_rows)

res = session.execute("SELECT type FROM Complex WHERE day = 20 ALLOW FILTERING")
print(res.current_rows)

res = session.execute("SELECT exercise_name, repeats FROM Exercise WHERE complex_name = 'sit-down'")
print(res.current_rows)

# Deletes

session.execute("DELETE user_name, age, weight, activity FROM User WHERE user_id = 001")
session.execute("DELETE age, activity FROM User WHERE user_id = 003")
session.execute("DELETE age, weight, activity FROM User WHERE user_id = 002")
session.execute("DELETE address FROM Messanger WHERE user_id = 001 and messanger_name = 'ukr.net'")
session.execute("DELETE address FROM Messanger WHERE user_id = 002 and messanger_name = 'telegram'")
session.execute("DELETE address FROM Messanger WHERE user_id = 003 and messanger_name = 'telegram' ")
session.execute("DELETE complex_name, time_start, type FROM Complex WHERE user_id = 003 and day = 20")
session.execute("DELETE complex_name FROM Complex WHERE day = 20 and user_id = 002")
session.execute("DELETE type FROM Complex WHERE user_id = 001 and day = 21")
session.execute("DELETE kcal FROM Exercise WHERE exercise_name = 'push ups' and complex_name = 'squat'")
session.execute("DELETE time_length FROM Exercise WHERE exercise_name = 'squat' and complex_name = 'midl'")
session.execute("DELETE time_length, kcal, repeats FROM Exercise WHERE complex_name = 'morning fresh' and exercise_name = 'sleep'")