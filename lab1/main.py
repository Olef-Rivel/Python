# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Задание 3.1
# NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
#NAT_modified = NAT.replace("FastEthernet", "GigabitEthernet")
#print(NAT_modified)

#Задание 3.2
#MAC = 'AAAA:BBBB:CCCC'
#MAC_modified = MAC.replace(":", ".")
#print(MAC_modified)

#Задание 3.3
# CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
# vlans = CONFIG.split()[-1].split(',')
# print(vlans)


#Задание 3.4
# command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
# command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
# vlans1 = set(command1.split()[-1].split(','))
# vlans2 = set(command2.split()[-1].split(','))
# common_vlans = sorted(vlans1 & vlans2)
# print(common_vlans)

#Задание 3.5
# VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
# unique_vlans = set(VLANS)
# sorted_vlans = sorted(unique_vlans)
# print(sorted_vlans)


#Задание 3.6
# ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
#
# route_parts = ospf_route.split()
#
# protocol = "OSPF"
# prefix = route_parts[1]
# ad_metric = route_parts[2].strip("[]")
# next_hop = route_parts[4].strip(",")
# last_update = route_parts[5].strip(",")
# outbound_interface = route_parts[6]
#
# # Специальный символ {} указывает, что сюда подставится значение, которое
# # передается методу format. Три кавычки используются в Python для создания многострочных строк
# output = """\
# Protocol:               {}
# Prefix:                 {}
# AD/Metric:              {}
# Next-Hop:               {}
# Last update:            {}
# Outbound Interface:     {}
# """.format(protocol, prefix, ad_metric, next_hop, last_update, outbound_interface)
# print(output)


#Задание 3.7
# MAC = 'AAAA:BBBB:CCCC'
# mac_parts = MAC.split(':')
# binary_mac = ''.join(bin(int(part, 16))[2:].zfill(16) for part in mac_parts)
# print(binary_mac)


#Задание 3.8
# IP = '192.168.3.1'
# octets = IP.split('.')
# binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
# print("{:<10} {:<10} {:<10} {:<10}".format(octets[0], octets[1], octets[2], octets[3]))
# print("{:<10} {:<10} {:<10} {:<10}".format(binary_octets[0], binary_octets[1], binary_octets[2], binary_octets[3]))


