import cx_Oracle;

#create connection
conn = cx_Oracle.connect('HR/HR@localhost');
print(conn.version())