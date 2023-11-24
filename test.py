import subprocess

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
    # Replace these values with the actual SSID, BSSID, and handshake file
    wifi_ssid = "YourWiFiSSID"
    wifi_bssid = "YourWiFiBSSID"
    handshake_file_path = "path/to/your/handshake.cap"

    # Call the function to test the Wi-Fi network
    test_wifi_with_hashcat(wifi_ssid, wifi_bssid, handshake_file_path)
