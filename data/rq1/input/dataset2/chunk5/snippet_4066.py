#Source: https://stackoverflow.com/questions/52556478/pyvbox-typeerror
vm = vbox.find_machine(vm_name)
session = vm.create_session()
guest_session = session.console.guest.create_session(vm_username, vm_password)
guest_session.execute('C:\\Program Files\\Internet Explorer\\iexplore.exe', [url])