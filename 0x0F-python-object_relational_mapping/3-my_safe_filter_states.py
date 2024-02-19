#!/usr/bin/python3
""" same as the script in 2-my_filter_states, but now free from sql injections
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    h, p = "localhost", 3306,
    u, ps, db_name, search = argv[1], argv[2], argv[3], argv[4]

    with MySQLdb.connect(host=h, user=u, passwd=ps, db=db_name, port=p) as db:
        with db.cursor() as cursor_obj:
            query = """SELECT * FROM states
            WHERE name = %s ORDER BY id ASC"""
            cursor_obj.execute(query, (search,))
            fetched_state = cursor_obj.fetchall()
            for state in fetched_state:
                print(state)
