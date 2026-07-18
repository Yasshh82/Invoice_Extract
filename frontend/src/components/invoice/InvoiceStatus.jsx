import { Badge } from "../ui/badge";

export default function InvoiceStatus({ status, }){
    return (
        <Badge>{status}</Badge>
    );
}