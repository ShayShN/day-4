def reverse_string(ss:str):
    return ss[::-1]

def is_palindrome(ff:str):
    return ff[::].replace(' ', '') == ff[::-1].replace(' ', '')
  
  
# dd = "was it a cat i saw"      
# print(reverse_string(dd))
# print(is_palindrome(dd))