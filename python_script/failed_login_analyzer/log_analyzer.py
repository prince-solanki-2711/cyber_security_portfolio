import re

file_handler = open("mock_auth_data.txt","rt")

ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

ip_counts = {}
username_counts = {}

#=============================================================================================================================
# if file_handler:
#     print("Found")
# else:                       # checking if file exist or not
#     print("Not Found")
#==============================================================================================================================

for line in file_handler:
    if "Failed password" in line:
        match = re.search(ip_pattern,line)

        if match:
            ip = match.group()        # this section is use to extract failed password and after it 
                                      # extract the ip and then it counts the ip occurrence and store 
            if ip in ip_counts:       # it in the dictinory has a key value pair
                ip_counts[ip] +=1

            else:
                ip_counts[ip] = 1

print("===================================================================================")
print("Failed Login Attempts")
print("===================================================================================")        

# failed login report generate 

for ip, count in ip_counts.items():
    print(f"{ip} → {count}")

print("===================================================================================")

#===============================================================================================================================

suspicious_limit = 5

for ip, count in ip_counts.items():

    if count > suspicious_limit:        # generating the report of suspicious ip failed attempts for than 5 times
        
        print("Sucpicous Attempts")
        print(f"{ip} -> {count} Failed Attempts More Than Five Times")

file_handler.seek(0)
print("===================================================================================")   

#===============================================================================================================================

username_pattern = r"Failed password for (\S+)"

for line1 in file_handler:

    if "Failed password" in line1:

        match_user = re.search(username_pattern,line1)  # finding user name who is targeted and grouping them with their counts

        if match_user:
            username = match_user.group(1)

            if username in username_counts:
                username_counts[username] += 1
            else:
                username_counts[username] = 1

print("Targeted Username")
print("===================================================================================") 
for username,counts in username_counts.items():
    print(f"{username} -> {counts}")

#================================================================================================================================
file_handler.close()        # closing the file

