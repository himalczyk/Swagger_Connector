# get env variables here and make a connection with anonymous data happen here
# call the object and methods here to run

from config import url, password, username
from connector import MakeConnection

token = MakeConnection(username, password, url)
print(MakeConnection.getToken(token))

