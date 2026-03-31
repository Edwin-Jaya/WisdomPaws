from controller import Controller

class Game:
    def __init__(self, controller=None):
        self.controller = controller if controller else Controller()

    def update(self):
        if not self.controller.update():
            return "quit"  # stop loop if camera closed

        gesture = self.controller.get_gesture()
        if gesture == "Open_Palm":
            return "idle"   # override to idle

        return "continue"   # no override
