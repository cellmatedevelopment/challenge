
############################
## PUBLIC SERVICE OBJECT ###
############################

# Singularly exposed public resource in this service.
# It serves as the logical front end of an elevator system.
# It's concerend with software functions a real elevator system
# would require; system state/status and routing/dispatching.
class ElevatorController(object):
    pass


###############################
## PRIVATE INTERNAL OBJECTS ###
###############################

# Class, private to this service module, that
# models an elevator's hierarchy and function
# in an elevator system. That is to say, it is strictly
# under the control of the above controller.
class _Elevator(object):
    pass