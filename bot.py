import random, os, ctypes, httpx, threading, time
from colorama import init, Fore

os.system("cls||clear")
init()

proxies, valid_proxies = [], []
proxies_lock = threading.Lock()
start_time = time.time()

checked, available = 0, 0

usernames = list(open("usernames.txt", "r").read().splitlines())

def worker(usernames, thread_id):
    global check
    while check[thread_id] < len(usernames):
        seek(usernames[check[thread_id]])
        check[thread_id] += 1

def runner():
    threadsAmount = 50
    global check
    check = [0 for _ in range(threadsAmount)]
    for i in range(threadsAmount):
        sliced_combo = usernames[int(len(usernames) / threadsAmount * i) : int(len(usernames) / threadsAmount * (i + 1))]
        threading.Thread(target=worker,args=(sliced_combo,i,)).start()

def seek(username):
    global checked, available
    while True:
        if not valid_proxies:
            continue
        proxy = random.choice(valid_proxies)
        headers = {"accept": "*/*","content-type": "application/json","user-agent": "noplace/1 CFNetwork/1402.0.8 Darwin/22.2.0","accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br"}
        params = {
            "username": f"{username}"
        }
        try:
            response = httpx.get("https://api.nospace.app/api/v1/profiles/username/availability", headers=headers, params=params, proxies=proxy)
            if response.status_code == 200 or response.status_code == 204:
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {username}")
                available+=1
                with open("hits.txt", "a") as file: file.write(username+"\n")
            elif response.status_code == 429:
                continue
            else:
                print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {username}")
        except:
            continue # Proxy issue
        checked+=1
        break

def get_proxies():
    global proxies, valid_proxies
    while True:
        try:
            proxies = httpx.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=elite").text.splitlines()
            valid_proxies.clear()
            for proxy in proxies:
                threading.Thread(target=check_proxy, args=(f"http://{proxy}",)).start()
            time.sleep(60)
        except Exception as e:
            print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Failed to fetch proxies. Retrying in 3 seconds. Error: {e} {Fore.RESET}")
            time.sleep(3)

def check_proxy(proxy):
    try:
        if httpx.get("https://google.com/", proxies=proxy).status_code:
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Found valid proxy {Fore.RESET}")
            valid_proxies.append(proxy)
    except: pass

def updateTitle():
    global checked, available
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f"Usernames Checked: {checked} - Available: {available} | Proxies Scraped: {len(proxies)} - Proxies Valid: {len(valid_proxies)}")


threading.Thread(target=updateTitle).start()
threading.Thread(target=runner).start()
threading.Thread(target=get_proxies).start()
