# Задание 7.1
# def generate_access_config(access):
#     """
#     access - словарь access-портов,
#     для которых необходимо сгенерировать конфигурацию, вида:
#     { 'FastEthernet0/12':10,
#       'FastEthernet0/14':11,
#       'FastEthernet0/16':17}
    
#     Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
#     """
#     access_template = [
#         'switchport mode access',
#         'switchport access vlan {}',
#         'switchport nonegotiate',
#         'spanning-tree portfast',
#         'spanning-tree bpduguard enable'
#     ]
    
#     config_list = []
#     for port, vlan in access.items():
#         config_list.append(f"interface {port}")
#         config_list.extend([cmd.format(vlan) if '{}' in cmd else cmd for cmd in access_template])
    
#     return config_list

# # Проверка работы функции
# access_dict = {
#     'FastEthernet0/12': 10,
#     'FastEthernet0/14': 11,
#     'FastEthernet0/16': 17,
#     'FastEthernet0/17': 150
# }

# config_output = generate_access_config(access_dict)

# # Вывод без лишних переводов строк
# print("\n".join(config_output))


# Задание 7.1а
# def generate_access_config(access, psecurity=False):
#     """
#     access - словарь access-портов,
#     для которых необходимо сгенерировать конфигурацию, вида:
#     { 'FastEthernet0/12':10,
#       'FastEthernet0/14':11,
#       'FastEthernet0/16':17}
#     psecurity - если True, добавляется конфигурация port-security.

#     Возвращает список всех портов в режиме access с конфигурацией на основе шаблона.
#     """
#     access_template = [
#         "switchport mode access",
#         "switchport access vlan {}",
#         "switchport nonegotiate",
#         "spanning-tree portfast",
#         "spanning-tree bpduguard enable"
#     ]

#     port_security_template = [
#         "switchport port-security",
#         "switchport port-security maximum 2",
#         "switchport port-security violation restrict",
#         "switchport port-security aging time 2",
#         "switchport port-security aging type inactivity"
#     ]

#     config_list = []
#     for port, vlan in access.items():
#         config_list.append(f"interface {port}")
#         config_list.extend([cmd.format(vlan) if '{}' in cmd else cmd for cmd in access_template])

#         # Добавление port-security, если psecurity=True
#         if psecurity:
#             config_list.extend(port_security_template)

#     return config_list

# # Проверка функции с psecurity=True (включен port-security)

# access_dict = {
#     'FastEthernet0/12': 10,
#     'FastEthernet0/14': 11,
#     'FastEthernet0/16': 17,
#     'FastEthernet0/17': 150
# }
# print("\n--- Конфигурация с Port Security ---")
# print("\n".join(generate_access_config(access_dict, psecurity=True)))

# print("\n" + "-"*50 + "\n")

# # Проверка функции с psecurity=False (без port-security)
# print("\n--- Конфигурация без Port Security ---")
# print("\n".join(generate_access_config(access_dict, psecurity=False)))


# Задание 7.1b
# def generate_access_config(access, psecurity=False):
#     """
#     access - словарь access-портов,
#     для которых необходимо сгенерировать конфигурацию, вида:
#     { 'FastEthernet0/12':10,
#       'FastEthernet0/14':11,
#       'FastEthernet0/16':17 }
    
#     psecurity - если True, добавляется конфигурация port-security.

#     Возвращает словарь:
#     - ключи: имена интерфейсов, вида 'FastEthernet0/1'
#     - значения: список команд, который надо выполнить на этом интерфейсе
#     """
#     access_template = [
#         'switchport mode access',
#         'switchport access vlan {}',
#         'switchport nonegotiate',
#         'spanning-tree portfast',
#         'spanning-tree bpduguard enable'
#     ]

#     port_security = [
#         'switchport port-security maximum 2',
#         'switchport port-security violation restrict',
#         'switchport port-security'
#     ]

#     config_dict = {}
#     for port, vlan in access.items():
#         config_list = [cmd.format(vlan) if '{}' in cmd else cmd for cmd in access_template]

#         # Добавление port-security, если psecurity=True
#         if psecurity:
#             config_list.extend(port_security)

#         config_dict[port] = config_list

#     return config_dict

# # Проверка работы функции
# access_dict = {
#     'FastEthernet0/12': 10,
#     'FastEthernet0/14': 11,
#     'FastEthernet0/16': 17,
#     'FastEthernet0/17': 150
# }

# print("Конфигурация без port-security:")
# for interface, commands in generate_access_config(access_dict).items():
#     print(f"{interface}:\n" + "\n".join(commands))

# print("\n" + "-"*50 + "\n")

# print("Конфигурация с port-security:")
# for interface, commands in generate_access_config(access_dict, psecurity=True).items():
#     print(f"{interface}:\n" + "\n".join(commands))


