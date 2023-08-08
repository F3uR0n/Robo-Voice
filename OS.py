import os

if __name__ == '__main__':
    print("Wlecome to Robo Voice")
    while True:
        z = input("Enter what you want me to speak: ")
        if z == "end":
        command = f"say {z}"
        os.system(command)