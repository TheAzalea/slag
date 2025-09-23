import os
import re
import glob
import pypandoc
from pathlib import Path
import shutil

import re

def render(template, **context):
    def replacer(match):
        code = match.group(1)
        code = code.replace("“", "\"").replace("”", "\"")
        local_ns = dict(context)
        output = []
        def write(*args):
            output.append(" ".join(map(str, args)))
        local_ns["write"] = write
        exec(code, {}, local_ns)
        return "".join(output)
    return re.sub(
        r"```python-eval\s+(.*?)```",
        replacer,
        template,
        flags=re.DOTALL
    )

def get_markdown_paths(folder):
    return glob.glob(f"{folder}/*.md")

def load_template(path="./templates/general.html"):
    with open(path, "r") as f:
        return f.read()

def convert_markdown(md_text):
    return pypandoc.convert_text(md_text, "html", format="md")

def generate(src_folder, dst_folder):
    Path(dst_folder).mkdir(parents=True, exist_ok=True)
    template = load_template()

    for md_file in get_markdown_paths(src_folder):
        stem = Path(md_file).stem
        timestamp = stem.split("-")[-1] if "-" in stem else None

        context = {
                "timestamp": timestamp,
                "html_content": "",
                "posts": get_markdown_paths("./posts/")
                }

        with open(md_file, "r") as f:
            md_content = f.read()
        md_content = render(md_content, **context)

        context["html_content"] = convert_markdown(md_content)
        html = render(render(template, **context), **context)
        out_file = Path(dst_folder) / f"{stem}.html"
        with open(out_file, "w") as f:
            f.write(html)

def build():
    shutil.rmtree("html", ignore_errors=True)
    generate("./posts", "./html/post")
    generate("./pages", "./html")
    os.system("cp ./static/* ./html/ -r")

if __name__ == "__main__":
    build()
