import { useParams } from "react-router-dom";

import Loading from "../components/common/Loading";
import EmptyState from "../components/common/EmptyState";

import InvoiceMetadata from "../components/invoice/InvoiceMetadata";
import InvoicePreview from "../components/invoice/InvoicePreview";
import InvoiceStatus from "../components/invoice/InvoiceStatus";
import ExtractedFields from "../components/invoice/ExtractedFields";

import { Button } from "../components/ui/button";

import useInvoice from "../hooks/useInvoices";

export default function InvoiceDetails() {
    const { id, } = useParams();

    const { data, isLoading, isError, } = useInvoice(id);

    if(isLoading) return <Loading />;

    if(isError)
        return (
            <EmptyState title="Invoice not found" description="Unable to load invoice." />
        );

    return (
        <div className="space-y-6">
            <div className="flex justify-between items-center">
                <div>
                    <h1 className="text-3xl font-bold">
                        Invoice Details
                    </h1>

                    <InvoiceStatus status={data.processing_status} />
                </div>

                <Button asChild>
                    <a href={data.file_url} download>Download</a>
                </Button>
            </div>

            <div className="grid gap-6 lg:grid-cols-3">
                <div className="space-y-6">
                    <InvoiceMetadata invoice={data} />
                    <ExtractedFields />
                </div>

                <div className="lg:col-span-2">
                    <InvoicePreview invoice={data} />
                </div>
            </div>
        </div>
    );
}
