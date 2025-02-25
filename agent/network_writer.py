import requests
from iWriter import IWriter


class NetworkWriter(IWriter):
    def __init__(self):
        """אתחול המחלקה."""
        self.SERVER_URL = "http://127.0.0.1:5000"  # כתובת השרת שאליו נשלחים הנתונים

    def send_data(self, encrypted_words: str, machine_name: str):
        """
        שולח נתונים מוצפנים לשרת.

        Args:
            encrypted_words (list): רשימה של מילים מוצפנות לשליחה.
            machine_name (str): שם המכונה שממנה נשלחים הנתונים.
        """
        # בודק אם הנתונים חסרים
        if not encrypted_words or not machine_name:
            print("Error: Missing data to send.")  # מדפיס הודעת שגיאה אם חסרים נתונים
            return

        # יוצר את גוף הבקשה (payload) לשליחה לשרת
        payload = {
            "machine_name": machine_name,  # שם המכונה
            "encrypted_words": encrypted_words,  # המילים המוצפנות
        }

        try:
            # שולח את הנתונים לשרת באמצעות בקשת POST
            response = requests.post(f"{self.SERVER_URL}/api/send_data", json=payload)

            # בודק אם התשובה מהשרת היא 200 (הצלחה)
            if response.status_code == 200:
                print("Data successfully sent to the server.")  # מדפיס הודעת הצלחה
            else:
                # מדפיס הודעת שגיאה אם השרת החזיר קוד שגיאה
                print(f"Failed to send data. Server responded with: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            # מטפל בשגיאות רשת (למשל, חיבור לא זמין)
            print(f"Network error: {e}")