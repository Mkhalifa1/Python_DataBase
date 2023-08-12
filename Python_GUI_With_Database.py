import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.title("Student Registration")

conn = sqlite3.connect('student_data.db')

def create_table():
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS students (
                name TEXT,
                national_number TEXT PRIMARY KEY,
                address TEXT,
                age INTEGER,
                course TEXT,
                phone TEXT,
                email TEXT
            )
        ''')

create_table()

def save_data():
    name = entry_name.get()
    national_number = entry_national_number.get()
    address = entry_address.get()
    age = entry_age.get()
    course = entry_course.get()
    phone = entry_phone.get()
    email = entry_email.get()

    with conn:
        conn.execute('''
            INSERT INTO students (name, national_number, address, age, course, phone, email)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, national_number, address, age, course, phone, email))

    print("Data saved successfully.")

    entry_name.delete(0, tk.END)
    entry_national_number.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def open_edit_window():
    edit_window = tk.Toplevel(root)
    
    edit_window.title("Edit Data")
    
    label_edit_national_number = ttk.Label(edit_window, text="National Number:")
    entry_edit_national_number = ttk.Entry(edit_window)
    
    label_edit_field = ttk.Label(edit_window, text="Choose Field:")
    edit_field_combobox = ttk.Combobox(edit_window, values=["Name", "Address", "Age", "Course", "Phone", "Email"])
    
    label_edit_value = ttk.Label(edit_window, text="New Value:")
    entry_edit_value = ttk.Entry(edit_window)
    
    def apply_changes():
        national_number = entry_edit_national_number.get()
        field_to_edit = edit_field_combobox.get()
        new_value = entry_edit_value.get()

        with conn:
            cursor = conn.cursor()
            cursor.execute(f'UPDATE students SET {field_to_edit.lower()}=? WHERE national_number=?', (new_value, national_number))
            conn.commit()
            print("Data updated successfully.")
            
            #entry_edit_national_number.delete(0, tk.END)
            edit_field_combobox.delete(0, tk.END)
            entry_edit_value.delete(0, tk.END)
    
    apply_button = ttk.Button(edit_window, text="Apply Changes", command=apply_changes)
    
    label_edit_national_number.grid(row=0, column=0, padx=5, pady=5)
    entry_edit_national_number.grid(row=0, column=1, padx=5, pady=5)
    
    label_edit_field.grid(row=1, column=0, padx=5, pady=5)
    edit_field_combobox.grid(row=1, column=1, padx=5, pady=5)
    
    label_edit_value.grid(row=2, column=0, padx=5, pady=5)
    entry_edit_value.grid(row=2, column=1, padx=5, pady=5)
    
    apply_button.grid(row=3, columnspan=2, padx=5, pady=10)

def open_find_window():
    find_window = tk.Toplevel(root)
    find_window.title("Find Data")
    
    label_find_national_number = ttk.Label(find_window, text="National Number:")
    entry_find_national_number = ttk.Entry(find_window)
    
    def find_data():
        national_number = entry_find_national_number.get()

        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE national_number=?', (national_number,))
            data = cursor.fetchall()

            if data:
                result_text.config(state="normal")
                result_text.delete(1.0, tk.END)
                for record in data:
                    result_text.insert('1.0', f"Name: {record[0]}\n")
                    result_text.insert('2.0', f"National Number: {record[1]}\n")
                    result_text.insert('3.0', f"Address: {record[2]}\n")
                    result_text.insert(tk.END, f"Age: {record[3]}\n")
                    result_text.insert(tk.END, f"Course: {record[4]}\n")
                    result_text.insert(tk.END, f"Phone: {record[5]}\n")
                    result_text.insert(tk.END, f"Email: {record[6]}\n\n")
                result_text.config(state="disabled")
            else:
                result_text.config(state="normal")
                result_text.delete(1.0, tk.END)
                result_text.insert('1.0', "No data found for the given National Number.")
                result_text.config(state="disabled")
    
    find_button = ttk.Button(find_window, text="Find Data", command=find_data)
    
    result_text = tk.Text(find_window, width=50, height=10)
    result_text.config(state="disabled")
    
    label_find_national_number.grid(row=0, column=0, padx=5, pady=5)
    entry_find_national_number.grid(row=0, column=1, padx=5, pady=5)
    
    find_button.grid(row=1, columnspan=2, padx=5, pady=10)
    result_text.grid(row=2, columnspan=2, padx=5, pady=5)

label_name = ttk.Label(root, text="Name:")
entry_name = ttk.Entry(root)

label_national_number = ttk.Label(root, text="National Number:")
entry_national_number = ttk.Entry(root)

label_address = ttk.Label(root, text="Address:")
entry_address = ttk.Entry(root)

label_age = ttk.Label(root, text="Age:")
entry_age = ttk.Entry(root)

label_course = ttk.Label(root, text="Course:")
entry_course = ttk.Entry(root)

label_phone = ttk.Label(root, text="Phone:")
entry_phone = ttk.Entry(root)

label_email = ttk.Label(root, text="Email:")
entry_email = ttk.Entry(root)

save_button = ttk.Button(root, text="Save", command=save_data)


menu_bar = tk.Menu(root)
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Edit Data", command=open_edit_window)
edit_menu.add_command(label="Find Data", command=open_find_window)
menu_bar.add_cascade(label="Go To", menu=edit_menu)
root.config(menu=menu_bar)

label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_national_number.grid(row=1, column=0, padx=5, pady=5)
entry_national_number.grid(row=1, column=1, padx=5, pady=5)

label_address.grid(row=2, column=0, padx=5, pady=5)
entry_address.grid(row=2, column=1, padx=5, pady=5)

label_age.grid(row=3, column=0, padx=5, pady=5)
entry_age.grid(row=3, column=1, padx=5, pady=5)

label_course.grid(row=4, column=0, padx=5, pady=5)
entry_course.grid(row=4, column=1, padx=5, pady=5)

label_phone.grid(row=5, column=0, padx=5, pady=5)
entry_phone.grid(row=5, column=1, padx=5, pady=5)

label_email.grid(row=6, column=0, padx=5, pady=5)
entry_email.grid(row=6, column=1, padx=5, pady=5)

save_button.grid(row=7, columnspan=2, padx=5, pady=10)

root.mainloop()
conn.close()
