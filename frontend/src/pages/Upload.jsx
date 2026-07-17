import { useState } from "react";

import UploadHeader from "../components/invoice/UploadHeader";
import UploadDropzone from "../components/invoice/UploadDropzone";
import SelectedFiles from "../components/invoice/SelectedFiles";

import { Button } from "../components/ui/button";


export default function Upload() {
    const [files, setFiles] = useState([]);

    return (
        <div className="space-y-8">
            <UploadHeader />
            <UploadDropzone
                files={files}
                setFiles={setFiles}
            />

            <SelectedFiles files={files} />

            <Button>
                Upload
            </Button>
        </div>
    );
}