# Define rooms and their connections
game_world = {
    "entrance": {
        "description": "You are at the entrance of a dark cave.",
        "exits": {"north": "hall"},
    },
    "hall": {
        "description": "The hall is dimly lit. You see doors leading in different directions.",
        "exits": {"south": "entrance", "east": "armory", "west": "library"},
    },
    "armory": {
        "description": "The armory is filled with old, rusty weapons.",
        "exits": {"west": "hall"},
        "item": "sword",
    },
    "library": {
        "description": "Rows of ancient books line the walls. A faint whisper can be heard.",
        "exits": {"east": "hall"},
    },
}

# Initialize the player state
player_state = {
    "current_room": "entrance",
    "inventory": ["sowrd"]
}

def show_room_details():
    room = game_world[player_state["current_room"]]
    print("\n" + room["description"])
    for direction, next_room in room["exits"].items():
        print(f"There is a path to the {direction}.")
    if "item" in room:
        print(f"You see a {room['item']} here.")

def move(direction):
    current_room = game_world[player_state["current_room"]]
    if direction in current_room["exits"]:
        player_state["current_room"] = current_room["exits"][direction]
        show_room_details()
    else:
        print("You can't go that way.")

def pick_up_item():
    current_room = game_world[player_state["current_room"]]
    if "item" in current_room:
        item = current_room.pop("item")
        player_state["inventory"].append(item)
        print(f"You picked up a {item}!")
    else:
        print("There is nothing to pick up here.")
        
def process_command(command):
    words = command.split()
    if words[0] == "go" and len(words) > 1:
        move(words[1])
    elif command == "look":
        show_room_details()
    elif command == "pick":
        pick_up_item()
    elif command == "inventory":
        print("You have:", player_state["inventory"])
    else:
        print("I don't understand that command.")

# Game loop
def start_game():
    print("Welcome to the Adventure Game!")
    show_room_details()

    while True:
        command = input("\nWhat would you like to do? ").lower()
        if command == "quit":
            print("Thanks for playing!")
            break
        process_command(command)

# Start the game
start_game()