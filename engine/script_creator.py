import shutil


def create(name: str = "new_script.py", dest_path: str = "./scripts/", src_path: str = "./assets/default_script.txt"):
    with open(src_path, "r") as f:
        contents = f.readlines()

    with open(dest_path + name, "w") as f:
        f.writelines(contents)
