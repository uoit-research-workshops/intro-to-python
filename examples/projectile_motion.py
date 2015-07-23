#!/usr/bin/python

#Import the math module
import math

#Lets read in our input file

input_file = open('input.txt', 'r')

#Loop over each line of the file
for line in input_file:

    #Split the line based on spaces
    line_split = line.split()

    #Check the name of the first column
    #If it is y0 then set 
    if line_split[0] == 'init_h':
        #Set y_0 to be the value of the second column
        y_0 = float(line_split[1])

    if line_split[0] == 'init_v':
        #Set v_0 to be the value of the second column
        v_0 = float(line_split[1])
    
    if line_split[0] == 'angle':
        #Set theta_deg to be the value of the second column
        theta_deg = float(line_split[1])
        #It will be in degrees so we need to convert to radians
        theta = math.radians(theta_deg)

#Close the input file
input_file.close()

#Set the value of g
g = 9.81
#Set the initial time to be 0
t = 0.0
#Initialize y to be the initial height
y = y_0
#Initialize empty lists to store our coordinates in
x_vals = []
y_vals = []

#Lets calculate some trajectories!
while y > 0.0 : 

    #Get the height using the equation 
    # y(t) = y_0 + (t*v_0*sin(theta)) -(g*t**2)/2
    y = y_0 + (t*v_0*math.sin(theta)) -(0.5)*g*(t**2)

    #Append it onto our list
    y_vals.append(y)

    #Get x using the equation
    # x = v_0*cos(theta)*t
    x = v_0*math.cos(theta)*t

    #Append it to our list
    x_vals.append(x)

    #Update the timestep
    t += 0.01


#Find the distance travelled
max_x = max(x_vals)
#Find the maximum height
max_y = max(y_vals)

#Print them out to the screen
print 'The distance traveled was ' + str(max_x) + ' m'
print 'The peak height was ' + str(max_y) + ' m'

#Write out the data to a file
output_file = open('output.txt', 'w')

#Write a header
output_file.write('Time[s] x[m] y[m]\n')

for i in range(len(x_vals)):

    #Put the values into one string
    data_string = str(i*0.01) + ' ' + str(x_vals[i]) + ' ' + str(y_vals[i]) + '\n'
    #Write out the data_string
    output_file.write(data_string)

#Close the output file
output_file.close()











