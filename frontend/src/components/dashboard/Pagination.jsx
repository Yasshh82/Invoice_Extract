import { Button } from "../ui/button";

export default function Pagination({ page, total, pageSize, onPage }) {

    const pages = Math.ceil(total / pageSize);

    return (
        <div className="flex gap-2">
            <Button
                disabled={page === 1}
                onClick={() => onPage(page - 1)}
            >
                Previous
            </Button>

            <Button
                disabled={page >= pages}
                onClick={() => onPage(page + 1)}
            >
                Next
            </Button>
        </div>
    );
}