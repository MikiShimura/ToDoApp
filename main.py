todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = input("Number of the todo to edit: ")
            todos[int(number)-1] = input("Enter new todo:")
        case "exit":
            break

print("Bye!")