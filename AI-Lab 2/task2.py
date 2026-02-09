class Threat:
    def __init__(self, threat_id, name, severity):
        self.threat_id = threat_id
        self.name = name
        self.severity = severity

    def display(self):
        print(f"Threat ID: {self.threat_id}, Name: {self.name}, Severity: {self.severity}")


class PhishingThreat(Threat):
    def analyze_email(self):
        print("Analyzing suspicious emails for phishing attempts...")


class RansomwareThreat(Threat):
    def scan_files(self):
        print("Scanning system files for ransomware behavior...")


class BotnetThreat(Threat):
    def detect_traffic(self):
        print("Detecting unusual network traffic linked to botnets...")


# Objects
phishing = PhishingThreat(201, "Email Phishing", "High")
ransomware = RansomwareThreat(202, "Crypto Locker", "Critical")
botnet = BotnetThreat(203, "Botnet Attack", "Medium")

# Simulation
phishing.display()
phishing.analyze_email()

ransomware.display()
ransomware.scan_files()

botnet.display()
botnet.detect_traffic()