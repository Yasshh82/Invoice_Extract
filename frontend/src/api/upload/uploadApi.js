import client from "../client";

export function uploadInvoice(file, config) {

    const form = new FormData();

    form.append("file", file);

    return client.post("/upload", form, config);
}

export function uploadBulk(files, config) {
    const form = new FormData();

    files.forEach((file) => {
        form.append("files", file)
    });

    return client.post("/upload/bulk", form, config);
}