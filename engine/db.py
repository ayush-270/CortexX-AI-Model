import sqlite3

conn = sqlite3.connect("cortix.db")

cursor = conn.cursor()

# Creating a table Sys_command

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
#cursor.execute(query)

# Creating a table web_command

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
#cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (NULL, 'Spotify', 'C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (NULL, 'Facebook', 'https://www.facebook.com/')"
# cursor.execute(query)


conn.commit()