#  File: BabyNames.py

#  Description: This program sorts the top 1000 baby names in various different ways.  

#  Student Name:  Jordan Weeks

#  Student UT EID:  jaw6235

#  Course Name: CS 313E

#  Unique Number: 50295

#  Date Created: 2/5/2020

#  Date Last Modified: 3/4/2020


class BabyNames(object):

    with open('C:/Users/jorda/desktop/names.txt', 'r') as f:
                file_name = f.read
  # Initializes the dictionary that will hold all the baby names
    def __init__(self):
        with open('C:/Users/jorda/desktop/names.txt', 'r') as f:
                file_name = f.read
                self.file_name = file_name
                baby_dict = {}
                self.baby_dict = baby_dict
                self.fill_data(file_name)
    # key: name
    # value: list of ranks


  # Reads in the file and adds to the dictionary
    def fill_data(self, file_name):
        f = open('C:/Users/jorda/desktop/names.txt', 'r')
        i = 0
        try:
            while True:
                f_line = f.readline()
                if not f_line:
                    break
                f_line = f_line.split()
                for i in range(1, len(f_line)):
                    f_line[i] = int(f_line[i])
                self.baby_dict[f_line[0]] = f_line[1:]
        except:
            return('an error occured')

    # True if a name exists in the dictionary and False otherwise.
    def contains_name (self, name):
        try:
            if name in self.baby_dict:
                return True
        except:
            print(name, 'is not in list')
            raise Exception()

# Returns all the rankings for a given name. Assume the name exists
    def find_ranking(self, name):
        if BabyNames.contains_name(self, name):
            decade_pop = self.baby_dict[name]
        return(decade_pop)

    #  Returns a list of all the names that have a rank in a given decade in order of rank.
    def ranks_of_a_decade(self, decade):
        app_names = []
        ranks = {}
        names = []
        decade = (int(decade)%1900)//10
        for i in self.baby_dict:
            if self.baby_dict[i][decade] != 0:
                app_names.append([self.baby_dict[i][decade], i])
        app_names.sort()
        for i in range(len(app_names)):
            names.append(app_names[i][1])
        print(names)

# Returns a list of names that have a rank in all the decades in sorted order by name.
    def ranks_of_all_decades(self):
        list_dict = []
        names = []
        for i in self.baby_dict:
            temp = True
            for j in self.baby_dict[i]:
                if j == 0:
                    temp = False
            if temp:
                list_dict.append(i)
        for i in list_dict:
            names.append(i)
        return names


    # Return all names that are getting more popular in every decade. The list must be sorted by name.
    def getting_popular(self):
        popularity = []
        temp_list = []
        temp = True
        for i in self.baby_dict:
            for j in range(len(self.baby_dict[i])):
                if self.baby_dict[i][j] == 0:
                    self.baby_dict[i][j] = 2000
            if self.baby_dict[i] == sorted(self.baby_dict[i], reverse = True):
                popularity.append(i)
        return popularity


# Return all names that are getting less popular in every decade. The list must be sorted by name.
    def less_popular(self):
        popularity = []
        temp_list = []
        temp = True
        for i in self.baby_dict:
            for j in range(len(self.baby_dict[i])):
                if self.baby_dict[i][j] == 0:
                    self.baby_dict[i][j] = 2000
            if self.baby_dict[i] == sorted(self.baby_dict[i]):
                popularity.append(i)
        return popularity



def main():
    myBabyNames = BabyNames()
    print('Options:\n Enter 1 to search for names.\n Enter 2 to display data for one name.\n Enter 3 to display all names that appear in only one decade.\n Enter 4 to display all names that appear in all decades.\n Enter 5 to display all names that are more popular in every decade.\n Enter 6 to display all names that are less popular in every decade.\n Enter 7 to quit.')
    choice = int(input())
    while choice != 7:
        if choice == 1:
            print('name to find:', 'press 7 to quit')
            name = input()
            if name == '7':
                print('goodbye.')
                break
            final = myBabyNames.contains_name(name)
            print(final)
        if choice == 2:
            print('name to find:', 'enter 7 to quit')
            name = input()
            if name == '7':
                print('goodbye.')
                break
            final = myBabyNames.find_ranking(name)
            print(final)
        if choice == 3:
            print('choose decade')
            decade = input()
            final = myBabyNames.ranks_of_a_decade(decade)
            print(final)
            break
        if choice == 4:
            final = myBabyNames.ranks_of_all_decades()
            print(final)
            break
        if choice == 5:
            final = myBabyNames.getting_popular()
            print(final)
            break
        if choice == 6:
            final = myBabyNames.less_popular()
            print(final)
            break
    if choice == 7:
        print('goodbye.')


if __name__ == '__main__':
        main()

