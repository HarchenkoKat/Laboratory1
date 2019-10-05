from datetime import datetime
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement

cluster = Cluster()
session = cluster.connect('katya')

insert_user = session.prepare(
    "INSERT INTO User ( user_id, user_name, age, weight, activity ) VALUES (user_id, user_name, age, weight, activity)")
insert_messanger = session.prepare(
    "INSERT INTO user_event ( user_id, messanger_name, addres) VALUES (user_id, messanger_name, addres)")
insert_user_batch = BatchStatement()
user_id = {4}
user_name = {'Penny'}
age = {21}
weight = {88}
activity = {13}
messanger_name = {'telegrame'}
addres = {'@PEnnymay'}

insert_user_batch .add(insert_user,(user_id, user_name, age, weight, activity)))
insert_user_batch .add(insert_messanger,(user_id, messanger_name, addres))

session.execute(insert_user_batch)