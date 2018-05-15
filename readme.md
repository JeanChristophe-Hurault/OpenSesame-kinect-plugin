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

Then, to install Kinect plugin in OpenSesame, simply copy every folders (kinect_init, kinect_calibration, kinect_start_recording, kinect_stop_recording) from the "plugins" folder and paste them to the OpenSesame program folder (for OpenSesame 3.0 or newer):
- C:\Program Files (x86)\OpenSesame\share\opensesame_plugins
</br>
  
![folder plugins](/images/install_pluginsKinect.png "Copy-Paste folders from plugins")  

That's it ! Launch Opensesame and you should now see new elements in the leftbar (restart it if it's already open).

## Using plugins in an experiment
<em><b>Requirements :
- Adequate space (130 centimeter/4.25 feet minimum and 300 centimeter/938 feet maximum) between the camera and the participant  
- Cleared space between the camera and the participant to ensure accurate measurements
- If possible, a uniform background color for the participant
- A Kinect device, the version with an adapter for windows !  
![kinect for windows](/images/Kinect_for_windows.jpg "Kinect for Windows")  
</b></em>


### Get tracked skeleton of the participant

- Kinect_init plugin
![kinect_init plugin](/images/kinect_init_large.png "kinect_init plugin")</br>  
- Kinect_calibration plugin
![Kinect_calibration plugin](/images/Kinect_calibration_large.png "Kinect_calibration plugin")</br>  
- Kinect_start_recording plugin
![Kinect_start_recording plugin](/images/Kinect_start_recording_large.png "Kinect_start_recording plugin")</br>  
- Kinect_stop_recording plugin
![Kinect_stop_recording plugin](/images/Kinect_stop_recording_large.png "Kinect_stop_recording plugin")</br>  

### Data and Logfile
The data collected by the Kinect is the three-dimensional coordinates of the joints of the human body, at 30 measurements per second (i.e., every 30 ms).


