### Introduction

A small script intended for calculating optimal camera placement and lens angle choices when intending to capture photo/videographic data on a plane at an angle. Though it can be used in other contexts, this was specifically intended for Computer Vision capture setups and as such prioritises optimal lens choices irrespective of potential visual distortion, allowing a targeted depth to be captured without any need for artificial zooming or cropping, both of which lead to a reduction in output quality. With that being said, if you are aware of the lens angle range you would like to use when capturing footage, you can adjust your input values to adhere to those bounds.

Due to the nature of the depth calculations being used, **vertical lens angle** is calculated and output, contrasting with the advertising of most standard lenses which tend to only list their horizontal lens angle. As such if you use the conversion chart [found here](https://www.nikonians.org/reviews/fov-tables), you should be able to figure out the appropriate standard lens size you require, though may need to round up in the case purchasing/using a fixed length lens.

This script was written relatively quickly and as such, whilst I have taken some steps for optimisation and error prevention, some errors may still occur when making requests outside of the bounds of realistic proportions/measurements. Finally, to "calculate" an optimal lens angle, this script conducts a binary search, I'm sure that there must be a way to mathematically derive the optimal angle faster via rearrangement but I couldn't figure out how to in the time I had available to me, thus went with this option for now. 


### Installation

1. Clone this repo:
```bash
git clone https://github.com/x-ix/CameraPlacement.git
```
2. Install dependencies (please refer to [requirements.txt](requirements.txt)):
```bash
pip install -r requirements.txt
```

### Usage
```
Usage:
    python CameraPlacement.py


Inputs:
    The script will prompt you to input the following:
    
        "Enter depth of surface to be captured in M:" #The script calculates positional and angular
                                                      #values based off of the depth or length of the
                                                      #surface you intend to capture

        "Enter height of surface from ground level in M:" #Relates to how high the surface you are
                                                          #capturing is in relation to the area you
                                                          #would like to have within your camera lens

        "Enter camera height in M:" #To account for items such as tripods, stands and different
                                    #lengths of camera lenses (as some of them can be quite long)

        "Enter Camera angle in degrees relative to the ground (negative angle if looking downwards):"
        #The angle the centre of your camera is at based on the direction you are capturing in,
        #relative to the ground being 0° in said direction. If your camera is above its subject,
        #provide the angle it is point down by as a negative value as its pointing down


Outputs:
    The script will provide you with the following:

        "Optimal Vertical lens Angle (M)" #Vertical angle, considerations outlined in introduction

        "Optimal distance from end of surface (M)" #This is the distance the centre of your lens
                                                   #should be placed away from the closest edge of
                                                   #the depth area you are capturing. If negative,
                                                   #your camera needs to be placed past that edge
                                                   #by the calculated distance

        plt #A matplotlib plot of how the cameras should be placed to better illustrate the two values
            #explained above
```


### Miscellaneous
Contents of [requirements.txt](requirements.txt):
```
matplotlib==3.8.4
numpy==1.26.4
```


### Closing Notes
There are a fair few optimisations and adjustments that could be made to this script and as such I've tried to structure it relatively logically to circle back around to but for the moment it seems to calculate desired outputs within normal (non-extreme) input bounds relatively efficiently.
