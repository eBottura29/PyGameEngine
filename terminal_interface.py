import engine.script_creator as sc
import engine.engine as engine
import json

quit_keywords = ["quit", "exit", "back"]

with open("engine/assets/settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)

print("\nWelcome to the PyGameEngine!")
print("Enter an operation to run:")


def print_operations():
    print("\n############################")
    print("| 1: Run the game          |")
    print("| 2: Create (a) script(s)  |")
    print("| 3: Rename your game      |")
    print("| 9: Quit the engine       |")
    print("############################\n")


print_operations()

while True:
    ipt = input("> ")

    match ipt:
        case "1":
            engine.add_scripts()
            engine.run()
            engine.pygame.quit()
        case "2":
            print("\nEnter a filename(s) for your script(s)")
            print("Do not include extensions and type 'quit', 'exit' or 'back' to exit the script creator.\n")

            r = True
            while r:
                ipt = input("SC: ")

                if ipt.lower() in quit_keywords:
                    r = False
                else:
                    sc.create(ipt + ".py")

                print("Script has been created\n")
        case "3":
            name = input("\nEnter your game's new name: ")
            settings["game_name"] = name
            print(f"Game name has been changed to: {name}\n")
        case "9":
            print("\nThanks for using PyGameEngine!")
            break
        case _:
            print("\nOperation not recognized... Try again.")

    print_operations()
