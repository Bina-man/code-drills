// src/components/OrganizationHeader.tsx
import React from 'react';
import { useNavigate } from 'react-router-dom'; // Updated to use useNavigate instead of useHistory

interface OrganizationHeaderProps {
  organizationName: string;
  reportDate: string;
}

const OrganizationHeader: React.FC<OrganizationHeaderProps> = ({ organizationName, reportDate }) => {
  const navigate = useNavigate();

  const handleLogoClick = () => {
    navigate('/'); // Redirect to the home page
  };

  return (
    <header style={{ 
      display: 'flex', 
      justifyContent: 'space-between', 
      alignItems: 'center', 
      padding: '10px 50px', 
      backgroundColor: '#2C3E50', // Keeping the dark professional color
      color: '#ECF0F1', // Matching text color for better contrast
      position: 'fixed',
      top: 0,           
      left: 0,
      width: '100%',    
      zIndex: 1000,
      boxShadow: '0 2px 10px rgba(0, 0, 0, 0.2)',
    }}>
      {/* Left Side: Organization Name and Logo */}
      <div style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }} onClick={handleLogoClick}>
        <img 
          src="/client-app/public/logo512.png" 
          alt="Organization Logo" 
          style={{ width: '50px', height: '50px', marginRight: '15px' }} 
        />
        <h1 style={{ margin: 0, fontSize: '24px', fontWeight: '600' }}>{organizationName || 'Organization Name'}</h1>
      </div>
      
      {/* Center: Report Date */}
      <div style={{ flexGrow: 1, textAlign: 'center' }}>
        <p style={{ margin: 0, fontSize: '18px', fontWeight: '500' }}>{reportDate || 'As at Date'}</p>
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
