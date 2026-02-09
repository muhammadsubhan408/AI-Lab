class SecurityAgent:
    def __init__(self, agent_id, name, status):
        self.agent_id = agent_id
        self.name = name
        self.status = status

    def show_info(self):
        print(f"Agent ID: {self.agent_id}, Name: {self.name}, Status: {self.status}")


# Derived classes
class FirewallAgent(SecurityAgent):
    def monitor_traffic(self):
        print(f"{self.name} is monitoring network traffic...")


class MalwareDetectionAgent(SecurityAgent):
    def scan_files(self):
        print(f"{self.name} is scanning files for malware...")


class AutomationAgent(SecurityAgent):
    def run_automation(self):
        print(f"{self.name} is running automated security tasks...")


# Creating objects
firewall = FirewallAgent(101, "Firewall Defender", "Active")
malware = MalwareDetectionAgent(102, "Malware Scanner", "Active")
automation = AutomationAgent(103, "Auto Secure", "Running")

# Calling methods
firewall.show_info()
firewall.monitor_traffic()

malware.show_info()
malware.scan_files()

automation.show_info()
automation.run_automation()