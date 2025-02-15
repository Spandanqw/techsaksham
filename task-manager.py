import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from datetime import datetime

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        due_date = askstring("Due Date", "Enter due date (YYYY-MM-DD) or leave blank:")
        priority = askstring("Priority", "Enter priority (High/Medium/Low) or leave blank:")
        category = askstring("Category", "Enter category or leave blank:")
        task_details = {
            "task": task,
            "completed": False,
            "due_date": due_date if due_date else "No due date",
            "priority": priority if priority else "No priority",
            "category": category if category else "No category"
        }
        tasks.append(task_details)
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def search_tasks():
    keyword = search_entry.get()
    if keyword:
        search_results = [task for task in tasks if keyword.lower() in task["task"].lower()]
        task_listbox.delete(0, tk.END)
        for task in search_results:
            status = "Completed" if task["completed"] else "Pending"
            task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')
    else:
        messagebox.showwarning("Warning", "Search keyword cannot be empty!")

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')

def clear_all_tasks():
    tasks.clear()
    update_tasks()

# Create the main window
root = tk.Tk()
root.title("Task Manager")

# Create and place the widgets
task_label = tk.Label(root, text="Enter a task:" , font=("ariel",18))
task_label.pack()

task_entry = tk.Entry(root, width=50 , font=("ariel",18))
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task , font=("ariel",18))
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task , font=("ariel",18))
delete_button.pack()

complete_button = tk.Button(root, text="Complete Task", command=complete_task , font=("ariel",18))
complete_button.pack()

search_label = tk.Label(root, text="Search tasks:" , font=("ariel",18))
search_label.pack()

search_entry = tk.Entry(root, width=50 , font=("ariel",18))
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_tasks , font=("ariel",18))
search_button.pack()

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks , font=("ariel",18))
clear_button.pack()

task_listbox = tk.Listbox(root, width=50, height=10 , font=("ariel",18))
task_listbox.pack()

# Start the main loop
root.mainloop()
