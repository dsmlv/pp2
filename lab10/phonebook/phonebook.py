import psycopg2
import csv
conn=psycopg2.connect("dbname=postgres user=postgres password=Adg12332,")
cursor=conn.cursor()
 
def createUser(name,phone):
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
    with open(csvName+".csv") as file:
        reader=csv.reader(file,delimiter=' ')
        for i in reader:
            query="""INSERT INTO phonebook(name,phone) VALUES(%s,%s)"""
            cursor.execute(query,[i[0],i[1]])
            conn.commit()

inp=int(input("введите что вы хотите сделать \n1 Изменить номер юзера \n2 показать юзеров \n3 вывести данные с csv и добавить их в базу\n4 удалить юзера по имени \n5 создать юзера\n"))
if inp==1:
    inp=input("Введите какой номер хотите поставить какому юзеру\n").split()
    updateData(inp[0],inp[1])
elif inp==2:
    inp=input("введите лимит юзера\n")
    getDataFromPhonebook(inp)
elif inp ==3:
    inp=input("введите имя csv файла\n")
    addCsvDataInDB(inp)
elif inp ==4 :
    inp =input("ВВЕДИТЕ ИМЯ ЮЗЕРА КОТОРЫЙ ХОТИТЕ УДАЛИТЬ\n")
    deleteDataByName(inp)
else :
    inp=input("Введите имя и номер одной строкой\n").split()
    createUser(inp[0],inp[1])




