
############################
## PUBLIC SERVICE OBJECT ###
############################

# Singularly exposed public resource in this service.
# It serves as the logical front end of an elevator system.
# It's concerend with software functions a real elevator system
# would require; system state/status and routing/dispatching.
class ElevatorController(object):
    
    def __init__(self, num_floors, num_elevators):
        self._num_floors = num_floors
        # list of elevators for criticial operations
        self._elevators = [];
        # dict of elevator data for reporting
        self.elevator_status = {};
        
        for num in range(num_elevators):
            elevator = _Elevator(num, self._update_elevator_status)
            # init state we keep on elevators
            self._elevators.append(elevator)
            self._update_elevator_status(elevator)


    # only public method and primary interface to the system
    def request_move(self, from_floor, to_floor):
        if not(1 < to_floor <= self._num_floors):
            raise Exception('Elevator System is configured to onyl reach floor {0}'.format(self._num_floors))

    # a private instance method(to the outside world) used as a callback for
    # elevators to update the controller with their status. simple observer pattern mod.
    def _update_elevator_status(self, elevator):
        # extract
        elevator_id = elevator.id
        current_floor = elevator.current_floor
        is_open = elevator.is_open
        # update status
        self.elevator_status[elevator_id] = {
            'current_floor': current_floor,
            'is_open': is_open
        }


###############################
## PRIVATE INTERNAL OBJECTS ###
###############################

# Class, private to this service module, that
# models an elevator's hierarchy and function
# in an elevator system. That is to say, it is strictly
# under the control of the above controller.
class _Elevator(object):

    def __init__(self, id, update_system_callback):
        # relevant state to make this thing move
        # keeping them public so the controller can do as it pleases
        # relying on class level modifier to keep them out of service-external
        # entities. 
        self.id = id
        self.update_system_callback = update_system_callback;
        self.current_floor = 1
        self.is_open = True
        self.total_trips = 0
        self.floors_passed = 0
        self.in_service = True

    # well this moves to a new floor, named to keep
    # a bit of symmetry with the controller
    def move(self, desired_floor):
        # shouldnt happen, but people go in here!
        if not self.in_service:
            raise Exception('Elevator {0} is not in service'.format(self.id))

        # this tells the elevator to go up or down by 1 floor
        # might be a 1-off error in these ranges
        if desired_floor < self.current_floor:
            move_sequence = range(self.current_floor - 1, desired_floor -1, -1)
        else:
            move_sequence = range(self.current_floor + 1, desired_floor + 1, 1)

    def _toggle_door(self):
        self.is_open = not self.is_open
        self.update_system_callback(self)
