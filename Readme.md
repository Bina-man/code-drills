# Show Me The Money

The goal of this project is to build a simple one-page application to display the Balance Sheet Report from [Xero](https://www.xero.com/au/).

## Project Overview

This application is designed to fetch and present the Balance Sheet Report by leveraging data from Xero's API. The project comprises a backend service that communicates with a local API, which in turn interacts with a locally deployed Docker container to retrieve the data. The frontend application then takes this data and displays it in a user-friendly manner.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following software installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Node.js](https://nodejs.org/) (for client-side development)

### Installation

1. **Load the mock data to check locally:**

    ```bash
    $ docker pull jaypeng2015/show-me-the-money
    
    $ docker run -d -p 3000:3000 jaypeng2015/show-me-the-money
    ```


2. **Clone the repository:**

   ```bash
    $ git clone https://github.com/Bina-man/code-drills
    
    $ cd code-drills

    $ docker-compose up --build
    ```


3. **Local url:**

   http://localhost:300/


## Technology Stack
    Backend:
        Python
        Flask
        Xero API
    Frontend:
        JavaScript
        React
        React Router
        Axios
    Containerization:
        Docker
    CICD    
        Github actions
## Future Enhancements
    - Implement authentication and authorization for secure access to Xero data
    - Add support for additional Xero reports (e.g., Profit and Loss, Cash Flow)
    - Improve data visualization with charts and graphs
    - Implement export functionality (e.g., PDF, CSV)
## Contact
    For any inquiries or questions, feel free to reach out to binasisayet8790@gmail.com.