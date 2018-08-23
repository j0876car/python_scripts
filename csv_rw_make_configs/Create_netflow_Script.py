import csv


def ASR_Config(int_list,os_sys):
    print('Start of ASR Config for ',os_sys)
    Template=open('ASR-Netflow_Base_config_v1.1.txt')
    f_OS=open(os_sys,"w")
    f_OS.write('ssh into ' + os_sys+'\n')
    f_OS.write('!\n')
    f_OS.write('conf t\n')
    for items in Template:
        #print(items)
        f_OS.write(items)
    for elements in int_list:
        t = elements.strip()
        r = (t.strip("[]"))
        interface = (r.strip("'"))
        f_OS.write('interfaces '+interface+'\n')
        f_OS.write('ip flow monitor wan_monitor_v9 output\n')
        f_OS.write('ip flow monitor wan_monitor_v9 input\n')
        f_OS.write('!\n')
    f_OS.write('end\n')
    f_OS.write('copy run start\n')
    f_OS.write('!\n')
    f_OS.write('exit\n')
    print('End of ASR Config')
def IOS_Config(int_list,os_sys):
    print('Inside IOS Config')
    Template=open('IOS-2900-3900-Netflow_Base_config_v1.1.txt')
    f_OS = open(os_sys, "w")
    f_OS.write('ssh into ' + os_sys + '\n')
    f_OS.write('!\n')
    f_OS.write('conf t\n')
    for items in Template:
        # print(items)
        f_OS.write(items)
    for elements in int_list:
        t = elements.strip()
        r = (t.strip("[]"))
        interface = (r.strip("'"))
        f_OS.write('interfaces ' + interface + '\n')
        f_OS.write('ip flow monitor wan_monitor_v9 output\n')
        f_OS.write('ip flow monitor wan_monitor_v9 input\n')
        f_OS.write('!\n')
    f_OS.write('end\n')
    f_OS.write('copy run start\n')
    f_OS.write('!\n')
    f_OS.write('exit\n')
    print('End of IOS Config')
def NXOS_Config(int_list,os_sys):
    print('Inside NX-OS Config')
    Template=open('NX-OS-Netflow_Base_config_v1.1.txt')
    f_OS = open(os_sys, "w")
    f_OS.write('ssh into ' + os_sys + '\n')
    f_OS.write('!\n')
    f_OS.write('conf t\n')
    for items in Template:
        # print(items)
        f_OS.write(items)
    for elements in int_list:
        t = elements.strip()
        r = (t.strip("[]"))
        interface = (r.strip("'"))
        f_OS.write('interfaces ' + interface + '\n')
        f_OS.write('ip flow monitor wan_monitor_v9 output\n')
        f_OS.write('ip flow monitor wan_monitor_v9 input\n')
        f_OS.write('!\n')
    f_OS.write('end\n')
    f_OS.write('copy run start\n')
    f_OS.write('!\n')
    f_OS.write('exit\n')
    print('End of NXOS Config')

os_ver=int(input('What OS version type 2:'))
os_hostname=int(input('What OS Name type 3:'))
os_interface_list=int(input('What is int list Name type 11:'))

for i in range(41):
    with open('CopyofNetflowExporters-v1.5-csv.csv') as csvfile:
        csvitem=csv.reader(csvfile)
        transposed_csv = list(zip(*csvitem))
        os_flavor=(transposed_csv[os_ver][i])
        os_type=os_flavor.split(',')
        os_name = (transposed_csv[os_hostname][i])
        sys_name = os_name.split(',')
        os_interface = (transposed_csv[os_interface_list][i])
        Interface_list = os_interface.split(',')
        for items1 in os_type:
            os_1=items1.strip()
        for items2 in sys_name:
            os_2=items2.strip()
        if items1=='ASR 1002-X':
            os_interface = (transposed_csv[os_interface_list][i])
            Interface_list = os_interface.split(',')
            ASR_Config(Interface_list,os_2)
            for items3 in Interface_list:
                t = items3.strip()
                r = (t.strip("[]"))
                k=(r.strip("'"))
        elif items1=='Cisco 2921 Router':
            os_interface = (transposed_csv[os_interface_list][i])
            Interface_list = os_interface.split(',')
            IOS_Config(Interface_list, os_2)
            for items3 in Interface_list:
                t = items3.strip()
                r = (t.strip("[]"))
                k = (r.strip("'"))
        elif items1=='Nexus 7010 Switch':
            os_interface = (transposed_csv[os_interface_list][i])
            Interface_list = os_interface.split(',')
            NXOS_Config(Interface_list, os_2)
            for items3 in Interface_list:
                t = items3.strip()
                r = (t.strip("[]"))
                k = (r.strip("'"))




