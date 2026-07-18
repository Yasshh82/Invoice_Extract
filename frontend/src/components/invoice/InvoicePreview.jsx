import { Card } from "../ui/card";

export default function InvoicePreview({ invoice, }){
    const image = invoice.mime_type.startsWith("image/");

    return (
        <Card className="p-6">
            <h2 className="text-xl font-semibold mb-5">
                Preview
            </h2>
            {image ? 
                (<img src={invoice.file_url} alt={invoice.filename} className="rounded" />) : 
                (<iframe src={invoice.file_url} title="Invoice" className="w-full h-175" />)
            }
        </Card>
    );
}