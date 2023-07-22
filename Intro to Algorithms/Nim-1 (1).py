#  File: Nim.py

#  Description: This program determines the best first move of the game NIM.

#  Student's Name: Jordan Weeks

#  Student's UT EID: Jaw6235
 
#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 50295

#  Date Created: 1/31/2020

#  Date Last Modified: 1/30/2020

#  Input: heaps is a list of integers giving the count in each heap
#  Output: function returns a single integer which is the nim-sum

heaps = [8, 13, 5] #these are the theoretical values for the heaps, these numbers are for testing

def nim_sum (heaps):
    if len(heaps) == 0: #this assigns nim_sum to 0 if there are no piles
        return (0)
    else:
        ns = heaps[0]
        for i in range(1, len(heaps)): #using range here compiles nim_sum a correct number of times
            ns = ns^(heaps[i])
        return ns #I changed nim_sum to ns instead of nim_sum to avoid conflicts with the function

#  Input: heaps is a list of integers giving the count in each heap
#         nim_sum is an integer 
#  Output: function returns two integers. The first integer is number
#          of counters that has to be removed. The second integer is
#          the number of the heap from which the counters are removed.
#          If the nim_sum is 0, then return 0, 0

def find_heap (heaps, ns):
    for i in range(len(heaps)): #I did not use range(1, ...) here since I want i to start at 0
        if i == len(heaps)-1:
            print('Lose Game') #no more possibilities so you lose game
        if heaps[i]^ns < heaps[i]:
            counters = (heaps[i]) - (heaps[i]^ns) #this calcuates the number to take from heap
            final_heap = i+1 #this is a counter to determine which heap to take the counters from
            print('Remove {} counters from Heap {}'.format(counters, final_heap)) #prints requested output
            return counters, final_heap
    return '(0,0)' #if no scenario works, return '0, 0' is the assumption
def main():
    print(nim_sum(heaps)) #prints nim_sum (for testing)
    print(find_heap(heaps, nim_sum(heaps))) #prints either lose game or how to win
    
  # call function nim_sum() with inputs as given

  # call function find_heap() with inputs as given

  # print the results

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
      main()




    
