import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Business Simulation class: handles financial data and updates
class BusinessSimulation:
    def __init__(self):
        self.revenue = 50000  # Starting revenue
        self.expenses = 30000  # Starting expenses
        self.profit = self.revenue - self.expenses  # Initial profit
        self.loan = 10000  # Starting loan amount
        self.days_passed = 0  # Days tracker
        self.revenue_history = [self.revenue]
        self.expenses_history = [self.expenses]
        self.profit_history = [self.profit]
        self.loan_history = [self.loan]
        self.days_history = [self.days_passed]

    def update_data(self, revenue, expenses, loan):
        self.revenue = revenue
        self.expenses = expenses
        self.profit = self.revenue - self.expenses
        self.loan = loan
        self.days_passed += 1

        # Update the history
        self.revenue_history.append(self.revenue)
        self.expenses_history.append(self.expenses)
        self.profit_history.append(self.profit)
        self.loan_history.append(self.loan)
        self.days_history.append(self.days_passed)

# GUI class to create the application window and manage user input
class BusinessSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Business Simulation")
        self.root.geometry("800x600")

        # Initialize simulation object
        self.simulation = BusinessSimulation()

        # Create the user interface elements
        self.create_widgets()

    def create_widgets(self):
        # Company financial status label
        self.status_label = tk.Label(self.root, text="Company Financial Status", font=("Arial", 16))
        self.status_label.pack(pady=10)

        self.revenue_label = tk.Label(self.root, text=f"Revenue: ${self.simulation.revenue}")
        self.revenue_label.pack()

        self.expenses_label = tk.Label(self.root, text=f"Expenses: ${self.simulation.expenses}")
        self.expenses_label.pack()

        self.profit_label = tk.Label(self.root, text=f"Profit: ${self.simulation.profit}")
        self.profit_label.pack()

        self.loan_label = tk.Label(self.root, text=f"Loan: ${self.simulation.loan}")
        self.loan_label.pack()

        # Entry fields to input revenue, expenses, and loan
        self.revenue_entry = tk.Entry(self.root)
        self.revenue_entry.insert(0, str(self.simulation.revenue))
        self.revenue_entry.pack(pady=5)

        self.expenses_entry = tk.Entry(self.root)
        self.expenses_entry.insert(0, str(self.simulation.expenses))
        self.expenses_entry.pack(pady=5)

        self.loan_entry = tk.Entry(self.root)
        self.loan_entry.insert(0, str(self.simulation.loan))
        self.loan_entry.pack(pady=5)

        # Button to update the financial data
        self.update_button = tk.Button(self.root, text="Update Finances", command=self.update_finances)
        self.update_button.pack(pady=20)

        # Create a frame for the chart
        self.chart_frame = tk.Frame(self.root)
        self.chart_frame.pack()

        # Initial chart plot
        self.plot_chart()

    def update_finances(self):
        try:
            # Get user input and update the simulation data
            revenue = int(self.revenue_entry.get())
            expenses = int(self.expenses_entry.get())
            loan = int(self.loan_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")
            return

        # Update the simulation data
        self.simulation.update_data(revenue, expenses, loan)

        # Update the financial status display
        self.revenue_label.config(text=f"Revenue: ${self.simulation.revenue}")
        self.expenses_label.config(text=f"Expenses: ${self.simulation.expenses}")
        self.profit_label.config(text=f"Profit: ${self.simulation.profit}")
        self.loan_label.config(text=f"Loan: ${self.simulation.loan}")

        # Update the chart with new data
        self.plot_chart()

    def plot_chart(self):
        # Create the chart figure
        fig, ax = plt.subplots(figsize=(8, 6))

        # Plot different financial data on the chart
        ax.plot(self.simulation.days_history, self.simulation.revenue_history, label='Revenue', color='blue')
        ax.plot(self.simulation.days_history, self.simulation.expenses_history, label='Expenses', color='red')
        ax.plot(self.simulation.days_history, self.simulation.profit_history, label='Profit', color='green')
        ax.plot(self.simulation.days_history, self.simulation.loan_history, label='Loan', color='orange')

        ax.set_xlabel("Days")
        ax.set_ylabel("Amount ($)")
        ax.set_title("Company Financial Trends")

        # Add legend
        ax.legend()

        # Embed the chart in the Tkinter window
        for widget in self.chart_frame.winfo_children():
            widget.destroy()  # Clear old charts
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BusinessSimulationApp(root)
    root.mainloop()
