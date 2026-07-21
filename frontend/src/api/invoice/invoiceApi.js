import client from "../client";

export function getInvoices() {
    return client.get("/invoices");
}

export function getInvoice(id) {
    return client.get(`/invoices/${id}`);
}

export function deleteInvoice(id){
    return client.delete(`/invoices/${id}`);
}