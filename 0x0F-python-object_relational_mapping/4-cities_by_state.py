#!/usr/bin/python3
""" connects and executes an SQL query to retrieve data from the 'cities'
and 'states' tables, joining them on the 'state_id' and ordering by 'cities.id'.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    h, p = "localhost", 3306,
    u, psw, db_name = argv[1], argv[2], argv[3]

    with MySQLdb.connect(host=h, user=u, passwd=psw, db=db_name, port=p) as db:
        with db.cursor() as cursor_obj:
            query = """SELECT cities.id, cities.name, states.name FROM cities,
            states WHERE cities.state_id = states.id ORDER BY cities.id ASC"""
            cursor_obj.execute(query)
            data = cursor_obj.fetchall()
            for state in data:
                print(state)
