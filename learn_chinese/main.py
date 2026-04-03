"""
learn_chinese/main.py — Entry points for Learn Chinese.

Sets the skill-packs directory for the engine, then launches
the appropriate pack.
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 output (handles Chinese characters, tone marks, etc.)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

_HERE = Path(__file__).parent
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", str(_HERE / "skill-packs"))

from engine.main import run, run_campaign          # noqa: E402
from engine.updater import check_and_prompt        # noqa: E402

_PACKAGE = "learn-chinese"
_PACKS_DIR = str(_HERE / "skill-packs")

_WEB = "--web" in sys.argv

CHINESE_PACKS = [
    "pinyin", "greetings", "numbers_chinese", "food_drink",
    "family", "daily_life", "travel", "culture", "colors_shapes", "weather_time", "body_health",
]


def _web(pack_name: str, port: int = 8080):
    """Launch the web interface for *pack_name*."""
    from engine.web.server import serve
    serve(pack_name, port=port, packs_dir=_PACKS_DIR)


def main_chinese():
    if _WEB:
        from engine.web.hub import serve_hub
        serve_hub(CHINESE_PACKS, port=8080, packs_dir=_PACKS_DIR)
        return
    check_and_prompt(_PACKAGE)
    run_campaign("learn_chinese")


def main_pinyin():
    if _WEB:
        _web("pinyin")
        return
    check_and_prompt(_PACKAGE)
    run("pinyin")


def main_greetings():
    if _WEB:
        _web("greetings")
        return
    check_and_prompt(_PACKAGE)
    run("greetings")


def main_numbers_chinese():
    if _WEB:
        _web("numbers_chinese")
        return
    check_and_prompt(_PACKAGE)
    run("numbers_chinese")


def main_food_drink():
    if _WEB:
        _web("food_drink")
        return
    check_and_prompt(_PACKAGE)
    run("food_drink")


def main_family():
    if _WEB:
        _web("family")
        return
    check_and_prompt(_PACKAGE)
    run("family")


def main_daily_life():
    if _WEB:
        _web("daily_life")
        return
    check_and_prompt(_PACKAGE)
    run("daily_life")


def main_travel():
    if _WEB:
        _web("travel")
        return
    check_and_prompt(_PACKAGE)
    run("travel")


def main_culture():
    if _WEB:
        _web("culture")
        return
    check_and_prompt(_PACKAGE)
    run("culture")
