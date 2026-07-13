from sqlalchemy.orm import Session
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
        return self.db.query(Invoice).all()
    
    def get(self, invoice_id: int):
        return self.db.query(Invoice).filter(
            Invoice.id == invoice_id
        ).first()
    
    def delete(self, invoice):
        self.db.delete(invoice)
        self.db.commit()