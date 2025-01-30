Automated Booking Bot Documentation

Overview

This script automates the booking process on Ginnipal Cus Cosenza using Selenium and Schedule. It logs in with predefined credentials and books a slot for the next day at a specified time.


---

Requirements

1. Install Dependencies

Ensure you have Python installed, then install the required packages:

`pip install selenium schedule`

2. ChromeDriver Setup

Download and install ChromeDriver from here and ensure it matches your Chrome version. Place the driver in your system PATH or specify its location in the script.


---

How It Works

1. Credentials Storage

User credentials are stored in a dictionary:

credentials = {
    "lunedi": [[], ["test", "test"]],
    "martedi": [[]],
    "mercoledi": [[]],
    "giovedi": [[]],
    "venerdi": [[]],
}

Each entry corresponds to a day of the week, containing email-password pairs.

2. Booking Function (prenota)

Opens the Ginnipal Cus Cosenza website.

Logs in with the provided credentials.

Navigates to the booking section.

Selects the next day's date and time slot (14:00 - 16:00).

Confirms the reservation.


3. Scheduled Execution (schedule)

The script runs every day at 00:00, making reservations for the following day.
Example schedule:

schedule.every().sunday.at("00:00").do(prenota_per_giorno, "lunedi")

Each scheduled job calls prenota_per_giorno, which loops through stored credentials and calls prenota.


---

Usage

1. Run the script:



`python script.py`

2. The bot will run continuously and book slots automatically.




---

Error Handling

Uses try-except to catch Selenium exceptions.

If an error occurs, it prints the exception and ensures the WebDriver closes properly.



---

Customization

Modify credentials to add or remove users.

Change the booking time by updating the XPath:


`select_element = driver.find_element(By.XPATH, "//*[contains(text(),'14:00 - 16:00')]").click()`

Adjust the scheduling time by modifying schedule.every().sunday.at("00:00").



---

Notes

Ensure credentials are correct.

The script must be running for the automation to work.

If the website structure changes, update the By.ID and By.XPATH locators.



---

Author:
Zeta
Date: 30 Jan 2025

