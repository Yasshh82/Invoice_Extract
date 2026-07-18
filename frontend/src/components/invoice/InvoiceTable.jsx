import { Link } from "react-router-dom";

import { Button } from "../ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow, } from "../ui/table";

export default function InvoiceTable({invoices,}) {
    return (
        <Table>
            <TableHeader>
                <TableRow>
                    <TableHead>
                        Filename
                    </TableHead>
                    <TableHead>
                        Status
                    </TableHead>
                    <TableHead>
                        Uploaded At
                    </TableHead>
                    <TableHead>
                        Action
                    </TableHead>
                </TableRow>
            </TableHeader>
            
            <TableBody>
                {invoices.map((invoice) => (
                    <TableRow key={invoice.id}>
                        <TableCell>
                            {invoice.filename}
                        </TableCell>
                        <TableCell>
                            {invoice.processing_status}
                        </TableCell>
                        <TableCell>
                            {new Date(invoice.uploaded_at).toLocaleString()}
                        </TableCell>
                        <TableCell>
                            <Button asChild size="sm">
                                <Link to={`/invoice/${invoice.id}`}>
                                    View
                                </Link>
                            </Button>
                        </TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
    )
}