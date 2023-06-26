# XSS Injection Check Program

This program checks for XSS (Cross-Site Scripting) vulnerabilities by injecting payloads into web forms found on a target URL. It sends the payloads to the server and checks if the response contains an alert. If an alert is found, the payload is marked as vulnerable, otherwise, it is marked as not vulnerable.

## Prerequisites

- Python 3.x
- Required libraries: `requests`, `bs4`, `colorama`

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/rishav9713/lzy-xss.git

2. Navigate to the project directory:

   cd lzy-xss
