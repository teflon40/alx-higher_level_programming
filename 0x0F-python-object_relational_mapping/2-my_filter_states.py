#!/usr/bin/python3
""" Mysqldb script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    h, p = "localhost", 3306,
    u, ps, db_name, search = argv[1], argv[2], argv[3], argv[4]

    with MySQLdb.connect(host=h, user=u, passwd=ps, db=db_name, port=p) as db:
        with db.cursor() as cursor_obj:
            query = """SELECT * FROM states
            WHERE BINARY name = '{}' ORDER BY id ASC""".format(search)
            cursor_obj.execute(query)
            fetched_state = cursor_obj.fetchall()
            for state in fetched_state:
                print(state)
