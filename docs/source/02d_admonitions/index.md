# Admonitions

Demonstrates all admonition types and edge cases.

## Standard Admonitions

```{note}
This is a standard note admonition. Use for helpful information.
```

```{tip}
Here's a helpful tip for readers.
```

```{important}
This information is important for understanding the topic.
```

```{caution}
Use caution when handling production credentials.
```

```{warning}
This is a warning — something could go wrong if you ignore it.
```

```{danger}
**Danger!** Immediate action required.
```

```{error}
An error occurred during processing.
```

## Collapsible Admonitions (MyST Tabs Alternative)

```{dropdown} Click to expand details
:color: primary
:open:

You can place any content here, including code blocks and tables.
```

## Admonition with Code Block

````{example}
Example admonition with embedded code:

```bash
#!/bin/bash
# Deploy to all routers
for host in $(cat hosts.txt); do
    ansible $host -m ios_config -a "src=configs/{{ item }}"
done
````

````

## Empty Admonition (Edge Case)

```{note}
(empty)
````

Avoid empty admonitions — they add noise without value.

## Admonition with Tables

```{seealso}
Related documentation:

| Directive    | Purpose                          |
| ------------ | -------------------------------- |
| `note`       | General information              |
| `warning`    | Potential problems               |
| `danger`     | Immediate action required        |
| `tip`        | Helpful advice                   |
```

## Admonition with Figures

```{figure} ../images/sample.png
:alt: Diagram
:width: 30%
:align: right
:name: fig-admonition-img

Image inside admonition.
```

See also: {ref}`fig-admonition-img` for the figure referenced here.

## Special Characters in Admonitions

```{warning}
Special characters that must work:

- Arrow: ➜
- Check: ✗
- Box drawing: ─  ├  └  │
- Dollar: $100
- Ampersand: &
- Less than / greater than: < >
```
