// src/components/OrganizationHeader.tsx
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Updated to use useNavigate instead of useHistory

interface OrganizationHeaderProps {
  organizationName: string;
  reportDate: string;
}

const OrganizationHeader: React.FC<OrganizationHeaderProps> = ({ organizationName, reportDate }) => {
  const navigate = useNavigate();
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    return () => clearInterval(timer); // Cleanup the interval on component unmount
  }, []);

  const handleLogoClick = () => {
    navigate('/'); // Redirect to the home page
  };

  return (
    <header style={{ 
      display: 'flex', 
      justifyContent: 'space-between', 
      alignItems: 'center', 
      padding: '10px 50px', 
      backgroundColor: '#2C3E50',
      color: '#ECF0F1',
      position: 'fixed',
      top: 0,           
      left: 0,
      width: '100%',    
      zIndex: 1000,
      boxShadow: '0 2px 10px rgba(0, 0, 0, 0.2)',
    }}>
      <div style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }} onClick={handleLogoClick}>
        <img 
          src="https://media.giphy.com/media/Rlwz4m0aHgXH13jyrE/giphy.gif" 
          alt="Organization Logo" 
          style={{ width: '50px', height: '50px', marginRight: '15px' }} 
        />
        <h1 style={{ margin: 0, fontSize: '24px', fontWeight: '600' }}>{organizationName || 'Organization Name'}</h1>
      </div>

      
      {/* Center: Report Date */}
      <div style={{ flexGrow: 1, textAlign: 'center' }}>
        <p style={{ margin: 0, fontSize: '18px', fontWeight: '500' }}>
          {currentTime.toLocaleTimeString()} {/* Display the current time */}
        </p>
      </div>

      {/* Right Side: Login/Logout Button */}
      <div>
        <button style={{
          backgroundColor: '#E74C3C',
          color: '#fff',
          border: 'none',
          borderRadius: '4px',
          padding: '8px 16px',
          fontSize: '14px',
          cursor: 'pointer',
          marginRight:'90px',
          transition: 'background-color 0.3s ease',
        }}
        onMouseOver={(e) => (e.currentTarget.style.backgroundColor = '#C0392B')}
        onMouseOut={(e) => (e.currentTarget.style.backgroundColor = '#E74C3C')}
        >
          Login/Logout
        </button>
      </div>
    </header>
  );
};

export default OrganizationHeader;
