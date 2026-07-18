import useInvoices from "../hooks/useInvoices";

import Loading from "../components/common/Loading";
import EmptyState from "../components/common/EmptyState";

import InvoiceTable from "../components/invoice/InvoiceTable";

export default function InvoiceHistory() {
    const { data, isLoading, isError, } = useInvoices();

    if(isLoading){
        return <Loading />;
    }

    if(isError){
        return (
            <EmptyState 
                title="Something went wrong" description="Unable to load invoices" 
            />
        );
    }

    if(!data || data.length === 0){
        return (
            <EmptyState
                title="No invoices found"
                description="Upload your first invoice to get started"
            />
        );
    }

    return (
        <div className="space-y-6">
            <h1 className="text-3xl font-bold">
                Invoice History
            </h1>

            <InvoiceTable invoices={data} />
        </div>
    );
}