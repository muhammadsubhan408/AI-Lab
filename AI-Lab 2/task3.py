class ResponseAgent:
    def execute_response(self):
        print("Executing response...")


class AlertAgent(ResponseAgent):
    def execute_response(self):
        print("Sending alert notifications to admin.")


class BlockAgent(ResponseAgent):
    def execute_response(self):
        print("Blocking malicious activity.")


class RecoverAgent(ResponseAgent):
    def execute_response(self):
        print("Recovering affected systems.")


# Mixed list
agents = [AlertAgent(), BlockAgent(), RecoverAgent()]

# Polymorphism in action
for agent in agents:
    agent.execute_response()
