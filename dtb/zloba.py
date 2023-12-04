import mysql.connector
mydb = mysql.connector.connect(
	host = "dbs.spskladno.cz",
	user = "student22",
	passwd = "xxx",
	database = "vyuka22"
)

mycursor = mydb.cursor()
sql_select = "SELECT name FROM IT2020_Ucitel;"
mycursor.execute(sql_select)

while True:
	ziskano = mycursor.fetchone()
	if ziskano is None:
		break
	print("ucitel se jmenuje:", ziskano[0])



mycursor.close()
mydb.close()
