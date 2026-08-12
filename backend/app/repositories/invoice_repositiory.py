from sqlalchemy.orm import Session
from sqlalchemy import desc, or_, func
from app.models.invoice import Invoice

class InvoiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, invoice):
        self.db.add(invoice)
        self.db.commit()
        self.db.refresh(invoice)
        return invoice
    
    def get_all(self):
        return self.db.query(Invoice).order_by(Invoice.uploaded_at.desc()).all()
    
    def get(self, invoice_id: int):
        return self.db.query(Invoice).filter(
            Invoice.id == invoice_id
        ).first()
    
    def update(self, invoice):
        self.db.add(invoice)
        self.db.commit()
        self.db.refresh(invoice)
        return invoice

    def delete(self, invoice):
        self.db.delete(invoice)
        self.db.commit()

    def query(self, query):
        invoices = self.db.query(Invoice)

        if query.search:
            invoices = invoices.filter(
                or_(Invoice.filename.ilike(
                    f"%{query.search}%"
                ), Invoice.vendor_name.ilike(
                    f"%{query.search}%"
                ), Invoice.invoice_number.ilike(
                    f"%{query.serch}%"
                ))
            )

        if query.status:
            invoices = invoices.filter(Invoice.processing_status == query.status)

        total = invoices.count()
        column = getattr(Invoice, query.sort_by)

        if query.descending:
            column = desc(column)

        invoices = invoices.order_by(column).offset(query.offset).limit(query.page_size).all()

        return invoices, total

    def statistics(self):
        return {
            "total": self.db.query(func.count(Invoice.id)).scalar(),
            "completed": self.db.query(func.count(Invoice.id)).filter(Invoice.processing_status == "Completed").scalar(),
            "failed": self.db.query(func.count(Invoice.id)).filter(Invoice.processing_status == "Failed").scalar()
        }