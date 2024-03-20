import pymssql
import pyodbc


def conn():

    connect = pyodbc.connect(
                'DRIVER={{ODBC Driver 18 for SQL Server}};'
                'SERVER=P1A-11127-0\SQLEXPRESS;'
                'USERNAME=sa;'
                'PASSWORD=12345;'
                'DATABASE="TncDig";'
                'Trusted_Connection=yes;'
    )
    if connect:

        print("連線成功")

    else:

        print("連線失敗")

    return connect

