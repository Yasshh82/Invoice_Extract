import { UploadCloud } from "lucide-react";
import { useDropzone } from "react-dropzone";

import { Card } from "../ui/card";

const ACCEPTED_FILES = {
    "application/pdf": [".pdf"],
    "image/png": [".png"],
    "image/jpeg": [".jpg", ".jpeg"],
}

export default function UploadDropzone({
    files,
    setFiles,
}) {
    const onDrop = (acceptedFiles) => {
        setFiles((prev) => [
            ...prev,
            ...acceptedFiles,
        ]);
    };

    const {
        getRootProps,
        getInputProps,
        isDragActive,
    } = useDropzone({
        onDrop,
        multiple: true,
        accept: ACCEPTED_FILES,
    });

    return (
        <Card
            {...getRootProps()}
            className={`
                p-10
                cursor-pointer
                border-2
                border-dashed
                text-center
                transition

                ${
                    isDragActive ? "border-blue-500" : ""
                }
            `}
        >
            <input {...getInputProps()} />
            <UploadCloud 
                size={50}
                className="mx-auto mb-5"
            />

            <h2 className="text-lg font-semibold">
                Drag & Drop invoices here
            </h2>

            <p className="text-muted-foreground mt-2">
                or click to browse
            </p>

            <p className="mt-4 text-sm">
                {files.length} file(s) selected
            </p>

        </Card>
    );
}