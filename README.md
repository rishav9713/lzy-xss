# lzy-xss


Auto XSS Injection Check Program
This Python program allows you to automatically check for XSS (Cross-Site Scripting) vulnerabilities in a target URL by injecting various payloads into the form fields and analyzing the server's response.

Prerequisites
Make sure you have the following dependencies installed:

Python 3.x
requests library
beautifulsoup4 library
colorama library
You can install the required libraries using the following command:

Copy code
pip install -r requirements.txt
Usage
Place the payloads.txt file in the same directory as the script. This file should contain one payload per line.
Run the script using the following command:
Copy code
python xss_injection_check.py
Provide the target URL when prompted.
The program will check if the required libraries are installed. If any libraries are missing, it will automatically install them.
The program will then proceed to check for XSS vulnerabilities. It will identify forms on the webpage, inject payloads into each form field, and analyze the server's response.
If a payload triggers an alert in the response, indicating a potential XSS vulnerability, it will be displayed in red color. Otherwise, non-vulnerable payloads will be displayed in green color.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

