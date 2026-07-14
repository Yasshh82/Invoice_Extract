import { Routes, Route } from "react-router-dom";

import Dashboard from "../pages/Dashboard";
import Upload from "../pages/Upload";
import InvoiceHistory from "../pages/InvoiceHistory";
import InvoiceDetails from "../pages/InvoiceDetails";
import NotFound from "../pages/NotFound";

import MainLayout from "../layouts/MainLayout";

export default function AppRoutes() {
    return (
        <Routes>

            <Route element={<MainLayout />}>
                <Route path="/" element={<Dashboard />} />

                <Route path="/upload" element={<Upload />} />

                <Route path="/history" element={<InvoiceHistory />} />

                <Route 
                    path="/invoice/:id" 
                    element={<InvoiceDetails />} 
                />
            </Route>

            <Route path="*" element={<NotFound />} />

        </Routes>
    );
}