import toast from "react-hot-toast";

export function showApiError(error) {
    toast.error(error.message || "Something went wrong.");
}