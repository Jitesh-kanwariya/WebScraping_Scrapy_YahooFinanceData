import sqlite3

con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()

# cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")

con.commit()


