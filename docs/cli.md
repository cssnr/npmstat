---
icon: lucide/square-terminal
---

# :lucide-square-terminal: Command Line Interface

To use run `npmstat` from your command line.

```shell
npmstat [COMMAND] [PACKAGE] [OPTIONS]  # (1)!
```

1.  View the [commands](#commands) and options below.

Example, get package stats for `@cssnr/vitepress-swiper`.

```shell
npmstat stats @cssnr/vitepress-swiper
```

To see the help use the `[COMMAND] -h` flag.

??? abstract "Global Help Output: `npmstat -h`"

    ```text
    usage: npmstat [-h] [-C] [-V] [command] ...

    example: npmstat stats @cssnr/vitepress-swiper

    positional arguments:
      [command]
        info             get package info
        stats            get download stats

    options:
      -h, --help         show this help message and exit
      -C, --clear-cache  clear the request cache and exit
      -V, --version      show the package version and exit
    ```

!!! quote "Output Format"

    Currently all output is in **JSON** format and can be piped directly into `jq`.

## Commands

Currently, there are 2 available commands, [info](#info) and [stats](#stats).

You can also view the [Examples](#examples) below.

### info

Get package information. Without a `version` all versions are returned.

```text
usage: npmstat info [-h] [-i N] [-p] [-f] [-v] package [version]

positional arguments:
  package            Package name
  version            Package version

options:
  -h, --help         show this help message and exit

global options:
  -i, --indent N     indent level of json, default: 2
  -p, --purge        purge cache for this request
  -f, --force-purge  force purge for this request
  -v, --verbose      enable verbose command output
```

### stats

Get package stats for a `period`. The default is `last-day`.

```text
usage: npmstat stats [-h] [-i N] [-p] [-f] [-v] [-r] package [period]

positional arguments:
  package            Package name
  period             Stats period

options:
  -h, --help         show this help message and exit
  -r, --range        show a range vs cumulative

global options:
  -i, --indent N     indent level of json, default: 2
  -p, --purge        purge cache for this request
  -f, --force-purge  force purge for this request
  -v, --verbose      enable verbose command output
```

**Period Options**

To print individual stats for each day use the `-r` flag.

| period                  | description |
| :---------------------- | :---------- |
| `last-day`              | Last Day    |
| `last-week`             | Last Week   |
| `last-month`            | Last Month  |
| `2025-01-21`            | Single Day  |
| `2025-01-14:2023-02-21` | Date Range  |

Reference: https://github.com/npm/registry/blob/main/docs/download-counts.md

## Examples

??? abstract "`npmstat stats -v @cssnr/vitepress-swiper last-week`"

    ```shell
    npmstat stats -v @cssnr/vitepress-swiper last-week
    ```

    ```shell
    package: @cssnr/vitepress-swiper
    period: last-week
    range: False
    url: https://api.npmjs.org/downloads/point/last-week/@cssnr/vitepress-swiper
    from_cache: True
    {
      "downloads": 752,
      "start": "2025-11-28",
      "end": "2025-12-04",
      "package": "@cssnr/vitepress-swiper"
    }
    ```

??? abstract "`npmstat stats -v @cssnr/vitepress-swiper last-week -r`"

    ```shell
    npmstat stats -v @cssnr/vitepress-swiper last-week -r
    ```

    ```shell
    package: @cssnr/vitepress-swiper
    period: last-week
    range: True
    url: https://api.npmjs.org/downloads/range/last-week/@cssnr/vitepress-swiper
    from_cache: True
    {
      "start": "2025-11-28",
      "end": "2025-12-04",
      "package": "@cssnr/vitepress-swiper",
      "downloads": [
        {
          "downloads": 186,
          "day": "2025-11-28"
        },
        {
          "downloads": 6,
          "day": "2025-11-29"
        },
        {
          "downloads": 15,
          "day": "2025-11-30"
        },
        {
          "downloads": 109,
          "day": "2025-12-01"
        },
        {
          "downloads": 261,
          "day": "2025-12-02"
        },
        {
          "downloads": 118,
          "day": "2025-12-03"
        },
        {
          "downloads": 57,
          "day": "2025-12-04"
        }
      ]
    }
    ```

## Autocomplete :lucide-flask-conical:{ title="Experimental Feature" }

Supports tab auto-complete when using the CLI.

After [installing](index.md#install) run.

```shell
activate-global-python-argcomplete
```

Reference: https://kislyuk.github.io/argcomplete/#activating-global-completion

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
