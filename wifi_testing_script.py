import subprocess
import argparse
from tqdm import tqdm
from wifi_testing_logger import setup_logger, log_info, log_warning, log_error, log_exception, log_debug
from parallel_processing import test_wifi_with_hashcat_parallel
from error_handling import (
    install_hashcat_ubuntu, install_hashcat_arch, install_aircrack_ubuntu,
    install_hashcat_kali, install_hashcat_parrot, check_chipset_compatibility,
    enable_monitor_mode, start_analysis
)
from cleanup import cleanup  # Import the cleanup function

def disclaimer():
    print("Disclaimer: This script is intended for educational purposes only. Ensure you have proper authorization "
          "before conducting any security testing. Unauthorized testing may lead to legal consequences.")

def test_wifi_with_hashcat(ssid, bssid, handshake_file, hash_mode, hashcat_params):
    # For backward compatibility, redirect to the parallel processing version
    test_wifi_with_hashcat_parallel(ssid, bssid, handshake_file, hash_mode, hashcat_params)

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

    # Set up logging...
    setup_logger()

    # Install Hashcat and related tools...
    install_functions = {
        "ubuntu": install_hashcat_ubuntu,
        "arch": install_hashcat_arch,
        "kali": install_hashcat_kali,
        "parrot": install_hashcat_parrot
    }

    install_function = install_functions.get(args.distribution)
    if install_function:
        install_function()
    else:
        print("Invalid distribution. Exiting.")
        exit()

    # Check Wi-Fi chipset compatibility...
    if not check_chipset_compatibility():
        print("Exiting script.")
        exit()

    # Enable monitor mode on the specified interface...
    monitor_interface = enable_monitor_mode(args.interface)
    if monitor_interface is None:
        print("Exiting script.")
        exit()

    # Start Wi-Fi analysis...
    start_analysis(monitor_interface)

    # Test Wi-Fi with Hashcat...
    test_wifi_with_hashcat("YourWiFiSSID", "YourWiFiBSSID", args.handshake_file, args.security_protocol, args.hashcat_params)

    # Perform cleanup
    cleanup()
