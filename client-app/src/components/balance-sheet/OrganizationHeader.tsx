import React, { useEffect, useState } from 'react';
import { HeaderContainer, HeaderTitle, HeaderLogo, HeaderDate, LoginLogoutButton } from '../../styles/balanceSheetStyles';

interface OrganizationHeaderProps {
  organizationName: string;
  reportDate: string;
}

const OrganizationHeader: React.FC<OrganizationHeaderProps> = ({ organizationName, reportDate }) => {
  const handleLogoClick = () => {
    window.location.href = '/';
  };
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    return () => clearInterval(timer); // Cleanup the interval on component unmount
  }, []);

  return (
    <HeaderContainer>
      <div style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }} onClick={handleLogoClick}>
        <img 
          src="https://media.giphy.com/media/Rlwz4m0aHgXH13jyrE/giphy.gif" 
          alt="Organization Logo" 
          style={{ width: '50px', height: '50px', marginRight: '15px' }} 
        />
        <HeaderTitle>{organizationName || 'Organization Name'}</HeaderTitle>
      </div>
      <div style={{ flexGrow: 1, textAlign: 'center' }}>
        <p style={{ margin: 0, fontSize: '18px', fontWeight: '500' }}>
          {currentTime.toLocaleTimeString()} {/* Display the current time */}
        </p>
      </div>
      <LoginLogoutButton>Login/Logout</LoginLogoutButton>
    </HeaderContainer>
  );
};

export default OrganizationHeader;
