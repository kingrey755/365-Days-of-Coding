todo = []
while True:
    print("List:", todo)
    action = input("Enter 'add <task>', 'remove <number>', or 'exit': ")
    if action == "exit": break
    todo.append(action[4:]) if action.startswith("add ") else todo.pop(int(action[7:]) - 1) if action.startswith("remove ") and action[7:].isdigit() and 0 < int(action[7:]) <= len(todo) else print("Invalid")
# i experimented with trying to fit it all on one kine...
