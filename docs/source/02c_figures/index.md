# Figures {#figures-chapter}

Demonstrates figure edge cases including scaling, positioning, and cross-references.

## Basic Figure

```{figure} ../images/sample.png
:alt: Sample figure showing template structure
:width: 60%
:name: fig-sample

This is a basic figure with caption. The :alt: field provides accessibility text,
and :width: controls scaling.
```

Figure {ref}`fig-sample` shows the sample image.

## Multiple Figures Side by Side

```{figure} ../images/sample.png
:alt: Sample 1
:width: 45%
:name: fig-side-1

Left figure.
```

```{figure} ../images/sample.png
:alt: Sample 2
:width: 45%
:name: fig-side-2

Right figure.
```

## Figure with No Width (Original Size)

```{figure} ../images/sample.png
:alt: Full-size figure

This figure uses its natural size. In PDF, large images may overflow margins.
```

## Figure with Caption and Legend

```{figure} ../images/sample.png
:alt: Network topology diagram
:width: 80%
:name: fig-topology

**Figure 2:** Simplified network topology for lab environment.

- **Routers:** CSR1000v instances running IOS-XE
- **Switches:** Catalyst 9300 with IOS 17.x
- **Firewalls:** Firepower 1010 with FTOS
- **Management:** Out-of-band via dedicated mgmt interface
```

## Edge Case: Missing Image File

```{note}
The following figure references a **non-existent file** to demonstrate error handling:

The build will emit a warning:
```

WARNING: image file not readable: ../images/nonexistent.png

```
And in PDF:
```

! Package pdftex.def Error: File `images/nonexistent.png' not found: using draft setting.

```

Always verify image paths exist before committing.
```

## Embedded SVG (Alternative to PNG)

For vector graphics, SVG embeds cleanly:

```{figure} ../images/sample.png
:alt: Vector-compatible figure
:width: 50%
:name: fig-vector

SVG figures scale without quality loss in both HTML and PDF.
```

## Large Figure (Potential PDF Overflow)

```{figure} ../images/sample.png
:alt: Oversized figure
:width: 150%
:name: fig-large

**Warning:** This figure exceeds 100% width. In PDF builds, this may cause
overfull hbox warnings or clipping. Keep figures within page margins.
```

## Figure with Numbering Disabled

```{figure} ../images/sample.png
:alt: Unnumbered figure
:width: 40%
:name: fig-unnumbered

To disable automatic numbering, omit the :name: option or use `.. figure::`
without a caption in raw reStructuredText mode.
```

## Cross-Referencing Figures

Figure {ref}`fig-sample` appears in section 02c_figures. You can reference it
from anywhere in the book using `ref` or `numref`.

**Numref example:** See Figure {numref}`fig-sample` for details.
