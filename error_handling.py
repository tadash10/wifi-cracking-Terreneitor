import subprocess
from tqdm import tqdm

def run_command(command, error_message):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{error_message}: {e}")
        exit()

def install_hashcat_ubuntu():
    command = "sudo apt-get update && sudo apt-get install -y hashcat"
    run_command(command, "Error installing Hashcat on Ubuntu")

def install_hashcat_arch():
    command = "sudo pacman -Syu hashcat"
    run_command(command, "Error installing Hashcat on Arch Linux")

def install_aircrack_ubuntu():
    command = "sudo apt-get install -y aircrack-ng"
    run_command(command, "Error installing Aircrack-ng on Ubuntu")

def install_hashcat_kali():
    command = "sudo apt-get update && sudo apt-get install -y hashcat"
    run_command(command, "Error installing Hashcat on Kali Linux")

def install_hashcat_parrot():
    command = "sudo apt-get update && sudo apt-get install -y hashcat"
    run_command(command, "Error installing Hashcat on Parrot Security OS")

def check_chipset_compatibility():
    command = "airodump-ng --version"
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
        print("Chipset is compatible with aircrack-ng.")
    except subprocess.CalledProcessError as e:
        print(f"Error checking chipset compatibility: {e}")
        exit()

def enable_monitor_mode(interface):
    command = f"airmon-ng start {interface}"
    run_command(command, f"Error enabling monitor mode on {interface}")

def start_analysis(interface):
    command = f"airodump-ng {interface}"
    run_command(command, f"Error starting analysis on {interface}")
