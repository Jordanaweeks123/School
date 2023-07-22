#  File: Pancake.py

#  Description: Finds the most efficient way to sort a stack of pancakes only being able to reverse parts of the stack

#  Student's Name: Jordan Weeks

#  Student's UT EID: jaw6235

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 50295

#  Date Created: 2/21/2020

#  Date Last Modified: 2/21/2020

#  Input: pancakes is a list of positive integers
#  Output: a list of the pancake stack each time you
#          have done a flip with the spatula
#          this is a list of lists
#          the last item in this list is the sorted stack
def sort_pancakes ( pancakes ):
  every_flip = []
  first_flip = pancakes  #not necessary but made the algorithm easier to understand
  p_sorted = True  #this is to check if the program is already sorted
  for ctr in range(len(first_flip), 1, -1): #creates a counter to read the list backwards
      for i in range(len(pancakes)-1):
        if first_flip[i] > first_flip[i+1]:  #checks to see if the list is in order; prints false otherwise
            p_sorted = False
      if p_sorted:
          if (len(every_flip) == 0):  #if the list is sorted from the start, every_flip is appended to the original list
            every_flip.append(first_flip)  #appending only if every_flip == 0 stops duplicate appends at the end
          return(every_flip)
      find_max = max(first_flip[:ctr]) #finds the max value of the remaining function
      if first_flip[0] != max(first_flip[:ctr]): #skips moving max to front if max is already at front
        first_flip = list(reversed(first_flip[:first_flip.index(find_max)+1])) + first_flip[first_flip.index(find_max)+1:]
        every_flip.append(first_flip) #finds the max in the string, flips it to the front
      second_flip =  list(reversed(first_flip[:ctr]))+first_flip[ctr:]
      first_flip = second_flip #gets the max value now at the front and flips it to the next adjacent ctr spot
      every_flip.append(first_flip)
      p_sorted = True #checks in the above for loop to see if the string is now sorted
  return every_flip    # return a list of flipped pancake stacks

def main():
   #open the file pancakes.txt for reading
  in_file = open ("./pancakes.txt", "r")

  line = in_file.readline()
  line = line.strip()
  line = line.split()
  print (line)
  pancakes = [1, 3, 5, 1, 2, 3, 4, 5]
  for item in line:
    pancakes.append (int(item))

  # print content of list before flipping
  print ("Initial Order of Pancakes = ", pancakes)

  # call the function to sort the pancakes
  every_flip = sort_pancakes ( pancakes )

  # print the contents of the pancake stack after
  # every flip
  for i in range (len(every_flip)):
    print (every_flip[i])

  # print content of list after all the flipping
  print ("Final Order of Pancakes = ", every_flip[-1])

if __name__ == "__main__":
  main()