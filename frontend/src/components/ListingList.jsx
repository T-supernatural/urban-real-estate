// src/components/ListingList.jsx

import React, { useState, useEffect } from 'react';
import axios from 'axios'; // We will use axios for cleaner HTTP requests

// You may need to install axios: npm install axios

const ListingList = () => {
    const [listings, setListings] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const API_URL = 'http://127.0.0.1:8000/api/v1/listings/'; // Adjust port if necessary

    useEffect(() => {
        const fetchListings = async () => {
            try {
                // Fetch the data from your DRF endpoint
                const response = await axios.get(API_URL);
                setListings(response.data);
                setError(null);
            } catch (err) {
                console.error("Failed to fetch listings:", err);
                setError("Failed to load listings. Please check the API server.");
            } finally {
                setLoading(false);
            }
        };

        fetchListings();
    }, []); // Empty dependency array means this runs only once on mount

    if (loading) {
        return <div className="text-center p-8">Loading properties...</div>;
    }

    if (error) {
        return <div className="text-center p-8 text-red-600">Error: {error}</div>;
    }

    if (listings.length === 0) {
        return <div className="text-center p-8">No properties found.</div>;
    }

    return (
        <div className="container mx-auto p-4">
            <h2 className="text-3xl font-bold mb-6">Available Listings ({listings.length})</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {listings.map(listing => (
                    // Placeholder for the ListingCard component
                    <div key={listing.id} className="bg-white shadow-lg rounded-lg overflow-hidden border">
                        {/* TO DO: Replace this with the <ListingCard listing={listing} /> component 
                        */}
                        <div className="p-4">
                            <h3 className="text-xl font-semibold">{listing.title}</h3>
                            <p className="text-gray-700 font-bold mt-1">${listing.price}</p>
                            <p className="text-sm text-gray-500">{listing.location}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ListingList;