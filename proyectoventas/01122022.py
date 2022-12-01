import cx_Oracle
import os

os.environ['TNS_ADMIN'] = 'Z:/Wallet_DB20220530152721'
conn = cx_Oracle.connect('admin', '.Inacap2022.', 'db20220530152721_high')
c = conn.cursor()
c.execute('select * from usuarios')
for row in c:
    print(row)
