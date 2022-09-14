class CustomPasswordException(Exception):
    """Custom exception class."""
    def __init__(self, message = "Hint: Password has 8 characters"):
        self.message = message
        super().__init__(self.message)

    def  __str__(self):
        return f"{self.message}"