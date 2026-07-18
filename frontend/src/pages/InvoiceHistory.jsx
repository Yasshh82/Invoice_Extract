import useInvoices from "../hooks/useInvoices";

export default function InvoiceHistory() {
    const { data, isLoading, } = useInvoices();

    if(isLoading){
        return <p>Loading...</p>;
    }

    return (
        <div>
            <h1 className="text-3xl mb-6">
                Invoice History
            </h1>
            <table className="w-full">
                <thead>
                    <tr>
                        <th>Filename</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <body>
                    {data?.map(
                        (invoice) => (
                            <tr key={invoice.id}>
                                <td>
                                    {invoice.filename}
                                </td>
                                <td>
                                    invoice.processing_status
                                </td>
                            </tr>
                        )
                    )}
                </body>
            </table>
        </div>
    );
}