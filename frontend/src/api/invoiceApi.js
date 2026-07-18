import api from "./axios";

export const getInvoices = () => api.get("/invoices");

export const getInvoice = (id) => api.get(`/invoices/${id}`);

export const uploadBulk = (files, config) => {
    const form = new FormData();

    files.forEach((file) => {
        form.append("files", file)
    });

    return api.post("/upload/bulk", form, config);
};

export const uploadInvoice = (file, config) => {
    const form = new FormData();

    form.append("file", file);

    return api.post("/upload", form, config);
};