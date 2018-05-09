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
from libqtopensesame.items.qtautoplugin import qtautoplugin
# Import modules to access and load a file.
import imp
import os.path

class kinect_init(item):

    # Provide an informative description for your plug-in.
    description = u'This plugin initiate the object Kinect (place at the beginning of the experiment)'

    def reset(self):

        # Set default experimental variables and values
        self.var.item_type = u'kinect_init'
        # Debugging output is only visible when OpenSesame is started with the
        # --debug argument.
        debug.msg(u'Kinect init plugin has been initialized !')

    def prepare(self):

        # Call parent functions.
        item.prepare(self)

        # Get the path of the file, named "libkinect.py", which contain the Kinect library
        path = os.path.join(os.path.dirname(__file__), u'libkinect.py')
        # Load the Kinect library
        libkinect = imp.load_source(u'libkinect', path)

        # Debugging output is only visible when OpenSesame is started with the
        # --debug argument.
        debug.msg(u'Loading the Kinect library from : %s' % path)

        # Create an instance of a Kinect by calling the init function of the library
        self.experiment.kinect = libkinect.libkinect(self.experiment)

        # Call the function close when the experiment is finished
        self.experiment.cleanup_functions.append(self.close)

    def run(self):

        # Record the timestamp of the plugin execution.
        self.set_item_onset()

    def close(self):

        # Call the function to kill the Kinect's instance and close the special log file in "..\kinect_init\libkinect.py".
        self.experiment.kinect.close()
        # Clean the variable "kinect" by putting it at "None"
        self.experiment.kinect = None


class qtkinect_init(kinect_init, qtautoplugin):

    def __init__(self, name, experiment, script=None):

        # Call parent constructors.
        kinect_init.__init__(self, name, experiment, script)
        qtautoplugin.__init__(self, __file__)

    def init_edit_widget(self):
        """Initializes the controls."""

        # Pass the word on to the parent		
        qtautoplugin.init_edit_widget(self)