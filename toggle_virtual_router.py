#! python3

import os

test = os.popen("netsh.exe wlan show hostednetwork").read()

#converts test to a list[]
test_list = [y for y in (x.strip() for x in test.splitlines()) if y]

if "Not started" in test_list[-1]:
    print("Starting the virtual router...")
    result = os.popen("netsh.exe wlan start hostednetwork").read()
elif "Number of clients" in test_list[-2] and "0" not in test_list[-2]:
    result = "\nIf attempting to turn off the virtual router, please disconnect all connected clients first and try again."
elif "Started" in test_list[-5]:
    print("Stopping the virtual router...")
    result = os.popen("netsh.exe wlan stop hostednetwork").read()
else:
    result = "Something is wrong... \n"

print(result)
os.system('netsh.exe wlan show hostednetwork')
os.system('pause')