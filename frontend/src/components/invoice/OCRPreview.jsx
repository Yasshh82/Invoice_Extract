import { useMemo, useState } from "react";

import { Button } from "../ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../ui/card";

export default function OCRPreview({ invoice }) {
    const pages = useMemo(() => {
        if (!invoice?.visualization_urls?.length) {
            return [];
        }

        return invoice.visualization_urls;
    }, [invoice]);

    const [currentPage, setCurrentPage] = useState(0);
    const [zoom, setZoom] = useState(1);

    if (!pages.length) {
        return (
            <Card className="p-6">
                <h2 className="text-xl font-semibold mb-2">
                    OCR Preview
                </h2>
                <p className="text-sm text-muted-foreground">
                    Annotated OCR images will appear here once they are generated for this invoice.
                </p>
            </Card>
        );
    }

    const safePageIndex = pages.length ? Math.min(currentPage, pages.length - 1) : 0;
    const currentImage = pages[safePageIndex];

    const handlePrevious = () => {
        setCurrentPage((page) => (page > 0 ? page - 1 : 0));
    };

    const handleNext = () => {
        setCurrentPage((page) => (page < pages.length - 1 ? page + 1 : page));
    };

    const handleZoomOut = () => {
        setZoom((value) => Number(Math.max(0.75, value - 0.25).toFixed(2)));
    };

    const handleZoomIn = () => {
        setZoom((value) => Number(Math.min(2.5, value + 0.25).toFixed(2)));
    };

    return (
        <Card className="overflow-hidden">
            <CardHeader className="border-b px-6 py-4">
                <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                    <div>
                        <CardTitle className="text-lg">
                            OCR Preview
                        </CardTitle>
                        <p className="text-sm text-muted-foreground">
                            Review one annotated page at a time and compare it with the original document.
                        </p>
                    </div>

                    <div className="flex items-center gap-2">
                        <Button variant="outline" size="sm" onClick={handleZoomOut}>
                            −
                        </Button>
                        <span className="min-w-16 text-center text-sm font-medium">
                            {zoom.toFixed(2)}×
                        </span>
                        <Button variant="outline" size="sm" onClick={handleZoomIn}>
                            +
                        </Button>
                    </div>
                </div>
            </CardHeader>

            <CardContent className="p-6">
                <div className="mb-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                    <div className="flex gap-2">
                        <Button variant="outline" size="sm" onClick={handlePrevious} disabled={safePageIndex === 0}>
                            Previous
                        </Button>
                        <Button variant="outline" size="sm" onClick={handleNext} disabled={safePageIndex === pages.length - 1}>
                            Next
                        </Button>
                    </div>

                    <p className="text-sm text-muted-foreground">
                        Page {safePageIndex + 1} of {pages.length}
                    </p>
                </div>

                <div className="flex min-h-105 items-center justify-center overflow-auto rounded-lg border bg-muted/20 p-4">
                    <img
                        src={currentImage}
                        alt={`Annotated OCR page ${safePageIndex + 1}`}
                        className="max-w-full rounded-md shadow-sm"
                        style={{ transform: `scale(${zoom})`, transformOrigin: "center center" }}
                    />
                </div>
            </CardContent>
        </Card>
    );
}
