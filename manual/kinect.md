# Kinect Plugin


## About the Kinect

The Kinect is a motion-sensing input device developed by Microsoft© and introduced in November 2010 (https://en.wikipedia.org/wiki/Kinect). This tool consists of a box equipped with sensors and cameras that connects to a computer. It allows to measure the position of the body of one person and thus to allow the detection of gestures.


## About the Kinect plugin

This plugin provides Python bindings between OpenSesame and a Kinect device. The plugin integrate “pykinect”, a package providing access to the Kinect device, to control a Kinect as an input for OpenSesame. By using the “pykinect” package (https://github.com/Microsoft/PTVS/wiki/PyKinect), the plugin can interact with the Kinect camera and tracked the skeleton of one participant.

Thus, it’s possible to record the position of a participant during any phase of an experiment and even (by adding inline script in OpenSesame) defining specifics gesture to use as responses.




## Install the plugin for Windows

First, you need to install the drivers, runtime environment and Software Development Kit (SDK) required by Kinect for Windows applications using Kinect sensor technology. You can find them here:
- Kinect for Windows Runtime v1.8 : <https://www.microsoft.com/en-us/download/details.aspx?id=40277>
- Kinect for Windows SDK v1.8 : <https://www.microsoft.com/en-us/download/confirmation.aspx?id=40278>

The "pykinect" package is already included in the plugin folder, so you don't need to download it.

Then, to install Kinect plugin in OpenSesame, simply copy this folder to the OpenSesame program folder (for OpenSesame 3.0 or newer):
- C:\Program Files (x86)\OpenSesame\share\opensesame_plugins


## Using the plugin in an experiment

### Get tracked skeleton of the participant
Add the 

### Logging
The plugin create its own log file, directly in the folder of the experiment file.
