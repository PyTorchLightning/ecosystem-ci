import os

import pytest

from actions.assistant import AssistantCLI

_PATH_DIR = os.path.dirname(__file__)
_PATH_SCRIPT = os.path.join(_PATH_DIR, "assistant.py")
_PATH_CONFIG = os.path.join(_PATH_DIR, "_config.yaml")


@pytest.mark.parametrize(
    "cmd", ["folder_repo", "contacts", "list_env", "before_commands", "prepare_env", "specify_tests"]
)
def test_assistant_commands(cmd):
    AssistantCLI().__getattribute__(cmd)(_PATH_CONFIG)
