# OpenSesame Kinect plugins (only Windows)

Created by : Jean-Christophe Hurault
<jeanchristophe.hurault@gmail.com>

A serie of plugins that allows non-intrusive body motion capture and gesture detection of a participant by making Opensesame communicate with a Kinect device.

<b>Feel free to contact me if you have any problems, comments or suggestions for improvements !</b>

## About the Kinect

The Kinect is a motion-sensing input device developed by Microsoft© and introduced in November 2010 (https://en.wikipedia.org/wiki/Kinect). Originally designed for the video game industry, offers an affordable, inexpensive and portable solution for studying body movement. This device consists of a box equipped with sensors and cameras that connects to a computer. Positioned in front of the participant, it collects movements in three-dimensional space by providing real-time positions and rotations of the human body (Shotton et al., 2011). By evaluating the Kinect® error in the temporal and spatial domain compared to reference systems (Clark et al., 2012), previous research validated the measurement qualities of this tool.

## About Kinect plugins

The study of body movements is an important source of knowledge for psychology, these systems of analysis often require the use of skills outside the laboratories. This is why I present here an innovative device allowing both researchers and students, with the simplest possible and minimal resources, to measure and use as response the body movements of participants during experiments.

This plugins provides Python bindings between OpenSesame and a Kinect device. The plugin integrate “pykinect”, a package providing access to the Kinect device, to control a Kinect as an input for OpenSesame. By using the “pykinect” package (https://github.com/Microsoft/PTVS/wiki/PyKinect), the plugin can interact with the Kinect camera and tracked the skeleton of one participant.

Thus, it’s possible to record the position of a participant during any phase of an experiment and, by using an python inline script, to detect and use a specific gesture of the participant.

## Install plugins for Windows

First, you need to install the driver, runtime environment and Software Development Kit (SDK) required for Windows applications using Kinect sensor technology. You can find them here:
- Kinect for Windows Runtime v1.8 : <https://www.microsoft.com/en-us/download/details.aspx?id=40277>
- Kinect for Windows SDK v1.8 : <https://www.microsoft.com/en-us/download/confirmation.aspx?id=40278>

The "pykinect" package is already included in the plugin folder, so you don't need to download it.

Then, to install Kinect plugin in OpenSesame, simply copy this folder to the OpenSesame program folder (for OpenSesame 3.0 or newer):
- C:\Program Files (x86)\OpenSesame\share\opensesame_plugins


## Using plugins in an experiment
Requirements : Adequate space (1m50 minimum) and space between the camera and the participant should be ensured to ensure accurate measurements.


### Get tracked skeleton of the participant


### Logging
The data collected by the Kinect is the three-dimensional coordinates of the joints of the human body, at 30 measurements per second (i.e., every 30 ms).


![Kinect device](https://www.resna.org/sites/default/files/conference/2014/Wheelchair%20Seating/Student%20Scientific/McCutcheon/Fig1.png "Kinect device and human articulation it detect")
<em><b>Figure : Characteristics of the Kinect</b></em>
<em><b>(A) Captured human joints      (B) Technical components      (C) Coordinate system</b></em>


The plugin create its own log file, directly in the folder of the experiment file.

`Be careful : you can have another heads lines after the first row in the log file. It appears when an element in your opensesame's experiment is launched. By adding a variable in Opensesame, the plugin add a new head line to fit the data it get from Opensesame.`

### Use gestures as responses

You can't directly use gestures as response in your experiment yet. But, it is possible to modify the python file (name "libkinect.py" in the folder "kinect_init") and add this functionnality. Don't hesite to contact me for more informations or help.

<pre><code>code</code></pre>

---check if coordonnates not negative
---

## License

No rights reserved. All files in this repository are released into the public domain.

## Bibliographical references

Clark, R.A., Pua, Y.H., Fortin, K., Ritchie, C., Webster, K.E., Denehy, L., & Bryant, A.L. (2012). Of the Microsoft Kinect for assessment of postural control. Gait & posture, 36 (3), 372-377.

Mathot, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. Behavior Research Methods, 44 (2), 314-324.

Shotton, J., Fitzgibbon, A., Cook, M., Sharp, T., Finocchio, M., Moore, R. & Blake, A. (2011). Real-time human poses recognition in parts of single depth images. In Computer Vision and Pattern Recognition (CVPR), 2011 IEEE Conference on (pp. 1297-1304).
