#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from high_stakes.events import *

# Open log based on config
config_open_log()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    robot_position.reset(Position(-1500, 600))
    inertial.set_heading(-90)

    reset_robot_position_and_heading_to_gps()

    slow_trigger_mover.move(Position(-800, 600), REVERSE)
    clamp.set(True)

    # Use this for 4-ring
    trigger_mover.move(Position(-600, 1200))
    trigger_mover.move(Position(-300, 1300))
    trigger_mover.move(Position(-600, 1200))
    trigger_mover.move(Position(-300, 1150))
    wait(1500, MSEC)
    trigger_mover.move(Position(-300, 300))
    clamp.set(False)

    # Use this for 2-ring
    # trigger_turner.turn(42, FRAME_ABSOLUTE)
    # intake.spin_forward()
    # trigger_mover.move(Position(-350, 1000))
    # clamp.set(False)

    wait(1000, MSEC)
    reset_robot_position_and_heading_to_gps()

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
