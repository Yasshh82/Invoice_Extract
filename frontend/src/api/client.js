import axios from "axios";

const client = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    timeout:30000,
});

client.interceptors.request.use(
    (config) => {
        // Future authentication support
        // const token = localStorage.getItem("token");
        // if (token) {
        //     config.headers.Authorization = `Bearer ${token}`;
        // }

        return config;
    },
    (error) => Promise.reject(error)
);

client.interceptors.response.use(
    (response) => response,
    (error) => {
        return Promise.reject(normalizeError(error));
    }
);

function normalizeError(error){
    return {
        status: error.response?.status,
        message: error.response?.data?.detail || error.message || "Unexpected error.",
    };
}

export default client;