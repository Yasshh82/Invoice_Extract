import { useQuery } from "@tanstack/react-query";

import { getInvoice } from "../api";

const POLL_INTERVAL_MS = 3000;
const STOP_STATUSES = new Set(["Completed", "Failed"]);

export default function useInvoiceStatus(id) {
    return useQuery({
        queryKey: ["invoiceStatus", id],
        queryFn: async () => {
            const response = await getInvoice(id);
            return response.data;
        },
        enabled: !!id,
        refetchInterval: (data) => {
            if (!data) {
                return POLL_INTERVAL_MS;
            }

            const status = data.processing_status ?? data.status;
            return STOP_STATUSES.has(status) ? false : POLL_INTERVAL_MS;
        },
    });
}
