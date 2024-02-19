![orm](https://github.com/El-gibbor/alx-higher_level_programming/assets/107848793/597719af-74fd-4022-91d1-2768c646c478)
# Python Object Relational Mapping 💫
In this project, we seamlessly bridge two dynamic realms: Databases and Python!  
In the initial phase, the `MySQLdb` module takes center stage, empowering us to establish a connection with a `MySQL` database and effortlessly execute `SQL` queries.  
Transitioning to the second part, SQLAlchemy – the Object Relational Mapper (ORM). This is a game-changer because it eliminates the need for traditional `SQL` queries. The essence of an ORM lies in abstracting storage complexities, allowing us to focus on the potential of our objects rather than delving into the intricacies of storage logistics. The primary concern becomes _"What can I achieve with my objects?"_  
#### Without ORM ⤵️  
```mysql
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
#### With an ORM ⤵️  
```mysql
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
## Learning Objectives 
Be able to profieciently do the following at the end of this project:
- Connect to a `MySQL` database from a Python script  
- SELECT rows in a `MySQL` table from a Python script
- INSERT rows in a `MySQL` table from a Python script
- Know what ORM means  
- Map a Python Class to a MySQL table  
- Create a Python Virtual Environment
## General Requirements
- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)  
- Files are executed with MySQLdb version 2.0.x    
- Files are executed with SQLAlchemy version 1.4.x  
- All code confrom with pycodestyle (version 2.8.*)  
- All files are executable  
- The length of your files will be tested using wc  
