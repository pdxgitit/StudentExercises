# Given two text files containing numbers, return a list of the numbers
# that they share.  (Use happy.txt and primes.txt)

# This requires: reading a file, converting from strings to integers
# and some list manipulation

a_file = open('happy.txt', encoding='utf-8')
a_string = a_file.read()
a_file.close()
