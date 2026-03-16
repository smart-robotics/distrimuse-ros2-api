# Information about the skeleton joint positions of a person, provided by EMOJ
string HEAD = HEAD
string COM = COM  # Center Of Mass
string SHOULDER_LEFT = SHOULDER_LEFT
string SHOULDER_RIGHT = SHOULDER_RIGHT
string ELBOW_LEFT = ELBOW_LEFT
string ELBOW_RIGHT = ELBOW_RIGHT
string HAND_LEFT = HAND_LEFT
string HAND_RIGHT = HAND_RIGHT
string KNEE_LEFT = KNEE_LEFT
string KNEE_RIGHT = KNEE_RIGHT
string FOOT_LEFT = FOOT_LEFT
string FOOT_RIGHT = FOOT_RIGHT

string name             # Joint name (e.g. "HEAD", "SHOULDER_LEFT", "ELBOW_RIGHT", ...)
geometry_msgs/Point position_2d    # 2D position in camera frame (pixels)
geometry_msgs/Point position_3d    # 3D position in camera frame (meters) [OPTIONAL]
float32 confidence      # Confidence score of skeleton joint position (0.0 to 1.0) (-1.0 if not used)