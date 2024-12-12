# creating base class
class GeneralNeuron:
    def __init__(self, firing_rate):
         self.firing_rate = firing_rate # firing rate of neuron
    

    def activate(self, stimulus):
         '''
         calculates firing rate based on strength of stimuli
         '''
         pass
    print(f"Neuron is activated in firing rate {self.firing_rate}")


 #creating intermediate classes   
class SensoryNeuron:
    def __init__(self, firing_rate, receptor_type):
        super().__init__(firing_rate) # inheritance from class GeneralNeuron
        self.receptor_type = receptor_type # the type of stimulus the neuron detects

    def sense_stimulus(self, stimulus):
        '''
        processes specific stimulus (which is sensitive to) and activates neuron based on its strength/type
        '''
        pass


class MotorNeuron:
    def __init__(self, firing_rate, target_muscle):
        super().__init__(firing_rate) # inheritance from class GeneralNeuron
        self.target_muscle = target_muscle # specifies muscle controlled bt motor neuron

    def control_muscle(self, activation_level):
        '''
        triggers response in target muscle based on neuron's activation level
        '''
        pass


#creating leaf classes
class Photoreceptor:
    def __init__(self, firing_rate):
        super().__init__(firing_rate, receptor_type = "Light") # inheritance from class SensoryNeuron and override receptor type

    def light_detection(self, light_intensity):
        '''
        receives light intensity as input and activates according to light levels
        '''
        pass


class Mechanoreceptor:
    def __init__(self, firing_rate):
        super().__init__(firing_rate, receptor_type = "Pressure") # inheritance from class SensoryNeuron and override receptor type

    def pressure_detection(self, pressure_level):
        '''
        receives pressure as input and activates in response to the strength of the applied pressure
        '''
        pass


class AlphaMotorNeuron:
    def __init__(self, firing_rate):
        super().__init__(firing_rate, target_muscle = "Muscle Spindle") # inheritance from class MotorNeuron and override activation level

    def skeletal_muscle_control(self, activation_level):
        '''
        initiates muscle contraction or movement in response to its activation level
        '''
        pass


class GammaMotorNeuron:
    def __init__(self, firing_rate):
        super().__init__(firing_rate, target_muscle = "Muscle Spindle") # inheritance from class MotorNeuron and override activation level

    def muscle_spindle_control(self, activation_level):
        '''
        adjusts muscle spindle tension in response to activation, affecting muscle tone
        '''
        pass
         
    