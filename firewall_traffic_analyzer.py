# FILE NAME - firewall_traffic_analyzer.py

# NAME: Ethan Carson
# DATE: 10/5/2025
# BRIEF DESCRIPTION:  This program identifies potentiall risks in a firewall based on user input for port used and data transfer size.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
print('=== Network Traffic Security Analyzer ===\n')
port = int(input('Enter the port number (e.g., 80, 22, 443, 3389): '))
data_size = int(input('Enter the data transfer size in megabytes (MB): '))
print(f'\nFIREWALL LOG:\nPort: {port}, Transfer Size: {data_size} MB')
#Checks
if (port == 22 or port == 3389) and data_size >= 100:
    print('Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!\n------------------------')
elif port == 80 and data_size > 100:
    print('Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.\n------------------------')
elif port == 443:
    print('Risk Assessment: LOW RISK: Secure encrypted transfer detected.\n------------------------')
else: print('Risk Assessment: UNKNOWN: Unrecognized traffic pattern.\n------------------------')









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 12

FIREWALL LOG:
Port: 22, Transfer Size: 12 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?

Not really, no. Like I said last lab, they are more intuitive then they are in JS, and I understand those pretty well.





'''
