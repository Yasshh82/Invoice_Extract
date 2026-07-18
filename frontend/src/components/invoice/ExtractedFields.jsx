import { Card } from "../ui/card";

export default function ExtractedFields(){
    return (
        <Card className="p-6">

            <h2 className="text-xl font-semibold mb-4">
                Extracted Fields
            </h2>

            <p className="text-muted-foreground">
                OCR processing has not started yet.
            </p>
        </Card>
    );
}