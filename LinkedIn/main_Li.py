import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Környezeti változók betöltése
load_dotenv()

class LinkedInCopilotGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LinkedIn Copilot Chat")
        self.setGeometry(100, 100, 800, 600)
        
        # API beállítások
        self.access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')
        self.api_base_url = "https://api.linkedin.com/v2"
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0'
        }
        
        # Központi widget létrehozása
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout beállítása
        layout = QVBoxLayout(central_widget)
        
        # Chat szövegdoboz létrehozása
        self.chat_text = QTextEdit()
        layout.addWidget(self.chat_text)
        
        # Küldés gomb létrehozása
        self.send_button = QPushButton("Küldés")
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

    def send_message(self):
        """Üzenet küldése a LinkedIn Copilotnak API-n keresztül"""
        try:
            message = self.chat_text.toPlainText()
            
            # Copilot API endpoint
            endpoint = f"{self.api_base_url}/copilot/messages"
            
            # Kérés adatainak összeállítása
            payload = {
                "message": message,
                "timestamp": datetime.now().isoformat(),
                "conversationId": "new"  # Új beszélgetés indítása
            }
            
            # API kérés küldése
            response = requests.post(
                endpoint,
                headers=self.headers,
                json=payload
            )
            
            if response.status_code == 200:
                copilot_response = response.json()
                # Válasz hozzáadása a chat szövegdobozhoz
                self.chat_text.append("\n\nCopilot válasza:\n" + copilot_response['message'])
            else:
                error_message = f"\n\nHiba történt: {response.status_code} - {response.text}"
                self.chat_text.append(error_message)
                
        except Exception as e:
            error_message = f"\n\nHiba történt az API hívásnál: {str(e)}"
            self.chat_text.append(error_message)
            print(error_message)

def main():
    app = QApplication(sys.argv)
    window = LinkedInCopilotGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
