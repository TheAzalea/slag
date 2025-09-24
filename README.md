# ![slag](https://github.com/TheAzalea/slag/blob/main/logo.png)

Slag is a dead simple blog builder.

It can convert your markdown files into a static website that you provide the
template for.

- `pages/`: Put your pages in markdown to have them hosted at `/`.
- `posts/`: Posts are named in `title-timestamp.md` format.
- `static/`: The contents of this directory are directly copied into the final
result. Useful for hosting media or CSS/JS.
- `template/`: Holds the HTML file that is used as a template to insert the
specific page contents in.

Markdown and HTML files support Python code evaluation in the format of:

```python-eval
import math
write(math.pi) # Use this function to insert text
write("Pi times two is: " + str(math.pi * 2))
```

The code is only evaluated at build. This can be used to generate a list of
your most recent posts in your homepage (`pages/index.md`) or even maybe
generate SVG images of fractals.

