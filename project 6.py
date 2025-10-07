from datetime import datetime

print("Welcome to Personal Journal Manager!")

class JournalManager:
    def __init__(self, filename='text1.txt'):
        self.filename = filename

    def add(self):
        data = input("Write your journal entry: ")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"{time} - {data}\n")
            print("Entry added successfully.")

    def show(self):
        print("Your Journal Entries:")
        with open(self.filename, "r") as f:
            entries = f.readlines()
            if entries:
                for line in entries:
                    print(line.strip())
            else:
                print("Journal is empty.")

    def search(self):
        keyword = input("Enter a keyword or date to search: ")
        with open(self.filename, "r") as f:
            entries = f.readlines()
            found = [e for e in entries if keyword.lower() in e.strip().lower()]
            if found:
                print("Matching Entries:")
                for entry in found:
                    print(entry.strip())
            else:
                print("No matching entry found.")

    def delete(self):
        choice = input("Are you sure you want to delete all entries? (yes/no): ")
        if choice.lower() == "yes":
            with open(self.filename, "w") as f:
                pass
            print("Entries deleted successfully.")
        else:
            print("Deletion is cancelled.")

obj = JournalManager()
while True:
    print("\nPlease select an option:")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search for an entry")
    print("4. Delete all entries")
    print("5. Exit")

    option = int(input("User input: ")) 

    match option:
        case 1:
            obj.add()
        case 2:
            obj.show()
        case 3:
            obj.search()
        case 4:
            obj.delete()
        case 5:
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        case _:
            print("Please enter a valid choice .")
