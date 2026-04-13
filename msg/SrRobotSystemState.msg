# This message contains information about the current state of the robot system

sensor_msgs/JointState joint_states  # robot joint states
bool is_holding_box  # boolean about whether or not the robot is holding a box
string[] vacuum_pads  # Which vacuum pads it's using to hold the box
string current_pallet_side  # Which pallet the robot is currently stacking on (either "left" or "right")
float32 lift_position  # Current height of the lift
distrimuse_ros2_api/SrPalletState[] pallet_states  # State of each pallet
