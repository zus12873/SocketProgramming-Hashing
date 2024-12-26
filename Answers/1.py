import sys
import http.client

def fetch_html(url, max_redirects=10):
    if max_redirects == 0:
        raise Exception("Too many redirects")

    url = url.replace("http://", "").replace("https://", "")
    host = url.split("/")[0]
    path = "/" + "/".join(url.split("/")[1:]) if "/" in url else "/"
    use_https = sys.argv[1].startswith("https://")

    try:
        conn_class = http.client.HTTPSConnection if use_https else http.client.HTTPConnection
        conn = conn_class(host, timeout=10)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        conn.request("GET", path, headers=headers)
        response = conn.getresponse()

        if response.status in (301, 302):  # Handle redirection
            location = response.getheader('Location')
            conn.close()
            return fetch_html(location, max_redirects - 1)

        if response.status == 200:
            return response.read().decode('utf-8')  # Read and decode HTML content
        else:
            conn.close()
            return None
    except Exception as e:
        return None

if len(sys.argv) != 2:
    print("Usage: python 1.py <URL>")
    sys.exit(1)

html = fetch_html(sys.argv[1])
if html:
    count = html.count('0')
  
    print(f'{count}\n', end='')
