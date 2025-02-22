# web / crawler / python with something 
# How to use this
# python crawler.py https://example.com --max-pages 50 --same-domain --delay 1 --output results.txt

# ===============================================
import sys, requests, time, logging, argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# =================================================
# Global storage for URLs to crawl and already-crawled URLs
webCrawl = []
CRAWLED = set()

def request(url):
    """Request the page content for the given URL."""
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; x64; rv: 109.0) Gecko/20100101 Firefox/116.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    }
    try:
        response = requests.get(url, headers=header, timeout=10)
        return response.text
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def getLinks(soup, base_url, same_domain_filter, main_domain):
    links = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        absolute_url = urljoin(base_url, href)
        if absolute_url.startswith("http"):
            if same_domain_filter:
                if urlparse(absolute_url).netloc == main_domain:
                    links.append(absolute_url)
            else:
                links.append(absolute_url)
    return links

def crawl(webCrawl, same_domain_filter, main_domain, max_pages, delay=0):
    """
    Crawl pages until no URLs remain in the queue or the maximum number of pages is reached.
    
    Args:
        webCrawl (list): List of URLs pending crawl.
        same_domain_filter (bool): If True, only crawl URLs within the main domain.
        main_domain (str): The starting domain to enforce same-domain filtering.
        max_pages (int): Maximum number of pages to crawl.
        delay (float): Seconds to wait between each request.
    """
    while webCrawl and len(CRAWLED) < max_pages:
        url = webCrawl.pop(0)
        if url in CRAWLED:
            continue
        html = request(url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            title_tag = soup.find("title")
            title = title_tag.text.strip() if title_tag else "No Title"
            logging.info(f"Crawling: {url} - {title}")
            links = getLinks(soup, url, same_domain_filter, main_domain)
            for link in links:
                if link not in CRAWLED and link not in webCrawl:
                    webCrawl.append(link)
            CRAWLED.add(url)
        else:
            logging.erro54r(f"Failed to retrieve: {url}")
            CRAWLED.add(url)

        if delay > 0:
            time.sleep(delay)
    logging.info("Crawling finished.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enhanced Web Crawler")
    parser.add_argument("url", help="Starting URL for the crawler")
    parser.add_argument("--max-pages", type=int, default=100,
                        help="Maximum number of pages to crawl (default: 100)")
    parser.add_argument("--same-domain", action="store_true",
                        help="Only crawl pages within the same domain as the starting URL")
    parser.add_argument("--delay", type=float, default=0,
                        help="Delay between requests in seconds (default: 0)")
    parser.add_argument("--output", default="crawled_urls.txt",
                        help="File to output crawled URLs (default: crawled_urls.txt)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    start_url = args.url
    max_pages = args.max_pages
    same_domain = args.same_domain
    delay = args.delay

    main_domain = urlparse(start_url).netloc

    webCrawl.append(start_url)
    crawl(webCrawl, same_domain, main_domain, max_pages, delay)

    try:
        with open(args.output, "w", encoding="utf-8") as f:
            for url in CRAWLED:
                f.write(url + "\n")
        logging.info(f"Crawled URLs have been written to {args.output}")
    except Exception as e:
        logging.error(f"Error pas ngewrite outpute: {e}")