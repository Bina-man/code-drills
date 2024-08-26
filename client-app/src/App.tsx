import React from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import BalanceSheetTable from './components/BalanceSheetTable';
import './App.css';
import Footer from './components/Footer';

const Home: React.FC = () => {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    navigate('/balance-sheet');
  };

  return (
    <div>
      <header className="App-header">
        <div className="home">
          <div className="hero">
            <h1 className="hero-title">Welcome to Our Financial Dashboard</h1>
            <p className="hero-subtitle">Manage your finances with ease and precision.</p>
          </div>
        </div>
      </header>
      <main>
        <button className="cta-button" onClick={handleButtonClick}> View Balance Sheet </button>
      </main>
    </div>
  );
};

const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/balance-sheet" element={<BalanceSheetTable />} />
        </Routes>
        <footer className="App-footer">
          <Footer/>
        </footer>
      </div>
    </Router>
  );
};

export default App;
