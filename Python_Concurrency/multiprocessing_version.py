import requests
import multiprocessing
import time

session = None
des = None


def set_global_session():
    global des
    global session
    if not session:
        session = requests.Session()

    if not des:
        des = open('multiprocessing_version_output.txt', 'w')


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}", file=des)


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    des = open('multiprocessing_version_output.txt', 'w')
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 30
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds", file=des)

    des.close()