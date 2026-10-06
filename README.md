# Sphinx Book Template

A ready-to-publish book project: [Sphinx](https://www.sphinx-doc.org/) +
[MyST Markdown](https://myst-parser.readthedocs.io/) +
[sphinx-book-theme](https://sphinx-book-theme.readthedocs.io/), pre-configured
to build **HTML + PDF + ePub** locally and on
[Read the Docs](https://readthedocs.org/).

## Start a new book

1. Click **Use this template** → *Create a new repository* on GitHub.
2. Clone your new repo and edit the placeholders:
   - `docs/source/conf.py` — `project`, `author`, `copyright`, `html_title`
     (and optionally add a logo in `docs/source/_static/`)
   - `README.md` — this file: title and description
   - `docs/source/index.md` — your real introduction
3. Write chapters under `docs/source/<NN_topic>/` and register each one in the
   toctree in `docs/source/index.md` (see `01_introduction/` for a worked
   example of headings, code blocks, figures, admonitions and tables).
4. Publish on Read the Docs: import the repo (dashboard → *Import a project*).
   `.readthedocs.yaml` is already set up for HTML + PDF + ePub, so no extra
   configuration is needed. The hosted **Downloads** menu serves the PDF/ePub.
   (Note: pull-request builds only produce HTML — PDF/ePub are built after
   merging.)

## Building the book locally

### Prerequisites

```bash
sudo apt-get update
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic
sudo apt install latexmk

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Note: `pandoc` is **not** required. The pipeline is
> `sphinx-build` (MyST parses the Markdown natively) → `latexmk` → `pdflatex`.

### Build

```bash
source .venv/bin/activate
cd docs
make latexpdf     # PDF  -> docs/build/latex/<project-name>.pdf
make html         # HTML -> docs/build/html/index.html
```

The PDF filename is derived from `project` in `docs/source/conf.py`.

## Unicode glyphs in code blocks

Shell prompts and directory trees use non-ASCII characters (`➜`, `✗`, `─`,
`├`, `└`, `│`). pdflatex only knows them because of the `latex_elements`
preamble in `docs/source/conf.py`. **If you add a new non-ASCII character to a
code block, add a matching `\DeclareUnicodeCharacter{...}{...}` line there**,
otherwise the PDF build fails with
`LaTeX Error: Unicode character ... not set up for use with LaTeX`.

## Continuous integration

`.github/workflows/build-pdf.yml` builds the PDF on every push to `main` and
uploads it as a workflow artifact — a GitHub-only fallback if Read the Docs is
not connected yet. Delete the file if you don't want it.
