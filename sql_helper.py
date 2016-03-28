def generate_add_host_sql(request):
    v_business_dep=request.form.get('business_dep')
    v_business_contact=request.form.get('business_contact')
    v_ip = request.form.get('ip')
    v_environment = request.form.get('environment')
    v_service_ports = request.form.get('service_ports')
    v_ipmi_address = request.form.get('ipmi_address')
    v_location = request.form.get('location')
    v_services = request.form.get('services')
    v_os_type = request.form.get('os_type')
    v_tech_contact = request.form.get('tech_contact')
    create_sql = '''INSERT INTO hostinfo (ip,os_type,services,business_dep,service_ports,location,ipmi_address,business_contact,tech_contact,environment) \
           values \
      ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');'''%(v_ip,v_os_type,v_services,v_business_dep,v_service_ports,v_location,v_ipmi_address,v_business_contact,v_tech_contact,v_environment)
    return create_sql


def generate_update_host_sql(request):
    business_dep=request.form.get('business_dep')
    business_contact=request.form.get('business_contact')
    ip = request.form.get('ip')
    environment = request.form.get('environment')
    service_ports = request.form.get('service_ports')
    ipmi_address = request.form.get('ipmi_address')
    location = request.form.get('location')
    services = request.form.get('services')
    os_type = request.form.get('os_type')
    tech_contact = request.form.get('tech_contact')
    row_id = request.form.get('DT_RowId')
    update_sql = '''update hostinfo set business_dep = '%s', business_contact= '%s', ip = '%s', environment = '%s', service_ports = '%s', ipmi_address = '%s', location = '%s', services = '%s', os_type = '%s', tech_contact = '%s' where DT_RowId = %s '''%(business_dep,business_contact,ip,environment,service_ports,ipmi_address,location,services,os_type,tech_contact,row_id)
    return update_sql

def generate_delete_host_sql(request):
    row_id = request.form.get('DT_RowId',None)
    del_sql = 'delete from hostinfo where DT_RowId= %s ;'%(row_id)
    return del_sql

def generate_list_host_sql(request):
    offset,limit = request.args.get('jtStartIndex','0'),request.args.get('jtPageSize','10')
    show_host_sql = 'select * from hostinfo limit %s offset %s ;'%(limit,offset)
    return show_host_sql
