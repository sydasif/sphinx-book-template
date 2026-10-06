# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# TODO: Replace these values for each new book.

project = "My New Book"
copyright = "2026, Your Name"
author = "Your Name"
release = "0.1"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx.ext.autosectionlabel",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"
# Put a logo file (e.g. logo.png) into docs/source/_static/ to brand the HTML.
html_static_path = ["_static"]
html_title = "My New Book"

# -- Options for LaTeX/PDF output -------------------------------------------
# pdflatex cannot handle arbitrary Unicode characters. The mappings below are
# the glyphs used in shell prompts and directory trees inside code blocks.
# If you add a new non-ASCII character to any code block, add a matching
# \DeclareUnicodeCharacter{...}{...} line here, otherwise `make latexpdf`
# fails with:
#   ! LaTeX Error: Unicode character ... not set up for use with LaTeX
latex_elements = {
    "preamble": r"""
\DeclareUnicodeCharacter{2500}{-}  % ─  box-drawing horizontal
\DeclareUnicodeCharacter{2502}{|}  % │  box-drawing vertical
\DeclareUnicodeCharacter{251C}{+}  % ├  box-drawing tee
\DeclareUnicodeCharacter{2514}{+}  % └  box-drawing elbow
\DeclareUnicodeCharacter{279C}{$\rightarrow$}  % ➜  heavy arrow (shell prompt)
\DeclareUnicodeCharacter{2717}{$\times$}       % ✗  ballot cross
""",
    # Use default Computer Modern fonts as fallback if TeX Gyre unavailable
    "fontpkg": r"""
% If TeX Gyre fonts are not installed, fall back to Computer Modern
\IfFileExists{tgtermes.sty}{
  \usepackage{tgtermes}
  \usepackage{tgheros}
  \usepackage{tgcursor}
}{
  \usepackage{mathptmx}  % Times-like math font
}
""",
}
