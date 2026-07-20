class UploadException(Exception):
    """Base upload exception."""


class InvalidFileTypeException(UploadException):
    pass


class InvalidMimeTypeException(UploadException):
    pass


class FileTooLargeException(UploadException):
    pass


class FileSaveException(UploadException):
    pass