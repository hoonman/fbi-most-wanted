import React, { useState, useEffect } from "react";
import { fetchMostWanted, } from "./FBIService";
import type WantedPerson from "../types/fbi.types";
import Button from '@mui/material/Button';

const FBIDashboard: React.FC = () => {
    const [mostWanted, setMostWanted] = useState<WantedPerson[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<unknown>(null);

    useEffect(() => {
        const loadData = async () => {
            try {
                setLoading(true);
                const data = await fetchMostWanted(1, 5);
                setMostWanted(data.results);
                console.log("data.results: ", data.results);
            } catch (error) {
                setError(error);
                console.error("error occurred: ", error);
            } finally {
                setLoading(false);
            }
        };

        loadData();
    }, []);

    if (loading) return <div>Loading...</div>
    if (error) return <div>Error: {String(error)} </div>

    return (
        <div>
            <Button variant="contained">hello world</Button>
            {mostWanted.map((person: WantedPerson)=> (
                <div>{person.uid}</div>
            ))}
        </div>
    );
}

export default FBIDashboard;