import sys
import socket
from http.client import HTTPConnection

def count_zeros_in_html(url):
    try:
        if not url.startswith('http://'):
            url = 'http://' + url
        host = url.split('//')[1].split('/')[0]
        path = '/' + '/'.join(url.split('//')[1].split('/')[1:])
        
        connection = HTTPConnection(host)
        connection.request('GET', path)
        response = connection.getresponse()

        if response.status == 200:
            html = response.read().decode('utf-8')
            zero_count = html.count('0')
            print(f'The number 0 appears {zero_count} times in the HTML document.')
        else:
            print(f"Failed to fetch the URL: {url}, Status: {response.status}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1.py <URL>")
    else:
        count_zeros_in_html(sys.argv[1])




