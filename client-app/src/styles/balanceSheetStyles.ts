import styled from "styled-components";

export const HeaderContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background-color: #333333;
  color: #fff;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
`;

export const HeaderLogo = styled.img`
  width: 50px;
  height: 50px;
  margin-right: 15px;
`;

export const HeaderTitle = styled.h1`
  margin: 0;
  font-size: 24px;
  font-weight: 600;
`;

export const HeaderDate = styled.p`
  flex-grow: 1;
  text-align: center;
  margin: 0;
  font-size: 18px;
  font-weight: 500;
`;

export const LoginLogoutButton = styled.button`
  background-color: #e74c3c;
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-right: 50px;
`;

export const TableContainer = styled.div`
  flex-grow: 1;
  padding: 20px;
  background-color: #f4f4f4;
  width: 100%;
  max-width: 100%;
  border-collapse: collapse;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #e7edf8;
`;

export const StyledTable = styled.table`
  width: 100%;
  border-collapse: collapse;
  margin: 0 auto; /* Center the table */
  background-color: #e7edf8;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
`;

export const TableHeader = styled.th`
  background-color: #3f4b5b;
  color: #fff;
  padding: 10px;
  text-align: left;
  font-weight: bold;
`;

export const DataRow = styled.tr`
  &:nth-child(even) {
    background-color: #f2f2f2;
  }
`;

export const DataCell = styled.td`
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
`;


export const TableTitle = styled.h2`
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
`;
