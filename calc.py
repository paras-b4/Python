#
# def add(a,b):
#     print("add",__name__)
#     print(a+b)
# def sub(a,b):
#     print("sub",__name__)
#     print(a-b)
#
# def mul(a,b):
#     print("mul",__name__)
#     print(a*b)
#
# def div(a,b):
#     print("div",__name__)
#     print(a/b)
#
# def main():
#     add(2,3)
#     sub(5,3)
#     mul(3,4)
#     div(5,5)
# if __name__ == "__main__" :
#     print("value",__name__)
#     main()
#

# def main():
#     print("hello")
#     print("welcome to the coding world")
# if __name__ == "__main__":
#     main()


import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="paras@yadav")
mycursor=mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
    print(i)