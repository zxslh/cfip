import requests
import re
import os

# 正则表达式用于匹配IP地址
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
url = 'https://ip.164746.xyz'
try:
        # 发送HTTP请求获取网页内容
    response = requests.get(url, timeout=5)        
        # 确保请求成功
    if response.status_code == 200:
            # 获取网页的文本内容
        html_content = response.text            
            # 使用正则表达式查找IP地址
        ip_matches = re.findall(ip_pattern, html_content, re.IGNORECASE)

        if ip_matches:
            token = 'yDmZaZ13RqSEpjZzr5yoihdT_g3hp6'
            domain = 'cf-zxs.dynv6.net'
            ipv4 = ip_matches[0]
            update_url = f'http://dynv6.com/api/update?token={token}&hostname={domain}&ipv4={ipv4}'
            response = requests.get(update_url, timeout=10).text.strip()
            #print(response)
except requests.exceptions.RequestException as e:
    print(f'请求 {url} 失败: {e}')
        
url = 'https://ipdb.api.030101.xyz/?type=bestcf&country=true'
try:
        # 发送HTTP请求获取网页内容
    response = requests.get(url, timeout=5)        
        # 确保请求成功
    if response.status_code == 200:
            # 获取网页的文本内容
        html_content = response.text            
            # 使用正则表达式查找IP地址
        ip_matches = re.findall(ip_pattern, html_content, re.IGNORECASE)

        if ip_matches:
            token = 'c4qv9NXXa6WEv5RyR2LpK-tnoZso92'
            domain = 'cf-zxs.v6.army'
            ipv4 = ip_matches[0]
            update_url = f'http://dynv6.com/api/update?token={token}&hostname={domain}&ipv4={ipv4}'
            response = requests.get(update_url, timeout=10).text.strip()
            #print(response)
except requests.exceptions.RequestException as e:
    print(f'请求 {url} 失败: {e}')

url = 'https://ip.164746.xyz/ipTop10.html'
try:
        # 发送HTTP请求获取网页内容
    response = requests.get(url, timeout=5)        
        # 确保请求成功
    if response.status_code == 200:
            # 获取网页的文本内容
        html_content = response.text            
            # 使用正则表达式查找IP地址
        ip_matches = re.findall(ip_pattern, html_content, re.IGNORECASE)

        if ip_matches:
            token = 'vTTXvP2dGw8dtHjwFRXXjVfWL1rcLU'
            domain = 'cf-zxs.dns.army'
            ipv4 = ip_matches[0]
            update_url = f'http://dynv6.com/api/update?token={token}&hostname={domain}&ipv4={ipv4}'
            response = requests.get(update_url, timeout=10).text.strip()
            #print(response)
except requests.exceptions.RequestException as e:
    print(f'请求 {url} 失败: {e}')

url = 'https://www.wetest.vip/page/cloudflare/total_v4.html'
try:
        # 发送HTTP请求获取网页内容
    response = requests.get(url, timeout=5)        
        # 确保请求成功
    if response.status_code == 200:
            # 获取网页的文本内容
        html_content = response.text            
            # 使用正则表达式查找IP地址
        ip_matches = re.findall(ip_pattern, html_content, re.IGNORECASE)

        if ip_matches:
            token = 'w-2rwUkVh_6XfEuUgYddGz89T3qTCg'
            domain = 'cf-zxs.dns.navy'
            ipv4 = ip_matches[0]
            update_url = f'http://dynv6.com/api/update?token={token}&hostname={domain}&ipv4={ipv4}'
            response = requests.get(update_url, timeout=10).text.strip()
            #print(response)
except requests.exceptions.RequestException as e:
    print(f'请求 {url} 失败: {e}')

url = 'https://www.wetest.vip/page/cloudflare/total_v4.html'
try:
        # 发送HTTP请求获取网页内容
    response = requests.get(url, timeout=5)        
        # 确保请求成功
    if response.status_code == 200:
            # 获取网页的文本内容
        html_content = response.text            
            # 使用正则表达式查找IP地址
        ip_matches = re.findall(ip_pattern, html_content, re.IGNORECASE)

        if ip_matches:
            token = 'qAprRPsvN9xZJ3_Mr9_A87aRaxHWsY'
            domain = 'cf-zxs.v6.navy'
            ipv4 = ip_matches[-1]
            update_url = f'http://dynv6.com/api/update?token={token}&hostname={domain}&ipv4={ipv4}'
            response = requests.get(update_url, timeout=10).text.strip()
            #print(response)
except requests.exceptions.RequestException as e:
    print(f'请求 {url} 失败: {e}')

