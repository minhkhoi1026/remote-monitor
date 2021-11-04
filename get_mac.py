import socket
import psutil

def get_all_mac():
    res = []
    for interface, snics in psutil.net_if_addrs().items():
        cur_nic = {"Name": interface}
        for snic in snics:
            if snic.family == socket.AF_INET:
                cur_nic["IP"] = snic.address
                cur_nic["Subnet mask"] = snic.netmask
            if snic.family == psutil.AF_LINK:
                cur_nic["MAC"] = snic.address
        res.append(cur_nic)
    return res