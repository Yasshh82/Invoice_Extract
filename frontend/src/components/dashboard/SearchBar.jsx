import { Input } from "../ui/input";

export default function SearchBar({ value, onChange }) {
    return (
        <Input
            placeholder="Search invoices..."
            value={value}
            onChange={(event) => onChange(event.target.value)}
        />
    );
}