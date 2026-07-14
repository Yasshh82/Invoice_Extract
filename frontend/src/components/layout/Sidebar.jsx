import { NavLink } from "react-router-dom";

export default function Sidebar() {
    return (
        <aside className="w-64 border-r">

            <h1 className="text-2xl font-bold p-6">
                Invoice AI
            </h1>

            <nav className="flex flex-col">
                <NavLink
                    to="/"
                    className="p-4"
                >
                    Dashboard
                </NavLink>

                <NavLink
                    to="/upload"
                    className="p-4"
                >
                    Upload
                </NavLink>

                <NavLink
                    to="/history"
                    className="p-4"
                >
                    Invoice History
                </NavLink>

            </nav>

        </aside>
    );
}