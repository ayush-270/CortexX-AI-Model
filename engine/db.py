import csv
import sqlite3

conn = sqlite3.connect("cortex.db")

cursor = conn.cursor()

# Creating a table Sys_command

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
# cursor.execute(query)

# Creating a table web_command

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (NULL, 'notepad', 'C:\\Windows\\system32\\notepad.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (NULL, 'spotify', 'C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (NULL, 'vs code', 'C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (NULL, 'excel', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\XLICONS.exe')"
# cursor.execute(query)


# query = "INSERT INTO web_command VALUES (NULL, 'github', 'https://github.com/')"
# cursor.execute(query)


# query = "UPDATE web_command SET name='facebook' WHERE path ='https://www.facebook.com/'"
# cursor.execute(query)


# conn.commit()

# Create a table with the desired columns
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), 
#     mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
desired_columns_indices = [0, 18]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
# conn.commit()
# conn.close()

# query = 'papa'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])
