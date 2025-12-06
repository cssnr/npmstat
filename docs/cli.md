---
icon: lucide/square-terminal
---

# :lucide-square-terminal: Command Line Interface

To use run `npmstat` from your command line.

```shell
npmstat package [GLOBAL-OPTS] [COMMAND] [CMD-OPTS]
```

Example, get package stats for `@cssnr/vitepress-swiper`.

```shell
npmstat @cssnr/vitepress-swiper stats
```

Global options, see `npmsta -h`.

```text
usage: npmstat [-h] [-i N] [-v] [-C] [-V] [package] {info,stats} ...

NPM Stat

positional arguments:
  package            Package name
  {info,stats}
    info             get detailed package info
    stats            get package download stats

options:
  -h, --help         show this help message and exit
  -i N, --indent N   indent level of json, default: 2
  -v, --verbose      enable verbose command output
  -C, --clear-cache  clear the request cache and exit
  -V, --version      show the package version and exit
```

## Commands

Currently, there are 2 available commands, [info](#info) and [stats](#stats).

### info

Get package information. Without a `version` all versions are returned.

```text
usage: npmstat package info [-h] [version]

positional arguments:
  version     Package version

options:
  -h, --help  show this help message and exit
```

### stats

Get package stats for a `period`. The default is `last-day`.

```text
usage: npmstat package stats [-h] [-r] [period]

positional arguments:
  period       Package name

options:
  -h, --help   show this help message and exit
  -r, --range  show a range vs cumulative
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

## Autocomplete :lucide-flask-conical:{ title="Experimental Feature" }

Supports tab auto-complete when using the CLI.

After [installing](index.md#install) run.

```shell
activate-global-python-argcomplete
```

Reference: https://kislyuk.github.io/argcomplete/#activating-global-completion

## Examples

??? abstract "`npmstat -v @cssnr/vitepress-swiper stats last-week`"

    ```shell
    npmstat -v @cssnr/vitepress-swiper stats last-week
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

??? abstract "`npmstat -v @cssnr/vitepress-swiper stats last-week -r`"

    ```shell
    npmstat -v @cssnr/vitepress-swiper stats last-week -r
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

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
