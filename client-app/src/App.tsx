import React from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import BalanceSheetPage from './components/balance-sheet/BalanceSheetPage';
import Footer from './components/Footer/Footer';

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
          <Route path="/balance-sheet" element={
            <div>
            <BalanceSheetPage />
          </div>
          } />
        </Routes>
        <footer className="App-footer">
          <Footer/>
        </footer>
      </div>
    </Router>
  );
};

export default App;
