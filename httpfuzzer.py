import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# --- Loader as payloads
url = ""
payloads = ["' OR 1=1 -- ", "\" OR \"\"=\"", "<script>alert(1)</script>"]

for p in payloads:
    data = {"param": p}
    r = requests.post(url, data=data)
    if "error" in r.text or "syntax" in r.text or "<script>alert(1)</script>" in r.text:
        print(f"Possible injection found with payload: {p}")
        soup = BeautifulSoup(r.text, "html.parser")
        for script in soup.find_all("script"):
            print(f"Possible XSS found in {url}: {script.text}")
    else:
        print(f"No injection or XSS found with payload: {p}")

# ----------------------------------------------------------------
def get_website_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {url}")
        return None
    return BeautifulSoup(response.content, "html.parser")

# ----------------------------------------------------------------
def find_and_print_xss_in_website(url):
    soup = get_website_content(url)
    if soup:
        for script in soup.find_all("script"):
            print(f"Possible XSS found in {url}: {script.text}")
            if "<script>" in script.text and "</script>" in script.text:
                print(f"Possible inline XSS found in {url}: {script.text[script.text.index("<script>")+8:script.text.index("</script>")]}")
            elif "<script src=" in script.text:
                src = script.text[script.text.index("<script src=")+12:script.text.index(">")]
                src_url = urljoin(url, src)
                find_and_print_xss_in_website(src_url)
                print(f"Possible cross-site scripting found in {url}: {script.text}")


find_and_print_xss_in_website("localhost")

# ----------------------------------------------------------------
def find_and_print_injection_in_website(url):
    soup = get_website_content(url)
    if soup:
        for form in soup.find_all("form"):
            for input_tag in form.find_all("input"):
                if input_tag.get("type") == "text":
                    data = {input_tag.get("name"): payloads[0]}
                    r = requests.post(url, data=data)
                    if "error" in r.text or "syntax" in r.text:
                        print(f"Possible injection found in {url} with field: {input_tag.get('name')}")
                    else:
                        print(f"No injection found in {url} with field: {input_tag.get('name')}")
                elif input_tag.get("type") == "submit":
                    data = {input_tag.get("name"): payloads[0]}
                    r = requests.post(url, data=data)
                    if "error" in r.text or "syntax" in r.text:
                        print(f"Possible injection found in {url} with field: {input_tag.get('name')}")
                    else:
                        print(f"No injection found in {url} with field: {input_tag.get('name')}")

                    # ----------------------------------------------------------------
                    def find_and_print_injection_in_website_with_js(url):
                        soup = get_website_content(url)
                    if soup:
                        for script in soup.find_all("script"):
                            for payloads in script.findall("payload"):
                                data = {}