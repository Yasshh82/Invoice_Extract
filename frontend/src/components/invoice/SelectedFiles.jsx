import { Card } from "../ui/card";

export default function SelectedFiles({
    files,
}){
    return (
        <Card className="p-5">
            <h2 className="font-semibold mb-4">
                Selected Files
            </h2>
            {
                files.length == 0 && (
                    <p>
                        No files selected
                    </p>
                )
            }
            {
                files.map((file) =>(
                    <div 
                        key={file.name}
                        className="py-2 border-b"
                    >
                        {file.name}
                    </div>
                ))
            }
        </Card>
    );
}