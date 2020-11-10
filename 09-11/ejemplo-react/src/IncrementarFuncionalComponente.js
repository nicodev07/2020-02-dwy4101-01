import React, { useState } from 'react'
const IncrementarFuncionalComponente = (props) => {
    const [clicks, setClicks] = useState(0);
    const Incrementar = () => {
        setClicks(clicks + 1)
    }
    const Disminuir = () => {
        setClicks(clicks - 1)
    }
    const Resetear = () => {
        setClicks(0)
    }

    return (
        <div>
            <p><b>Clicks actuales: </b> {clicks}</p>
            <button onClick={Incrementar}>Incrementar</button>
            <button onClick={Disminuir}>Disminuir</button>
            <button onClick={Resetear}>Resetear</button>
        </div>
    );

}

export default IncrementarFuncionalComponente