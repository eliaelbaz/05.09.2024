import sqlite3

# Connect to the correct database file
conn = sqlite3.connect('identifier.sqlite')  # Make sure this matches your database file name
cursor = conn.cursor()

# Check if the table song_details exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

# Update Netta Barzilai's song length for 2018 from 175 to 180 seconds
cursor.execute('''
    UPDATE song_details
    SET song_length_seconds = 180
    WHERE year = 2018 AND song_length_seconds = 175;
''')

# Commit the changes to the database
conn.commit()

print("Updated Netta Barzilai's song length for 2018 from 175 to 180 seconds.")

# Closing the connection
conn.close()
