import client from "../client";

export function getInvoices(page = 1, pageSize = 10, search = null, status = null) {
    return client.get("/invoices", {
        params: {
            page,
            page_size: pageSize,
            ...(search && { search }),
            ...(status && { status }),
        },
    });
}

export function getInvoice(id) {
    return client.get(`/invoices/${id}`);
}

export function deleteInvoice(id){
    return client.delete(`/invoices/${id}`);
}

export function getStats() {
    return client.get("/invoices/stats");
}