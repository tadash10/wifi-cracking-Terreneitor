import subprocess
import platform
from tqdm import tqdm
import argparse
from wifi_testing_logger import setup_logger, log_info, log_warning, log_error, log_exception, log_debug

def disclaimer():
    print("Disclaimer: This script is intended for educational purposes only. Ensure you have proper authorization "
          "before conducting any security testing. Unauthorized testing may lead to legal consequences.")

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

def install_hashcat_kali():
    try:
        subprocess.run("sudo apt-get update", shell=True, check=True)
        subprocess.run("sudo apt-get install -y hashcat", shell=True, check=True)
        print("Hashcat installed successfully on Kali Linux.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Hashcat on Kali Linux: {e}")

def install_hashcat_parrot():
    try:
        subprocess.run("sudo apt-get update", shell=True, check=True)
        subprocess.run("sudo apt-get install -y hashcat", shell=True, check=True)
        print("Hashcat installed successfully on Parrot Security OS.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Hashcat on Parrot Security OS: {e}")

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

def test_wifi_with_hashcat(ssid, bssid, handshake_file, hash_mode, hashcat_params):
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

    hashcat_command = f"hashcat {hash_mode_option} -a 3 --force --stdout {hashcat_params} --outfile=result.txt " \
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

def parse_arguments():
    parser = argparse.ArgumentParser(description="Wi-Fi Network Testing Script")
    parser.add_argument("distribution", choices=["ubuntu", "arch", "kali", "parrot"],
                        help="Select your Linux distribution")
    parser.add_argument("interface", help="Wireless interface to use")
    parser.add_argument("handshake_file", help="Path to the handshake capture file")
    parser.add_argument("security_protocol", choices=["wpa2", "wep", "wpa3"],
                        help="Select the Wi-Fi security protocol")
    parser.add_argument("--hashcat-params", help="Additional Hashcat parameters (e.g., --hash-type, --increment)")

    return parser.parse_args()

if __name__ == "__main__":
    disclaimer()

    args = parse_arguments()

    if args.distribution == "ubuntu":
        install_hashcat_ubuntu()
        install_aircrack_ubuntu()
    elif args.distribution == "arch":
        install_hashcat_arch()
    elif args.distribution == "kali":
        install_hashcat_kali()
    elif args.distribution == "parrot":
        install_hashcat_parrot()
    else:
        print("Invalid distribution. Exiting.")
        exit()

    if not check_chipset_compatibility():
        print("Exiting script.")
        exit()

    monitor_interface = enable_monitor_mode(args.interface)
    if monitor_interface is None:
        print("Exiting script.")
        exit()

    start_analysis(monitor_interface)

    test_wifi_with_hashcat("YourWiFiSSID", "YourWiFiBSSID", args.handshake_file, args.security_protocol, args.hashcat_params)
