# Import Python 3 compatibility functions
from libopensesame.py3compat import *
# Import the required modules.
from libopensesame import debug
from libopensesame.item import item
from libqtopensesame.items.qtautoplugin import qtautoplugin

class kinect_start_recording(item):

    description = u'This plugin launch the recording of the skeleton (place whitin each trial)'

    def reset(self):

        # Set default experimental variables and values
        self.var.item_type = u'kinect_start_recording'
        # Debugging output is only visible when OpenSesame is started with the
        # --debug argument.
        debug.msg(u'Kinect start recording plugin has been initialized !')

    def prepare(self):

        # Call parent functions.
        item.prepare(self)

    def run(self):

        # Record the timestamp of the plugin execution.
        self.set_item_onset()
        # Call the function to start the recording of the participant's skeleton in "..\kinect_init\libkinect.py".
        self.experiment.kinect.start_recording()


class qtkinect_start_recording(kinect_start_recording, qtautoplugin):

    def __init__(self, name, experiment, script=None):

        # Call parent constructors.
        kinect_start_recording.__init__(self, name, experiment, script)
        qtautoplugin.__init__(self, __file__)

    def init_edit_widget(self):
        """Initializes the controls."""

        # Pass the word on to the parent        
        qtautoplugin.init_edit_widget(self)