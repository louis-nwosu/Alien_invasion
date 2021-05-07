##ceaser cipher

##encryption
#plain_text = input('enter a message to be encrypted: ')
#distance = input('enter the distance value: ')
#code = ''
#for ch in plain_text:
# ord_value = ord(ch)
# cipher_value = int(ord_value) + int(distance)
# if cipher_value > ord('z'):
# cipher_value = int(ord('a')) + int(distance) - int(
# (ord('z') - ord_value + 1))
# code += chr(cipher_value)
#print(code)

##decryption
#en_code = input('enter the encrypted code here: ')
#en_distance = input('enter distance value: ')
#d_plain_text = ''
#if en_code == '':
# en_code = code
#en_distance = distance
#for ch in en_code:
# en_ord_value = ord(ch)
# en_cipher_value = int(en_ord_value) - int(en_distance)
# if en_cipher_value < ord('a'):
# en_cipher_value = ord('z') - int(en_distance) - (ord('a') -
#                     en_ord_value - 1)
# d_plain_text += chr(en_cipher_value)
#print(d_plain_text)
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 6, 2]


def get_median(lst):
    length = len(lst)
    if length % 2 != 0:
        get_mid = (length + 1) / 2
        median = lst[int(get_mid) - 1]
        print(median)
    else:
        get_mid_index = length / 2
        get_mid_1 = lst[int(get_mid_index)]
        get_mid_2 = lst[int(get_mid_index) - 1]
        median = float((get_mid_1 + get_mid_2) / 2)
        print(median)


get_median(my_list)

######dictionaries
mydict = {'name': 'nonso', 'email': 'louis@gmail.com'}
mydict['name'] = 'egbon'
print(mydict.items())
print(mydict.get('pussy', 'squirt'))
##for (key, value) in mydict.items():
##print( key, ':', value)

#### finfing the mode of a list
myList = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c', 'c', 'g', 'f']


def mode(lst):
    freq = {}
    for cur in lst:
        letter = freq.get(cur, None)
        if letter == None:
            freq[cur] = 1
        else:
            freq[cur] = letter + 1
    return freq


frequency = mode(myList)


def findMode(freq):
    freq_list = list(freq.values())
    biggest_num = max(freq_list)
    for key in freq.keys():
        if freq[key] == biggest_num:
            print(f' the mode of the array is {key}')


findMode(frequency)

"""

# a python program to check if a number is a polindron

def Palindrone(number):
   median_num = find_median(number)
   num_str = str(number)
   num_list = list(num_str)
   start_list = num_list[:median_num]
   end_list = num_list[median_num + 1:]
   isPalidrone = check_match_index(start_list, end_list)
   if(isPalidrone):
       print('the number in question is a polidrone')
   else:
       print('the number you provided is not a palidrone')

def check_match_index(lst_1, lst_2):
    lst_2_len = len(lst_2)
    for num in lst_1:
        if num == lst_2[lst_2_len - 1]:
            lst_2_len = lst_2_len - 1
        else:
            return False
    return True
        
def find_median(number):
    num_str = str(number)
    num_list = list(num_str)
    if len(num_str) % 2 != 0:
        mid_index = int((len(num_list) + 1) / 2 - 1)
        return mid_index
    else:
        mid_index = int(len(num_list) / 2)
        first = num_list[mid_index - 1]
        Second = num_list[mid_index]
        return [first, Second]

Palindrone(123454321)
