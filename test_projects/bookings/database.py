import sqlite3

connection = sqlite3.connect("data.db")

if __name__ == "__main__":
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE bookings (name text, minute integer, hour integer, day integer, month integer, year integer)"
    )


def get_bookings(month: int, year: int):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookings WHERE month=? AND year=?", (month, year))
    return cursor.fetchall()


def add_booking(name, minute, hour, day, month, year):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO bookings VALUES (?, ?, ?, ?, ?, ?)",
        (name, minute, hour, day, month, year),
    )
    connection.commit()


def remove_booking():
    pass


def modify_booking_date():
    pass


def close_database_connection():
    connection.close()
