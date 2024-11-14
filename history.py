import os
class HistoryManager:
    def save_to_history(self, operation):
        file_name = "history.txt"
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                file.write("История операций:\n")
        with open(file_name, 'a') as file:
            file.write(operation + "\n")