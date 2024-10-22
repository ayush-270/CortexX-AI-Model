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


query = "UPDATE web_command SET name='facebook' WHERE path ='https://www.facebook.com/'"
cursor.execute(query)


conn.commit()

# app_name = query.strip()

# if app_name != "":
#     try :
#         cursor.execute(
#         "SELECT path FROM sys_command WHERE name IN (?)",(app_name,))
#         results = cursor.fetchall()

#         if len(results) != 0:
#             speak("Opening "+query)
#             os.startfile(results[0][0])

#         elif len(results) == 0:
#             cursor.execute("SELECT url FROM web_command WHERE name IN (?)",(app_name,))
#             results = cursor.fetchall()

#             if len(results) != 0:
#                 speak("Opening "+query)
#                 webbrowser.open(results[0][0])

#             else:
#                 speak("Opening "+query)
#                 try:
#                     os.system("start "+query)
#                 except:
#                     speak("not found")
#     except:
#         speak("Soemthing went wrong")

