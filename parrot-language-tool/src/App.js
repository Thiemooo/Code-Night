import './App.css';
import Card from './Card';
import Sidebar from './Sidebar';

function App() {
  return (
    <div className="app">
      <div className='app-left'>
        <h1> Parrot Language Tool </h1>
        <a href="https://github.com/Thiemooo/Code-Night" target = "_blank"> Hilfe </a>
        <Card />
      </div>
      <div className='app-right'>
        <Sidebar />
      </div>
    </div>
  );
}

export default App;
