import requests

def get_content(url):
    cookies = {
        'ahoy_visitor': '6daad725-ba5b-4f28-8a61-4e7a372f524d',
        '_ga': 'GA1.2.1534259563.1599059062',
        'ahoy_visit': '03ba7280-f03b-4bfb-976b-f2e3918dcf7e',
        '_gid': 'GA1.2.63598564.1607243943',
        '_Synced_session': 'HhhK8Ys8%2BFSefqtSCShgvNxJ38a2RuPn1GZxbv5NitS4GJRs88UKYfIvL%2FjI0sOGwuStndqCy%2BS3YNmkj7Ori74euJ%2B%2F7pzsLWzMDC2wl3h6jJ%2BnBhLx7Xxq%2FbyZ%2FkWsbgH88YwSlqdkWyR9hbmt%2FOzUtPSoXxf2N5xmIfDGvTTnymNP%2BAyFKwyQ%2FE49mV3C%2FP%2Ba5n4Du58UV0b1JGugryArAzMGwtwIREFq6w9n7KHjByLY6Hkrm7wMe1LATH%2FDHJB8eWazpwPBmonPADRedWrOqTmFUEmSFP8Kq4J8VUR2weXdBh8L%2Ffj4qfbkVqg%2FCiwXen6fG1mZJflUwstrO8WLBzDQdWzdFjZPyKRRr3QJL2FNQ8w0y%2B9prolD4Ebdi%2FMl3T%2F3VwXoCJTi%2BSEcVGQ%3D--nh9zCZlDUwsHjeaD--Be3%2FrdVaySQkBWNIm2ehVw%3D%3D',
    }
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': url,
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'If-None-Match': 'W/"debf651895542dafb77525d026710391"',
    }
    response = requests.get(url, headers=headers)
    return response.text