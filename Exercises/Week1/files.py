# 'r' when the file will only be read
# 'w' for only writing (an existing file with the same name will be erased)
# 'a' opens the file for appending; any data written to the file is automatically
# added to the end.
# 'r+' opens the file for both reading and writing.

txt = open("happy.txt", 'a')
data = txt.read()
txt.close()

print(data)
