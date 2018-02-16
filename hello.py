import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.say_text("All finished").wait_for_completed()

cozmo.run_program(cozmo_program)
