import client from "../client";

export function downloadCSV() {
    return client.get(
        "/export/csv",
        {responseType: "blob"}
    );
}

export function downloadJSON() {
    return client.get(
        "/export/json",
        {responseType: "blob"}
    );
}