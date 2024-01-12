import os
import hashlib

def scan_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        file_hash = hashlib.md5(content).hexdigest()
        print(f"Scanning file: {file_path} | MD5 Hash: {file_hash}")

        # Add your malware detection logic here
        # You can use various techniques like signature-based scanning, heuristics, etc.
        # For simplicity, let's assume any file with 'virus' in its name is considered malware.
        if 'virus' in file_path.lower():
            print("File is infected with malware!")
        else:
            print("File is clean.")

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path)

def main():
    directory = input("Enter the directory path to scan: ")
    scan_directory(directory)

if __name__ == '__main__':
    main()