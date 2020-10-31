import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { ListGroup } from 'react-bootstrap'

const PlanComponent = () => {
    const [planes, setPlanes] = useState([]);

    useEffect(() => {
        axios
            .get('http://localhost:8000/planes/?format=json')
            .then((response) => setPlanes(response.data))
            .catch((error) => console.error(error));
    }, [])

    const renderPlanes = (plan) => {
        return (<ListGroup.Item>{plan.name}</ListGroup.Item>)
    }
    
    return (
        <ListGroup>
            {planes.map(renderPlanes)}
        </ListGroup>
    );
}
export default PlanComponent;