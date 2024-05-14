#Source: https://stackoverflow.com/questions/57441298/attributeerror-x962
server = SSHTunnelForwarder(
    ('<ssh_host>', 22),
    ssh_username="<ssh_user>",
    ssh_config_file='<path_to_config>',
    ssh_pkey="<path_to_pkey>",
    remote_bind_address=('127.0.0.1', 5432)
)

server.start()