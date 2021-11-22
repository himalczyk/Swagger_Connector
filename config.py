from dotenv import load_dotenv
import os

#load env variables here

load_dotenv()
url = os.getenv('BASE_URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
dev_eu_url = os.getenv('DEV_EU_URL')