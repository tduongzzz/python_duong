from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def get_all_danhmuc():
    connection = None
    cursor = None
    try:
        connection = connect_mysql()
        if connection is None:
            print("❌ Không thể kết nối đến cơ sở dữ liệu.")
            return

        cursor = connection.cursor()
        sql = "SELECT id, ten_danhmuc, mota FROM danhmuc"
        cursor.execute(sql)
        records = cursor.fetchall()

        if len(records) == 0:
            print("⚠️ Chưa có danh mục nào trong cơ sở dữ liệu.")
        else:
            print("\n📋 DANH SÁCH CÁC DANH MỤC:")
            print("-" * 60)
            print(f"{'ID':<5} {'Tên danh mục':<25} {'Mô tả':<30}")
            print("-" * 60)
            for row in records:
                print(f"{row[0]:<5} {row[1]:<25} {row[2]:<30}")
            print("-" * 60)

    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
