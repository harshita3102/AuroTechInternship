import tkinter as tk
from tkinter import messagebox, simpledialog

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("Python ATM")
        self.root.geometry("400x300")
        self.balance = 1000  # Initial balance for demo
        self.transactions = []

        self.create_widgets()

    def create_widgets(self):
        self.label_balance = tk.Label(self.root, text=f"Balance: ${self.balance}", font=("Arial", 14))
        self.label_balance.pack(pady=10)

        self.button_history = tk.Button(self.root, text="Transactions History", command=self.display_transactions)
        self.button_history.pack(pady=10)

        self.button_withdraw = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.button_withdraw.pack(pady=10)

        self.button_deposit = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.button_deposit.pack(pady=10)

        self.button_transfer = tk.Button(self.root, text="Transfer", command=self.transfer)
        self.button_transfer.pack(pady=10)

        self.button_quit = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.button_quit.pack(pady=10)

    def display_transactions(self):
        if not self.transactions:
            messagebox.showinfo("Transaction History", "No transactions yet.")
        else:
            transactions_text = "\n".join(self.transactions)
            messagebox.showinfo("Transaction History", transactions_text)

    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amount is not None and amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}. Balance: ${self.balance}")
            self.label_balance.config(text=f"Balance: ${self.balance}")

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        if amount is not None and amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append(f"Withdrew ${amount}. Balance: ${self.balance}")
                self.label_balance.config(text=f"Balance: ${self.balance}")
            else:
                messagebox.showwarning("Withdraw", "Insufficient balance.")

    def transfer(self):
        amount = simpledialog.askfloat("Transfer", "Enter amount to transfer:")
        if amount is not None and amount > 0:
            if self.balance >= amount:
                recipient = simpledialog.askstring("Transfer", "Enter recipient's account number:")
                if recipient:
                    self.balance -= amount
                    self.transactions.append(f"Transferred ${amount} to account {recipient}. Balance: ${self.balance}")
                    self.label_balance.config(text=f"Balance: ${self.balance}")
                else:
                    messagebox.showwarning("Transfer", "Recipient's account number is required.")
            else:
                messagebox.showwarning("Transfer", "Insufficient balance.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATM(root)
    root.mainloop()
