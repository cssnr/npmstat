---
icon: lucide/rocket
---

# :lucide-rocket: Get Started

[![NPM Stat](assets/images/logo.png){ align=right width=96 }](https://github.com/cssnr/npmstat?tab=readme-ov-file#readme)

[![PyPI Version](https://img.shields.io/pypi/v/npmstat?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/npmstat/)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Fnpmstat%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/npmstat?tab=readme-ov-file#readme)
[![GitHub Downloads](https://img.shields.io/github/downloads/cssnr/npmstat/total?logo=github&label=downloads)](https://github.com/cssnr/npmstat/releases/latest)
[![PyPI Downloads](https://img.shields.io/pypi/dm/npmstat?logo=socialblade&logoColor=white)](https://pypistats.org/packages/npmstat)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/npmstat?logo=rolldown&logoColor=white&label=total)](https://clickpy.clickhouse.com/dashboard/npmstat)
[![Codecov](https://codecov.io/gh/cssnr/npmstat/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/npmstat)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/npmstat/test.yaml?logo=cachet&label=test)](https://github.com/cssnr/npmstat/actions/workflows/test.yaml)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/npmstat?logo=listenhub&label=updated)](https://github.com/cssnr/npmstat/pulse)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/npmstat?logo=southwestairlines)](https://github.com/cssnr/npmstat/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/npmstat?logo=codeforces&logoColor=white)](https://github.com/cssnr/npmstat/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/npmstat?logo=theconversation)](https://github.com/cssnr/npmstat/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/npmstat?style=flat&logo=forgejo&logoColor=white)](https://github.com/cssnr/npmstat/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/npmstat?style=flat&logo=gleam&logoColor=white)](https://github.com/cssnr/npmstat/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=apachespark&logoColor=white&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

Get NPM Package Stats and Info from the [command line](cli.md) or as a [Python module](module.md).

If you run into any issues or have any questions, [support](support.md) is available.

## Install

Using [PyPI :lucide-arrow-up-right:](https://pypi.org/project/npmstat),
with [Homebrew :lucide-arrow-up-right:](https://github.com/cssnr/homebrew-tap?tab=readme-ov-file#readme),
or from [GitHub :lucide-arrow-up-right:](https://github.com/cssnr/npmstat/releases/latest).

--8<-- "docs/snippets/install.md"

Upgrade.

=== "pip"

    ```shell
    pip install -U npmstat
    ```

=== "uv"

    ```shell
    uv tool upgrade npmstat
    ```

=== "brew"

    ```shell
    brew update && brew install  npmstat
    ```

=== "github"

    ```shell
    curl https://i.jpillora.com/cssnr/npmstat! | bash  # (1)!
    ```

    1.  To upgrade, install the [latest release :lucide-arrow-up-right:](https://github.com/cssnr/npmstat/releases).

Uninstall.

=== "pip"

    ```shell
    pip uninstall npmstat
    ```

=== "uv"

    ```shell
    uv tool uninstall npmstat
    ```

=== "brew"

    ```shell
    brew uninstall npmstat
    ```

=== "github"

    ```shell
    rm -f /usr/local/bin/npmstat  # (1)!
    ```

    1.  If you used the installation script above.

## Usage

- From the command line run `npmstat`.

```shell
npmstat stats @cssnr/vitepress-swiper
```

:lucide-square-terminal: View the [CLI Documentation](cli.md) for more details.

- Or as a Python module.

```python
from npmstat import api

downloads = api.get_downloads("@cssnr/vitepress-swiper")
print(downloads.json())
```

:fontawesome-brands-python: View the [Module Documentation](module.md) for more details.

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
