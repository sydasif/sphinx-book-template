# Math and Citations {#math-chapter}

Demonstrates mathematical expressions and bibliography handling.

## Inline Math

Use `$...$` for inline math: `$E = mc^2$`, `$\alpha + \beta$`, `$\sum_{i=1}^{n} x_i$`.

## Display Math

```{math}
:label: eq-einstein

E = m c^2
```

See Equation {ref}`eq-einstein` for the famous relation.

## Multi-line Equations

```{math}
:label: eq-extended

\nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
```

Equations {ref}`eq-extended` are Maxwell's equations in differential form.

## Math with References

The impedance of free space is:

```{math}
:label: eq-impedance

Z_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 377 \, \Omega
```

Where $Z_0$ is defined in {ref}`eq-impedance`.

## Bibliography

To add citations, create a `bibliography.bib` file in `docs/source/`:

```bibtex
@book{gosling2015python,
  title={Python Network Programming},
  author={Gosling, J.},
  year={2015},
  publisher={O'Reilly Media}
}

@manual{nornir-docs,
  title={Nornir Documentation},
  author={Dieter, M.},
  year={2024},
  url={https://nornir.readthedocs.io}
}
```

Then reference them in your documents:

```{bibliography}
:bibliography: bibliography.bib
```

## Citing Sources

According to Gosling (2015) {cite}`gosling2015python`, network automation
has transformed operations. The Nornir framework {cite}`nornir-docs` provides
a robust foundation for orchestration.

## Citation Edge Cases

### Empty Citation Key

```{note}
The following citation key does not exist and will generate a warning:

{cite}`nonexistent-key`
```

Sphinx emits:

```
WARNING: Citation 'nonexistent-key' is not referenced. [ref.citation]
```

### Multiple Citations

```{note}
Multiple citations work: {cite}`gosling2015python, nornir-docs`
```

### Citation with Numbers

```{note}
Superscript citations: {cite:t}`gosling2015python` or {cite:np}`gosling2015python`
```

## Math in Tables

| Symbol          | Meaning                    | Value                       |
| --------------- | -------------------------- | --------------------------- |
| $c$             | Speed of light             | $3 \times 10^8$ m/s         |
| $\varepsilon_0$ | Permittivity of free space | $8.854 \times 10^{-12}$ F/m |
| $\mu_0$         | Permeability of free space | $4\pi \times 10^{-7}$ H/m   |

## LaTeX Commands in Math

```{math}
\mathcal{H} = \hbar \omega \left(a^\dagger a + \frac{1}{2}\right)
```

The Hamiltonian $\mathcal{H}$ for a quantum harmonic oscillator.

## Special Characters in Math Mode

```{math}
\% \& \# \$ \{ \} \_ \textless \textgreater
```

Math mode handles special characters differently than text mode.

## Footnotes

This is a sentence with a footnote.{^}`fn1`

[^fn1]: This is the footnote text. Footnotes appear at the bottom of pages in PDF builds.

Another sentence with multiple footnotes.{^}`fn2`{^}`fn3`

[^fn2]: Second footnote.

[^fn3]: Third footnote, which can contain **bold**, _italic_, and `code`.
