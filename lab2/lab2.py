# Задание 5.1
# def classify_ip(ip_address):
#     first_byte = int(ip_address.split('.')[0])

#     if ip_address == "255.255.255.255":
#         return "local broadcast"
#     elif ip_address == "0.0.0.0":
#         return "unassigned"
#     elif 1 <= first_byte <= 127:
#         return "unicast"
#     elif 128 <= first_byte <= 191:
#         return "unicast"
#     elif 192 <= first_byte <= 223:
#         return "unicast"
#     elif 224 <= first_byte <= 239:
#         return "multicast"
#     else:
#         return "unused"

# ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")
# print(classify_ip(ip_address))


# Задание 5.1a
# IP = input('Enter IP (10.0.1.1): ')
# octets = IP.split('.')
# if (len(octets) == 4 and int(octets[0]) >= 0 and int(octets[0]) <= 255 and
#       int(octets[1]) >= 0 and int(octets[1]) <= 255 and
#       int(octets[2]) >= 0 and int(octets[2]) <= 255 and
#       int(octets[3]) >= 0 and int(octets[3]) <= 255):
#   if (int(octets[0]) >= 1) and (int(octets[0]) <= 223):
#     print('unicast')
#   elif (int(octets[0]) >= 224) and (int(octets[0]) <= 239):
#     print('multicast')
#   elif IP == '255.255.255.255':
#     print('local broadcast')
#   elif IP == '0.0.0.0':
#     print('unassigned')
#   else:
#     print('unused')
# else:
#   print("Incorrect IPv4 address")
     


#Задание 5.1b
# IP = input('Enter IP (10.0.1.1): ')

# while True:
#   octets = IP.split('.')
#   if (len(octets) == 4 and int(octets[0]) >= 0 and int(octets[0]) <= 255 and
#       int(octets[1]) >= 0 and int(octets[1]) <= 255 and
#       int(octets[2]) >= 0 and int(octets[2]) <= 255 and
#       int(octets[3]) >= 0 and int(octets[3]) <= 255):
#     if (int(octets[0]) >= 1) and (int(octets[0]) <= 223):
#       print('unicast')
#     elif (int(octets[0]) >= 224) and (int(octets[0]) <= 239):
#       print('multicast')
#     elif IP == '255.255.255.255':
#       print('local broadcast')
#     elif IP == '0.0.0.0':
#       print('unassigned')
#     else:
#       print('unused')
#     break
#   else:
#     print('Incorrect IPv4 address')
#     IP = input('Enter IP again (10.0.1.1): ')
#     octets = IP.split('.')
     

#Задание 5.3
# access_template = ['switchport mode access',
#                    'switchport access vlan',
#                    'spanning-tree portfast',
#                    'spanning-tree bpduguard enable']

# trunk_template = ['switchport trunk encapsulation dot1q',
#                   'switchport mode trunk',
#                   'switchport trunk allowed vlan']

# fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
#             'trunk':{'0/1':['add','10','20'],
#                      '0/2':['only','11','30'],
#                      '0/4':['del','17']} }

# for intf, vlan in fast_int['access'].items():
#   print('interface FastEthernet' + intf)
#   for command in access_template:
#     if command.endswith('access vlan'):
#       print(' {} {}'.format(command, vlan))
#     else:
#       print(' {}'.format(command))

# print()

# for intf, vlan in fast_int['trunk'].items():
#   print('interface FastEthernet' + intf)
#   for command in trunk_template:
#     if command.endswith('allowed vlan'):
#       if vlan[0] == 'add':
#         print(' {} {} {},{}'.format(command, vlan[0], vlan[1], vlan[2]))
#       elif vlan[0] == 'del':
#         print(' {} remove {}'.format(command, vlan[1]))
#       elif vlan[0] == 'only':
#         print(' {} {},{}'.format(command, vlan[1], vlan[2]))
#     else:
#       print(' {}'.format(command))


