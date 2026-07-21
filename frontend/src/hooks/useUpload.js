import { useState } from "react";
import { useQueryClient } from "@tanstack/react-query";
import toast from "react-hot-toast";

import { uploadBulk } from "../api";
import { showApiError } from "../utils/errorHandler";

export default function useUpload() {
    const [loading, setLoading] = useState(false);
    const [progress, setProgress] = useState(0);
    const queryClient = useQueryClient();

    async function upload(files) {
        if (files.length === 0) {
            toast.error("Please select files");
            return false;
        }

        try {
            setLoading(true);
            setProgress(0);
            await uploadBulk(files, {
                onUploadProgress(event) {
                    const percent = Math.round((event.loaded * 100) / event.total);
                    setProgress(percent);
                },
            });

            toast.success("Upload successful.");

            await queryClient.invalidateQueries({
                queryKey: ["invoices"],
            });
            
            return true;
        } catch(error) {
            showApiError(error);
            return false;
        } finally {
            setLoading(false);
            setProgress(0);
        }
    }

    return { upload, loading, progress };
}