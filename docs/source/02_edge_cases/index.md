# Edge Cases and Advanced Features

This chapter demonstrates edge cases and advanced features that must work correctly
in both HTML and PDF builds. Copy this pattern when building your own documentation.

```{toctree}
:maxdepth: 1
:caption: 'Edge Cases:'

02a_code_blocks
02b_tables
02c_figures
02d_admonitions
02e_math_citations
02f_cross_references
```

## Shell Prompts in Code Blocks

Shell-prompt glyphs render correctly in both HTML and PDF:

```console
(.venv) ➜  my-book git:(main) ✗ ansible-playbook site.yml
```

## Directory Trees in Code Blocks

```text
.
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
└── tasks
    └── main.yml
```

## Figures

```{figure} ../images/sample.png
:alt: Sample figure
:width: 60%

Figure captions appear below the image in HTML and in the PDF.
```

## Notes and Warnings

```{note}
MyST admonitions such as this note also work in the PDF build.
```

## Tables

| Command         | Output                                |
| --------------- | ------------------------------------- |
| `make html`     | `docs/build/html/index.html`          |
| `make latexpdf` | `docs/build/latex/<project-name>.pdf` |
