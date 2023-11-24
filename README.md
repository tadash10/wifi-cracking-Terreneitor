# Terreneitor-wifi-cracking-
Cracking WPA and WPA2 networks without dictionary

## Overview
The script provides an educational tool for automated Wi-Fi network testing with a cracking method without a dictionary. It does so by installing the necessary tools, checking compatibility, enabling monitor mode, starting analysis,automated cleanup and performing an automatic cracking attack using Hashcat . The script is designed to provide detailed information about each step and potential errors, enhancing its educational value. The separation of concerns into different modules makes the script modular and maintainable.


## Disclaimer

This script is intended for educational purposes only. Ensure you have proper authorization before conducting any security testing. Unauthorized testing may lead to legal consequences.

## Prerequisites

- Linux distribution (Ubuntu, Arch, Kali, Parrot)
- Python 3.6 or later
- Git
- Administrative privileges for some operations (sudo)
- 
### We seriously advise you to read the manual.md. This file will have a practical and short manual how to operate this script

## Installation

### Step 1: Clone the Repository

Open a terminal and run the following command to clone the repository:

bash
git clone https://github.com/your-username/wifi-network-testing-script.git

### Step 2: Navigate to the Script Directory

cd wifi-network-testing-script

### Step 3: Run the Script
Execute the script using the following command:

bash

python main_script.py <options>

Replace <options> with the required arguments and options for the script. For example:

bash

python main_script.py ubuntu wlan0 handshake.cap wpa2 --hashcat-params="--increment"

Usage

The script provides a user-friendly menu with the following options:

    Install Tools
    Check Compatibility
    Enable Monitor Mode
    Start Wi-Fi Analysis
    Launch Cracking Attack
    Clean up and Exit

Follow the on-screen prompts and choose the desired option. Ensure to follow ethical guidelines and legal requirements while using this script.
License

This project is licensed under the MIT License.
How to Contribute

    Fork the repository to your GitHub account.
    Create a new branch for your contribution: git checkout -b feature/your-feature.
    Implement the desired feature or improvement.
    Commit your changes: git commit -m "Add your commit message".
    Push the changes to your fork: git push origin feature/your-feature.
    Create a pull request from your fork to the main repository.

Thank you for your contributions!


