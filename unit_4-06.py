# created by Matthew Walsh
# created for ics3u
# created on nov 2017
# compares if strings are the same 


def compare_strings(string_1, string_2):
	# compare strings
  string_1_upper = string_1.upper()
  string_2_upper = string_2.upper()
  if str(string_1_upper) == str(string_2_upper):
  	return True
  else:
  	return False 
  	
  	
def main():
	#get inputs
  string_1 = raw_input('enter a string: ')
  string_2 = raw_input('enter another string: ')
  print(compare_strings(string_1, string_2))
  
main()

