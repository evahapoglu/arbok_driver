"""Module containing generic sequence for a simple square pulse sequence"""
from qm import qua
from arbok_driver import SubSequence, Sample, qua_helpers

class SquarePulse(SubSequence):
    """
    Class containing parameters and sequence for a simple square pulse
    """
    def __init__(self, name: str,sample: Sample, seq_config: dict):
        """
        Constructor method for 'SquarePulse' class
        
        Args:
            name (str): name of sequence
            sample  (Sample): Sample class for physical device
            config (dict): config containing pulse parameters
        """
        super().__init__(name, sample, seq_config)

    def qua_sequence(self):
        """Macro that will be played within the qua.program() context"""
        qua.align()
        qua.play('ramp'*qua.amp(self.amplitude()), self.element(), duration = self.ramp_time())
        qua.wait(self.t_square_pulse(), self.element())
        qua.play('ramp'*qua.amp(-self.amplitude()), self.element(), duration = self.ramp_time())

