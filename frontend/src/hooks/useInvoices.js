import { useQuery, } from "@tanstack/react-query";

import { getInvoices } from "../api";

export default function useInvoice() {
    return useQuery({
        queryKey: ["invoices"],

        queryFn: async () => {
            const response = await getInvoices();
            return response.data;
        },
        
        staleTime: 60000,
    });
}