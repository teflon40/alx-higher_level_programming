#!/usr/bin/python3
""" Msqldb script that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    host, port = "localhost", 3306
    user_name, password, db_name = argv[1], argv[2], argv[3]

    with MySQLdb.connect(host, user_name, password, db_name, port) as db:
        with db.cursor() as cur:
            cur.execute("SELECT * FROM states ORDER BY states.id ASC")
            table_rows = cur.fetchall()
            for state in table_rows:
                print(state)
