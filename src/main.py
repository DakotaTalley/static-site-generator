import os
import shutil

from html_markdown import markdown_to_html_node


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    build_project_dir(dir_path_static, dir_path_public)
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

def generate_page(from_path, template_path, dest_path):
    print("Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        md = f.read()
    with open(template_path) as f:
        html_template = f.read()

    html_node = markdown_to_html_node(md)
    html_content = html_node.to_html()

    title = extract_title(md)
    html = html_template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_content)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(html)

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
        from_path = os.path.join(source_dir, item)
        destination_path = os.path.join(destination_dir, item)
        if os.path.isfile(from_path):
            shutil.copy(from_path, destination_dir)
        else:
            build_project_dir(from_path, destination_path)
    return 0

main()