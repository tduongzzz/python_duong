import tkinter as tk
from tkinter import ttk, messagebox
from commom.insert_danhmuc import insert_danhmuc
from commom.delete_danhmuc import delete_danhmuc
from commom.update_danhmuc import update_danhmuc


# === Giao diện chính ===
root = tk.Tk()
root.title("Quản lý Danh mục Thuốc")
root.geometry("750x500")
root.resizable(False, False)

# === Khung nhập liệu ===
frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.pack(fill="x")

tk.Label(frame_input, text="ID:").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame_input, width=10)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=2, padx=5, pady=5)
entry_ten = tk.Entry(frame_input, width=25)
entry_ten.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=0, column=4, padx=5, pady=5)
entry_mota = tk.Entry(frame_input, width=25)
entry_mota.grid(row=0, column=5, padx=5, pady=5)

# === Bảng hiển thị ===
columns = ("id", "ten_danhmuc", "mota")
tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
tree.pack(fill="both", padx=10, pady=10, expand=True)

tree.heading("id", text="ID")
tree.heading("ten_danhmuc", text="Tên danh mục")
tree.heading("mota", text="Mô tả")

tree.column("id", width=50, anchor="center")
tree.column("ten_danhmuc", width=250)
tree.column("mota", width=350)

# === Các hàm xử lý ===
def load_data():
    for item in tree.get_children():
        tree.delete(item)
    try:
        from ketnoidb.ketnoi_mysql import connect_mysql
        conn = connect_mysql()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT id, ten_danhmuc, mota FROM danhmuc")
            for row in cur.fetchall():
                tree.insert("", "end", values=row)
            conn.close()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi tải dữ liệu: {e}")

def add_danhmuc():
    ten = entry_ten.get().strip()
    mota = entry_mota.get().strip()
    if not ten:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục!")
        return
    insert_danhmuc(ten, mota)
    load_data()

def update_selected():
    id_val = entry_id.get().strip()
    ten = entry_ten.get().strip()
    mota = entry_mota.get().strip()
    if not id_val or not ten:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập ID và tên danh mục!")
        return
    update_danhmuc(int(id_val), ten, mota)
    load_data()

def delete_selected():
    id_val = entry_id.get().strip()
    if not id_val:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập ID cần xóa!")
        return
    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa ID {id_val}?")
    if confirm:
        delete_danhmuc(int(id_val))
        load_data()

def on_row_select(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        entry_id.delete(0, tk.END)
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        entry_id.insert(0, values[0])
        entry_ten.insert(0, values[1])
        entry_mota.insert(0, values[2])

tree.bind("<<TreeviewSelect>>", on_row_select)

# === Các nút thao tác ===
frame_buttons = tk.Frame(root, pady=5)
frame_buttons.pack()

btn_add = tk.Button(frame_buttons, text="➕ Thêm", width=10, command=add_danhmuc, bg="#4CAF50", fg="white")
btn_add.grid(row=0, column=0, padx=10)

btn_update = tk.Button(frame_buttons, text="✏️ Sửa", width=10, command=update_selected, bg="#2196F3", fg="white")
btn_update.grid(row=0, column=1, padx=10)

btn_delete = tk.Button(frame_buttons, text="🗑️ Xóa", width=10, command=delete_selected, bg="#f44336", fg="white")
btn_delete.grid(row=0, column=2, padx=10)

btn_load = tk.Button(frame_buttons, text="🔄 Hiển thị", width=10, command=load_data)
btn_load.grid(row=0, column=3, padx=10)

# === Chạy khởi động ===
load_data()
root.mainloop()
