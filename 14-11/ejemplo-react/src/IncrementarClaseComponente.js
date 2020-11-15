import React, { Component } from 'react'
class IncrementarClaseComponente extends Component {
    constructor(props){
        super(props);
        this.state = {
            clicks: 0,
            sePuedeMostrar: true
        }
    }
    Incrementar = () => {
        this.setState({ clicks: this.state.clicks + 1 })
    }
    Disminuir = () => {
        this.setState({ clicks: this.state.clicks - 1 })
    }
    Resetear = () => {
        this.setState({ clicks: 0 })
    }

    render() {
        return (
          <div>
            <p><b>Clicks actuales: </b> {this.state.clicks}</p>
            <button onClick={this.Incrementar}>Incrementar</button>
              <button onClick={this.Disminuir}>Disminuir</button>
              <button onClick={this.Resetear}>Resetear</button>
          </div>
        );
    }

}

export default IncrementarClaseComponente