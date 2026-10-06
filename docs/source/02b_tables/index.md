# Tables {#tables-chapter}

Demonstrates table edge cases in MyST Markdown and Sphinx.

## Simple Table

| Hostname     | Platform | Vendor |
| ------------ | -------- | ------ |
| router1.corp | IOS-XE   | Cisco  |
| switch1.corp | IOS      | Cisco  |
| ftd1.corp    | FTOS     | Cisco  |

## Table with Code

| Command              | Description                | Example                             |
| -------------------- | -------------------------- | ----------------------------------- |
| `napalm.get_facts()` | Get device facts           | `{'os': 'IOS-XE', 'hostname': ...}` |
| `napalm.cli()`       | Run arbitrary CLI commands | `{'show version': 'Cisco IOS...'}`  |
| `napalm.configure()` | Deploy configuration       | `True`                              |

## Table with Admonition Inside

| Field           | Type   | Required | Default | Notes                         |
| --------------- | ------ | -------- | ------- | ----------------------------- |
| `hostname`      | `str`  | Yes      | —       | Device IP or FQDN             |
| `username`      | `str`  | Yes      | —       | Use env var, never hardcode   |
| `timeout`       | `int`  | No       | `30`    | Connection timeout in seconds |
| `optional_args` | `dict` | No       | `{}`    | Driver-specific parameters    |

> **Note:** All tables above render correctly in both HTML and PDF builds.

## Table with Unicode

| Command         | Output                                |
| --------------- | ------------------------------------- |
| `make html`     | `docs/build/html/index.html`          |
| `make latexpdf` | `docs/build/latex/<project-name>.pdf` |
| `make epub`     | `docs/build/epub/<project>.epub`      |

## Empty Table (Edge Case)

| Header 1 | Header 2 |
| -------- | -------- |
| —        | —        |

> Empty tables render as minimal structures. Avoid relying on them.

## Wide Table (PDF Wrapping)

| Parameter          | Type    | Range        | Default | Description                                            |
| ------------------ | ------- | ------------ | ------- | ------------------------------------------------------ |
| `max_concurrent`   | `int`   | `1-100`      | `10`    | Maximum concurrent device connections                  |
| `retry_count`      | `int`   | `0-5`        | `2`     | Number of retry attempts on failure                    |
| `retry_delay`      | `float` | `0.1-30.0`   | `1.0`   | Delay between retries in seconds                       |
| `timeout`          | `int`   | `5-300`      | `30`    | Connection timeout in seconds                          |
| `log_level`        | `str`   | `DEBUG       | INFO    | WARNING                                                | ERROR` | `INFO` | Logging verbosity level |
| `dry_run`          | `bool`  | `True/False` | `False` | If True, only validate changes without applying        |
| `backup_on_change` | `bool`  | `True/False` | `True`  | Automatically backup config before making changes      |
| `notify`           | `list`  | —            | `[]`    | List of notification callbacks to invoke on completion |

## Nested Tables (Invalid — Not Supported)

```{note}
Nested tables are **not supported** in MyST/Sphinx. Use separate tables instead.
```

Example of what NOT to do:

| Column 1 | Column 2    |
| -------- | ----------- |
|          | Sub-table 1 | Sub-table 2 |
|          | a           | b           |
|          | c           | d           |

Instead, use separate tables or code blocks for nested data.

## LaTeX Table Directives

For complex tables requiring LaTeX control, use Sphinx directives:

```{rst:dirname} example
.. list-table:: Device Capabilities
   :widths: 25 25 50
   :header-rows: 1

   * - Device
     - Model
     - Features
   * - CSR1000v
     - IOS-XE 16.9
     - OSPF, BGP, VPN, QoS
   * - ASR1000
     - IOS-XE 17.3
     - MPLS, Segment Routing, VXLAN
   * - NCS5500
     - IOS-XR 7.7
     - Telemetry, Automation, ALE
```
