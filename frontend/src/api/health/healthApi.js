import client from "../client";

export function health() {
    return client.get("/health");
}