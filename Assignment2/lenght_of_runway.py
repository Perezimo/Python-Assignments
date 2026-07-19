
"""Program that calculate an airplane runway

Enter distance covered time(Velocity)
Enter the acceleration of the airplane change in velocity
length of runway is square of the velocity divided by twice its rate of acceleration

print the length of the runway"""


velocity_of_plane = int(input("Enter the velocity of the plane:"))

acceleration_of_plane = int(input("Enter the acceration of the plane:"))

length_of_runway = velocity_of_plane**2/2 * acceleration_of_plane

print("The minimum runway for the plane to take off is:" , length_of_runway) 


