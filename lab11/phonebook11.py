import psycopg2
import csv

conn=psycopg2.connect("dbname=postgres user=postgres password=Adg12332,")
cursor=conn.cursor()
 
def pattern(y):
    cursor.execute('SELECT * FROM phonebook')
    print('все совпадения')
    records=cursor.fetchall()
    for i in records:
        if i[0][:len(y)]==y:
            print(i)

def createUser(name,phone):
    query="""SELECT * FROM phonebook where name =%s"""
    cursor.execute(query,[name])
    records=cursor.fetchall()
    if len(records)!=0:
        updateData(name,phone)
    else:
        query="""INSERT INTO phonebook(name,phone) VALUES(%s,%s)"""
        cursor.execute(query,[name,phone])
        conn.commit()

def deleteDataByName(name):
    query="""DELETE FROM phonebook where name=%s"""
    cursor.execute(query,[name])
    conn.commit()

def getDataFromPhonebook(limit):
    query="""SELECT * FROM phonebook LIMIT %s"""
    cursor.execute(query,[limit])
    records=cursor.fetchall()
    print(records)

def updateData(name,phone):
    query="""UPDATE phonebook SET phone=%s WHERE name=%s"""
    cursor.execute(query,[phone,name])
    conn.commit()

def addCsvDataInDB(csvName):
    fail=[]
    with open(csvName+".csv") as file:
        reader=csv.reader(file,delimiter=' ')
       
        for i in reader:
            if i[1][:2]=="87":  
                query="""INSERT INTO phonebook(name,phone) VALUES(%s,%s)"""
                cursor.execute(query,[i[0],i[1]])
                conn.commit()
            else:fail.append(i)
    return fail
inp=int(input("введите что вы хотите сделать \n1 Изменить номер юзера \n2 показать юзеров \n3 вывести данные с csv и добавить их в базу\n4 удалить юзера по имени \n5 создать юзера\n"))
if inp==1:
    inp=input("Введите какой номер хотите поставить какому юзеру\n").split()
    updateData(inp[0],inp[1])
elif inp==2:
    inp=input("введите лимит юзера\n")
    getDataFromPhonebook(inp)
elif inp ==3:
    inp=input("введите имя csv файла\n")
    print("neveriy dannyi")
    print(addCsvDataInDB(inp))
elif inp ==4 :
    inp =input("ВВЕДИТЕ ИМЯ ЮЗЕРА КОТОРЫЙ ХОТИТЕ УДАЛИТЬ\n")
    deleteDataByName(inp)
elif inp==5 :
    inp=input("Введите имя и номер одной строкой\n").split()
    createUser(inp[0],inp[1])
elif inp==6:
    print('введите начало шаблона имени')
    y=input()
    pattern(y)

