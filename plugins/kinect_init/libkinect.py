# ############################################################################
#
# Author : Jean-Christophe Hurault
# Date : 2018
# Contact : jeanchristophe.hurault@gmail.com
#
# ###########################################################################/

#-*- coding:utf-8 -*-

# Import Python 3 compatibility functions
from libopensesame.py3compat import *
# Import the required modules.
from libopensesame import debug
from libopensesame.item import item
from libopensesame import exceptions
from libopensesame import widgets
from openexp.exceptions import response_error
from openexp.keyboard import keyboard
from openexp.canvas import canvas

# Import the module to connect with the Kinect device
from pykinect import nui

from time import sleep
import thread
import itertools
import ctypes
import unicodedata
# Import modules to access and load a file.
import imp
import os.path
import csv


# Initialize a object Kinect
_kinect = None
# Initialize a file to log Kinect data
logfile = None

class libkinect:

    def __init__(self, experiment):
    #"""Called by the kinect_init plugin - Initialize a Kinect object and a logfile."""

        global _kinect
        global logfile
        global file

        self.experiment = experiment
        self.recording = False

        # Initiate a sketchpad
        self.init_canvas = canvas(self.experiment)

        # Try to initiate an instance of kinect
        if _kinect == None:
            try:
                _kinect = nui.Runtime()
                debug.msg(u'Success to connect the kinect')
                print "Success to connect the kinect"
            except Exception as e:
                debug.msg(u'Fail to connect the kinect : '+str(e))
                print "Fail to connect the kinect : "+str(e)
                self.set_canvas("Fail to connect the kinect ! (press the spacebar to quit)", 0, 36, True)

        # Enable the detection of the participant skeleton
        _kinect.skeleton_engine.enabled = True
        # Put the kinect at a 0 degre angle
        _kinect.camera.elevation_angle = 0
        # Put a kinect instance in an Opensesame variable, to access it from an "inline script" element
        self.experiment.kinect = _kinect

        # Prepare the file for logging the data
        try :
            logname = self.experiment.logfile + "_kinect.csv"
            file = open(logname, "a")
            logfile = csv.writer(file, delimiter=',', lineterminator='\n')
        except Exception as e:
            debug.msg(u'Error in the log file ('+self.experiment.logfile+') : '+e)
            print "Error in the log file ("+self.experiment.logfile+") : "+e

        # Initiate the counter of trials and the list of Opensesame's variables
        self.experiment.TrialNb = 0
        self.opensesame_var_names_old = None

    def calibrate(self):
    #"""Called by the kinect_calibration plugin - Check indefinitively until a skeleton is found."""
        self.experiment.first_skeleton = None
        SkeletonNotFound = True
        while SkeletonNotFound :
            for skeleton in _kinect.skeleton_engine.get_next_frame().SkeletonData:
                if skeleton.eTrackingState == nui.SkeletonTrackingState.TRACKED:
                    self.experiment.first_skeleton = skeleton
                    SkeletonNotFound = False
                    debug.msg(u'Skeleton found')
                    print "Skeleton found"

    def get_data(self):
    #"""Get the online data of the skeleton from the kinect instance."""
        for skeleton in _kinect.skeleton_engine.get_next_frame().SkeletonData:
            if skeleton.eTrackingState == nui.SkeletonTrackingState.TRACKED:
                debug.msg(u'Skeleton data send')
                print "Skeleton data send"
                return skeleton

    def set_canvas(self, txt, time, fontsize, keypress = False):
    #"""Create and show a sketchpad element in Opensesame."""
        self.init_canvas.clear()
        self.init_canvas.set_font(style='serif',size=fontsize)
        self.init_canvas.text(txt)
        self.init_canvas.show()
        self.experiment.sleep(time)

        if keypress :
            # Add a keyboard object to be able to know when you press the spacebar
            my_keyboard = keyboard(self.experiment, keylist=['space'])
            while True:
                key, end_time = my_keyboard.get_key(timeout= 500)
                if key == 'space':
                    break

    def start_recording(self):
    #"""Called by the kinect_start_recording plugin - Start the recording of the Kinect object."""
    	# Set a variable at true to allow the recording 
        self.recording = True
    	# Call the get_event function in a thread to allow the collect of data in background
        thread.start_new_thread(self.get_event, ())

    def stop_recording(self):
    #"""Called by the kinect_stop_recording plugin - Stop the recording of the Kinect object."""
    	# Set a variable at false to stop the recording 
        self.recording = False

    def get_event(self):
    #"""Get and record the data from the Kinect object."""
        global logfile

        trial_time = 0
        # Get variables names of Opensesame and create a string with them, separated by a comma, adapted to row in the logfile
        opensesame_var_names = " ".join(str(var[0]).replace(" ", "_") for var in self.experiment.var.items()).split()

        # Check if the list of variable in Opensesame change (i.e., an element was launch), if so, add a new row in the logfile with variables names
        if opensesame_var_names != self.opensesame_var_names_old:
            # Get variables names of Opensesame and create a string with them, separated by a comma, adapted to row in the logfile
            kinect_var_names = ["Participant","Trials","Row","Time (ms)","Skeleton index","hip_center.x","hip_center.y","hip_center.z","spine.x","spine.y","spine.z","shoulder_center.x","shoulder_center.y","shoulder_center.z","head.x","head.y","head.z","shoulder_left.x","shoulder_left.y","shoulder_left.z","elbow_left.x","elbow_left.y","elbow_left.z","wrist_left.x","wrist_left.y","wrist_left.z","hand_left.x","hand_left.y","hand_left.z","shoulder_right.x","shoulder_right.y","shoulder_right.z","elbow_right.x","elbow_right.y","elbow_right.z","wrist_right.x","wrist_right.y","wrist_right.z","hand_right.x","hand_right.y","hand_right.z","hip_left.x","hip_left.y","hip_left.z","knee_left.x","knee_left.y","knee_left.z","ankle_left.x","ankle_left.y","ankle_left.z","foot_left.x","foot_left.y","foot_left.z","hip_right.x","hip_right.y","hip_right.z","knee_right.x","knee_right.y","knee_right.z","ankle_right.x","ankle_right.y","ankle_right.z","foot_right.x","foot_right.y","foot_right.z"]
            # Write a row with the headers (list of variable)
            logfile.writerow((kinect_var_names+opensesame_var_names))

            self.opensesame_var_names_old = opensesame_var_names

        self.experiment.TrialNb += 1
        self.experiment.RowNb = 0
        t = self.experiment.time()

        while 1 :
        	# Check if the recording variable is set to false
            if self.recording == False :
                # End the recording
                break
            trial_time = self.experiment.time() - t
            for skeleton in _kinect.skeleton_engine.get_next_frame().SkeletonData:
                print skeleton
                debug.msg(skeleton)
                if skeleton.eTrackingState == nui.SkeletonTrackingState.TRACKED:
                    # Indicate the correspondance of each skeleton's articulations
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

                    self.experiment.RowNb += 1
                    opensesame_var_values = " ".join(repr(var[1]).replace(" ", "_") for var in self.experiment.var.items()).split()
                    # Get variables names of Opensesame and create a string with them, separated by a comma, adapted to row in the logfile
                    kinect_var_values = [str(self.experiment.subject_nr),str(self.experiment.TrialNb),str(self.experiment.RowNb),str(trial_time),str(skeleton.dwUserIndex),str(hip_center.x),str(hip_center.y),str(hip_center.z),str(spine.x),str(spine.y),str(spine.z),str(shoulder_center.x),str(shoulder_center.y),str(shoulder_center.z),str(head.x),str(head.y),str(head.z),str(shoulder_left.x),str(shoulder_left.y),str(shoulder_left.z),str(elbow_left.x),str(elbow_left.y),str(elbow_left.z),str(wrist_left.x),str(wrist_left.y),str(wrist_left.z),str(hand_left.x),str(hand_left.y),str(hand_left.z),str(shoulder_right.x),str(shoulder_right.y),str(shoulder_right.z),str(elbow_right.x),str(elbow_right.y),str(elbow_right.z),str(wrist_right.x),str(wrist_right.y),str(wrist_right.z),str(hand_right.x),str(hand_right.y),str(hand_right.z),str(hip_left.x),str(hip_left.y),str(hip_left.z),str(knee_left.x),str(knee_left.y),str(knee_left.z),str(ankle_left.x),str(ankle_left.y),str(ankle_left.z),str(foot_left.x),str(foot_left.y),str(foot_left.z),str(hip_right.x),str(hip_right.y),str(hip_right.z),str(knee_right.x),str(knee_right.y),str(knee_right.z),str(ankle_right.x),str(ankle_right.y),str(ankle_right.z),str(foot_right.x),str(foot_right.y),str(foot_right.z)]
                    # Create a row in the kinect's logfile with all variables (kinect data and Opensesame variables).
                    logfile.writerow((kinect_var_values+opensesame_var_values))
        
        debug.msg(u'Stop getting events')
        print "Stop getting events"

    def close(self):
    #"""Close the Kinect object and the logfile."""
        global _kinect
        global file

        _kinect.close()
        file.close()