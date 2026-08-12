import { useEffect, useState, useCallback } from "react";
import { getInvoices, deleteInvoice } from "../../api/invoice/invoiceApi";
import {
    Table,
    TableBody,
    TableHead,
    TableHeader,
    TableRow,
    TableCell,
} from "../ui/table";
import { Badge } from "../ui/badge";
import { Button } from "../ui/button";
import Pagination from "./Pagination";

export default function InvoiceTable() {
    const [invoices, setInvoices] = useState([]);
    const [pagination, setPagination] = useState({
        total: 0,
        page: 1,
        page_size: 10,
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const fetchInvoices = useCallback(async (page) => {
        setLoading(true);
        setError(null);
        try {
            const response = await getInvoices(page, pagination.page_size);
            const data = response.data;
            setInvoices(data.items || []);
            setPagination({
                total: data.total,
                page: data.page,
                page_size: data.page_size,
            });
        } catch (err) {
            setError("Failed to load invoices");
            console.error(err);
        } finally {
            setLoading(false);
        }
    }, [pagination.page_size]);

    useEffect(() => {
        const timer = setTimeout(() => {
            fetchInvoices(pagination.page);
        }, 0);
        return () => clearTimeout(timer);
    }, [pagination.page, fetchInvoices]);

    const handlePageChange = (newPage) => {
        setPagination((prev) => ({ ...prev, page: newPage }));
    };

    const handleDelete = async (invoiceId) => {
        if (confirm("Are you sure you want to delete this invoice?")) {
            try {
                await deleteInvoice(invoiceId);
                fetchInvoices(pagination.page);
            } catch (err) {
                console.error("Failed to delete invoice:", err);
            }
        }
    };

    const getStatusVariant = (status) => {
        switch (status?.toLowerCase()) {
            case "completed":
                return "default";
            case "processing":
                return "secondary";
            case "failed":
                return "destructive";
            case "pending":
                return "outline";
            default:
                return "outline";
        }
    };

    const formatDate = (dateString) => {
        return new Date(dateString).toLocaleDateString("en-US", {
            year: "numeric",
            month: "short",
            day: "numeric",
        });
    };

    return (
        <div className="space-y-4">
            {error && (
                <div className="text-sm text-destructive bg-destructive/10 p-3 rounded-lg">
                    {error}
                </div>
            )}

            <div className="rounded-lg border">
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead>Filename</TableHead>
                            <TableHead>Vendor</TableHead>
                            <TableHead>Status</TableHead>
                            <TableHead>Uploaded</TableHead>
                            <TableHead>Actions</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {loading ? (
                            <TableRow>
                                <TableCell colSpan="5" className="text-center py-8">
                                    Loading...
                                </TableCell>
                            </TableRow>
                        ) : invoices.length === 0 ? (
                            <TableRow>
                                <TableCell colSpan="5" className="text-center py-8 text-muted-foreground">
                                    No invoices found
                                </TableCell>
                            </TableRow>
                        ) : (
                            invoices.map((invoice) => (
                                <TableRow key={invoice.id}>
                                    <TableCell className="font-medium">{invoice.filename}</TableCell>
                                    <TableCell>
                                        {invoice.vendor_name || <span className="text-muted-foreground">—</span>}
                                    </TableCell>
                                    <TableCell>
                                        <Badge variant={getStatusVariant(invoice.processing_status)}>
                                            {invoice.processing_status || "Unknown"}
                                        </Badge>
                                    </TableCell>
                                    <TableCell>{formatDate(invoice.uploaded_at)}</TableCell>
                                    <TableCell>
                                        <div className="flex gap-2">
                                            <Button
                                                variant="outline"
                                                size="sm"
                                                onClick={() => {
                                                    // Handle view action
                                                }}
                                            >
                                                View
                                            </Button>
                                            <Button
                                                variant="destructive"
                                                size="sm"
                                                onClick={() => handleDelete(invoice.id)}
                                            >
                                                Delete
                                            </Button>
                                        </div>
                                    </TableCell>
                                </TableRow>
                            ))
                        )}
                    </TableBody>
                </Table>
            </div>

            <div className="flex justify-between items-center">
                <div className="text-sm text-muted-foreground">
                    Page {pagination.page} of {Math.ceil(pagination.total / pagination.page_size)} (
                    {pagination.total} total)
                </div>
                <Pagination
                    page={pagination.page}
                    total={pagination.total}
                    pageSize={pagination.page_size}
                    onPage={handlePageChange}
                />
            </div>
        </div>
    );
}
