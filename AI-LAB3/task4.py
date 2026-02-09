import random

components = ["A","B","C","D","E","F","G","H","I"]
states = ["Safe", "Low Risk Vulnerable", "High Risk Vulnerable"]

system = {c: random.choice(states) for c in components}

print("Initial System State:")
for k, v in system.items():
    print(k, ":", v)

print("\nScanning System...")
for comp, state in system.items():
    if state == "Safe":
        print(f"{comp} is safe.")
    else:
        print(f"{comp} has {state}.")

print("\nPatching Low Risk Vulnerabilities...")
for comp in system:
    if system[comp] == "Low Risk Vulnerable":
        system[comp] = "Safe"
        print(f"{comp} patched successfully.")
    elif system[comp] == "High Risk Vulnerable":
        print(f"{comp} requires premium service!")

print("\nFinal System State:")
for k, v in system.items():
    print(k, ":", v)
