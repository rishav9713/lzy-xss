# -----------------------------------------------
# Created by: @LZY_XD, @LAZY_ROBO @rishav9713
# -----------------------------------------------
# All rights reserved.
# provide proper credits whenever you use this script
# -----------------------------------------------
# for reference you will find the guidance with scripts
# -----------------------------------------------


import requests
from bs4 import BeautifulSoup
import os
from colorama import init, Fore
import subprocess
import importlib.util


# Check if a module is installed
def check_module(module_name):
    return importlib.util.find_spec(module_name) is not None

# Check if the required libraries are installed
def check_dependencies():
    dependencies = ['requests', 'bs4', 'colorama']

    missing_dependencies = []
    installed_dependencies = []

    for dependency in dependencies:
        if check_module(dependency):
            installed_dependencies.append(dependency)
        else:
            missing_dependencies.append(dependency)

    if missing_dependencies:
        print(f'The following libraries are not installed: {", ".join(missing_dependencies)}')
        print('Installing missing libraries...')
        install_dependencies(missing_dependencies)

    print(f'All required libraries ({", ".join(installed_dependencies)}) are installed. \n Set to go for launch.')

# Install missing dependencies using pip
def install_dependencies(dependencies):
    subprocess.check_call(['pip', 'install'] + dependencies)


# Check if the required libraries are installed
check_dependencies()



# ----------------------------------------------------
# Rest of the Code

# Initialize colorama
init(autoreset=True)

# Function to check if XSS vulnerability exists in a given URL
def check_xss(url):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')

        if not forms:
            print('No forms found on the webpage.')
            return

        print(f'Found {len(forms)} form(s) on the webpage.')

        # Load payloads from file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        payloads_file = os.path.join(current_dir, 'payloads.txt')

        with open(payloads_file, 'r') as f:
            payloads = f.read().splitlines()

        # Loop through each form
        for form in forms:
            print('---')
            print(f'Checking form: {form}')

            # Get the form action URL
            form_action = form.get('action')
            if not form_action:
                form_action = url

            # Get the form inputs and their values
            form_data = {}
            inputs = form.find_all('input')

            for input_tag in inputs:
                if 'name' in input_tag.attrs:
                    input_name = input_tag['name']
                    input_value = input_tag.get('value', '')
                    form_data[input_name] = input_value

            if not form_data:
                print('No input fields found in the form.')
                continue

            print(f'Found {len(form_data)} input field(s) in the form.')

            # Iterate through payloads
            for payload in payloads:
                modified_data = form_data.copy()

                # Inject payload into each form input
                for input_name in form_data.keys():
                    modified_data[input_name] = payload

                # Submit the form with modified form data
                response = requests.get(form_action, params=modified_data)

                # Check if the payload triggers an alert in the response
                if '<script>alert' in response.text:
                    print(f'{Fore.RED}Payload: {payload}')
                    print('Modified form data:', modified_data)
                else:
                    print(f'{Fore.GREEN}Payload: {payload}')
                    print('Modified form data:', modified_data)

            print('---')

        # Check payloads in the URL
        for payload in payloads:
            modified_url = url + '/' + payload

            # Send a GET request with the modified URL
            response = requests.get(modified_url)

            # Check if the payload triggers an alert in the response
            if '<script>alert' in response.text:
                print(f'{Fore.RED}Payload in URL: {payload}')
                print('Modified URL:', modified_url)
            else:
                print(f'{Fore.GREEN}Payload in URL: {payload}')
                print('Modified URL:', modified_url)

        # Check payloads in the URL for search parameter
        for payload in payloads:
            modified_url = url + '/search?keyword=' + payload

            # Send a GET request with the modified URL
            response = requests.get(modified_url)

            # Check if the payload triggers an alert in the response
            if '<script>alert' in response.text:
                print(f'{Fore.RED}Payload in URL: {payload}')
                print('Modified URL:', modified_url)
            else:
                print(f'{Fore.GREEN}Payload in URL: {payload}')
                print('Modified URL:', modified_url)



 # Check payloads in the URL for q parameter
        for payload in payloads:
            modified_url = url + '/search?q=' + payload

            # Send a GET request with the modified URL
            response = requests.get(modified_url)

            # Check if the payload triggers an alert in the response
            if '<script>alert' in response.text:
                print(f'{Fore.RED}Payload in URL: {payload}')
                print('Modified URL:', modified_url)
            else:
                print(f'{Fore.GREEN}Payload in URL: {payload}')
                print('Modified URL:', modified_url)






    else:
        print(f'Request to {url} failed with status code {response.status_code}.')



# Function to print the LZY_XSS header banner
def print_banner():
    banner = r'''
 ___           ________       ___    ___  ___    ___  ________       ________      
|\  \         |\_____  \     |\  \  /  /||\  \  /  /||\   ____\     |\   ____\     
\ \  \         \|___/  /|    \ \  \/  / /\ \  \/  / /\ \  \___|_    \ \  \___|_    
 \ \  \            /  / /     \ \    / /  \ \    / /  \ \_____  \    \ \_____  \   
  \ \  \____      /  /_/__     \/  /  /    /     \/    \|____|\  \    \|____|\  \  
   \ \_______\   |\________\ __/  / /     /  /\   \      ____\_\  \     ____\_\  \ 
    \|_______|    \|_______||\___/ /     /__/ /\ __\    |\_________\   |\_________\
                            \|___|/      |__|/ \|__|    \|_________|   \|_________|
                                                                                   

                                                                - by LAZY_ROBO   
'''
    print(Fore.GREEN + banner)

# Print the LZY_XSS header banner
print_banner()

try:
    # Get the target URL from the user
    target_url = input('Enter the target URL (e.g. http://example.com or https://example.com): ')

    # Check the payloads file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    payloads_file = os.path.join(current_dir, 'payloads.txt')

    if not os.path.exists(payloads_file):
        print('Payloads file not found.')
        exit()

    # Check for XSS vulnerabilities
    check_xss(target_url)

except Exception as e:
    print('An error occurred:')
    print(str(e))
