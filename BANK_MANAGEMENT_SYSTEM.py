import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Example',database='BANK_MANAGEMENT')


def OpenAcc():
    n=input("Enter The Name: ")
    ac=input("Enter the Account No: ")
    db=input("Enter the Date Of Birth: ")
    add=input("Enter The Address: ")
    cn=input("Enter the Contact Number: ")
    ob=int(input("Enter The Opening Balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=(' insert into account values(%s,%s,%s,%s,%s,%s)')
    sql2=('insert into ammount values()%s,%s,%s')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Successfully")
    main()

def DepoAmo():
    amount=input("Enter the amount you want to deposit: ")
    ac=input("Enter the AccountNo: ")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0] + amount
    sql=('update amount set balance where AccNo%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def WithdrawAmount():
    amount=input("Enter the amount you want to withdraw: ")
    ac=input("Enter the AccountNo: ")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0] - amount
    sql=('update amount set balance where AccNo%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def BalEnq():
    ac=input("Enter the AccountNo: ")
    a='select * from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance For Account: ",ac," is ",result[-1] )
    main()
def DisDetails():
    ac=input("Enter the AccountNo: ")
    a='select * from account where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i)
    main()
def CloseAcc():
    ac=input("Enter the AccountNo: ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    print("Data Entered Successfully")
    main()
