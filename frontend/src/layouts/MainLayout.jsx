import { Outlet } from "react-router-dom";

import Navbar from "../components/layout/Navbar";
import Sidebar from "../components/layout/Sidebar";

export default function MainLayout() {
    return (
        <div className="flex h-screen">

            <Sidebar />

            <div className="flex flex-col flex-1">

                <Navbar />

                <main className="p-6 overflow-y-auto flex-1">

                    <Outlet />

                </main>
            </div>
        </div>
    );
}