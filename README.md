# XSS Injection Script

This program checks for XSS (Cross-Site Scripting) vulnerabilities by injecting payloads into web forms found on a target URL. It sends the payloads to the server and checks if the response contains an alert. If an alert is found, the payload is marked as vulnerable, otherwise, it is marked as not vulnerable.

## Prerequisites

- Python 3.x
- Required libraries: `requests`, `bs4`, `colorama`

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/rishav9713/lzy-xss.git

2. Navigate to the project directory:

   ```shell
   cd lzy-xss

3. Either you can Install the required libraries by following code or it will download itself:

   ```shell
   pip install -r requirements.txt

## Usage
1. Make sure you have the 'payloads.txt' file containing XSS payloads in the same directory as the program.
2. Run the program:

   ```shell
   python3 lzy-xss.py

3. Enter the target URL when prompted.
4. The program will check if the required libraries are installed. If any library is missing, it will install it automatically.
5. The program will then proceed to check for XSS vulnerabilities by injecting payloads into web forms. If a vulnerability is detected, it will be displayed in red color, otherwise, it will be displayed in green color.

## Example
Here's an example of the program in action:

   ```shell
   $ python3 lzy-xss.py
   
   Enter the target URL: https://example.com
   
   The following libraries are not installed: bs4, colorama
   Installing missing libraries...
   Collecting bs4
   ...
   Successfully installed bs4-0.0.1 colorama-0.4.4
   
   All required libraries (requests, bs4, colorama) are installed. Set to go for launch.
   
   Found 2 form(s) on the webpage.
   ---
   Checking form: <form action="/login" method="post">
   Found 2 input field(s) in the form.
   Payload: <script>alert(1)</script>
   Modified form data: {'username': '<script>alert(1)</script>', 'password': ''}
   Payload: <script>alert(2)</script>
   Modified form data: {'username': '<script>alert(2)</script>', 'password': ''}
   ---
   Checking form: <form action="/search" method="get">
   Found 1 input field(s) in the form.
   Payload: <script>alert(1)</script>
   Modified form data: {'keyword': '<script>alert(1)</script>'}
   Payload: <script>alert(2)</script>
   Modified form data: {'keyword': '<script>alert(2)</script>'}
   ---
   ```


## License ![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)
This project is licensed under the <a href="https://github.com/rishav9713/lzy-xss/blame/main/LICENSE">LZY License</a>.

