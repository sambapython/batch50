import sqlite3
import json
import psycopg2

def get_con():
	con = selite3.connect("batch50_bkp.sqlite3")
	cur=con.cursor()
	return con, cur
def get_postgres_con():
	f=open("config.json")
	data = json.load(f)
	db_data = data.get("dbdetails")
	dbname=  db_data.get("dbname")
	user= db_data.get("username")
	pwd= db_data.get("password")
	port=db_data.get("port")
	con = psycopg2.connect(database=dbname, user=user, password=pwd, port=port)
	cur = con.cursor()
	return con,cur

def create_table_customer():
	con,cur = get_postgres_con()
	cur.execute("create table customer(id int, name varchar(250))")
	con.commit()
	con.close()
def insert_customer():
	cust_id=raw_input("enter customer id:")
	cust_name=raw_input("enter customer name:")
	q="insert into customer values(%s,'%s')"%(cust_id, cust_name)
	con,cur=get_postgres_con()
	cur.execute(q)
	con.commit()
	con.close()
def update_customer():
	pass

if __name__ == "__main__":
	create_table_customer()