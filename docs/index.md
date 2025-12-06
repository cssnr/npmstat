---
icon: lucide/rocket
---

# :lucide-rocket: Get Started

[![NPM Stat](assets/images/logo.png){ align=right width=96 }](https://github.com/cssnr/npmstat?tab=readme-ov-file#readme)

[![PyPI Version](https://img.shields.io/pypi/v/npmstat?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/npmstat/)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Fnpmstat%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/npmstat?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/npmstat?logo=pypi&logoColor=white)](https://pypistats.org/packages/npmstat)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/npmstat?logo=pypi&logoColor=white&label=total)](https://clickpy.clickhouse.com/dashboard/npmstat)
[![Codecov](https://codecov.io/gh/cssnr/npmstat/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/npmstat)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/npmstat/test.yaml?logo=cachet&label=test)](https://github.com/cssnr/npmstat/actions/workflows/test.yaml)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/npmstat?logo=github&label=updated)](https://github.com/cssnr/npmstat/pulse)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/npmstat?logo=github)](https://github.com/cssnr/npmstat/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/npmstat?logo=github)](https://github.com/cssnr/npmstat/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/npmstat?style=flat&logo=github)](https://github.com/cssnr/npmstat/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/npmstat?style=flat&logo=github)](https://github.com/cssnr/npmstat/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

Get NPM Package Stats and Info.

Includes a [command line interface](cli.md) and a [Python module](module.md).

If you run into any issues or have any questions, [support](support.md) is available.

## Install

From PyPI: https://pypi.org/p/npmstat

=== "pip"

    ```shell
    python -m pip install npmstat
    ```

=== "uv"

    ```shell
    uv add npmstat
    ```

=== "requirements.txt"

    ``` text
    npmstat
    ```

=== "pyproject.toml"

    ``` toml
    dependencies = ["npmstat"]
    ```

From GitHub using pip.

```shell
python -m pip install git+https://github.com/cssnr/npmstat.git
```

From Source using pip.

```shell
git clone https://github.com/cssnr/npmstat.git
python -m pip install npmstat
```

Uninstall.

```shell
python -m pip uninstall npmstat
```

## Usage

- From the command line run.

```shell
npmstat stats @cssnr/vitepress-swiper
```

:lucide-square-terminal: View the [CLI Documentation](cli.md) for more details.

- Or as a Python module.

```python
from npmstat import api

downloads = api.get_downloads('@cssnr/vitepress-swiper')
print(downloads.json())
```

:fontawesome-brands-python: View the [Module Documentation](module.md) for more details.

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
