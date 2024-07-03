Python Test Automation Project

Assignment Overview
This automation script is designed to perform the following tasks:

Open BestBuy.com and select the USA site.
Login to the system with a random user from the predefined list stored in a JSON file.
Skip adding a phone number if prompted.
Enter the phrase "hello" in the search bar.
Verify if all search results contain the phrase "hello kitty".
Check if the "products for" section changes on hovering between different options.

Installation
Clone this repository:

bash
Copy code
git clone https://github.com/your/repository.git
cd repository
Install the required Python dependencies:

Copy code
pip install -r requirements.txt
Usage

Ensure you have added the necessary user details in the config.json file located in the project directory.

Run the automation script under tests_scenarios/test_login
Notes
This script assumes that the Chrome WebDriver is installed and its path is set correctly.
Modify the config.json file to include additional users as needed.
Ensure proper internet connectivity and access to BestBuy.com during script execution.
