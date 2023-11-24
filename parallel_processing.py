import multiprocessing
import subprocess
from tqdm import tqdm

def parallel_crack(hashcat_command):
    try:
        result = subprocess.run(hashcat_command, shell=True, check=True, stdout=subprocess.PIPE)
        return result.stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Hashcat failed with error: {e}"

def test_wifi_with_hashcat_parallel(ssid, bssid, handshake_file, hash_mode, hashcat_params, num_processes=2):
    progress_bar = tqdm(total=100, desc="Hash Cracking Progress", unit="%")

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
        # Split the task and run in parallel
        chunks = [(hashcat_command,)] * num_processes
        with multiprocessing.Pool(num_processes) as pool:
            results = list(tqdm(pool.starmap(parallel_crack, chunks), total=num_processes, desc="Parallel Tasks"))

        # Display results or handle errors
        for result in results:
            if "Hashcat failed with error" in result:
                print(result)
                exit()
            for _ in tqdm(result.split("\n")):
                progress_bar.update(1)

        print("\nHashcat completed successfully.")
    finally:
        progress_bar.close()
