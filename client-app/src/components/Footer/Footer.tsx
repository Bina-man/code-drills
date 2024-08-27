import React from 'react';
import styles from './Footer.module.css'; // Ensure this import is present

const Footer: React.FC = () => {
  return (
    <footer className={styles.footer}>
      <p>&copy; 2024 Binyam. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
