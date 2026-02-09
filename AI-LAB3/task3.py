import random

tasks = ["Backup1", "Backup2", "Backup3", "Backup4", "Backup5"]
status = ["Completed", "Failed"]

backup_system = {task: random.choice(status) for task in tasks}

print("Initial Backup Status:")
for t, s in backup_system.items():
    print(t, ":", s)

print("\nRetrying Failed Backups...")
for task in backup_system:
    if backup_system[task] == "Failed":
        print(f"{task} failed. Retrying...")
        backup_system[task] = "Completed"
        print(f"{task} is now completed.")

print("\nUpdated Backup Status:")
for t, s in backup_system.items():
    print(t, ":", s)
