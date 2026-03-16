# Information about a detected person, provided by EMOJ

string camera_id  # Identifier for the camera (e.g., "cam_front", "cam_back", "cam_side")
geometry_msgs/Point position_2d  # 2D position in camera frame (pixels)
distrimuse_ros2_api/EmojPersonJointPosition[] joints  # Array of detected skeleton joint positions

float64 confidence  # Person detection confidence (0.0 to 1.0) (-1.0 if not used)
int8 ergonomic_risk  # 0: no risk, 1: low risk, 2: high risk
