import os
import re
import glob
import pypandoc
from pathlib import Path
import shutil

def render(template, **context):
    def replacer(match):
        expr = match.group(1).strip()
        return str(eval(expr, {}, context))
    return re.sub(r"\{\{(.*?)\}\}", replacer, template)

def get_markdown_paths(folder):
    return glob.glob(f"{folder}/*.md")

def load_template(path="./templates/general.html"):
    with open(path, "r") as f:
        return f.read()

def convert_markdown(file_path):
    return pypandoc.convert_file(file_path, "html")

def generate(src_folder, dst_folder):
    Path(dst_folder).mkdir(parents=True, exist_ok=True)
    template = load_template()

    for md_file in get_markdown_paths(src_folder):
        stem = Path(md_file).stem

        timestamp = stem.split("-")[-1] if "-" in stem else None
        html_content = convert_markdown(md_file)

        context = {
            "timestamp": timestamp,
            "html_content": html_content
        }

        html = render(render(template, **context), **context)
        out_file = Path(dst_folder) / f"{stem}.html"
        with open(out_file, "w") as f:
            f.write(html)

def build():
    shutil.rmtree("html", ignore_errors=True)
    generate("./posts", "./html/post")
    generate("./pages", "./html")

if __name__ == "__main__":
    build()
