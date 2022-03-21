from flask import Flask, request, abort
import psycopg2
import json
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/getChat', methods=['GET'])
def get_chat():
    cur = con.cursor()
    cur.execute("SELECT name,message from chat")
    messages=cur.fetchall()
    return dict(messages)

@app.route('/sendMessage', methods=['POST'])
def send_message():
    a = len(request.args)
    if len(request.args) == 0:
        return "Запрос пустой"
    name1 = request.args.get("name")
    message1 = request.args.get("message")
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO CHAT (name,message) VALUES ('{name1}','{message1}')"
    )

    con.commit()
    return "Record inserted successfully"

if __name__ == '__main__':
    con = psycopg2.connect(
        database="HttpChat",
        user="postgres",
        password="root",
        host="127.0.0.1",
        port="5432"
    )
    # cur = con.cursor()
    # cur.execute('''CREATE TABLE CHAT
    #      (ID SERIAL,
    #      NAME TEXT NOT NULL,
    #      MESSAGE TEXT NOT NULL)''')
    #
    # print("Table created successfully")
    # con.commit()
    # con.close()

    print("Database opened successfully")
    app.run(debug=True)
