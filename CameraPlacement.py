import math
import numpy as np
import matplotlib.pyplot as plt
import sys

---------------------------
CENTIMETRES = 100

---------------------------

def projection_distance(height, camera_angle, lens_angle):
    source_distance = height / math.sin(math.radians(camera_angle)) #Distance for centre of lens to surface

    # Centre of lens bisects the lens angle, depths covered by either side of the bisection are not equal, 
    # thus are calculated separately and added together.
    a = source_distance / math.sin(math.radians(camera_angle - (0.5 * lens_angle))) * math.sin(math.radians(0.5 * lens_angle))
    b = source_distance / math.sin(math.radians(180 - camera_angle - (0.5 * lens_angle))) * math.sin(math.radians(0.5 * lens_angle))
    return a + b #Returns total depth projected onto



def find_lens_angle(desired_depth, height, camera_angle):

    #Essentially a binary search that alters the lens angle until the user's depth requirements 
    #have been equalised with two decimal places (working in centimetres).
    lb = 0
    ub = camera_angle * 2 #exclusive
    lens_angle = camera_angle
    while True:
        actual_depth = projection_distance(height, camera_angle, lens_angle)
        if np.round(actual_depth, 2) == desired_depth:
            return lens_angle
        elif actual_depth > desired_depth:
            ub = lens_angle
        else:
            lb = lens_angle
        lens_angle = (ub + lb)/ 2     



def distance_calculation(height, camera_angle, lens_angle):
    
    #Trigonometry to find camera's distance from the closest end of the projected surface
    distance = height / math.tan(math.radians(camera_angle + (0.5 * lens_angle)))
    return distance



def create_plot(distance, desired_depth, height, camera_height, camera_angle, lens_angle):

    #Translating back into metres
    distance /= CENTIMETRES
    desired_depth /= CENTIMETRES
    height /= CENTIMETRES
    camera_height /= CENTIMETRES
    
    #Plot to assist with visualisation of camera placement
    fig, ax = plt.subplots()
    x1, y1 = [distance + desired_depth, distance + desired_depth], [0, height] #height line
    x2, y2 = [distance, distance + desired_depth], [height, height] #depth line
    first_angle = camera_angle - (1/2 * lens_angle)
    second_angle = camera_angle + (1/2 * lens_angle)
    first_slope = math.tan(math.radians(first_angle))
    second_slope = math.tan(math.radians(second_angle))
    ax.plot([distance + desired_depth, distance + desired_depth], [0, height], 'r-', label="Height")
    ax.plot([distance, distance + desired_depth], [height, height], 'g-', label="Depth")
    ax.axline((0, camera_height), slope=first_slope, color="blue", linestyle="--", label="Camera View")
    ax.axline((0, camera_height), slope=second_slope, color="blue", linestyle="--")
    if distance > 0:
        plt.gca().set_xlim(left=0)
        plt.gca().set_ylim(bottom=0)
    ax.legend() 
    plt.show()
    

    
def main():

    #User specifies projected surface depth, height, camera height and angle as input parameters
    desired_depth = CENTIMETRES*(int(input("Enter depth of surface to be captured in M: ")))
    if desired_depth < 0.1:
        print("ERROR: Please increase desired projection depth")
        sys.exit()
    height = CENTIMETRES*(float(input("Enter height of surface from ground level in M: ")))
    camera_height = CENTIMETRES*(float(input("Enter camera height in M: ")))
    if height == camera_height:
        print("ERROR: Camera cannot be inline with projected surface, please alter values accordingly")
        sys.exit()
    camera_angle = int(input("Enter Camera angle in degrees relative to the ground (negative angle if looking downwards): "))

    #Finds angle, adjusts things if camera is looking down from above and outputs results
    lens_angle = find_lens_angle(desired_depth, height - camera_height, camera_angle)
    if height < camera_height:
        lens_angle = -lens_angle
        distance = distance_calculation(-(height - camera_height), -camera_angle, lens_angle)
    else:
        distance = distance_calculation(height - camera_height, camera_angle, lens_angle)
    print("Optimal Vertical lens Angle: ", lens_angle, "°")
    print("Optimal distance from end of surface: ", distance/CENTIMETRES, "M")
    create_plot(distance, desired_depth, height, camera_height, camera_angle, lens_angle)



if __name__ == "__main__": #to run itself
    try:
        main()
    except KeyboardInterrupt:
        pass  # Ignore the KeyboardInterrupt and exit silently

    #Should only trigger if lens angle is too large, resulting in an infinite (unmeasurable) projection
    except ZeroDivisionError:
        print("ERROR: Please lower desired projection depth")



