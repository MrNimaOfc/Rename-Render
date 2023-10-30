# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "10709915")

API_HASH = os.environ.get("API_HASH", "3251cd5818e8b2f1c3585b3429c8f705")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6850826949:AAGSg90nEKUf2tZ9I2J5pP4u2KZFhywZX8w") 

FORCE_SUB = os.environ.get("FORCE_SUB", "MrNima_Ofc") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "kingsaviyaofc13")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://kingsaviyaofc13:mBUNszZ99vqC1TkX@cluster0.ba6d4vu.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/File-Editor-10-30")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2033058463').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
