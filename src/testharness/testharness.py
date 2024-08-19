"""TestHarness CLI."""

import os
from asyncio import run as aiorun

from testharness.utils import TestharnessConfig, console
from testharness.webui import run_webui


def app() -> None:
    """Add application documentation here."""
    console.rule("Env Vars")
    for key, value in os.environ.items():
        if key not in {"PS1", "LS_COLORS", "PATH"}:
            console.log(f"{key}: {value}")

    console.rule("Settings")
    settings_object = TestharnessConfig().model_dump(mode="python")
    console.log(f"{settings_object=}")

    console.rule("Running WebUI")
    aiorun(run_webui())


if __name__ == "__main__":
    app()
