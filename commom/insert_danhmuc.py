from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(ten_danhmuc, mota):
    connection = None
    cursor = None
    try:
        connection = connect_mysql()
        if connection is None:
            print("⚠️ Không thể kết nối MySQL. Dừng thao tác thêm danh mục.")
            return

        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mota) VALUES (%s, %s)"
        data = (ten_danhmuc, mota)
        cursor.execute(sql, data)
        connection.commit()

        print(f"✅ Đã thêm danh mục: {ten_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
