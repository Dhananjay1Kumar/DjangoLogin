import cx_Oracle
class NoSuchAccount(Exception):
    pass
con=None
try:
    con=cx_Oracle.connect('system','manager','localhost:1521/XE')
    cur=con.cursor()
    dacid=input('Enter  id of the account to be debited')
    wamt=input('Enter money to be transfer')
    cacid=input('Enter  id of the account to be credited')
    cur.execute('update account set cbal=cbal-'+wamt+'where id='+dacid)
    if cur.rowcount!=1:
        print("this account does naot exist")
        raise NoSuchAccount
    else:
        cur.execute('update account set cbal=cbal+'+wamt+'where id='+cacid)
        if cur.rowcount!=1:
            print("this account does not exists")
            raise NoSuchAccount
        else:
            con.commit()
            cur.close()
            print('Transaction success')
except(cx_Oracle.DatabaseError):
        con.rollback()
        print('Ooh!!! Transaction failed')
finally:
    if con!=None:
            con.close()
    print('connection is closed')
        

