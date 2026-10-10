# Lab 3: System configuration and networking

## Aim

Inspect the operating system, memory, disk space, network interfaces, routes and connectivity using command-line tools.

These commands display configuration. They do not change addresses or reset adapters.

## Procedure

Run each command and record what it tells you. Output depends on the computer and network.

| Task | Linux | Windows Command Prompt | Observe |
| --- | --- | --- | --- |
| OS/kernel | `uname -sr` | `ver` | OS version |
| Host name | `hostname` | `hostname` | Computer name |
| System details | `cat /etc/os-release` | `systeminfo` | Distribution or system configuration |
| Memory | `free -h` | `systeminfo` | Total and available memory |
| Disk space | `df -h` | `dir C:\` | Available storage |
| IP interfaces | `ip -br address` | `ipconfig` | Interface state and addresses |
| Routes | `ip route` | `route print` | Default gateway |
| Local TCP/IP | `ping -c 4 127.0.0.1` | `ping -n 4 127.0.0.1` | Loopback replies |
| DNS lookup | `getent hosts example.com` | `nslookup example.com` | Resolved addresses |
| HTTPS connection | `curl -I --max-time 15 https://example.com` | `curl -I --max-time 15 https://example.com` | HTTP response headers |

On Linux these commands use common packages such as coreutils, procps, iproute2, iputils and curl. If a command is missing, note that in the record; it is not evidence of a network fault.

## Observation template

```text
Operating system:
Memory total / available:
Disk available:
Active interface:
Default gateway present: yes / no
Loopback replies: __ out of 4
DNS resolves: yes / no
HTTPS response or error:
```

Keep actual network addresses and hostnames in your local record if they identify your device. The repository deliberately includes no captured personal network configuration.

## Interpretation

1. Loopback success checks the local TCP/IP stack, not Internet access.
2. An IP address alone does not prove DNS or Internet access.
3. DNS resolution and HTTPS connectivity are separate checks.
4. Ping may be blocked even while HTTPS works.
5. A default gateway is the route normally used to reach other networks.

## Result

Use the commands to distinguish local configuration, name resolution and connectivity. Record the actual observations rather than copying example addresses.

Reference: [Microsoft Windows commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands).
