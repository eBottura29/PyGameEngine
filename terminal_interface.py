import engine.script_creator as sc
import engine.engine as engine
import engine.py_game_engine as pyg

quit_keywords = ["quit", "exit", "back"]

print("Welcome to the PyGameEngine!")
print("Enter an operation to run:")
print("\n1: Run the game\n2: Create (a) script(s)\n3: Rename your game\n9: Quit this interface\n")

while True:
    ipt = input("> ")

    match ipt:
        case "1":
            engine.add_scripts()
            engine.run()
            engine.pygame.quit()
        case "2":
            print("Enter a filename(s) for your script(s)")
            print("Do not include extensions and type 'quit', 'exit' or 'back' to exit the script creator.\n")

            r = True
            while r:
                ipt = input("> ")

                if ipt.lower() in quit_keywords:
                    r = False
                else:
                    sc.create(ipt + ".py")
        case "3":
            name = ipt("Enter your game's name: ")
            pyg.game_name = name
        case "9":
            print("Thanks for using PyGameEngine!")
            break
        case _:
            print("Operation not recognized... Try again.")
