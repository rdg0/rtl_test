import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = 'rtl_1'
COLLECTION_NAME = 'collection_name'
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

GROUP_TYPES = {
    'hour': {'format': '%Y-%m-%dT%H', 'date': '$dt'},
    'day': {'format': '%Y-%m-%d', 'date': '$dt'},
    'month': {'format': '%Y-%m', 'date': '$dt'}
}
