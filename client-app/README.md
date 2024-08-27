# Balance Sheet Viewer

This project is a React application designed to view balance sheets in a user-friendly manner. It has been structured with components, hooks, and services to ensure modularity and ease of maintenance.

## Project Structure

Here's an overview of the project's structure:

```bash
├── App.css
├── App.test.tsx
├── App.tsx
├── components
│   ├── Footer
│   │   ├── Footer.module.css
│   │   └── Footer.tsx
│   ├── RenderRows
│   │   ├── RenderRows.module.css
│   │   └── RenderRows.tsx
│   └── balance-sheet
│       ├── BalanceSheetPage.tsx
│       ├── BalanceSheetTable.tsx
│       └── OrganizationHeader.tsx
├── hooks
│   └── useBalanceSheetData.ts
├── index.css
├── index.tsx
├── logo.svg
├── react-app-env.d.ts
├── reportWebVitals.ts
├── services
│   ├── api.ts
│   └── get_summary.ts
├── setupTests.ts
├── styles
│   └── balanceSheetStyles.ts
└── type.ts

```

### Components

- **Footer**: Handles the footer section of the application.
  - `Footer.module.css`: CSS module for the Footer component.
  - `Footer.tsx`: React component for the footer.

- **RenderRows**: Responsible for rendering the rows of the balance sheet dynamically.
  - `RenderRows.module.css`: CSS module for the RenderRows component.
  - `RenderRows.tsx`: React component for rendering rows within the balance sheet.

- **balance-sheet**: Contains components related to the balance sheet display.
  - `BalanceSheetPage.tsx`: The main page component that integrates all parts of the balance sheet.
  - `BalanceSheetTable.tsx`: Handles the structure and presentation of the balance sheet table.
  - `OrganizationHeader.tsx`: Displays the organization’s header with name, date, and logo.

### Hooks

- **useBalanceSheetData.ts**: Custom hook to fetch and manage balance sheet data from the API.

### Services

- **api.ts**: Contains API calls for fetching balance sheet data.
- **get_summary.ts**: Handles the logic for fetching and processing summary data for sections of the balance sheet.

### Styles

- **balanceSheetStyles.ts**: Styled-components for consistent design across balance sheet-related components.

### Type Definitions

- **type.ts**: Contains TypeScript types and interfaces used across the application.

## Available Scripts

In the project directory, you can run:

### `npm start`

 ```bash
    $ git clone https://github.com/Bina-man/code-drills
    
    $ cd code-drills/client-app
```
#### Option-1  💨 Building the Docker Image
 ```bash
    $ docker build -t balance-sheet-viewer .
    $ docker run -p 3000:3000 balance-sheet-viewer

```

#### Option-2 
 ```bash
    $ npm install 
    $ npm start
```