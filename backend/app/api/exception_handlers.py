from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.exceptions.invoice_exceptions import InvoiceNotFoundException
from app.exceptions.upload_exceptions import (FileSaveException, FileTooLargeException, InvalidFileTypeException, InvalidMimeTypeException)

def register_exception_handlers(app: FastAPI,):

    @app.exception_handler(InvalidFileTypeException)
    async def invalid_file_type(request, exc,):
        return JSONResponse(
            status_code=400,
            content={"details": "Unsupported file type."},
        )
    
    @app.exception_handler(InvalidMimeTypeException)
    async def invalid_mime(request, exc,):
        return JSONResponse(
            status_code=400,
            content={"details": "Invalid MIME type."},
        )
    
    @app.exception_handler(FileTooLargeException)
    async def file_large(request, exc,):
        return JSONResponse(
            status_code=413,
            content={"details": "File too large."},
        )
    
    @app.exception_handler(FileSaveException)
    async def save_error(request, exc,):
        return JSONResponse(
            status_code=500,
            content={"details": "Failed to save file."},
        )
    
    @app.exception_handler(InvoiceNotFoundException)
    async def invoice_missing(request, exc,):
        return JSONResponse(
            status_code=404,
            content={"details": "Invoice not found."},
        )