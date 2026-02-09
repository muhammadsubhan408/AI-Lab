import random

components = ["A","B","C","D","E","F","G","H","I"]

# Initialize system with random states
system = {}
for comp in components:
    system[comp] = random.choice(["Safe", "Vulnerable"])

print("Initial System State:")
for k, v in system.items():
    print(k, ":", v)

# Scan system
vulnerable_list = []

print("\nScanning System...")
for comp, state in system.items():
    if state == "Vulnerable":
        print(f"Warning! Component {comp} is vulnerable.")
        vulnerable_list.append(comp)
    else:
        print(f"Component {comp} is secure.")

# Patch vulnerabilities
print("\nPatching Vulnerabilities...")
for comp in vulnerable_list:
    system[comp] = "Safe"
    print(f"Component {comp} has been patched.")

# Final check
print("\nFinal System State:")
for k, v in system.items():
    print(k, ":", v)
