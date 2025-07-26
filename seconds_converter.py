# str_seconds = input("Please enter the number of seconds you wish to convert")
# total_secs = int(str_seconds)

# hours = total_secs // 3600
# secs_still_remaining = total_secs % 3600
# minutes =  secs_still_remaining // 60
# secs_finally_remaining = secs_still_remaining  % 60

# print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

str_seconds = input("Enter the number of seconds you want to convert : ")
total_seconds = int(str_seconds)

hours = total_seconds//3600
# print(f"{hours} hours")
remaning_seconds = total_seconds % 3600
print(f"Remaining Seconds: {remaning_seconds}")
minutes = remaning_seconds // 60
# print(f"{minutes} minutes")
seconds = remaning_seconds % 60
print(f"{hours} hours {minutes} minutes and {seconds} seconds")
