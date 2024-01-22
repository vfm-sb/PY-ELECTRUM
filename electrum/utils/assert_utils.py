# Built-in Modules
from typing import Any

# Exceptions
from electrum.exceptions import MissingInputError


def assert_input(user_input: Any) -> None:
    if not user_input:
        raise MissingInputError
