#Aditya Chunduru
#00335780
#Problem Set 6
#CIS 153 L8
#Program description: Dictionaries and tuples.


#Chapter 9 exercise 3 and 4
def email_addresses():   
    #dictionary of all emails from the file
    Dict = {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
            'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
            'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
            'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
            'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
            'ray@media.berkeley.edu': 1}
    largest = None    
    for itervar in Dict:
        if largest is None or Dict[itervar] > Dict[largest]:
            largest = itervar

    print('Largest:', largest)

    
email_addresses()


#Chapter 9 exercise 5/ exercise 1 and 2 chapter 10 revision
hour_counts = {}


file_name = input("enter a file name:")

try:
    with open (file_name, 'r') as file:  
        for line in file: 
            if line.startswith('From'): 
                parts = line.split()

                if len(parts) >= 6:


                    time = parts[1]

                    hour = time.split(':')[0]

                    hour_counts[hour] = hour_counts.get(hour, 0) + 1


    sorted_counts = sorted(hour_counts.items())


    for hour, count in sorted_counts:
        print(hour, count)




except FileNotFoundError:
    print(f"File '{file_name}' not found ")





