from flask import Flask, render_template, request, g
import pickle
import numpy as np
import sqlite3
import requests
import os
import pandas as pd

app = Flask(__name__)

def download_combined_cosine_sim_matrix(url, local_file_path):
    if not os.path.exists(local_file_path):
        print("Downloading combined similarity matrix please wait...")
        response = requests.get(url)

        with open(local_file_path, 'wb') as file:
            file.write(response.content)
    
    with open(local_file_path, 'rb') as file:
        combined_cosine_sim_matrix = pickle.load(file)
    
    return combined_cosine_sim_matrix

combined_cosine_sim_matrix_url = 'https://combinedcosinesimbucket.s3.ap-south-1.amazonaws.com/combined_cosine_sim_matrix.pkl'
local_combined_cosine_sim_path = 'combined_cosine_sim_matrix.pkl'

combined_cosine_sim_matrix = download_combined_cosine_sim_matrix(combined_cosine_sim_matrix_url, local_combined_cosine_sim_path)

table = pickle.load(open('./pickle_files/table.pkl', 'rb'))
booksdb = pickle.load(open('./pickle_files/booksdb.pkl', 'rb'))

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

titles = get_book_titles()

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
    user_input = request.form.get('user_input')
    try:
        book_index = np.where(table.index == user_input)[0][0]
        book_similarities = combined_cosine_sim_matrix[book_index]
        sorted_indices = np.argsort(book_similarities)[::-1]
        top_recommendations = [i for i in sorted_indices[:7] if i != book_index]
        rc = []
        for i in range(1, len(top_recommendations)):
            item = []
            b = table.iloc[top_recommendations[i]].name
            temp_df = booksdb[booksdb['title'] == b]
            item.extend(list(temp_df.drop_duplicates('title')['title'].values))
            item.extend(list(temp_df.drop_duplicates('title')['author'].values))
            item.extend(list(temp_df.drop_duplicates('title')['img'].values))
            rc.append(item)
        return render_template('recommend.html', data=rc)
    except:
        return "not found"

if __name__ == '__main__':
    app.run(debug=True)
