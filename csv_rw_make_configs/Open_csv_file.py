import csv
#The purpose of this script is to read a csv file 
#and capture a column and a row with list and zip functions
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
            items1.strip()
        for items2 in sys_name:
            items2.strip()
        if items1=='ASR 1002-X':
            os_interface = (transposed_csv[os_interface_list][i])
            Interface_list = os_interface.split(',')
            print(items1)
            print(items2)
            #print(Interface_list)
            for items3 in Interface_list:
                t = items3.strip()
                r = (t.strip("[]"))
                print(r.strip("'"))
        elif items1=='Cisco 2921 Router':
            os_interface = (transposed_csv[os_interface_list][i])
            Interface_list = os_interface.split(',')
            print(items1)
            print(items2)
            # print(Interface_list)
            for items3 in Interface_list:
                t = items3.strip()
                r = (t.strip("[]"))
                print(r.strip("'"))
        elif items1=='Nexus 7010 Switch':
            os_interface = (transposed_csv[os_interface_list][i])
            Interface_list = os_interface.split(',')
            print(items1)
            print(items2)
            # print(Interface_list)
            for items3 in Interface_list:
                t = items3.strip()
                r = (t.strip("[]"))
                print(r.strip("'"))