# Задание 7.3а
# def generate_trunk_config(trunk):
#     trunk_template = [
#         'switchport trunk encapsulation dot1q',
#         'switchport mode trunk',
#         'switchport trunk native vlan 999',
#         'switchport trunk allowed vlan'
#     ]

#     config_lines = []

#     for interface, vlans in trunk.items():
#         config_lines.append(f'interface {interface}')
#         for command in trunk_template:
#             if command.endswith('allowed vlan'):
#                 vlan_list = ','.join(str(vlan) for vlan in vlans)
#                 config_lines.append(f'{command} {vlan_list}')
#             else:
#                 config_lines.append(command)

#     return config_lines

# trunk_dict = {
#     'FastEthernet0/1': [10, 20, 30],
#     'FastEthernet0/2': [11, 30],
#     'FastEthernet0/4': [17]
# }


# result = generate_trunk_config(trunk_dict)
# for line in result:
#     print(line)

# Задание 7.4
# def get_int_vlan_map(filename):
#     access_ports = {}
#     trunk_ports = {}

#     with open(filename, 'r') as file:
#         current_interface = ''
#         for line in file:
#             line = line.strip()

#             if line.startswith('interface'):
#                 current_interface = line.split()[-1]

#             elif line.startswith('switchport access vlan'):
#                 vlan = int(line.split()[-1])
#                 access_ports[current_interface] = vlan

#             elif line.startswith('switchport trunk allowed vlan'):
#                 vlans = list(map(int, line.split()[-1].split(',')))
#                 trunk_ports[current_interface] = vlans

#     return access_ports, trunk_ports

# access_dict, trunk_dict = get_int_vlan_map('config_sw1.txt')

# print('Access-порты:')
# for port, vlan in access_dict.items():
#     print(f'{port}: VLAN {vlan}')

# print('\nTrunk-порты:')
# for port, vlans in trunk_dict.items():
#     print(f'{port}: VLANs {vlans}')


# # Задание 7.4
# def get_int_vlan_map(filename):
#     access_ports = {}
#     trunk_ports = {}

#     with open(filename, 'r') as file:
#         current_interface = ''
#         for line in file:
#             line = line.strip()

#             if line.startswith('interface'):
#                 current_interface = line.split()[-1]
#             elif line.startswith('switchport mode access'):
#                 access_ports[current_interface] = 1
#             elif line.startswith('switchport access vlan'):
#                 vlan = int(line.split()[-1])
#                 access_ports[current_interface] = vlan

#             elif line.startswith('switchport trunk allowed vlan'):
#                 vlans = list(map(int, line.split()[-1].split(',')))
#                 trunk_ports[current_interface] = vlans

#     return access_ports, trunk_ports


# access_dict, trunk_dict = get_int_vlan_map('config_sw2.txt')

# print('Access-порты:')
# for port, vlan in access_dict.items():
#     print(f'{port}: VLAN {vlan}')

# print('\nTrunk-порты:')
# for port, vlans in trunk_dict.items():
#     print(f'{port}: VLANs {vlans}')

# Задание 7.4а
# def check_ignore(command, ignore):
#     """
#     Функция проверяет содержится ли в команде слово из списка ignore.
#     command - строка. Команда, которую надо проверить.
#     ignore - список. Список слов, которые надо игнорировать.
#     Возвращает True, если в команде содержится слово из списка ignore, False - если не содержит.
#     """
#     for word in ignore:
#         if word in command:
#             return True
#     return False


# def config_to_dict(config):
#     """
#     config - имя конфигурационного файла.
#     Возвращает словарь с учетом всех уровней вложенности.
#     """
#     ignore = ['duplex', 'alias', 'Current configuration']
#     config_dict = {}
#     current_command = None
#     current_subcommands = []
#     current_level = config_dict

#     with open(config, 'r') as file:
#         for line in file:
#             line = line.strip()

#             if line.startswith('!') or check_ignore(line, ignore):
#                 continue


#             if not line.startswith(' '):
#                 if current_command:

#                     if current_subcommands:
#                         current_level[current_command] = current_subcommands
#                     else:
#                         current_level[current_command] = []
#                 current_command = line
#                 current_subcommands = []

#                 if line.startswith('interface ') or line.startswith('router '):

#                     current_level[line] = {}
#                     current_level = current_level[line]
#                 else:
#                     current_level = config_dict
#             else:
#                 if current_level != config_dict:
#                     subcommands_list = current_level.setdefault(current_command, [])
#                     subcommands_list.append(line)
#                 else:

#                     current_subcommands.append(line)

#         if current_command:
#             if current_subcommands:
#                 current_level[current_command] = current_subcommands
#             else:
#                 current_level[current_command] = []

#     return config_dict

# config_dict = config_to_dict('config_r1.txt')

# from pprint import pprint
# pprint(config_dict)