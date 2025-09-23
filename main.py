import os
import re
import glob
import pypandoc
from pathlib import Path

def render(template, **context):
    def replacer(match):
        expr = match.group(1).strip()
        return str(eval(expr, {}, context))
    return re.sub(r"\{\{(.*?)\}\}", replacer, template)

def get_post_paths():
    posts = glob.glob("./posts/*-*.md")
    return posts

def get_page_paths():
    pages = glob.glob("./pages/*.md")
    return pages

os.system("rm -rf html")
os.system("mkdir -p html/post/")

for post in get_post_paths():
    post_stem = Path(post).stem
    timestamp = post_stem.split("-")[-1]
    html_content = pypandoc.convert_file(post, "html")

    template = ""
    with open("./templates/general.html", "r") as f:
        template = f.read()

    context = {k: v for k, v in locals().items() if k != "template"}
    html = render(render(template, **context), **context)

    with open(f"./html/post/{post_stem}.html", "w") as f:
        f.write(html)

for page in get_page_paths():
    page_stem = Path(page).stem
    html_content = pypandoc.convert_file(page, "html")
    template = ""
    with open("./templates/general.html", "r") as f:
        template = f.read()

    context = {k: v for k, v in locals().items() if k != "template"}
    html = render(render(template, **context))
    with open(f"./html/{page_stem}.html", "w") as f:
        f.write(html)

