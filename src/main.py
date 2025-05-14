import os
import shutil


def main():
    build_project_dir("./static", "./public")

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("#").strip()
    raise Exception("missing h1 header")

def build_project_dir(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        raise Exception("source directory does not exist")
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)
    path_dir = os.listdir(source_dir)
    if len(path_dir) <= 0:
        return 0
    for item in path_dir:
        item_dir = f"{source_dir}/{item}"
        if os.path.isfile(item_dir):
            shutil.copy(item_dir, destination_dir)
        else:
            build_project_dir(item_dir, f"{destination_dir}/{item}")
    return 0

main()