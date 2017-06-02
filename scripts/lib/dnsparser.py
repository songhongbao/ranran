# -*- coding:utf-8 -*-
import dns.resolver
from lib import log
import hashlib

# alibaba dns and 114 dns are so fast
dns_ips = [
    '223.5.5.5',
    '223.6.6.6',
    '114.114.114.114',
    '114.114.115.115'
]
# dns time settings
time_out = 5
# valid dns ips
valid_ips = None


def get_valid_dns():
    """
    get valid dns list from dns ips
    use dns to parse existing url and nonexistent url
    """
    global valid_ips
    if valid_ips is not None:
        return valid_ips
    valid_ips = []
    for ip in dns_ips:
        parser = dns.resolver.Resolver()
        parser.lifetime = parser.timeout = time_out
        parser.nameservers = [ip]
        try:
            if parser.query('love.ranshy.com')[0].address == '121.42.153.188':
                try:
                    parser.query('notexists.ranshy.com')
                except (dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.exception.Timeout):
                    valid_ips.append(ip)
        except dns.resolver.NXDOMAIN:
            log.error('dnsparser parser failed. ip ' + str(ip) + ' is invalid.')
        except dns.exception.Timeout:
            log.error('dnsparser parser timeout. ip ' + str(ip) + ' is invalid.')
    return valid_ips


def url2ips(url):
    """
    get the url ip
    if url use cdn, then return ip list
    """
    parser = dns.resolver.Resolver()
    parser.lifetime = parser.timeout = time_out
    url_ips = []
    for ip in dns_ips:
        parser.nameservers = [ip]
        try:
            url_ip = parser.query(url)[0].address
            if url_ip not in url_ips:
                url_ips.append(str(url_ip))
        except (dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.exception.Timeout):
            log.error('dns(' + ip + ') parse url(' + url + ') error.')
    return url_ips


def url2ip(url):
    """
    get the url ip
    if url use cdn, then return random one of the cdn ips
    """
    parser = dns.resolver.Resolver()
    parser.lifetime = parser.timeout = time_out
    prefix = int(hashlib.md5(url).hexdigest()[-1], 16) % len(get_valid_dns())
    parser.nameservers = [get_valid_dns()[prefix]]
    try:
        url_ip = parser.query(url)[0].address
    except (dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.exception.Timeout):
        url_ip = False
        log.error('dns(' + get_valid_dns()[prefix] + ') parse url(' + url + ') error.')
    finally:
        return url_ip
