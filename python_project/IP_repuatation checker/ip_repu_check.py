import requests
import os
import json
import ipaddress


# This function checks the reputation of an IP address using VirusTotal
def check_ip_reputation(ip):

    # Get the VirusTotal API key from the environment variable
    api_key = os.getenv("VT_API_KEY")

    # Check if the entered IP address is valid
    try:
        if not ipaddress.ip_address(ip):
            print("Invalid IP address format.")

    except ValueError:
        print("Invalid IP address format.")
        return

    # Check if the VirusTotal API key is available
    if not api_key:
        print(
            "Virus Total API key not found. "
            "Please set the VT_API_KEY environment variable."
        )

    # Create the VirusTotal API URL using the IP address
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    # Add the API key to the request headers
    headers = {
        "x-apikey": api_key
    }

    # Send a GET request to VirusTotal
    response = requests.get(url, headers=headers)

    # Print the response status code
    print(f"Response Status Code: {response.status_code}")

    # Convert the JSON response into a Python dictionary
    data = response.json()
    #print(json.dumps(data, indent=2)) # Uncomment this line to print the entire JSON response for debugging purposes

    # Display the main heading
    print("==========================================")
    print("           IP Reputation Checker          ")
    print("==========================================")
    print()

    # Display the IP address being checked
    print(f" IP Address : {ip}")
    print()

    # Display network information
    print("------------Network Information------------")
    print()

    print(f" Country : {data.get('data').get('attributes').get('country', 'Unknown')}")
    print(f" Organization : {data.get('data').get('attributes').get('as_owner', 'Unknown')}")
    print(f" ASN : {data.get('data').get('attributes').get('asn', 'Unknown')}")
    print(f" Reputation Score : {data.get('data').get('attributes').get('reputation', 'Unknown')}")

    print()

    # Display threat intelligence information
    print("------------Threat Intelligence------------")
    print()

    print(f" Malicious : {data.get('data').get('attributes').get('last_analysis_stats').get('malicious', 'Unknown')}")
    print(f" Suspicious : {data.get('data').get('attributes').get('last_analysis_stats').get('suspicious', 'Unknown')}")
    print(f" Harmless : {data.get('data').get('attributes').get('last_analysis_stats').get('harmless', 'Unknown')}")
    print(f" Undetected : {data.get('data').get('attributes').get('last_analysis_stats').get('undetected', 'Unknown')}")

    print()

    # Check and display the overall reputation
    print("------------Reputation------------")

    # Get the attributes from the VirusTotal response
    attributes = data.get('data').get('attributes')

    # Get the analysis statistics
    stat = attributes.get('last_analysis_stats')

    # Check if the IP has been flagged as malicious
    if stat.get('malicious') > 0:
        print("\nThis IP address is flagged as malicious.")

    # Check if the IP has been flagged as suspicious
    elif stat.get('suspicious') > 0:
        print("\nThis IP address is flagged as suspicious.")

    # If there are no malicious or suspicious detections
    else:
        print("\nThis IP address has a good reputation.")

    print()
    print("----------------------------------")


# Main function of the program
def main():

    # Ask the user to enter multiple IP addresses separated by commas
    # split(",") separates the IP addresses
    # strip() removes extra spaces around each IP address
    ips = [
        ip.strip()
        for ip in input("Enter IP addresses separated by commas: ").split(",")
    ]

    # Check each IP address one by one
    for ip in ips:
        check_ip_reputation(ip)


# Run the main function when this file is executed
if __name__ == "__main__":
    main()

