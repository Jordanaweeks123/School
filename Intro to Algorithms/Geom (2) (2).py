#  File: Geom.py

#  Description: Program uses Python classes to model geometrical concepts

#  Student Name: Jordan Weeks

#  Student UT EID: Jaw6235

#  Partner Name: Alec Biggerstaff

#  Partner UT EID: ajb5766

#  Course Name: CS 313E

#  Unique Number: 50295

#  Date Created: 2/13/20

#  Date Last Modified: 2/13/20

import math
tol = 1.0e-6

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0):

        self.x = float(x)
        self.y = float(y)

    # get distance to other which is another Point object
    def dist (self, other):

        # using distance formula with two points
        dist = math.sqrt(((self.x-other.x)**2)+((self.y-other.y)**2))
        return round(dist,2)

    # create a string representation of a Point (x, y)
    def __str__ (self):

        # defines how the point is printed
        str_x = str(self.x)
        str_y = str(self.y)
        return '('+str_x+','+str_y+')'

    # test for equality between two points
    def __eq__ (self, other):

        # determines whether the two points are the same point or if they form a line
        x = False
        y = False
        if is_equal(self.x,other.x):
            x = True
        if is_equal(self.y,other.y):
            y = True
        if x and y:
            return True
        else:
            return False

class Line (object):
    # line is defined by two Point objects p1 and p2
    # constructor assign default values if user does not define
    # the coordinates of p1 and p2 or the two points are the same
    def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):

        # if both points are not the same, they will form a line
        if  (p1_x.__eq__(p2_x) and p1_y.__eq__(p2_y)) == False:
            
            self.p1_x = p1_x
            self.p1_y = p1_y
            self.p2_x = p2_x
            self.p2_y = p2_y
        
    # returns True if the line is parallel to the x axis 
    # and False otherwise
    def is_parallel_x (self):

        # determines if the slope of the line is close to zero
        if (self.p1_y-self.p2_y)/(self.p1_x-self.p2_x) <= tol:
            return True
        else:
            return False
        
    # returns True if the line is parallel to the y axis
    # and False otherwise
    def is_parallel_y (self):

        # determines if the slope of the line is close to infinity
        if (self.p1_y-self.p2_y)/(self.p1_x-self.p2_x) >= (1/tol):
            return True
        else:
            return False
        
    # determine slope for the line
    # return float ('inf') if line is parallel to the y-axis
    def slope (self):

        # calculates the slope of the line using rise over run
        numerator = (self.p1_y-self.p2_y)
        denominator = (self.p1_x-self.p2_x)

        # if the line is vertical, returns infinty
        if abs(denominator) <= tol:
            return float('inf')
        else:
            return numerator/denominator
        
    # determine the y-intercept of the line
    # return None if line is parallel to the y axis
    def y_intercept (self):

        # calculates the y-intercept of the line using y = mx + b
        slope = self.slope()
        if is_equal(self.p1_x,self.p2_x):
            return None
        else:
            return self.p1_y - (slope*self.p1_x)
        
    # determine the x-intercept of the line
    # return None if line is parallel to the x axis
    def x_intercept (self):

        # calculates the x-intercept of the line using the y-intercept and y = mx + b.
        # Returns none if slope is zero
        slope = self.slope()
        if is_equal(self.p1_y,self.p2_y):
            return None
        else:
            y_int = self.y_intercept()
            if abs(slope) >= (1/tol):
                return self.p1_x
            else:
                b = self.p1_y - (slope*self.p1_x)
                return (-b/slope)
        
    # returns True if line is parallel to other and False otherwise
    def is_parallel (self, other):

        # determines if two lines are parallel by comparing their slopes
        if is_equal(self.slope(),other.slope()):
            return True
        else:
            return False
        
    # returns True if line is perpendicular to other and False otherwise
    def is_perpendicular (self, other):

        # determines if two lines are perpendicular by comparing their slopes
        if is_equal(self.slope(),(-1/other.slope())):
            return True
        else:
            return False
        
    # returns True if Point p is on the line or an extension of it
    # and False otherwise
    def is_on_line (self, p):

        # determines if a point is on a line by using y = mx + b
        if self.y_intercept() == None:
            if is_equal(p.x,self.p1_x):
                return True
            else:
                return False
        elif is_equal(p.y,(self.slope()*self.p1_x) + self.y_intercept()):
            return True
        else:
            return False
        
    # determine the perpendicular distance of Point p to the line
    # return 0 if p is on the line
    def perp_dist (self, p):

        # calculates the perpendicular distance of a point to a line using the perpendicular distance formula
        # and the two points that describe the line
        if self.is_on_line(p):
            return 0
        else:
            numerator = abs((self.p2_y-self.p1_y)*p.x - (self.p2_x-self.p1_x)*p.y + self.p2_x*self.p1_y - self.p2_y*self.p1_x)
            denominator = math.sqrt((self.p2_y-self.p1_y)**2 + (self.p2_x-self.p1_x)**2)
            perp_dist = numerator / denominator
            
            return round(perp_dist,2)
            
    # returns a Point object which is the intersection point of line
    # and other or None if they are parallel
    def intersection_point (self, other):

        # finds the point of intersection of two lines if they are not parallel
        # using their y-intercepts and points slope form
        if self.is_parallel(other):
            return None
        # takes into account whether one of the lines is vertical and thus has no y-intercept
        elif self.y_intercept() == None:
            x = self.p1_x
            y = other.slope()*self.p1_x + other.y_intercept()
        elif other.y_intercept() == None:
            x = other.p1_x
            y = self.slope()*other.p1_x + self.y_intercept()
        else:
            # uses point slope form to calculate intersection point
            x = (other.y_intercept()-self.y_intercept())/(self.slope()-other.slope())
            y = (self.slope() * x) + self.y_intercept()
            if abs(x) == float(0):
                x = float(0)
            if abs(y) == float(0):
                y = float(0)
            intersection = Point(x,y)
            return intersection
        
    # return True if two points are on the same side of the line
    # and neither points are on the line
    # return False if one or both points are on the line or both 
    # are on the same side of the line
    def on_same_side (self, p1, p2):

        # determines if two given points are on the same side of a line by comparing their y-values to the y-values of the line at that x-value
        if is_equal(p1.y,(self.slope()*p1.x) + (self.p1_y - self.slope() * self.p1_x)):
            return False
        if is_equal(p2.y,(self.slope()*p2.x) + (self.p2_y - self.slope() * self.p2_x)):
            return False
        if (((self.slope() * p1.x) + (self.p1_y - self.slope() * self.p1_x)) < p1.y) and (((self.slope() * p2.x) + (self.p1_y - self.slope() * self.p1_x)) < p2.y):
            return True
        if (((self.slope() * p1.x) + (self.p1_y - self.slope() * self.p1_x)) > p1.y) and (((self.slope() * p2.x) + (self.p1_y - self.slope() * self.p1_x)) > p2.y):
            return True
        else:
            return False
        
    # string representation of the line - one of three cases
    # y = c if parallel to the x axis
    # x = c if parallel to the y axis
    # y = m * x + b
    def __str__ (self):

        # defines the way an instance of the Line class is printed
        str_p1 = '('+str(self.p1_x)+','+str(self.p1_y)+')'
        str_p2 = '('+str(self.p2_x)+','+str(self.p2_y)+')'
        return str_p1+' to '+str_p2

