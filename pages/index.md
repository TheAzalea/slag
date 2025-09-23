# what is this

i finally have a **blog** huh?

# post list

```python-eval
from datetime import datetime

write("---\n\n")
for post in posts:
    post_title = ""
    post_url   = post.replace("posts", "post").replace(".md", ".html")
    post_timestamp = int(post_url.split(".")[-2].split("-")[-1])
    with open(post, "r") as f:
        post_title = f.readline().split("#")[-1].strip()
        post_content = f.read().strip()

    dt = datetime.utcfromtimestamp(post_timestamp)
    formatted_time = dt.strftime("%d %b %Y %a __%H:%M UTC__")  # Custom format

    write(f"### >> [{post_title}]({post_url})\n\n")
    write(f"**Published:** {formatted_time}\n\n")
    write(f"{post_content}\n\n")
    write(f"---\n\n")
```
