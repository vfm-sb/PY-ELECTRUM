"""Generic Exceptions for Py-Electrum"""


class ObjectMismatchError(TypeError):
    def __init__(
        self,
        message: str = "Objects Must Match",
        expected: object | None = None,
        received: object | None = None
    ) -> None:
        self.message = message
        if expected and received:
            expected_msg = f"Expected: {expected.__class__.__name__}"
            received_msg = f"Received: {received.__class__.__name__}"
            self.message += f" >> {expected_msg}, {received_msg}."
        super().__init__(self.message)


class InvalidOperandError(ObjectMismatchError):
    def __init__(
        self,
        message: str = "Invalid Operand Type",
        expected: object | None = None,
        received: object | None = None
    ) -> None:
        self.message = message
        super().__init__(self.message, expected, received)
