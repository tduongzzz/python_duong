import mysql.connector

def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # <-- Điền mật khẩu MySQL của bạn (nếu có)
            database="qlthuocankhang"
        )
        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection
    except mysql.connector.Error as e:
        print(f"❌ Lỗi kết nối MySQL: {e}")
        return None
