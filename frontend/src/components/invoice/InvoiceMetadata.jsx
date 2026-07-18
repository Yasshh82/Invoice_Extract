import { Card } from "../ui/card";

export default function InvoiceMetadata({ invoice, }) {
    return (
        <Card className="p-6 space-y-4">
            <h2 className="text-xl font-semibold">
                Metadata
            </h2>

            <div>
                <strong>Filename:</strong>
                <p>{invoice.filename}</p>
            </div>

            <div>
                <strong>File Size:</strong>
                <p>{(invoice.file_size / 1024).toFixed(2)} KB</p>
            </div>

            <div>
                <strong>Type:</strong>
                <p>{invoice.mime_type}</p>
            </div>

            <div>
                <strong>Uploaded:</strong>
                <p>
                    {new Date(invoice.uploaded_at).toLocaleString()}
                </p>
            </div>

        </Card>
    );
}