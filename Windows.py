import pyttsx3

engine = pyttsx3.init()

print("Wlecome to Robo Voice")
while True:
        z = input("Enter what you want me to speak: ")
        if z == "end":
            break
        engine.say(z)
        engine.runAndWait()
        engine.stop()
