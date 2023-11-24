import subprocess
import platform
from tqdm import tqdm

def install_hashcat_ubuntu():
    try:
        subprocess.run("sudo apt-get update", shell=True, check=True)
        subprocess.run("sudo apt-get install -y hashcat", shell=True, check=True)
        print("Hashcat installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Hashcat on Ubuntu: {e}")

def install_hashcat_arch():
    try:
        subprocess.run("sudo pacman -Syu hashcat", shell=True, check=True)
        print("Hashcat installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Hashcat on Arch Linux: {e}")

def install_aircrack_ubuntu():
    try:
        subprocess.run("sudo apt-get install -y aircrack-ng", shell=True, check=True)
        print("Aircrack-ng installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Aircrack-ng on Ubuntu: {e}")

def check_chipset_compatibility():
    try:
        subprocess.run("airodump-ng --version", shell=True, check=True, stdout=subprocess.PIPE)
        print("Chipset is compatible with aircrack-ng.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error checking chipset compatibility: {e}")
        return False

def enable_monitor_mode(interface):
    try:
        subprocess.run(f"airmon-ng start {interface}", shell=True, check=True)
        print(f"Monitor mode enabled on {interface}.")
        return f"{interface}mon"
    except subprocess.CalledProcessError as e:
        print(f"Error enabling monitor mode: {e}")
        return None

def start_analysis(interface):
    try:
        subprocess.run(f"airodump-ng {interface}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting analysis: {e}")

def test_wifi_with_hashcat(ssid, bssid, handshake_file, hash_mode):
    # Use a progress bar to display the hash cracking progress
    progress_bar = tqdm(total=100, desc="Hash Cracking Progress", unit="%")

    # Use different hash modes for different Wi-Fi security protocols
    if hash_mode == "wpa2":
        hash_mode_option = "-m 2500"
    elif hash_mode == "wep":
        hash_mode_option = "-m 10400"
    elif hash_mode == "wpa3":
        hash_mode_option = "-m 22000"
    else:
        print("Unsupported hash mode. Exiting.")
        exit()

    hashcat_command = f"hashcat {hash_mode_option} -a 3 --force --stdout --outfile=result.txt " \
                      f"{handshake_file} ?d?d?d?d?d?d?d?d"

    try:
        # Run the Hashcat command with progress bar
        for _ in tqdm(subprocess.run(hashcat_command, shell=True, check=True, stdout=subprocess.PIPE).stdout.decode("utf-8")):
            progress_bar.update(1)

        print("\nHashcat completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Hashcat failed with error: {e}")
    finally:
        progress_bar.close()

if __name__ == "__main__":
    # Get the Linux distribution name
    distro = platform.linux_distribution()[0].lower()

    # Display menu
    print("Select your Linux distribution:")
    print("1. Ubuntu")
    print("2. Arch Linux")

    # Get user input
    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        # Install Hashcat and Aircrack-ng on Ubuntu
        install_hashcat_ubuntu()
        install_aircrack_ubuntu()
    elif choice == "2":
        # Install Hashcat on Arch Linux
        install_hashcat_arch()
    else:
        print("Invalid choice. Exiting.")
        exit()

    if not check_chipset_compatibility():
        print("Exiting script.")
        exit()

    # Replace these values with the actual wireless interface you want to use
    wireless_interface = "wlan1"

    monitor_interface = enable_monitor_mode(wireless_interface)
    if monitor_interface is None:
        print("Exiting script.")
        exit()

    start_analysis(monitor_interface)

    # Get the Wi-Fi security protocol choice from the user
    security_protocol = input("Enter the number corresponding to the Wi-Fi security protocol:\n"
                             "1. WPA2\n"
                             "2. WEP\n"
                             "3. WPA3\n")

    if security_protocol == "1":
        test_wifi_with_hashcat("YourWiFiSSID", "YourWiFiBSSID", "path/to/your/handshake.cap", "wpa2")
    elif security_protocol == "2":
        test_wifi_with_hashcat("YourWiFiSSID", "YourWiFiBSSID", "path/to/your/handshake.cap", "wep")
    elif security_protocol == "3":
        test_wifi_with_hashcat("YourWiFiSSID", "YourWiFiBSSID", "path/to/your/handshake.cap", "wpa3")
    else:
        print("Invalid choice. Exiting.")
