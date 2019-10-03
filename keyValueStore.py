# data structures
values = {}
count = {}
stack = []

def process_input():
    global values
    global count
    global stack

    user_input = input("> ")
    split = user_input.split(" ")
    command = split[0].upper()
    if command == "SET":
        key, value = split[1], split[2]
        count[value] = count.get(value, 0) + 1
        if key in values and values[key] is not None:
            count[values[key]] -= 1
        values[key] = value

        if len(stack) > 0:
            changes = stack[-1]
            changes[key] = value
    elif command == "GET":
        key = split[1]
        if key in values and values[key] is not None:
            print(values[key])
        else:
            print(f"{key} not set")
    elif command == "DELETE":
        key = split[1]
        if key in values:
            count[values[key]] -= 1
            values[key] = None 

        if len(stack) > 0:
            changes = stack[-1]
            changes[key] = None

    elif command == "COUNT":
        value = split[1]
        print(count.get(value, 0))
    elif command == "BEGIN":
        # Push the next few transactions onto the stack
        if len(stack) == 0:
            stack.append(values.copy())
        stack.append({})
    elif command == "COMMIT":
        # Pop off stack and keep changes
        if len(stack) > 0:
            stack.pop()
            if len(stack) == 1:
                stack.pop()
        else:
            print("NO TRANSACTION")
    elif command == "ROLLBACK":
        if len(stack) > 0:
            # discard the top value and iterate through the
            # rest of the stack and update values, then count at the end
            stack.pop()
            prev_values = stack[0]
            # For every dictionary in the stack add the keys up
            for dict in stack[1:]:
                for key in dict:
                    prev_values[key] = dict[key]

            # Save and count occurrences
            values = prev_values
            count = {}
            for key in values:
                value = values[key]
                if value is not None:
                    count[value] = count.get(value, 0) + 1
                else:
                    count[value] = count.get(value, 1) - 1

            # If we only have one left that means we have no more transactions
            if len(stack) == 1:
                stack.pop()
        else:
            print("NO TRANSACTION")
    elif command == "EXIT":
       return True 
    else:
        print("Invalid command. Please try again")

    return False

def main():
    done = False
    while not done:
        done = process_input()

if __name__ == "__main__":
    main()
