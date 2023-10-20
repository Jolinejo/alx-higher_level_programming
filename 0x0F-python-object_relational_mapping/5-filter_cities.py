#!/usr/bin/python3
"""
module for printing states
"""


def main():
    """
    main states func
    """
    import MySQLdb
    import sys
    name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    tgt = sys.argv[4]
    host = "localhost"
    port = 3306
    db_connection = MySQLdb.connect(host=host, user=name, port=port,
                                    password=pwd, database=db)
    cursor = db_connection.cursor()
    query = "SELECT cities.name \
            FROM cities LEFT JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id"
    cursor.execute(query, (tgt,))
    rows = cursor.fetchall()
    flag = False
    for row in rows:
        if flag:
            print(", ", end='')
        flag = True
        print(row[0], end='')
    print()

if __name__ == "__main__":
    main()
