from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.api.dependencies import get_invoice_service
from app.exports.service import ExportService

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)

@router.get("/csv")
def export_csv(repository=Depends(get_invoice_service)):
    invoices = repository.get_all()
    stream = ExportService().export(invoices, "csv")

    return StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": 'attachment; filename="invoices.csv"'
        }
    )

@router.get("/json")
def export_json(repository=Depends(get_invoice_service)):
    invoices = repository.get_all()

    stream = ExportService().export(invoices, "json",)

    return StreamingResponse(
        iter([stream.getvalue()]),
        media_type="application/json",
        headers={
            "Content-Disposition":
                'attachment; filename="invoices.json"'
        }
    )