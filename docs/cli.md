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

    Example: npmstat -v stats @cssnr/vitepress-swiper

    ┌─ Options ────────────────────────────────────────────┐
    │ --verbose      -v        Verbose Output (jq safe).   │
    │ --version      -V        Show App Version.           │
    │ --clear-cache  -C        Clear Request Cache.        │
    │ --help         -h        Show this message and exit. │
    └──────────────────────────────────────────────────────┘
    ┌─ Commands ───────────────────────────────────────────┐
    │ info    Get Package Information.                     │
    │ stats   Get Package Download Stats.                  │
    └──────────────────────────────────────────────────────┘
    ```

To enable tab-completion follow the [Autocomplete](#autocomplete) instructions.

!!! quote "Output Format"

    Output format defaults to `table`. To use `JSON` add `--format json`.

## Commands

Currently, there are 2 available commands, [info](#info) and [stats](#stats).

You can also view the [Examples](#examples) below.

### info

Get package information. Without a `version` all versions are returned.

```text
 Usage: npmstat info [OPTIONS] PACKAGE [VERSION]

 Get Package Information.

┌─ Arguments ─────────────────────────────────────────────────────┐
│ *    package      TEXT       NPM Package Name. [required]       │
│      version      [VERSION]  Package Version                    │
└─────────────────────────────────────────────────────────────────┘
┌─ Options ───────────────────────────────────────────────────────┐
│ --format  -f      [table|json]  Output Format. [default: table] │
│ --indent  -i      INTEGER       JSON Indent. [default: 2]       │
│ --purge   -p                    Purge Cache for Request.        │
│ --help    -h                    Show this message and exit.     │
└─────────────────────────────────────────────────────────────────┘
```

!!! tip "In the terminal output is scaled and displays properly."

### stats

Get package stats for a `period`. The default is `last-day`.

```text
 Usage: npmstat stats [OPTIONS] PACKAGE [PERIOD]

 Get Package Download Stats.

┌─ Arguments ─────────────────────────────────────────────────────┐
│ *    package      TEXT      NPM Package Name. [required]        │
│      period       [PERIOD]  Stats Period. [default: last-day]   │
└─────────────────────────────────────────────────────────────────┘
┌─ Options ───────────────────────────────────────────────────────┐
│ --range   -r                    Get Range.                      │
│ --format  -f      [table|json]  Output Format. [default: table] │
│ --indent  -i      INTEGER       JSON Indent. [default: 2]       │
│ --purge   -p                    Purge Cache for Request.        │
│ --help    -h                    Show this message and exit.     │
└─────────────────────────────────────────────────────────────────┘
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

???+ abstract "`npmstat info @cssnr/vitepress-swiper`"

    ```shell
    npmstat info @cssnr/vitepress-swiper
    ```

    ```shell
                           @cssnr/vitepress-swiper
    ╭─────────────┬──────────────────────────────────────────────────────╮
    │ Key         │ Value                                                │
    ├─────────────┼──────────────────────────────────────────────────────┤
    │ Link        │ https://www.npmjs.com/package/@cssnr/vitepress-swip… │
    │ Description │ A VitePress Plugin to Easily add a SwiperJS Photo    │
    │             │ Gallery or Image Slideshow with Custom Options.      │
    │ License     │ GPL-3.0-only                                         │
    │ Homepage    │ https://vitepress-swiper.cssnr.com                   │
    │ Issues      │ https://github.com/cssnr/vitepress-swiper/issues     │
    │ Updated     │ 2025-09-23T02:27:26.786Z                             │
    │ Created     │ 2025-08-25T06:49:25.597Z                             │
    │ Latest      │ 0.2.1                                                │
    │ Versions    │ 11                                                   │
    ╰─────────────┴──────────────────────────────────────────────────────╯
    ```

??? abstract "`npmstat stats @cssnr/vitepress-plugin-contributors  last-week -r`"

    ```shell
    npmstat stats @cssnr/vitepress-plugin-contributors  last-week -r
    ```

    ```shell
    @cssnr/vitepress-plugin-contributors
    ╭────────────┬───────────╮
    │ Day        │ Downloads │
    ├────────────┼───────────┤
    │ 2025-12-21 │ 0         │
    │ 2025-12-22 │ 9         │
    │ 2025-12-23 │ 0         │
    │ 2025-12-24 │ 2         │
    │ 2025-12-25 │ 0         │
    │ 2025-12-26 │ 1         │
    │ 2025-12-27 │ 1         │
    ╰────────────┴───────────╯
    ```

??? abstract "`npmstat info @cssnr/vitepress-swiper 0.0.5 | jq '.peerDependencies'`"

    ```shell
    npmstat info @cssnr/vitepress-swiper 0.0.5 -f json | jq '.peerDependencies'
    ```

    ```json
    {
      "vue": "^3.0.0",
      "vitepress": "^1.0.0"
    }
    ```

## Autocomplete :lucide-flask-conical:{ title="Experimental Feature" }

Shell autocomplete support is provided by [Click :lucide-arrow-up-right:](https://github.com/pallets/click).

After [installing](index.md#install) run the following command.

```shell
npmstat --install-completion
```

Then restart your shell.

Reference: https://click.palletsprojects.com/en/stable/shell-completion/

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
