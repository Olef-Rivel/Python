# Задание 6.1
# with open('ospf.txt') as file:
#     for line in file:
#         parts = line.strip().split()  

#         protocol = "OSPF"
#         prefix = parts[1]
#         ad_metric = parts[2].strip("[]")
#         next_hop = parts[4].strip(",")
#         last_update = parts[5].strip(",")
#         outbound_interface = parts[6]

#         # Выводим отформатированную информацию
#         print(f"Protocol: {protocol}")
#         print(f"Prefix: {prefix}")
#         print(f"AD/Metric: {ad_metric}")
#         print(f"Next-Hop: {next_hop}")
#         print(f"Last update: {last_update}")
#         print(f"Outbound Interface: {outbound_interface}")
#         print("-" * 40)  

#Задание 6.2
# with open('config_sw1.txt') as f:
#   for line in f:
#     cleanLine = line.strip()

#     if not cleanLine or cleanLine.startswith('!'):
#       continue
#     print(cleanLine)


# Задание 6.2а
# ignore = ['duplex', 'alias', 'Current configuration']

# with open('config_sw1.txt') as f:
#   for line in f:
#     cleanLine = line.strip()

#     if not cleanLine or cleanLine.startswith('!'):
#       continue

#     for word in ignore:
#       if word in cleanLine:
#         break
#     else:
#       print(cleanLine)

#Задание 6.2b
# ignore = ['duplex', 'alias', 'Current configuration']
# with open('config_sw1.txt') as f, open('config_sw1_cleared.txt', 'w') as f2:
#   for line in f:
#     cleanLine = line.strip()

#     if not cleanLine:
#       continue

#     for word in ignore:
#       if word in cleanLine:
#         break
#     else:
#       f2.write(cleanLine + '\n')

# print('File confit_sw1_cleares.txt:')
# with open('config_sw1_cleared.txt', 'r') as f2:
#   print(f2.read())

#Задание 6.3
# with open('CAM_table.txt', 'r') as f:
#   for line in f:
#     cleanLine = line.strip()

#     if '.' in cleanLine:
#       columns = cleanLine.split()
#       print('%-6s %-15s %7s' % (columns[0], columns[1], columns[3]))
     
#Задание 6.3b
# print('Enter tne number of VLAN: ')
# numVlan = input()

# with open('CAM_table.txt', 'r') as f:
#   for line in f:
#     cleanLine = line.strip()

#     if '.' in cleanLine:
#       columns = cleanLine.split()
#       if columns[0] == numVlan:
#         print('%-6s %-15s %7s' % (columns[0], columns[1], columns[3]))