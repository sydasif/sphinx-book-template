# Introduction

This is a sample chapter showing the building blocks you can use everywhere in
the book. To add a new chapter:

1. Duplicate this directory: `cp -r 01_introduction 02_your_topic`
2. Edit `02_your_topic/index.md` (this file's content)
3. Add `02_your_topic/index` to the toctree in `../index.md`

## Shell prompts in code blocks

Shell-prompt glyphs render correctly in both HTML and PDF:

```console
(.venv) ➜  my-book git:(main) ✗ ansible-playbook site.yml
```

## Directory trees in code blocks

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

## Admonitions

```{note}
MyST admonitions such as this note also work in the PDF build.
```

## Tables

| Command        | Output                                  |
| -------------- | --------------------------------------- |
| `make html`    | `docs/build/html/index.html`            |
| `make latexpdf`| `docs/build/latex/<project-name>.pdf`   |
