print 'DROP TABLE IF EXISTS hostinfo;'
print 'create  table hostinfo(DT_RowId INTEGER PRIMARY KEY AUTOINCREMENT,ip text NULL UNIQUE,os_type varchar(10),services varchar(30),business_dep varchar(30),service_ports varchar(30),location varchar(10),ipmi_address varchar(30),business_contact varchar(30),tech_contact  varchar(30),environment varchar(10));'
f = open('sample.txt','r').readlines()
for line in f:
#    v_ip,v_os_type,v_service,v_service_dep,v_service_ports,v_location,v_ipmi_address,v_business_contact,v_tech_contact,v_environment = line.split()
    print '''INSERT INTO hostinfo (ip,os_type,services,business_dep,service_ports,location,ipmi_address,business_contact,tech_contact,environment) \
           values \
      ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');'''%tuple(line.split())
