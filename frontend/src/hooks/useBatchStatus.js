import { useQuery } from "@tanstack/react-query";
import api from "../api/client";

export default function useBatchStatus(batchId) {
    return useQuery({
        queryKey: ["batch", batchId],
        enabled: !!batchId,
        queryFn: async () => {
            const response = await api.get(`/batch/${batchId}`);
            return response.data;
        },
        refetchInterval: (query) => {
            const data = query.state.data;
            return data?.status === "Completed" ? false : 2000;
        },
    });
}