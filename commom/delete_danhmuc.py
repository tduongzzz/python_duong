from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def delete_danhmuc(id_danhmuc):
    connection = None
    cursor = None
    try:
        connection = connect_mysql()
        if connection is None:
            print("⚠️ Không thể kết nối MySQL. Dừng thao tác xóa.")
            return

        cursor = connection.cursor()
        sql = "DELETE FROM danhmuc WHERE id = %s"
        cursor.execute(sql, (id_danhmuc,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Đã xóa danh mục có ID: {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID: {id_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
