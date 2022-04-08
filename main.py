#%% Function to update a string position
def update_string(txt: str, position: int, char: str) -> str:
    '''
    Update a string at the given position

    Parameters
    ----------
    txt : str
        The string to update
    position : int
        The position to update
    char : str
        The new character

    Raises
    ------
    Exception
        Either char is not a single character, or position is out of range

    Returns
    -------
    str
        The updated string

    '''
    
    if position < len(txt):
        if len(char) == 1:
           return txt[0:position] + char + txt[(position + 1):]
        
        else:
            raise Exception("from update_string: char must be a single character")
    
    else:
        raise Exception("from update_string: position must be smaller than the length of txt")
          
#%% Function to mark multiples in a range

def mark_multiples(num: int, bitstring: str) -> (bool, str):
    '''
    Marks the multiples of a given number in a bitstring denoting
    a list of numbers. Each number n is at position (n - 1).

    Parameters
    ----------
    num : int
        The number for which to mark multiples of
    bitstring : str
        The string consisting of 0's and 1's. After the marking operation,
        all positions marked with 0 are divisible by num

    Returns
    -------
    (bool, str)
        A tuple in which the bool part part denotes success of the
        marking operation, and the str part is the marked bitstring.

    '''
    
    # get the max range
    max_range: int = len(bitstring)

    # use this condition to determine if marking is possible
    if num ** 2 <= max_range:
        # mark all multiples of num
        for pos in range(num ** 2, max_range + 1, num):
            # mark the multiple as not prime if not already marked
            if bitstring[pos - 1] == '1':
                bitstring = update_string(bitstring, pos - 1, '0')

        # return tuple containing marked bitstring and denoting success
        return (True, bitstring)

    else:
        # return tuple containing unmarked bitstring and denoting failure
        return (False, bitstring)

#%% Function to return a sieved list

def get_sieve(max_range: int) -> str:
    '''
    Generates a bitstring denoting a list of numbers. Each number n is 
    at position (n - 1). After the sieving operation, prime number
    positions are marked as 1's, and positions with prime multiples
    are marked as 0's

    Parameters
    ----------
    max_range : int
        The upper limit of the bitstring

    Returns
    -------
    str
        A bit string denoting a list of primes (marked with 1)
        and a non primes (marked with 0)

    '''
    
    if max_range > 0:
        # get an initial bitstring of 1's of length max_range
        n_bitstring: str = "1" * max_range

        # initialize the variables used in keeping track of
        # the computation:
        
        # 1 is not a prime, mark the position of 1 as false
        n_bitstring = update_string(n_bitstring, 0, '0')
        
        # keeps track of whether new multiples where marked 
        # by the mark multiples function. The variable is marked 
        # True because the first marking operation in the previous
        # line was successful
        new_multiples_marked: bool = True
        
        # r_bitstring is the result bitstring to finally return
        r_bitstring: str = n_bitstring     

        # the next prime is 2 at position 1
        prime_pos: int = 1           

        # initialize the first prime
        prime: int = 2
        
        # repeat the marking operation while the previous marking 
        # operation is succeessful
        while new_multiples_marked:
            # mark the multiples of prime in r_bitstring
            sieve_result =  mark_multiples(prime, r_bitstring)

            # get success/failure of marking operation
            new_multiples_marked = sieve_result[0]    
            
            # get the result bitstring
            r_bitstring = sieve_result[1]       
            
            # try getting the position of the next prime
            try:
                # get the position of the prime to be used for the next iteration
                # might throw an exception if index not found
                prime_pos = r_bitstring.index('1', prime_pos + 1) 
                        
                # get the next prime
                prime = prime_pos + 1

            except:
                pass

        # return the result bitstring
        return r_bitstring

    else:
        return ""


#%% Get user input

def get_input(prompt: str) -> None:
    '''
    Prompts the user for input until the user enters a non negative
    whole number

    Parameters
    ----------
    prompt : str
        The prompt to display to the user

    Returns
    -------
    None
        DESCRIPTION.

    '''
    
    # the number to return
    num: int = 0

    # repeat the operation indefinitely while the user
    # enters a wrong input
    while True:
        try:
            # try getting user input
            num = int(input(prompt))

        except:
            # The user entered non integer input
            print("You entered a non numeric input or a float")
            print("Please enter a non negative integer")

        else:
            if num < 0:
                # The user entered a negeative number
                print("You entered a negative number")
                print("Please enter a non negative integer")

            else:
                # User input OK; stop the loop
                break

    # return the input
    return num

