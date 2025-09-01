# Python Project In DSA Stack
#global declared

MAX_SIZE = 5   # Maximum value is 5 
stack = []
top = -1

#Add value 
def push(item):
    global top
    if top == MAX_SIZE - 1:
        print("\n## Stack is Full!")
    else:
        stack.append(item)
        top += 1
        print(f"\n## At Position: {top}, Pushed value: {item}")

#Delete Value
def pop():
    global top
    if top == -1:
        print("\n## Stack is Empty!")
    else:
        value = stack.pop()
        print(f"\n## At Position: {top}, Popped value: {value}")
        top -= 1

#Display te Value
def display():
    if top == -1:
        print("\n## Stack is Empty!")
    else:
        print(f"\n## Stack size: {top + 1}")
        for i in range(top, -1, -1):
            print(f"At Position: {i}, Value: {stack[i]}")


# list
run_flag = True
while run_flag:
    print("\nIn Stack list")
    print("1. Push\n")
    print("2. Pop\n")
    print("3. Display\n")
    print("Other to Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter the value to be Pushed: "))
        push(item)
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    else:
        run_flag   = False

print("\nThank You Run Again.")