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
    Usage: npmstat [OPTIONS] COMMAND [ARGS]...

    NPM Stat CLI

    Example: npmstat -v stats @cssnr/vitepress-swiper

    ┌─ Options ──────────────────────────────────────────────────────────┐
    │ --verbose             -v        Verbose Output (jq safe).     │
    │ --version             -V        Show App Version.             │
    │ --clear-cache         -C        Clear Request Cache.          │
    │ --install-completion            Install completion for the    │
    │                                 current shell.                │
    │ --show-completion               Show completion for the       │
    │                                 current shell, to copy it or  │
    │                                 customize the installation.   │
    │ --help                -h        Show this message and exit.   │
    └─────────────────────────────────────────────────────────────────────┘
    ┌─ Commands ─────────────────────────────────────────────────────────┐
    │ info    Get Package Information.                              │
    │ stats   Get Package Download Stats.                           │
    └─────────────────────────────────────────────────────────────────────┘
    ```

To enable tab-completion follow the [Autocomplete](#autocomplete) instructions.

!!! quote "Output Format"

    Currently all output is in **JSON** format and can be piped directly into `jq`.

## Commands

Currently, there are 2 available commands, [info](#info) and [stats](#stats).

You can also view the [Examples](#examples) below.

### info

Get package information. Without a `version` all versions are returned.

```text
 Get Package Information.

┌─ Arguments ────────────────────────────────────────────────────────┐
│ *    package      TEXT       NPM Package Name. [required]     │
│      version      [VERSION]  Package Version                  │
└─────────────────────────────────────────────────────────────────────┘
┌─ Options ──────────────────────────────────────────────────────────┐
│ --indent       -i      INTEGER  JSON Indent. [default: 2]     │
│ --purge        -p               Purge Cache for Request.      │
│ --force-purge  -f               Force Purge for Request.      │
│ --help         -h               Show this message and exit.   │
└─────────────────────────────────────────────────────────────────────┘
```

!!! tip "In the terminal output is scaled and displays properly."

### stats

Get package stats for a `period`. The default is `last-day`.

```text
 Usage: npmstat stats [OPTIONS] PACKAGE [PERIOD]

 Get Package Download Stats.

┌─ Arguments ────────────────────────────────────────────────────────┐
│ *    package      TEXT      NPM Package Name. [required]      │
│      period       [PERIOD]  Stats Period. [default: last-day] │
└─────────────────────────────────────────────────────────────────────┘
┌─ Options ──────────────────────────────────────────────────────────┐
│ --range        -r               Get Range.                    │
│ --indent       -i      INTEGER  JSON Indent. [default: 2]     │
│ --purge        -p               Purge Cache for Request.      │
│ --force-purge  -f               Force Purge for Request.      │
│ --help         -h               Show this message and exit.   │
└─────────────────────────────────────────────────────────────────────┘
```

!!! tip "In the terminal output is scaled and displays properly."

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

???+ abstract "`npmstat stats -v @cssnr/vitepress-swiper last-week`"

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

??? abstract "`npmstat info @cssnr/vitepress-swiper 0.0.5 | jq '.peerDependencies'`"

    ```shell
    npmstat info @cssnr/vitepress-swiper 0.0.5 | jq '.peerDependencies'
    ```

    ```json
    {
      "vue": "^3.0.0",
      "vitepress": "^1.0.0"
    }
    ```

## Autocomplete :lucide-flask-conical:{ title="Experimental Feature" }

Shell autocomplete support is provided by [click](https://github.com/pallets/click).

After [installing](index.md#install) run the following command.

```shell
npmstat --install-completion
```

Then restart your shell.

Reference: https://click.palletsprojects.com/en/stable/shell-completion/

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
