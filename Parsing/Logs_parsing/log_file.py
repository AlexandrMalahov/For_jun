"""Python 3.7 Analyze of log-file."""

import collections
import re

with open('access.log') as ac_log:
    # Opening, reading and treatment log-file.

    IP_COUNTER = collections.Counter()
    PLATFORM_COUNTER = collections.Counter()
    for line in ac_log:
        IP_COUNTER[line.split()[0]] += 1
        PLATFORM_COUNTER[''.join(re.findall(
            r'FreeBSD|Googlebot/2.1|SemrushBot/0.98~bl|Windows|MSIE|YandexBot/3.0|MJ12bot/v1.4.5|'
            r'Baiduspider/2.0|CrOS|bingbot/2.0|Yahoo!|AhrefsBot/5.0|YandexMetrika/2.0|'
            r'iPhone|Linux|Macintosh|Googlebot-Mobile/2.1|iPad|meanpathbot/1.0|'
            r'Android|Ubuntu|Exabot/3.0|coccoc/1.0', line)
        )] += 1



COUNT_IP = 0
for ip in reversed(
        sorted(
            IP_COUNTER,
            key=lambda x: IP_COUNTER[x]
        )):
    # Print of top 10 ip result.

    print('Ip: {0}, Ip_count: {1}'.format(ip, IP_COUNTER[ip]))
    COUNT_IP += 1
    if COUNT_IP == 10:
        break

COUNT_PLATFORM = 0
for platform in reversed(
        sorted(PLATFORM_COUNTER, key=lambda x: PLATFORM_COUNTER[x])):
    # Print of top 5 os's platforms.

    print(
        'Platform: {0}; Platform_count: {1}'.format(
            platform, PLATFORM_COUNTER[platform])
    )

    COUNT_PLATFORM += 1
    if COUNT_PLATFORM == 5:
        break