#%% Function to printout a list of numbers

def printout(lst: list, num_per_line: int) -> None:
    '''
    Print out the list line by line, with num_per_line
    items per line

    Parameters
    ----------
    lst : list
        The list to print out
    num_per_line : int
        The number of items per line

    Raises
    ------
    Exception
        num_per_line param must be greater than 0

    Returns
    -------
    None
        DESCRIPTION.

    '''
    
    if num_per_line > 0:
        # The final output list stores the output line by line
        output_list: list = []

        # The number of lines having num_per_line items
        q = len(lst) // num_per_line
        
        # The last line will have r items
        r = len(lst) % num_per_line
        
        # the max number of digits. This will help with formatting
        # each number. If the maximum num was 512, max_num_digits
        # will be 3, so all numbers will be formatted to have
        # a width of 3.
        last_num = lst[len(lst) - 1]
        max_num_digits: int = len(str(last_num))

        # Construct the output list, line by line
        # run the loop q times
        for i in range(0, q):
            # get the start of the list slice
            start = i * num_per_line
            
            # get the end of the list slice
            end = start + num_per_line

            # construct a list of numbers formatted to the width max_num_digits
            # and selected from the range  (start:end)
            tlist = [f"{str(n):>{max_num_digits}}" for n in lst[start:end]]
            
            # convert the tlist to a string and append it to output list
            output_list.append(", ".join(tlist))

        # append the leftovers:
            
        # get the start and end for the last list slice
        start = q * num_per_line
        end = start + r

        # construct a list of numbers formatted to the width max_num_digits
            # and selected from the range  (start:end)
        tlist = [f"{str(n):>{max_num_digits}}" for n in lst[start:end]]
        
        # convert the tlist to a string and append it to output list
        output_list.append(", ".join(tlist))


        # print out the final output list
        print("\n".join(output_list))

    else:
        # since num_per_line is greater than 0, raise an exception
        raise Exception("from printout: num_per_line param must be greater than 0")
    

#%% Get non primes
def extract_non_primes(bitstring: str, lower_limit: int, 
                       upper_limit: int) -> list:
    '''
    Extract the non primes from the input bitstring

    Parameters
    ----------
    bitstring : str
        The string consisting of 0's and 1's. All positions marked
        with 1's are prime, and all positions marked with 0's are
        non primes
        
    lower_limit : int
        The lower limit of the range
    upper_limit : int
        The upper limit of the range

    Returns
    -------
    list
        A list containing the non primes in the 
        range (lower_limit:upper_limit), both inclusive

    '''
    
    # create a list of numbers from the bitstring:
        
    # all elements are in the form (i + 1), since if i
    # is the position, (i + 1) will be the number at that position    
    # Also, the lower_limit and upper_limit denote the numbers
    # not positions
    
    # Since all elements are in the form (i + 1), the lower_limit has
    # to be shifted back (that is, lower_limit - 1), otherwise it 
    # will be skipped
    
    # The upper limit of the range will be included since all elements
    # are in the form (i + 1)
    return [(i + 1) for i in range(lower_limit - 1, upper_limit) 
                    if bitstring[i] == '0']

#%% The main program

# get the range limits
fnum: int = get_input("Enter the beginning of the range: ")
snum: int = get_input("Enter the end of the range: ")

# check the order in which the numbers were entered
# and correct them
if fnum <= snum:
    lower_limit = fnum
    upper_limit = snum

else:
    lower_limit = snum
    upper_limit = fnum

# get the sieved list of numbers from 1 to max
bitstring = get_sieve(upper_limit)

# get the non primes in the range (lower_limit:upperlimit) inclusive
non_primes_in_range = extract_non_primes(bitstring, lower_limit, upper_limit)

# display the non primes
print(f"Non Primes in range: {lower_limit} to {upper_limit}")
printout(non_primes_in_range, 10)
