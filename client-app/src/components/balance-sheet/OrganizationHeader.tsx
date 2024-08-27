import React from 'react';
import { HeaderContainer, HeaderTitle, HeaderLogo, HeaderDate, LoginLogoutButton } from '../../styles/balanceSheetStyles';

interface OrganizationHeaderProps {
  organizationName: string;
  reportDate: string;
}

const OrganizationHeader: React.FC<OrganizationHeaderProps> = ({ organizationName, reportDate }) => {
  const handleLogoClick = () => {
    window.location.href = '/';
  };

  return (
    <HeaderContainer>
      <div style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }} onClick={handleLogoClick}>
        <HeaderLogo src="/path/to/logo512.png" alt="Organization Logo" />
        <HeaderTitle>{organizationName || 'Organization Name'}</HeaderTitle>
      </div>
      <HeaderDate>{reportDate || 'As at Date'}</HeaderDate>
      <LoginLogoutButton>Login/Logout</LoginLogoutButton>
    </HeaderContainer>
  );
};

export default OrganizationHeader;
