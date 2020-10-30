import React, { useEffect, useState } from 'react'
import axios from 'axios'
const PlanComponent = () => {
    const [planes, setPlanes] = useState([]);

    useEffect(() => {
        axios
            .get('http://localhost:8000/planes/?format=json')
            .then((response) => setPlanes(response.data))
            .catch((error) => console.error(error));
    }, [])

    return (<ul>
        {planes.map((plan) => {
            return (<li>{plan.name}</li>)
        })}
        </ul>);
}
export default PlanComponent;