# determines if two float values are close to equal
def is_equal (a, b):
    return (abs(a - b) < tol)
    
def main():
  # open file "geom.txt" for reading
    infile = open('geom.txt','r')
  # read the coordinates of the first Point P
    line = infile.readline().strip().split()
    P = line[:2]
    P = Point(P[0],P[1])
  # read the coordinates of the second Point Q
    line = infile.readline().strip().split()
    Q = line[:2]
    Q = Point(Q[0],Q[1])
  # print the coordinates of points P and Q
    print('Coordinates of P:',P)
    print('Coordinates of Q:',Q)
  # print distance between P and Q
    distance = P.dist(Q)
    print('Distance between P and Q:',distance)
  # print the slope of the line PQ
    PQ = Line(P.x,P.y,Q.x,Q.y)
    print('Slope of PQ:',PQ.slope())
  # print the y-intercept of the line PQ
    print('Y-intercept of PQ:',PQ.y_intercept())
  # print the x-intercept of the line PQ
    print('X-intercept of PQ:',PQ.x_intercept())
  # read the coordinates of the third Point A
    line = infile.readline().strip().split()
    A = line[:2]
    A = Point(A[0],A[1])
  # read the coordinates of the fourth Point B
    line = infile.readline().strip().split()
    B = line[:2]
    B = Point(B[0],B[1])
  # print the string representation of the line AB
    AB = Line(A.x,A.y,B.x,B.y)
    print('Line AB:',AB)
  # print if the lines PQ and AB are parallel or not
    if PQ.is_parallel(AB):
        print('PQ is parallel to AB')
    else:
        print('PQ is not parallel to AB')
  # print if the lines PQ and AB (or extensions) are perpendicular or not
    if PQ.is_perpendicular(AB):
        print('PQ is perpendicular to AB')
    else:
        print('PQ is not perpendicular to AB')
  # print coordinates of the intersection point of PQ and AB if not parallel
    if not PQ.is_parallel(AB):
        print('Intersection point of PQ and AB:',PQ.intersection_point(AB))
  # read the coordinates of the fifth Point G
    line = infile.readline().strip().split()
    G = line[:2]
    G = Point(G[0],G[1])
  # read the coordinates of the sixth Point H
    line = infile.readline().strip().split()
    H = line[:2]
    H = Point(H[0],H[1])
  # print if the the points G and H are on the same side of PQ
    if PQ.on_same_side(G,H):
        print('G and H are on the same side of PQ')
    else:
        print('G and H are not on the same side of PQ')
  # print if the the points G and H are on the same side of AB
    if AB.on_same_side(G,H):
        print('G and H are on the same side of AB')
    else:
        print('G and H are not on the same side of AB')
  # close file "geom.txt"
    infile.close()
	
if __name__ == "__main__":
  main()
