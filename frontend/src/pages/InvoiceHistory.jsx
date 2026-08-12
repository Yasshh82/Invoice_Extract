import useInvoices from "../hooks/useInvoices";
import useExport from "../hooks/useExport";

import Loading from "../components/common/Loading";
import EmptyState from "../components/common/EmptyState";

import InvoiceTable from "../components/invoice/InvoiceTable";
import { Button } from "@base-ui/react/button";

export default function InvoiceHistory() {
    const { data, isLoading, isError } = useInvoices();
    const { exportCSV, exportJSON } = useExport();

    if (isLoading) {
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

            <Button onClick={exportCSV}>Export CSV</Button>
            <Button onClick={exportJSON}>Export JSON</Button>

            <InvoiceTable invoices={data} />
        </div>
    );
}