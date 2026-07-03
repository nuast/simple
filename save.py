FILE = "history.txt"

def save_input(value):
    with open(FILE, "a") as f:
        f.write(value + "\n")

def recent_input():
    with open(FILE) as f:
        return f.readlines()