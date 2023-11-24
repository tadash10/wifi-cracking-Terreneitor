import subprocess
import platform

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
        # Install Hashcat on Ubuntu
        install_hashcat_ubuntu()
    elif choice == "2":
        # Install Hashcat on Arch Linux
        install_hashcat_arch()
    else:
        print("Invalid choice. Exiting.")
        exit()

    # Replace these values with the actual SSID, BSSID, and handshake file
    wifi_ssid = "YourWiFiSSID"
    wifi_bssid = "YourWiFiBSSID"
    handshake_file_path = "path/to/your/handshake.cap"

    # Call the function to test the Wi-Fi network
    test_wifi_with_hashcat(wifi_ssid, wifi_bssid, handshake_file_path)
