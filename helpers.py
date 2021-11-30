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
        except:
            pass

        text_path = os.path.join(newdir_path, "input1test.txt")
        pathlib.Path(text_path).touch()

        text_path = os.path.join(newdir_path, "input2test.txt")
        pathlib.Path(text_path).touch()

        text_path = os.path.join(newdir_path, "input1.txt")
        pathlib.Path(text_path).touch()

        text_path = os.path.join(newdir_path, "input2.txt")
        pathlib.Path(text_path).touch()

        exercise_filename = f"exercise_{day_number}.py"
        shutil.copy((os.path.join(cwd, "template.py")), os.path.join(newdir_path, exercise_filename))

if __name__ == "__main__":
    create_folder_structure()