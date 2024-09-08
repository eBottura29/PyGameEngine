import engine.script_creator as sc

while True:
    ipt = input("Enter a filename for your script (extension not needed): ")

    sc.create(ipt + ".py")
