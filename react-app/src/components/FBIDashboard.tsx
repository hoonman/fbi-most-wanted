import React, { useState, useEffect } from "react";
import { fetchMostWanted, fetchDetails, fetchStats } from "./FBIService";

interface WantedPerson {
    additional_information?: string;
    age_max?: number;
    age_min?: number;
    age_range?: string;
    aliases?: string[];
    build?: string;
    caution?: string;
    complexion?: string;
    coordinates?: string[];
    dates_of_birth_used?: string[];
    description: string;
    details: string;
    eyes: string;
    eyes_raw: string;
    field_offices: string[];
    fiels: unknown[];
    hair: string;
    hair_raw: string;
    height_max: number;
    height_min: number;
    images: unknown[];
    languages?: string[];
    legat_names?: string[];
    locations?: string[];
    modified?: string;
    nationality?: string;
    ncic?: string;
    occuptaions: string[];
    path: string;
    pathId: string;
    person_classification: string;
    place_of_birth: string;
    possible_countries: string[];
    possible_states: string[]; 
    poster_classification: string;
    publication: string;
    race: string;
    race_raw: string;
    remarks: string;
    reward_max: number;
    reward_min: number;
    reward_text: string;
    scars_and_marks: string;
    sex: string;
    status: string;
    subjects: string[];
    suspects: string[] // 
    title: string;
    uid: string;
    url: string;
    warning_message: string;
    weight: string;
    weight_max: number;
    weight_min: number;
}

const FBIDashboard: React.FC = () => {
    const [mostWanted, setMostWanted] = useState<WantedPerson[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        const loadData = async () => {
            try {
                setLoading(true);
                const data = await fetchMostWanted(1, 5);
                setMostWanted(data.results);
                console.log("data.results: ", data.results);
            } catch (err) {
                const errorMessage = err instanceof Error ? err.message : 'An unknown error occurred';
                setError(`Failed to fetch data: ${errorMessage}`);
            } finally {
                setLoading(false);
            }
        };

        loadData();
    }, []);

    if (loading) return <div>Loading...</div>
    if (error) return <div>Error: {error} </div>

    return (
        <div>
            {mostWanted.map((person: WantedPerson)=> (
                <div>{person.uid}</div>
            ))}
        </div>
    );
}

export default FBIDashboard;