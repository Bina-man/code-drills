import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer
      style={{
        backgroundColor: '#333',
        color: 'white',
        textAlign: 'center',
        padding: '1rem 0',
        marginTop: 'auto',
        width: '100%',
        position: 'absolute',
        bottom: 0,
        left: 0,
      }}
    >
      <p>&copy; 2024 Binyam. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
