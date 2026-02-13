from distrimuse_ros2_api.msg import (
    DetectedPerson,
    DetectionResult,
    PersonBehavior,
    PersonJointPosition,
    PumacyActivity,
    RobotBehavior,
)


def test_robot_behavior_constants():
    """RobotBehavior has IDLE, RUNNING, and ANOMALY constants."""
    assert RobotBehavior.IDLE == 0
    assert RobotBehavior.RUNNING == 1
    assert RobotBehavior.ANOMALY == 2


def test_robot_behavior_default_fields():
    """RobotBehavior default instance has zero-valued fields."""
    msg = RobotBehavior()
    assert msg.type == 0
    assert msg.confidence == 0.0


def test_person_behavior_constants():
    """PersonBehavior has all seven behavior constants."""
    assert PersonBehavior.STANDING_STILL == 0
    assert PersonBehavior.SITTING == 1
    assert PersonBehavior.LAYING_DOWN == 2
    assert PersonBehavior.WALKING == 3
    assert PersonBehavior.RUNNING == 4
    assert PersonBehavior.BENDING_OVER == 5
    assert PersonBehavior.FAINTING == 6


def test_person_joint_position_fields():
    """PersonJointPosition can be constructed with name, positions, and confidence."""
    msg = PersonJointPosition()
    msg.name = "left_elbow"
    msg.position_2d = [120.0, 340.0]
    msg.position_3d = [1.0, 2.0, 3.0]
    msg.confidence = 0.95
    assert msg.name == "left_elbow"
    assert len(msg.position_2d) == 2
    assert len(msg.position_3d) == 3
    assert msg.confidence == 0.95


def test_detected_person_fields():
    """DetectedPerson contains camera_id, positions, joints, behavior, and anomalous flag."""
    msg = DetectedPerson()
    msg.camera_id = "cam_01"
    msg.position_2d = [100.0, 200.0]
    msg.position_3d = [1.0, 2.0, 3.0]
    msg.confidence = 0.88
    msg.anomalous = True
    assert msg.camera_id == "cam_01"
    assert msg.anomalous is True


def test_detected_person_nested_joint():
    """DetectedPerson can hold a list of PersonJointPosition messages."""
    joint = PersonJointPosition()
    joint.name = "right_knee"
    joint.confidence = 0.9

    person = DetectedPerson()
    person.joints = [joint]
    assert len(person.joints) == 1
    assert person.joints[0].name == "right_knee"


def test_detected_person_nested_behavior():
    """DetectedPerson embeds a PersonBehavior message."""
    person = DetectedPerson()
    person.behavior.type = PersonBehavior.WALKING
    person.behavior.confidence = 0.75
    assert person.behavior.type == 3
    assert person.behavior.confidence == 0.75


def test_detection_result_fields():
    """DetectionResult contains header, detected_persons, robot_behavior, and scene."""
    msg = DetectionResult()
    msg.scene = "warehouse_floor"
    msg.robot_behavior.type = RobotBehavior.RUNNING
    assert msg.scene == "warehouse_floor"
    assert msg.robot_behavior.type == 1
    assert len(msg.detected_persons) == 0


def test_detection_result_header():
    """DetectionResult header has stamp and frame_id fields."""
    msg = DetectionResult()
    msg.header.stamp.sec = 1000
    msg.header.stamp.nanosec = 500
    msg.header.frame_id = "base_link"
    assert msg.header.stamp.sec == 1000
    assert msg.header.frame_id == "base_link"


def test_pumacy_activity_constants():
    """PumacyActivity has all six activity constants."""
    assert PumacyActivity.STANDING == 0
    assert PumacyActivity.SITTING == 1
    assert PumacyActivity.LAYING_DOWN == 2
    assert PumacyActivity.WALKING == 3
    assert PumacyActivity.RUNNING == 4
    assert PumacyActivity.FALLING == 5


def test_pumacy_activity_fields():
    """PumacyActivity can be constructed with type, confidence, and anomalous."""
    msg = PumacyActivity()
    msg.type = PumacyActivity.FALLING
    msg.confidence = 0.99
    msg.anomalous = True
    assert msg.type == 5
    assert msg.confidence == 0.99
    assert msg.anomalous is True
