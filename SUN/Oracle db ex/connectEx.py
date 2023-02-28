import cx_Oracle
from oracledb import DatabaseError


##create a connection
try:

    con = cx_Oracle.connect('advjavabatch/admin@LAPTOP-2U9U6NF8:1521/xe')
    print(con.version);

    # Now execute the sqlquery
    cursor = con.cursor()

    cursor.execute("create table t1(t1name varchar2(20),t1age varchar2(20))");

except cx_Oracle.DatabaseError as e:
    print("There is Problem with Oracle",e);

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

