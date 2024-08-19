"""Instantiate TestharnessConfig class and set default values."""

from pathlib import Path
from typing import Annotated, ClassVar

from confz import BaseConfig, ConfigSources, EnvSource
from pydantic import BeforeValidator

from .console import console

DIR = Path(__file__).parents[3].absolute()


def convert_to_boolean(value: str) -> bool:
    """Confz does not work well with Typer options. Confz requires a value for each CLI option, but Typer does not. To workaround this, for example, if --log-to-file is passed, we set the value to "True" regardless of what follows the CLI option."""
    return bool(value.lower() in ["true", "t", "1"])


ENV_BOOLEAN = Annotated[
    bool,
    BeforeValidator(convert_to_boolean),
]


class TestharnessConfig(BaseConfig):  # type: ignore [misc]
    """TestHarness Configuration."""

    # WebUI Configuration
    webui_enable: ENV_BOOLEAN = False
    webui_host: str = "127.0.0.1"
    webui_port: str = "8000"
    webui_log_level: str = "INFO"
    webui_debug: ENV_BOOLEAN = False
    webui_base_url: str = "http://127.0.0.1:8088"
    redis_password: str = ""
    redis_addr: str = "127.0.0.1:6379"
    webui_secret_key: str = ""
    webui_behind_reverse_proxy: ENV_BOOLEAN = False
    something: str = "something"

    CONFIG_SOURCES: ClassVar[ConfigSources | None] = [
        EnvSource(prefix="TESTHARNESS_", file=DIR / ".env", allow_all=True),
        EnvSource(prefix="TESTHARNESS_", file=DIR / ".env.secrets", allow_all=True),
    ]

    def __init__(self, **kwargs) -> None:  # type: ignore [no-untyped-def]  # noqa: ANN003
        """Initialize the TestharnessConfig class."""
        super().__init__(**kwargs)
        console.rule("TestHarness Configuration")
        console.log(f"{self=}")
