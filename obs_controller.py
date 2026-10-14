import obsws_python as obs # pyautogui wasnt working so were gonna go straight through obs


class OBSController:
    def __init__(self, password, host="localhost", port=4455):
        self.client = obs.ReqClient( # creates the ws client for connection
            host=host,
            port=port,#4455 is default, wouldnt needa be changed
            password=password, # we will ask users for pasword
            timeout=3 # up to 3 seconds for connection
        )

    def save_replay(self):
        self.client.save_replay() # saves last 30 seconds
        print("Doggy: Replay saved!")

    def is_connected(self):
        try:
            self.client.get_version()#connection chcecker
            return True
        except Exception:
            return False