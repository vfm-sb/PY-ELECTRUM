"""Custom Input Exceptions"""


class MissingInputError(ValueError):
    def __init__(self, message: str = "Missing Input") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidInputTypeError(ValueError):
    def __init__(self, input_type: str | None = None) -> None:
        self.message = "Invalid Input Type"
        if input_type:
            self.message += f' >> "{input_type}"'
        super().__init__(self.message)


class InvalidNumericInputError(ValueError):
    def __init__(self, message: str = "Invalid Numeric Input", input_string: str | None = None) -> None:
        self.message = message
        if input_string:
            self.message += f' >> "{input_string}"'
        super().__init__(self.message)
