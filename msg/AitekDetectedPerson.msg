# Information about a detected person, provided by Aitek

string camera_id                          # Identifier for the camera (e.g., "cam_front", "cam_back", "cam_side")
vision_msgs/BoundingBox2D bounding_box    # Bounding box of detected person
geometry_msgs/Point position_3d           # 3D position in camera frame (meters) (OPTIONAL so all 0.0 if not available)

float32 confidence          # Person detection confidence (0.0 to 1.0) (-1.0 if not used)
distrimuse_ros2_api/AitekPersonBehavior behavior     # Detected behavior of the detected person
