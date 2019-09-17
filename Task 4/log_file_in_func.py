"""Python 3.7 Analyze of log-file."""

import collections
import re


def log_analize(logfile):
    """Opening, reading and treatment log-file."""

    with open(logfile) as ac_log:
        ip_counter = collections.Counter()
        platform_counter = collections.Counter()
        for line in ac_log:
            ip_counter[re.findall(r'\d+\.\d+\.\d+\.\d+', line)[0]] += 1
            platform_counter[''.join(re.findall(r'\((\S+\s+\S+)', line))] += 1

    count_ip = 0
    for ip_ in reversed(
            sorted(
                ip_counter,
                key=lambda x: ip_counter[x]
            )):
        print('Ip: {0}, Ip_count: {1}'.format(ip_, ip_counter[ip_]))
        # Print of top 10 ip result.
        count_ip += 1
        if count_ip == 10:
            break

    count_platform = 0
    for platform in reversed(
            sorted(platform_counter, key=lambda x: platform_counter[x])):
        print(
            'Platform: {0}; Platform_count: {1}'.format(
                platform, platform_counter[platform])
        )
        # Print of top 5 os's platforms.
        count_platform += 1
        if count_platform == 5:
            break


log_analize('access.log')
