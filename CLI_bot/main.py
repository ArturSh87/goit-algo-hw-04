from decorators import input_error

# Парсер команд
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Хендлери 

def add_contact(args, contacts):
    #if len(args) != 2:
        #return "Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Змінює номер телефону 

def change_contact(args, contacts):
    #if  len(args) != 2:
        #return "Usage: change [name] [new phone]" 
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated!"
    else:
        return "Contact not found."

# Виводить номер телефону 

def show_phone(args, contacts):
    #if len(args) != 1:
       # return "Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

# Виводить усі збережені контакти

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts saved."


# Основний цикл
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")   
    
        
# Старт       
if __name__ == "__main__":
    main()
