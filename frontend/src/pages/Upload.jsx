import { useState } from "react";

import UploadHeader from "../components/invoice/UploadHeader";
import UploadDropzone from "../components/invoice/UploadDropzone";
import SelectedFiles from "../components/invoice/SelectedFiles";
import UploadProgress from "../components/invoice/UploadProgress";

import { Button } from "../components/ui/button";

import useUpload from "../hooks/useUpload";


export default function Upload() {
    const [files, setFiles] = useState([]);

    const { upload, loading, progress } = useUpload();

    async function handleUpload() {
        await upload(files);
        setFiles([]);
    }

    return (
        <div className="space-y-8">
            <UploadHeader />
            <UploadDropzone
                files={files}
                setFiles={setFiles}
            />

            <SelectedFiles files={files} />

            <UploadProgress progress={progress} />

            <Button 
                disabled={loading || files.length === 0}
                onClick={handleUpload}
            >
                {loading ? "Uploading..." : "Upload"}
            </Button>
            
        </div>
    );
}