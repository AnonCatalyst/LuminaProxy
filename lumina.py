# Import necessary modules
import os
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from tabulate import tabulate

class ProxyScraper:
    def __init__(self, proxy_websites, target_ports):
        self.proxy_websites = proxy_websites
        self.target_ports = set(target_ports)
        self.valid_proxies = []
        self.invalid_proxies = []
        self.successful_sites = 0  # Track the number of sites successfully scraped
        self.failed_sites = 0  # Track the number of sites failed to scrape
        self.errors = 0

    def scrape_proxies(self, url):
        try:
            print(f"🌐 Scraping proxies from: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            scraped_proxies_count = 0  # Track the number of proxies scraped from this website

            for row in soup.find_all('tr')[1:]:
                cells = row.find_all(['td', 'th'])

                if len(cells) >= 2:
                    try:
                        ip, port = map(lambda cell: cell.text.strip(), cells[:2])

                        if self.is_valid_ip(ip) and self.is_valid_port(port):
                            proxy_info = f"{ip}:{port}"

                            if int(port) in self.target_ports:
                                self.valid_proxies.append(proxy_info)
                                scraped_proxies_count += 1
                            else:
                                self.invalid_proxies.append(proxy_info)
                        else:
                            self.invalid_proxies.append(f"❌ Invalid Proxy: {ip}:{port}")

                    except ValueError as ve:
                        print(f"❌ Error parsing proxy info: {ve}")

            if scraped_proxies_count > 0:
                print(f"✅ Successfully scraped \033[1m{scraped_proxies_count}\033[0m proxies from {url}")
                self.successful_sites += 1
            else:
                print(f"ℹ️ No proxies scraped from {url}")
                self.failed_sites += 1

        except requests.exceptions.RequestException as re:
            print(f"❌ Error scraping proxies from {url}: {re}")
            self.errors += 1
            self.failed_sites += 1

    def scrape_proxies_threaded(self):
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.scrape_proxies, website) for website in self.proxy_websites]

            for future in tqdm(futures, total=len(self.proxy_websites), desc="🌐 Scraping Proxies"):
                future.result()

    def is_valid_ip(self, ip):
        try:
            parts = ip.split(".")
            return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
        except ValueError:
            return False

    def is_valid_port(self, port):
        try:
            port = int(port)
            return 1 <= port <= 65535
        except ValueError:
            return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    clear_screen()
    print("\033[1m\033[92mWelcome to \033[1m\033[95mLuminaProxy\033[0m - Your \033[1m\033[96mBright Proxy Scraper\033[0m\n")
    print("\033[1m🌟 Description:\033[0m LuminaProxy is a powerful tool crafted by AnonCatalyst to streamline the process of gathering proxy information from various online sources.")
    print("Whether you're conducting research, enhancing security, or testing network configurations, LuminaProxy empowers you to effortlessly collect and categorize proxies.")
    print("Its threaded and efficient design ensures a swift scraping experience, providing you with a clear summary of valid proxies, invalid entries, and any encountered errors.")
    print("\033[1m👨‍💻 Developer:\033[0m AnonCatalyst\n\033[1m🔗 GitHub:\033[0m [AnonCatalyst on GitHub](https://github.com/AnonCatalyst)")
    print("\033[1m📸 Instagram:\033[0m [@istoleyourbutter](https://www.instagram.com/istoleyourbutter/)")

