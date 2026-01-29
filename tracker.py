import requests
import ipaddress
import os
import time
from datetime import datetime

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    clear_screen()
    banner = f"""
    \033[1;31m██╗██████╗ \033[1;37m██╗███╗   ██╗███████╗ ██████╗ 
    \033[1;31m██║██╔══██╗\033[1;37m██║████╗  ██║██╔════╝██╔═══██╗
    \033[1;31m██║██████╔╝\033[1;37m██║██╔██╗ ██║█████╗  ██║   ██║
    \033[1;31m██║██╔═══╝ \033[1;37m██║██║╚██╗██║██╔══╝  ██║   ██║
    \033[1;31m██║██║     \033[1;37m██║██║ ╚████║██║     ╚██████╔╝
    \033[1;31m╚═╝╚═╝     \033[1;37m╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
    \033[1;34m{"="*55}
    \033[1;32m🚀 Tool Name  : IP-INFO ADVANCED V2
    \033[1;33m👤 Created By : Priyanshu Gupta ❤️
    \033[1;31m📺 Subscribe  : The Black Hat Priyanshu
    \033[1;36m📅 Date       : {datetime.now().strftime('%Y-%m-%d %H:%M')}
    \033[1;34m{"="*55}\033[0m
    """
    print(banner)

def fetch_data(ip):
    # Method 1: ip-api.com (More stable for free users)
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get("status") == "success":
            return {
                "IP": data.get("query"),
                "City": data.get("city"),
                "Region": data.get("regionName"),
                "Country": f"{data.get('country')} ({data.get('countryCode')})",
                "Postal": data.get("zip"),
                "Lat": data.get("lat"),
                "Lon": data.get("lon"),
                "TZ": data.get("timezone"),
                "ISP": data.get("isp"),
                "Org": data.get("org"),
                "AS": data.get("as")
            }
    except:
        pass
    return None

def main():
    print_banner()
    ip = input("\033[1;37m[?] Enter Target IP (Leave blank for self): \033[0m").strip()

    if ip:
        try:
            if ipaddress.ip_address(ip).is_private:
                print("\n\033[1;31m[!] Error: Private IP detected. Cannot trace.\033[0m")
                return
        except:
            print("\n\033[1;31m[!] Error: Invalid IP address format.\033[0m")
            return

    print("\033[1;33m[*] Searching database...\033[0m")
    
    res = fetch_data(ip)
    
    if res:
        print(f"\n\033[1;32m[+] DATA FOUND FOR: {res['IP']}\n")
        fields = [
            ("City", res['City']), ("Region", res['Region']), ("Country", res['Country']),
            ("Zip Code", res['Postal']), ("Latitude", res['Lat']), ("Longitude", res['Lon']),
            ("Time Zone", res['TZ']), ("ISP", res['ISP']), ("ASN", res['AS'])
        ]
        
        for key, val in fields:
            print(f"\033[1;36m➤ {key:15}: \033[1;37m{val}")
            
        maps_url = f"https://www.google.com/maps?q={res['Lat']},{res['Lon']}"
        print(f"\n\033[1;35m🔗 Google Maps: \033[4;35m{maps_url}\033[0m")
    else:
        print("\033[1;31m[!] Error: All API limits reached. Try again later or use a VPN.\033[0m")

if __name__ == "__main__":
    try:
        main()
        print(f"\n\033[1;32m{'='*55}\n      Follow Priyanshu for more updates!\n{'='*55}\033[0m")
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Exiting...\033[0m")
      
