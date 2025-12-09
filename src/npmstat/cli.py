import sys
from typing import Optional

import typer
from rich import print, print_json
from typing_extensions import Annotated

from . import __doc__ as package_doc
from . import api
from ._version import __version__


app = typer.Typer(no_args_is_help=True)

state = {"verbose": False}


def vprint(*objects: str):
    if state.get("verbose"):
        print(*objects, file=sys.stderr)


def version_callback(value: bool):
    if value:
        print(package_doc, file=sys.stderr)
        print(__version__)
        raise typer.Exit()


def clear_cache_callback(value: bool):
    if value:
        api.session.cache.clear()
        print("[bold green]Cache Cleared.")
        raise typer.Exit()


@app.command()
def info(
    package: Annotated[str, typer.Argument(help="NPM Package Name")],
    version: Annotated[Optional[str], typer.Argument(help="Package Version")] = None,
    _indent: Annotated[Optional[int], typer.Option("-i", "--indent", help="JSON Indent.")] = 2,
    _purge: Annotated[Optional[bool], typer.Option("-p", "--purge", help="Purge Cache for Request.")] = False,
    _force: Annotated[Optional[bool], typer.Option("-f", "--force-purge", help="Force Purge for Request.")] = False,
):
    """Get Package Information."""
    vprint(f"package: {package}")
    vprint(f"version: {version}")
    vprint(f"_indent: {_indent}")
    vprint(f"_purge: {_purge}")
    vprint(f"_force: {_force}")
    r = api.get_package(package, version)
    vprint(f"url: {r.url}")
    vprint(f"from_cache: {r.from_cache}")
    data = r.json()
    print_json(data=data, indent=_indent or None)


@app.command()
def stats(
    package: Annotated[str, typer.Argument(help="NPM Package Name.")],
    period: Annotated[str, typer.Argument(help="Stats Period.")] = "last-day",
    _range: Annotated[bool, typer.Option("--range", "-r", help="Get Range.")] = False,
    _indent: Annotated[Optional[int], typer.Option("-i", "--indent", help="JSON Indent.")] = 2,
    _purge: Annotated[Optional[bool], typer.Option("-p", "--purge", help="Purge Cache for Request.")] = False,
    _force: Annotated[Optional[bool], typer.Option("-f", "--force-purge", help="Force Purge for Request.")] = False,
):
    """Get Package Download Stats."""
    vprint(f"package: {package}")
    vprint(f"period: {period}")
    vprint(f"_range: {_range}")
    vprint(f"_indent: {_indent}")
    vprint(f"_purge: {_purge}")
    vprint(f"_force: {_force}")
    r = api.get_downloads(package, period, get_range=_range)
    vprint(f"url: {r.url}")
    vprint(f"from_cache: {r.from_cache}")
    data = r.json()
    print_json(data=data, indent=_indent or None)


@app.callback(epilog="Docs: https://cssnr.github.io/npmstat/")
def main(
    _verbose: Annotated[Optional[bool], typer.Option("-v", "--verbose", help="Verbose Output (jq safe).")] = False,
    _version: Annotated[
        Optional[bool], typer.Option("-V", "--version", help="Show App Version.", callback=version_callback)
    ] = None,
    _cache: Annotated[
        Optional[bool], typer.Option("-C", "--clear-cache", help="Clear Request Cache.", callback=clear_cache_callback)
    ] = None,
):
    """
    NPM Stat CLI

    Example: npmstat stats @cssnr/vitepress-swiper
    """
    if _verbose:
        state["verbose"] = _verbose


if __name__ == "__main__":
    app()
