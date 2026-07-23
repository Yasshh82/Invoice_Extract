from sqlalchemy import Column, Date, DateTime, Integer, String, Numeric, func

from app.database.session import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    vendor_name = Column(String)
    invoice_number = Column(String, unique=True)
    invoice_date = Column(Date)
    gst_number = Column(String)
    total_amount = Column(Numeric(10, 2))

    processing_status = Column(
        String,
        default="Pending"
    )

    uploaded_at = Column(
        DateTime,
        server_default=func.now()
    )

    file_path = Column(String, nullable=False)

    file_size = Column(Integer)

    mime_type = Column(String)

    page_count = Column(Integer, default=0)