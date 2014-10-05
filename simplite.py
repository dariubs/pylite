import sqlite3

#Intract with sqlite3 in python as simple as it can be.
class Simplite:

	def __init__(self,db_name):
		
		self.db_name = db_name
		self.db = sqlite3.connect(db_name)


	#Add table
	def add_table(self,table_name,columns):

		self.cols = columns

		# for col_name,col_type in columns.values():
		# 	self.cols += col_name+" "+col_type+","
		# self.cols = self.cols[0:len(self.cols)-1]

		self.db.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table_name,self.cols))


	#insert data
	def insert(self,table_name,data):
		self.data = data
		self.db.execute("INSERT INTO {} values({})".format(table_name,self.data))

	#remove items
	def remove(self,table_name,where="1"):
		self.where = where
		self.db.execute("DELETE FROM {} WHERE {}".format(table_name,self.where))

	#get items from db
	def get_items(self,table_name,where):
		self.where = where
		return self.db.execute("SELECT * FROM {} WHERE {}".format(table_name,self.where))


