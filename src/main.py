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

    trigger_driver.drive(-900)
    clamp.set(True)
    trigger_turner.turn(132, FRAME_HEADING_RELATIVE)
    intake.spin_forward()
    trigger_driver.drive(650)
    trigger_turner.turn(-18, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(150)
    trigger_driver.drive(-400)
    trigger_turner.turn(-70, FRAME_HEADING_RELATIVE)
    reset_robot_position_and_heading_to_gps()
    trigger_driver.drive(500)
    trigger_turner.turn(-20, FRAME_HEADING_RELATIVE)
    reset_robot_position_and_heading_to_gps()
    trigger_driver.drive(1100)
    trigger_driver.drive(-460)
    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(-115, FRAME_HEADING_RELATIVE)
    intake_retract.set(True)
    trigger_driver.drive(1350)
    intake_retract.set(False)

    # trigger_driver.drive(-1080)  # overshoot_done=True
    # clamp.set(True)
    # trigger_turner.turn(120, FRAME_HEADING_RELATIVE)

    # wait(1000, MSEC)
    # reset_robot_position_and_heading_to_gps()
    # intake.spin_forward()
    # trigger_driver.drive(400)

    # trigger_turner.turn(-70, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(200)

    # # trigger_turner.turn(105, FRAME_HEADING_RELATIVE)
    # # trigger_driver.drive(270)

    # wait(500, MSEC)
    # reset_robot_position_and_heading_to_gps()
    # wait(50, MSEC)
    # # intake.stop()
    # trigger_turner.turn(-75, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(50)
    # # trigger_driver.drive(-900)

    # wait(1000, MSEC)
    # reset_robot_position_and_heading_to_gps()

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
