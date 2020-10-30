import logo from './logo.svg';
import './App.css';
import Planes from './Planes';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hola Mundo!
        </p>

        <Planes/>

      </header>
    </div>
  );
}

export default App;
