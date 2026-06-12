import os
import time

# System Configuration
total_slots = 5
available_slots = total_slots
# List representing parking spaces (False = empty, True = occupied)
parking_slots = [False] * total_slots

def clear_screen():
    # Clears the terminal screen for a clean dashboard look
    os.system('cls' if os.name == 'nt' else 'clear')

def display_dashboard(message=""):
    clear_screen()
    occupied_slots = total_slots - available_slots
    
    print("================================")
    print("    SMART PARKING DASHBOARD     ")
    print("================================")
    print(f" Total Slots:     {total_slots}")
    print(f" Available Slots: {available_slots}")
    print(f" Occupied Slots:  {occupied_slots}")
    print("--------------------------------")
    
    # Draw the parking slots visually using text
    visual = ""
    for i in range(total_slots):
        if parking_slots[i]:
            visual += "[ CAR ] "
        else:
            visual += f"[ P{i+1}  ] "
    print(visual)
    print("================================")
    
    # Display temporary status messages if any
    if message:
        print(f" >> {message} <<")
        print("================================")
        
    print("1. Simulate Car Entry")
    print("2. Simulate Car Exit")
    print("3. Quit Program")

def car_entry():
    global available_slots
    if available_slots > 0:
        # Find the first empty slot (False)
        for i in range(total_slots):
            if not parking_slots[i]:
                parking_slots[i] = True
                available_slots -= 1
                return f"Car entered Slot {i+1}!"
    return "Parking is FULL!"

def car_exit():
    global available_slots
    if available_slots < total_slots:
        # Find the last occupied slot (True)
        for i in range(total_slots - 1, -1, -1):
            if parking_slots[i]:
                parking_slots[i] = False
                available_slots += 1
                return f"Car exited Slot {i+1}!"
    return "Parking is already EMPTY!"

# Main Program Loop
current_message = ""
while True:
    display_dashboard(current_message)
    current_message = "" # Reset message after displaying
    
    # Wait for user input
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        current_message = car_entry()
    elif choice == '2':
        current_message = car_exit()
    elif choice == '3':
        print("\nShutting down Smart Parking System...")
        break
    else:
        current_message = "Invalid choice. Please enter 1, 2, or 3."
        
    time.sleep(0.5) # Slight pause to make the UI feel smooth
