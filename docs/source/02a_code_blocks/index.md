# Code Blocks {#code-blocks-chapter}

Demonstrates all code block types supported by MyST and Sphinx.

## Console / Shell Prompts

The `console` directive preserves shell prompt glyphs (`➜`, `✗`, `│`, etc.):

```console
(.venv) ➜  my-book git:(main) ✗ ansible-playbook site.yml -v
PLAY [Deploy to all nodes] *****************************************************

TASK [Gathering Facts] *********************************************************
ok: [node1]
ok: [node2]

TASK [Install Python] **********************************************************
changed: [node1] => (item=python3)
changed: [node2] => (item=python3)
```

## Python Code

```python
import napalm

device = napalm.get_network_driver("ios")
ios_vxr = device(hostname="10.0.0.1", username="admin", password="secret")
ios_vxr.open()

facts = ios_vxr.get_facts()
print(f"OS: {facts['os']}")
```

## Bash Scripts

```bash
#!/bin/bash
set -euo pipefail

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build documentation
cd docs && make latexpdf && make html
```

## YAML Configuration

```yaml
---
all:
  children:
    cisco:
      hosts:
        router1:
          hostname: 10.0.0.1
          groups:
            - ios_devices
        router2:
          hostname: 10.0.0.2
      groups:
        ios_devices:
          data:
            platform: ios
            username: admin
            password: "{{ secrets.password }}"
```

## JSON Data

```json
{
  "ansible_connection": "network_cli",
  "ansible_network_os": "ios",
  "groups": ["routers", "core"],
  "ansible_become": true,
  "ansible_become_method": "enable"
}
```

## Nornir Inventory

```python
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

def show_version(task):
    result = task.run(task=netmiko_send_command, command_string="show version")
    print(f"{task.host.name}: {result[0]['result'][:100]}")

nr.run(task=show_version)
```

## Indented Code with Long Lines

Long lines wrap correctly in the PDF:

```python
def deploy_configuration(device: str, config_path: str, dry_run: bool = False) -> dict:
    """
    Deploy configuration to a network device with optional dry-run support.

    Args:
        device: Hostname or IP of the target device
        config_path: Path to the configuration file to deploy
        dry_run: If True, only validate without applying

    Returns:
        Dictionary with deployment status and any error messages
    """
    driver = napalm.get_network_driver("ios")
    net_device = driver(
        hostname=device,
        username=os.environ["NETMiko_USER"],
        password=os.environ["NETMiko_PASSWORD"],
        optional_args={"timeout": 30}
    )
    try:
        net_device.open()
        if dry_run:
            net_device.load_replace_candidate(filename=config_path)
            diffs = net_device.compare_config()
            return {"status": "dry_run", "diffs": diffs}
        else:
            net_device.replace_config(filename=config_path)
            net_device.commit_config()
            return {"status": "success"}
    finally:
        net_device.close()
```

## Unicode in Code Blocks

```console
$ echo "Café résumé naïve"
Café résumé naïve

$ ls -la /home/user/docs
total 24
drwxr-xr-x  2 user user 4096 Jun 15 10:30 .
drwxr-xr-x  5 user user 4096 Jun 15 10:30 ..
-rw-r--r--  1 user user 1234 Jun 15 10:30 README.md
-rw-r--r--  1 user user 5678 Jun 15 10:30 main.yml
```

## Empty Code Block

Some edge cases involve empty code blocks (use sparingly):

```python
# TODO: Add implementation
```

## Multi-language Tabs (MyST Tabs)

```{tabs}
.. group:: python

   .. code:: python

      import napalm
      driver = napalm.get_network_driver("ios")
      device = driver(hostname="10.0.0.1")

.. group:: ansible

   ---
   - hosts: routers
     connection: network_cli
     tasks:
       - ios_command:
           commands:
             - show version
             - show ip interface brief
```
