import keyboard, winsound

print("listening...")
while True:
    key = keyboard.read_key()
    if key == "space": 
        winsound.Beep(10000, 1)
    elif key == "delete":
        break