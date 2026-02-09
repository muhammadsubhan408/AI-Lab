rooms = {
    'a': "safe", 'b': "safe", 'c': "fire",
    'd': "safe", 'e': "fire", 'f': "safe",
    'g': "safe", 'h': "safe", 'j': "fire"
}

path = ['a','b','c','d','e','f','g','h','j']

def display_env():
    print("\nEnvironment Status:")
    for i, room in enumerate(rooms):
        symbol = "🔥" if rooms[room] == "fire" else " "
        print(f"[{symbol}]", end=" ")
        if (i+1) % 3 == 0:
            print()

print("Robot starting at room 'a'")

for room in path:
    print(f"\nRobot moved to room {room}")

    if rooms[room] == "fire":
        print("Fire detected! Extinguishing...")
        rooms[room] = "safe"
        print("Fire extinguished.")
    else:
        print("Room is safe.")

    display_env()

print("\nFinal Status: All rooms are safe!")
