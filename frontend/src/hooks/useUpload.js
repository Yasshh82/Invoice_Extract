import { useState } from "react";
import { useQueryClient } from "@tanstack/react-query";
import toast from "react-hot-toast";

import { uploadBulk } from "../api/invoiceApi";

export default function useUpload() {
    const [loading, setLoading] = useState(false);
    const [progress, setProgress] = useState(0);
    const queryClient = useQueryClient();

    async function upload(files) {
        if(files.length === 0){
            toast.error("Please select files");
            return;
        }

        try{
            setLoading(true);
            setProgress(0);
            await uploadBulk(files, {onUploadProgress:(event) => {
                const percent = Math.round((event.loaded * 100)/event.total);
                setProgress(percent);
            },});

            toast.success("Upload successful.");

            queryClient.invalidateQueries({
                queryKey: ["invoices",],
            });
        } catch {
            toast.error("Upload failed.");
        } finally {
            setLoading(false);
            setProgress(0);
        }
    }

    return { upload, loading, progress };
}