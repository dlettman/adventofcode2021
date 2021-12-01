import os
import pathlib
import shutil

def parse_input(filename):
    with open(filename) as file:
        input_list = file.read().splitlines()
    return input_list


def create_folder_structure():
    cwd = pathlib.Path().resolve()
    for i in range(1,26):
        day_number = str(i).zfill(2)
        newdir_path = os.path.join(cwd, day_number)

        try:
            os.mkdir(newdir_path)
        except FileExistsError:
            pass

        for filename in ["inputtest.txt", "input.txt"]:
            pathlib.Path(os.path.join(newdir_path, filename)).touch()

        exercise_filename = f"exercise_{day_number}.py"
        shutil.copy((os.path.join(cwd, "template.py")), os.path.join(newdir_path, exercise_filename))

if __name__ == "__main__":
    create_folder_structure()