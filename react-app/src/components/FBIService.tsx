import axios from "axios";

export const fetchMostWanted = async (page=1, pageSize=20, filters={}) => {
    const params = { page, page_size: pageSize, ...filters};
    const res = await axios.get('/api/most_wanted', { params });
    console.log("res: ", res);
    return res.data;
}

export const fetchDetails = async (id: unknown) => {
    const res = await axios.get(`/api/most_wanted/${id}`)
    return res.data
}

export const fetchStats = async () => {
    const res = await axios.get('/api/stats')
    return res.data
}

