import os
import shutil
import sys

from html_markdown import markdown_to_html_node


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    build_project_dir(dir_path_static, dir_path_public)
    generate_pages_recursive(basepath, dir_path_content, template_path, dir_path_public)

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    path_dir = os.listdir(dir_path_content)
    if len(path_dir) <= 0:
        return 0
    for item in path_dir:
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))
        if os.path.isfile(from_path) and from_path.endswith(".md"):
            generate_page(basepath, from_path, template_path, dest_path)
        else:
            os.mkdir(dest_path)
            generate_pages_recursive(basepath, from_path, template_path, dest_path)
    return 0

def generate_page(basepath, from_path, template_path, dest_path):
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
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

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