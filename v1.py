import subprocess
import platform

def install_hashcat(distribution):
    try:
        if distribution == "ubuntu":
            subprocess.run("sudo apt-get update", shell=True, check=True)
            subprocess.run("sudo apt-get install -y hashcat", shell=True, check=True)
        elif distribution == "arch":
            subprocess.run("sudo pacman -Syu hashcat", shell=True, check=True)
        else:
            print("Unsupported distribution. Exiting.")
            exit()

        print("Hashcat installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Hashcat: {e}")
        exit()

def install_aircrack(distribution):
    try:
        if distribution == "ubuntu":
            subprocess.run("sudo apt-get install -y aircrack-ng", shell=True, check=True)
        elif distribution == "arch":
            subprocess.run("sudo pacman -Syu aircrack-ng", shell=True, check=True)
        else:
            print("Unsupported distribution. Exiting.")
            exit()

        print("Aircrack-ng installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Aircrack-ng: {e}")
        exit()

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

def test_wifi_with_hashcat(ssid, bssid, handshake_file):
    # Use a brute-force attack without a specific wordlist
    hashcat_command = f"hashcat -m 2500 -a 3 --force --stdout --outfile=result.txt " \
                      f"{handshake_file} ?d?d?d?d?d?d?d?d"

    try:
        # Run the Hashcat command
        subprocess.run(hashcat_command, shell=True, check=True)
        print("Hashcat completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Hashcat failed with error: {e}")

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
        install_hashcat("ubuntu")
        install_aircrack("ubuntu")
    elif choice == "2":
        # Install Hashcat and Aircrack-ng on Arch Linux
        install_hashcat("arch")
        install_aircrack("arch")
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

    # Test Wi-Fi with Hashcat (brute-force attack without a dictionary)
    test_wifi_with_hashcat("YourWiFiSSID", "YourWiFiBSSID", "path/to/your/handshake.cap")
