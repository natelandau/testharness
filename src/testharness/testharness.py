"""TestHarness CLI."""

from asyncio import run as aiorun

from testharness.utils import console
from testharness.webui import run_webui


def app() -> None:
    """Add application documentation here."""
    console.rule("TestHarness CLI")
    aiorun(run_webui())


if __name__ == "__main__":
    app()
