import random

servers = ["Server1", "Server2", "Server3", "Server4", "Server5"]
states = ["Underloaded", "Balanced", "Overloaded"]

system = {server: random.choice(states) for server in servers}

print("Initial Server Loads:")
for s, l in system.items():
    print(s, ":", l)

overloaded = [s for s in system if system[s] == "Overloaded"]
underloaded = [s for s in system if system[s] == "Underloaded"]

print("\nBalancing Load...")

for o in overloaded:
    if underloaded:
        u = underloaded.pop()
        system[o] = "Balanced"
        system[u] = "Balanced"
        print(f"Moved tasks from {o} to {u}")
    else:
        print(f"No underloaded server available for {o}")

print("\nUpdated Server Loads:")
for s, l in system.items():
    print(s, ":", l)
