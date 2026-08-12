import { downloadCSV, downloadJSON } from "../api/export/exportApi";
import { downloadFile } from "../utils/download";

export default function useExport(){
    async function exportCSV(){
        const response = await downloadCSV();
        downloadFile(response.data, "invoices.csv");
    }

    async function exportJSON(){
        const response = await downloadJSON();
        downloadFile(response.data, "invoices.json");
    }

    return { exportCSV, exportJSON };
}