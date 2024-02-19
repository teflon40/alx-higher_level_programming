#!/usr/bin/python3
""" connect and executes an SQL query to retrieve city names from the
'cities' table for a specified state, ordered by 'cities.id'
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    h, p = "localhost", 3306,
    u, psw, db_name, name_arg = argv[1], argv[2], argv[3], argv[4]

    with MySQLdb.connect(host=h, user=u, passwd=psw, db=db_name, port=p) as db:
        with db.cursor() as cursor_obj:
            sql = """SELECT cities.name from cities, states WHERE state_id IN
            (SELECT states.id WHERE states.name = %s ORDER BY cities.id ASC)"""
            cursor_obj.execute(sql, (name_arg,))
            city_names = cursor_obj.fetchall()
            print(', '.join([name[0] for name in city_names]))

    """ NB:
    fetchall() method fetches all the rows of the result set as a list of tuples.
    In this script, the data at index 0 of each tuple (city names) is what i extracted and printed.
    """
