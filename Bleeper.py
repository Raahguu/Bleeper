import keyboard, winsound

bleeping = False
bleep_key = "caps lock"
bleep_sound = "bleep.wav"

def on_down(event):
    global bleeping
    if event.name == bleep_key and not bleeping:
        bleeping = True
        winsound.PlaySound("bleep.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        print("ON")
    elif event.name == bleep_key and bleeping:
        bleeping = False
        winsound.PlaySound(None, winsound.SND_PURGE)
        print("OFF")

print("listening...")
keyboard.on_press(on_down)
keyboard.wait()