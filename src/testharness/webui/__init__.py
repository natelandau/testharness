"""Webui test harness package."""

import asyncio
from pathlib import Path

from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart, render_template, request, session
from quart_session import Session

from testharness.utils import TestharnessConfig, console

template_dir = Path(__file__).parent / "templates"

app = Quart(__name__)

# Initialize the quart app
app.config["SECRET_KEY"] = TestharnessConfig().webui_secret_key


app.config["SESSION_TYPE"] = "redis"
# app.config["SESSION_REVERSE_PROXY"] = (
#     "true" if TestharnessConfig().webui_behind_reverse_proxy else "false"
# )
app.config["SESSION_REVERSE_PROXY"] = "true"
app.config["SESSION_URI"] = (
    (f"redis://:{TestharnessConfig().redis_password}@{TestharnessConfig().redis_addr}")
    if {TestharnessConfig().redis_addr}
    else f"redis://{TestharnessConfig().redis_addr}"
)
Session(app)


@app.route("/")
async def homepage() -> str:
    """Serve a static file from the root directory."""
    session["test"] = "test"
    # console.log(f"{request.headers=}")
    # console.log(f"{session=}")
    settings_object = TestharnessConfig().model_dump(mode="python")
    console.log(f"{settings_object=}")

    settings = {k: v for (k, v) in settings_object.items() if k not in ["webui_secret_key"]}

    headers = {
        k: v for (k, v) in request.headers.items() if k not in ["Accept", "Cookie", "User-Agent"]
    }

    return await render_template("index.html", settings=settings, headers=headers)


async def run_webui() -> None:
    """Run the webui."""
    console.rule("Starting WebUI")
    hypercorn_config = Config()
    hypercorn_config.bind = [f"{TestharnessConfig().webui_host}:{TestharnessConfig().webui_port}"]
    hypercorn_config.loglevel = TestharnessConfig().webui_log_level.upper()
    hypercorn_config.use_reloader = TestharnessConfig().webui_debug

    await serve(app, hypercorn_config, shutdown_trigger=lambda: asyncio.Future())
