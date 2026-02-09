schedule = [
    {"room": 101, "patient": "Ali", "medicine": "Panadol"},
    {"room": 102, "patient": "Sara", "medicine": "Antibiotic"},
    {"room": 103, "patient": "Ahmed", "medicine": "Insulin"}
]

class DeliveryRobot:

    def move(self, location):
        print(f"Moving to room {location}...")

    def pick_medicine(self, med):
        print(f"Picked up {med} from storage.")

    def scan_id(self, patient):
        print(f"Scanning ID of {patient}... Verified!")

    def deliver(self, med, room):
        print(f"Delivered {med} to room {room}.")

    def alert_staff(self):
        print("Alerting staff for assistance!")


robot = DeliveryRobot()

print("Starting Medicine Delivery...\n")

for task in schedule:
    robot.move(task["room"])
    robot.pick_medicine(task["medicine"])
    robot.scan_id(task["patient"])
    robot.deliver(task["medicine"], task["room"])

print("\nAll deliveries completed!")