![Kinect device](https://www.resna.org/sites/default/files/conference/2014/Wheelchair%20Seating/Student%20Scientific/McCutcheon/Fig1.png "Kinect device and human articulation it detect")
<em><b>Figure : Characteristics of the Kinect     (  (A) Captured human joints (B) Technical components (C) Coordinate system</b>  )</em>  
<em>Photo credit: <a href="http://www.resna.org/sites/default/files/conference/2014/Wheelchair Seating/Student Scientific/McCutcheon/Fig1.png">Resna.org</a></em>
</br>  
</br>
The plugin create its own log file, directly in the folder of the experiment file.

`Be careful : you can have another heads lines after the first row in the log file. It appears when an element in your opensesame's experiment is launched. By adding a variable in Opensesame, the plugin add a new head line to fit the data it get from Opensesame.`

### Use gestures as responses

<em><b>Check if coordonnates from articulation of the participant are not negative (due to ..)
1. 
2. 
</b></em>

You can't directly use gestures as response in your experiment yet. But, it is possible to modify the python file (name "libkinect.py" in the folder "kinect_init") and add this functionnality. Don't hesite to contact me for more informations or help.

Inline script :</br>
<b>-- Prepare part --</b>  
<pre><code>
## Initialize new variables in Opensesame, so they exist from the start and there is no shift in the logfile
# Variable for the time of the movement
var.mvt_time = 0
# Variable for the type of the movement
var.mvt_type = None
</code></pre>
</br>
<b>-- Run part --</b>  
<pre><code>
# Get the time when the element started
start_time = self.experiment.time()
# Infinite loop until 'break' is call
while 1 :
	# Call the get_data function (in libkinect.py) to access the data from the kinect
	skeleton = self.experiment.kinect.get_data()
	# Indicate the correspondance of each skeleton's articulations
	# For each articulations, you have 3 coordonnates (x - horizontal axis, y - vertical axis, z - depth axis)
	hip_center      = skeleton.SkeletonPositions[0]
	spine           = skeleton.SkeletonPositions[1]
	shoulder_center = skeleton.SkeletonPositions[2]
	head            = skeleton.SkeletonPositions[3]
	shoulder_left   = skeleton.SkeletonPositions[4]
	elbow_left      = skeleton.SkeletonPositions[5]
	wrist_left      = skeleton.SkeletonPositions[6]
	hand_left       = skeleton.SkeletonPositions[7]
	shoulder_right  = skeleton.SkeletonPositions[8]
	elbow_right     = skeleton.SkeletonPositions[9]
	wrist_right     = skeleton.SkeletonPositions[10]
	hand_right      = skeleton.SkeletonPositions[11]
	hip_left        = skeleton.SkeletonPositions[12]
	knee_left       = skeleton.SkeletonPositions[13]
	ankle_left      = skeleton.SkeletonPositions[14]
	foot_left       = skeleton.SkeletonPositions[15]
	hip_right       = skeleton.SkeletonPositions[16]
	knee_right      = skeleton.SkeletonPositions[17]
	ankle_right     = skeleton.SkeletonPositions[18]
	foot_right      = skeleton.SkeletonPositions[19]
	
	
	## Examples of movement you can handle by comparing the position of different part of the participants body

	# If the participant has the right hand higher (the vertical axis of the Kinect, so the 'y' part) than the shoulder, 
	# it consider that the participant rise the right hand
	if hand_right.y > shoulder_right.y :
		# Set the time of the movement, by substracting the actual time to the starting time
		var.mvt_time = self.experiment.time() - start_time
		# Set the type of the movement
		var.mvt_type = "rising right hand"
		# End the loop and end the inline script element
		#break
	
	# If the participant has the left hand higher (the vertical axis of the Kinect, so the 'y' part) than the shoulder,
	# it consider that the participant rise the left hand
	if hand_left.y > shoulder_left.y :
		# Set the time of the movement, by substracting the actual time to the starting time
		var.mvt_time = self.experiment.time() - start_time
		# Set the type of the movement
		var.mvt_type = "rising left hand"
		# End the loop and end the inline script element
		#break
	
	# If you add the calibration plugin, you can compare the actual position of the participant to the position during 
	# the calibration (aka, 'initial position')
	# So, if the right hand is closer (50% of the initial distance) to the kinect than during the calibration, 
	# it consider that the right hand move forward
	
	
	# Indicate the correspondance of each skeleton's articulations
	# For each articulations, you have 3 coordonnates (x - horizontal axis, y - vertical axis, z - depth axis)
	first_hip_center      = self.experiment.first_skeleton.SkeletonPositions[0]
	first_spine           = self.experiment.first_skeleton.SkeletonPositions[1]
	first_shoulder_center = self.experiment.first_skeleton.SkeletonPositions[2]
	first_head            = self.experiment.first_skeleton.SkeletonPositions[3]
	first_shoulder_left   = self.experiment.first_skeleton.SkeletonPositions[4]
	first_elbow_left      = self.experiment.first_skeleton.SkeletonPositions[5]
	first_wrist_left      = self.experiment.first_skeleton.SkeletonPositions[6]
	first_hand_left       = self.experiment.first_skeleton.SkeletonPositions[7]
	first_shoulder_right  = self.experiment.first_skeleton.SkeletonPositions[8]
	first_elbow_right     = self.experiment.first_skeleton.SkeletonPositions[9]
	first_wrist_right     = self.experiment.first_skeleton.SkeletonPositions[10]
	first_hand_right      = self.experiment.first_skeleton.SkeletonPositions[11]
	first_hip_left        = self.experiment.first_skeleton.SkeletonPositions[12]
	first_knee_left       = self.experiment.first_skeleton.SkeletonPositions[13]
	first_ankle_left      = self.experiment.first_skeleton.SkeletonPositions[14]
	first_foot_left       = self.experiment.first_skeleton.SkeletonPositions[15]
	first_hip_right       = self.experiment.first_skeleton.SkeletonPositions[16]
	first_knee_right      = self.experiment.first_skeleton.SkeletonPositions[17]
	first_ankle_right     = self.experiment.first_skeleton.SkeletonPositions[18]
	first_foot_right      = self.experiment.first_skeleton.SkeletonPositions[19]
	
	if hand_right.x < (first_hand_right.x * 0.8) :
		# Set the time of the movement, by substracting the actual time to the starting time
		var.mvt_time = self.experiment.time() - start_time
		# Set the type of the movement
		var.mvt_type = "approaching right hand"
		# End the loop and end the inline script element
		break
</code></pre>  

## License

No rights reserved. All files in this repository are released into the public domain.

## Bibliographical references

Clark, R.A., Pua, Y.H., Fortin, K., Ritchie, C., Webster, K.E., Denehy, L., & Bryant, A.L. (2012). Of the Microsoft Kinect for assessment of postural control. Gait & posture, 36 (3), 372-377.

Mathot, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. Behavior Research Methods, 44 (2), 314-324.

Shotton, J., Fitzgibbon, A., Cook, M., Sharp, T., Finocchio, M., Moore, R. & Blake, A. (2011). Real-time human poses recognition in parts of single depth images. In Computer Vision and Pattern Recognition (CVPR), 2011 IEEE Conference on (pp. 1297-1304).
