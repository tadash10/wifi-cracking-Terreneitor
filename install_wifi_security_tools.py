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

def test_wifi_with_hashcat(ssid, bssid, handshake_file):
    # Replace the placeholders with your Hashcat command parameters
    hashcat_command = f"hashcat -m 2500 -a 3 --force --outfile=result.txt " \
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

    # Replace these values with the actual SSID, BSSID, and handshake file
    wifi_ssid = "YourWiFiSSID"
    wifi_bssid = "YourWiFiBSSID"
    handshake_file_path = "path/to/your/handshake.cap"

    # Call the function to test the Wi-Fi network
    test_wifi_with_hashcat(wifi_ssid, wifi_bssid, handshake_file_path)
