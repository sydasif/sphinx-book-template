# Cross-References

Demonstrates all cross-reference types in Sphinx and MyST.

## Labeling and Referencing

You can label any section, figure, table, or equation:

```{toctree}
:maxdepth: 1
:caption: 'Cross-Reference Examples:'

02a_code_blocks/index
02b_tables/index
02c_figures/index
02d_admonitions/index
02e_math_citations/index

```

### Section References

Refer to {ref}`code-blocks-chapter` for details.

**Note:** In MyST Markdown, use `{#label}` syntax for section labels.

### Figure References

See {ref}`fig-sample` from the Figures chapter for an example.

Or with number: {numref}`fig-sample`.

### Table References

See {ref}`tbl-config` for configuration examples.

```{list-table} Sample Configuration
:name: tbl-config
:header-rows: 1
:widths: 25 25 50

* - Parameter
  - Value
  - Description
* - Timeout
  - 30
  - Connection timeout in seconds
* - Retry
  - 3
  - Number of retry attempts
* - Dry Run
  - False
  - Whether to validate without applying
```

### Equation References

Refer to Equation {ref}`eq-einstein` for the energy-mass relation.

## Self-References

```{note}
:name: self-reference-note

This admonition references itself via its name.
```

Click {ref}`self-reference-note` to jump back.

## Implicit Cross-References

Sphinx can automatically create references for some elements:

- **Sections:** Use ` `Section Title` ` or {ref}`label`
- **Figures:** Use `Figure~\ref{label}` in reST, or {ref}`fig-label` in MyST
- **Tables:** Use `Table~\ref{label}` in reST, or {ref}`tbl-label` in MyST

## Cross-Chapter References

References to other chapters work seamlessly:

- Code examples: {ref}`code-blocks-chapter`
- Table examples: {ref}`tables-chapter`
- Figure examples: {ref}`figures-chapter`
- Admonition examples: {ref}`admonitions-chapter`
- Math examples: {ref}`math-chapter`

## Glossary Terms

Define terms once and reference them throughout:

```{glossary}
napalm
  Network Automation and Programmability Abstraction Layer with Multivendor support.

nornir
  A Python library for network automation that focuses on flexibility and
  performance.

ansible
  An open-source automation platform for configuration management, application
  deployment, and orchestration.
```

See the {term}`napalm` documentation for API details.
Also check {term}`nornir` and {term}`ansible` for related tools.

## Missing References (Edge Cases)

### Non-existent Reference

```{note}
The following reference does not exist and will generate a warning:

The build will emit:
```

WARNING: undefined label: nonexistent-label [ref.ref]

```

```

### Broken Link Targets

```{note}
Links to non-existent pages generate warnings:

The build will emit:
```

WARNING: nonlocal image URI found: ../nonexistent-image.png [misc.image_not_found]

```

Always verify external links and image paths before publishing.
```

## Cross-Reference Styles

| Style    | Syntax              | Output Example     |
| -------- | ------------------- | ------------------ |
| ref      | `{ref}`label``      | Section Title      |
| numref   | `{numref}`label``   | Figure 2.1         |
| option   | ` `option` `        | --verbose          |
| term     | `{term}`term``      | napalm             |
| glossary | `{glossary}`label`` | See glossary entry |
| doc      | `{doc}`path``       | Chapter Title      |

## Hyperlink Syntax

Standard Markdown links work alongside Sphinx references:

- Internal: [`index`](../index.md)
- External: [GitHub](https://github.com)
- Email: [Email me](mailto:support@example.com)
- Anchor: [`#section-heading`](#section-heading)

## Targeted Code Block References

```{code-block} python
:linenos:
:emphasize-lines: 3
:name: code-ref-example

import napalm
from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")  # Critical line
result = nr.run(task=deploy)
```

See the code block above for the highlighted implementation.

## Image Maps and Complex Figures

For interactive HTML builds, consider using image maps. For PDF, stick to
static figures:

```{figure} ../images/sample.png
:alt: Complex diagram
:width: 80%
:name: fig-complex

A complex figure with embedded annotations (HTML only).
```

HTML viewers can add interactivity; PDF renders the static image.

## Back-references

Every reference creates a back-reference in the PDF:

```{note}
Clicking the back-reference arrow (→) in the PDF jumps to the source.
```

## Math References

Refer to the math chapter for equations like Einstein's $E = mc^2$
and the impedance of free space calculation.

## Combining References

You can combine multiple reference types:

1. Figure {ref}`fig-sample` shows the setup
2. Table {ref}`tbl-config` lists the parameters
3. Equation {ref}`eq-einstein` describes the theory

See the {doc}`02a_code_blocks/index` chapter for code examples.
