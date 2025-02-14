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

    # Then try resetting to GPS if GPS sensor is installed and reports high quality
    reset_robot_position_and_heading_to_gps()

    slow_trigger_mover.move(Position(-600, 600), REVERSE)
    clamp.set(True)
    trigger_turner.turn(42, FRAME_ABSOLUTE)
    intake.spin_forward()
    trigger_mover.move(Position(-165, 1083))
    trigger_mover.move(Position(-104, 1220))
    trigger_mover.move(Position(-267, 855), REVERSE)
    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-626, 1202))
    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-1631, 1649))
    trigger_mover.move(Position(-1211, 1462), REVERSE)
    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(-115, FRAME_HEADING_RELATIVE)
    intake_retract.set(True)
    trigger_mover.move(Position(-1188, 113), REVERSE)
    intake_retract.set(False)

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
