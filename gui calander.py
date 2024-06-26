import tkinter as tk
import calendar

class CalendarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calendar")
        self.year = tk.StringVar()
        self.month = tk.StringVar()
        self.year.set(2024)
        self.month.set(1)
        
        self.year_label = tk.Label(root, text="Year:")
        self.year_label.pack()
        self.year_entry = tk.Entry(root, textvariable=self.year)
        self.year_entry.pack()
        
        self.month_label = tk.Label(root, text="Month:")
        self.month_label.pack()
        self.month_entry = tk.Entry(root, textvariable=self.month)
        self.month_entry.pack()
        
        self.show_button = tk.Button(root, text="Show Calendar", command=self.show_calendar)
        self.show_button.pack()
        
        self.calendar_output = tk.Text(root, height=10, width=25)
        self.calendar_output.pack()
    
    def show_calendar(self):
        year = int(self.year.get())
        month = int(self.month.get())
        cal = calendar.month(year, month)
        self.calendar_output.delete(1.0, tk.END)
        self.calendar_output.insert(tk.END, cal)

root = tk.Tk()
calendar_gui = CalendarGUI(root)
root.mainloop()

