import requests 
import argparse
import json

if __name__ == "__main__":
    # creates parser object
    parse = argparse.ArgumentParser()

    # adds arguements options that given when running program
    parse.add_argument("-i", "--ipaddress", help="IP address to track")

    # parses the args to you can indivdually access them
    args = parse.parse_args()

    # stores the ip address
    ip = args.ipaddress

    # creates the url string with ip address at the end
    url = "http://ip-api.com/json/" + ip

    # http://ip-api/json/192.168.0.1

    # calls the request using the url created previously
    response = requests.get(url)

    # loads the json data and stores it for later printing
    data = json.loads(response.content)

    print("\t[+] IP\t\t\t", data["query"])
    print("\t[+] CITY\t\t", data["city"])
    print("\t[+] ISP\t\t\t", data["isp"])
    print("\t[+] LOC\t\t\t", data["country"])
    print("\t[+] REG\t\t\t", data["regionName"])
    print("\t[+] TIME\t\t", data["timezone"])
    print("\t[+] ZIP\t\t\t", data["zip"])
    print("\t[+] LAT\t\t\t", data["lat"])
    print("\t[+] LON\t\t\t", data["lon"])