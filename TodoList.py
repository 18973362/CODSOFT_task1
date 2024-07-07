import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("ToDo List")

        self.task_list = []

        # Frame for new task entry and add button
        self.entry_frame = tk.Frame(master)
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=45)
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10))

        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Listbox to display tasks with a Scrollbar
        self.list_frame = tk.Frame(master)
        self.list_frame.pack()

        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL)
        self.tasks_listbox = tk.Listbox(self.list_frame, width=50, height=15, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tasks_listbox.yview)

        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Delete button to remove selected task
        self.delete_button = tk.Button(master, text="Delete Selected Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Button to clear all tasks
        self.clear_button = tk.Button(master, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "The task cannot be empty.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_tasks(self):
        self.tasks_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    todo_list_app = ToDoList(root)
    root.mainloop()