from flask import Flask,render_template,request,g
import pickle
import numpy as np
import sqlite3
import re
from pytrie import StringTrie

# table=pickle.load(open('table.pkl','rb'))
# indices=pickle.load(open('indices.pkl','rb'))

# booksdb=pickle.load(open('booksdb.pkl','rb'))


def get_db_connection():
    conn = sqlite3.connect('my_database.db')
    return conn

def get_book_titles():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT title FROM titles LIMIT 5')
    titles = [row[0] for row in cursor.fetchall()]
    conn.close()
    return titles

# Assuming you have already connected to the SQLite database and assigned the connection to 'conn'

def get_table():
    conn = sqlite3.connect('my_database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM t2 LIMIT 25')
    table = [row[0] for row in cursor.fetchall()]
    conn.close()
    return table


# titles2 = get_book_titles()
table=get_table()
print(table)
# print(titles2)