import subprocess
com = 'route PRINT 0* -4 | findstr 0.0.0.0'.split()
interface_temp = subprocess.check_output(com, shell=True).decode('cp866')
ip_route = interface_temp.split()[-3]
print(ip_route)

########################################################################