import { FileText } from "lucide-react";

export default function EmptyState({
    title,
    description,
}) {
    return (
        <div className="flex flex-col items-center justify-center py-16 text-center">

            <FileText className="mb-4 h-12 w-12 text-muted-foreground" />

            <h2 className="text-xl font-semibold">
                {title}
            </h2>
            
            <p className="mt-2 text-muted-foreground">
                {description}
            </p>

        </div>
    )
}