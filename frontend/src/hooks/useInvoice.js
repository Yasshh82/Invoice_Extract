import { useQuery } from "@tanstack/react-query";

import { getInvoice } from "../api/invoiceApi";

export default function useInvoice(id) {
    return useQuery({
        queryKey: ["invoice", id],
        queryFn: async () => {
            const response = await getInvoice(id);
            return response.data;
        },

        enabled: !!id,
    });
}