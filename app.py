from flask import Flask,render_template,request,g
import pickle
import numpy as np
import sqlite3
import pandas as pd
app = Flask(__name__)

table=pickle.load(open('table.pkl','rb'))
indices=pickle.load(open('indices.pkl','rb'))

booksdb=pickle.load(open('booksdb.pkl','rb'))

def get_db_connection():
    conn = sqlite3.connect('my_database.db')
    return conn

def get_book_titles():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT title FROM titles')
    titles = [row[0] for row in cursor.fetchall()]
    conn.close()
    return titles


titles= get_book_titles()


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/get_suggestions')
def get_suggestions():
    user_input = request.args.get('user_input', '')
    suggestions = [title for title in titles if user_input.lower() in title.lower()]
    max_suggestions = 5
    suggestions = suggestions[:max_suggestions]
    suggestions_html = '\n'.join([f"<div>{s}</div>" for s in suggestions])
    return suggestions_html



@app.route('/recommend', methods=['POST'])
def recommend():
    user_input=request.form.get('user_input')
    try:
        ind=np.where(table.index==user_input)[0][0]
        temp=indices[ind]
        rc=[]
        for i in range(1,len(temp)):
            item=[]
            b=table.iloc[temp[i]].name
            temp_df=booksdb[booksdb['title']==b]
            item.extend(list(temp_df.drop_duplicates('title')['title'].values))
            item.extend(list(temp_df.drop_duplicates('title')['author'].values))
            item.extend(list(temp_df.drop_duplicates('title')['img'].values))
            # s=closeness[ind][i]
            # t2=[b]
            rc.append(item)

        print(rc)
        return render_template('recommend.html',data=rc)
    except:
        return "not found"

if __name__=='__main__':
    app.run(debug=True)
