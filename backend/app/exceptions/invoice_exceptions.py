class InvoiceException(Exception):
    """Base invoice exception."""


class InvoiceNotFoundException(InvoiceException):
    pass