from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="attendance_db"
    )

# 🟢 Home route
@app.route('/')
def home():
    return "Attendance API Running 🚀"

# 🟢 Get all attendance
@app.route('/attendance')
def get_attendance():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM attendance")
    data = cursor.fetchall()
    
    return jsonify(data)

# 🟢 Analytics
@app.route('/analytics')
def analytics():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM attendance")
    data = cursor.fetchall()

    total = len(data)
    late = len([x for x in data if x['status'] == 'Late'])

    return jsonify({
        "total_records": total,
        "late_count": late
    })

# 🟢 NEW: Add attendance (POST API)
@app.route('/add', methods=['POST'])
def add_attendance():
    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO attendance (user_id, name, timestamp, status) VALUES (%s, %s, %s, %s)"
    values = (data['user_id'], data['name'], data['timestamp'], data['status'])

    cursor.execute(query, values)
    conn.commit()

    return {"message": "Data added successfully"}

# 🟢 Run server
if __name__ == '__main__':
    app.run(debug=True)