def main():
    proxy_websites = [
        'https://www.sslproxies.org/',
        'https://free-proxy-list.net/',
        'https://www.us-proxy.org/',
        'https://www.proxy-list.download/HTTP',
        'https://www.proxy-list.download/HTTPS',
        'https://spys.one/en/socks-proxy-list/',
        'https://www.socks-proxy.net/',
        'https://hidemy.name/en/proxy-list/',
        'https://www.proxy-list.org/en/',
        'https://www.proxyserverlist24.top/',
        'https://www.proxy-list.net/proxy-server-list/',
        'https://www.proxy-daily.com/',
        'https://www.proxynova.com/proxy-server-list/',
        'https://www.proxy-list.biz/',
        'https://www.proxy-list.net/anonymous-proxy-lists.shtml',
        'https://www.proxy-list.net/socks5-proxy-lists.shtml',
        'https://www.my-proxy.com/free-proxy-list.html',
        'https://www.proxy-list.site/',
        'https://www.webshare.io/',
        'https://www.proxyscrape.com/free-proxy-list',
        'https://free-proxy-list.net/uk-proxy.html',
        'https://www.proxynova.com/proxy-server-list/country-us/',
        'https://www.sslproxies.org/socks-proxy-list/',
        'https://free-proxy-list.net/anonymous-proxy.html',
        'https://www.proxynova.com/proxy-server-list/country-br/',
        'https://www.proxynova.com/proxy-server-list/country-cn/',
        'https://www.sslproxies.org/high-anonymous-proxy/',
        'https://www.proxynova.com/proxy-server-list/country-ru/',
        'https://www.proxygather.com/',
        'https://www.proxy-listen.de/azenv.php',
        'https://www.proxyscrape.com/free-proxy-list',
        'https://www.freeproxylists.net/',
        'https://proxy-list.org/english/index.php',
        'https://www.proxy-list.org/',
        'https://www.proxyscrape.com/',
        'https://www.xroxy.com/proxylist.htm',
        'https://www.proxy-list.net/',
        'https://www.proxy4free.com/',
        'https://www.proxybazaar.com/',
        'https://www.proxz.com/',
        'https://www.proxyrack.com/',
        'https://www.proxy-list.download/',
        'https://proxylist.me/',
        'https://proxylist.hidemyass.com/',
        'https://www.proxyscrape.com/api-proxylist/',
        'https://www.proxy-listen.de/azenv.php',
        'https://www.us-proxy.org/',
        'https://www.sslproxies.org/',
        'https://free-proxy-list.net/',
        'https://www.proxynova.com/proxy-server-list/country-fr/',
        'https://www.proxynova.com/proxy-server-list/country-de/',
        # Add more proxy websites here
    ]

    target_ports = {1080, 8000, 8001, 8002, 1082, 80, 8080, 8445, 8443, 8888, 8444, 3128, 1081}

    proxy_scraper = ProxyScraper(proxy_websites, target_ports)

    print_welcome()
    proxy_scraper.scrape_proxies_threaded()

    valid_proxy_count = len(proxy_scraper.valid_proxies)
    invalid_proxy_count = len(proxy_scraper.invalid_proxies)
    total_errors = proxy_scraper.errors
    successful_sites = proxy_scraper.successful_sites
    failed_sites = proxy_scraper.failed_sites

    proxy_summary = [
        {"Category": "\033[1m\033[92mValid Proxies\033[0m", "Count": valid_proxy_count},
        {"Category": "\033[1m\033[91mInvalid Proxies\033[0m", "Count": invalid_proxy_count},
        {"Category": "\033[1m\033[96mTotal Proxies\033[0m", "Count": valid_proxy_count + invalid_proxy_count},
        {"Category": "\033[1mSuccessful Sites\033[0m", "Count": successful_sites},
        {"Category": "\033[1mFailed Sites\033[0m", "Count": failed_sites},
        {"Category": "\033[1mErrors\033[0m", "Count": total_errors}
    ]

    print("\n\033[1m📊 Proxy Summary:\033[0m")
    print(tabulate(proxy_summary, headers="keys"))

    if valid_proxy_count > 0:
        print("\n\033[1m✅ Valid Proxies:\033[0m")
        for proxy in proxy_scraper.valid_proxies:
            print(proxy)
    else:
        print("\n\033[1mℹ️ No valid proxies were found.\033[0m")

if __name__ == "__main__":
    main()
          
