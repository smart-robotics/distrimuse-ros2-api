from distrimuse_ros2_api.msg import (
    AitekDetectedPerson,
    AitekDetectionResult,
    AitekPersonBehavior,
    EmojDetectedPerson,
    EmojDetectionResult,
    EmojPersonJointPosition,
    PumacyActivity,
    RelabOperatorInput,
    RelabPalletStatusUpdate,
    RulexAreaScore,
    RulexDetectionResult,
    SrAreaActivity,
    SrFusionModelOutput,
    SrPalletState,
    SrRobotSystemState,
    UnigraResult,
)


# --- Aitek ---


def test_aitek_person_behavior_constants():
    """AitekPersonBehavior has all behavior string constants."""
    assert AitekPersonBehavior.STANDING_STILL == "STANDING_STILL"
    assert AitekPersonBehavior.SITTING == "SITTING"
    assert AitekPersonBehavior.LAYING_DOWN == "LAYING_DOWN"
    assert AitekPersonBehavior.WALKING == "WALKING"
    assert AitekPersonBehavior.RUNNING == "RUNNING"
    assert AitekPersonBehavior.BENDING_OVER == "BENDING_OVER"
    assert AitekPersonBehavior.FALLING == "FALLING"


def test_aitek_person_behavior_default_fields():
    """AitekPersonBehavior default instance has empty/zero fields."""
    msg = AitekPersonBehavior()
    assert msg.type == ""
    assert msg.confidence == 0.0


def test_aitek_detected_person_fields():
    """AitekDetectedPerson has camera_id, bounding_box, position_3d, confidence, and behavior."""
    msg = AitekDetectedPerson()
    msg.camera_id = "cam_front"
    msg.confidence = 0.92
    assert msg.camera_id == "cam_front"
    assert msg.confidence == 0.92
    assert msg.position_3d.x == 0.0


def test_aitek_detected_person_nested_behavior():
    """AitekDetectedPerson embeds an AitekPersonBehavior message."""
    person = AitekDetectedPerson()
    person.behavior.type = AitekPersonBehavior.WALKING
    person.behavior.confidence = 0.75
    assert person.behavior.type == "WALKING"
    assert person.behavior.confidence == 0.75


def test_aitek_detection_result_fields():
    """AitekDetectionResult contains header and detected_persons."""
    msg = AitekDetectionResult()
    assert len(msg.detected_persons) == 0
    msg.header.frame_id = "base_link"
    assert msg.header.frame_id == "base_link"


def test_aitek_detection_result_with_person():
    """AitekDetectionResult can hold a list of AitekDetectedPerson messages."""
    person = AitekDetectedPerson()
    person.camera_id = "cam_01"
    result = AitekDetectionResult()
    result.detected_persons = [person]
    assert len(result.detected_persons) == 1
    assert result.detected_persons[0].camera_id == "cam_01"


# --- Emoj ---


def test_emoj_person_joint_position_constants():
    """EmojPersonJointPosition has all joint name string constants."""
    assert EmojPersonJointPosition.HEAD == "HEAD"
    assert EmojPersonJointPosition.COM == "COM"
    assert EmojPersonJointPosition.SHOULDER_LEFT == "SHOULDER_LEFT"
    assert EmojPersonJointPosition.SHOULDER_RIGHT == "SHOULDER_RIGHT"
    assert EmojPersonJointPosition.ELBOW_LEFT == "ELBOW_LEFT"
    assert EmojPersonJointPosition.ELBOW_RIGHT == "ELBOW_RIGHT"
    assert EmojPersonJointPosition.HAND_LEFT == "HAND_LEFT"
    assert EmojPersonJointPosition.HAND_RIGHT == "HAND_RIGHT"
    assert EmojPersonJointPosition.KNEE_LEFT == "KNEE_LEFT"
    assert EmojPersonJointPosition.KNEE_RIGHT == "KNEE_RIGHT"
    assert EmojPersonJointPosition.FOOT_LEFT == "FOOT_LEFT"
    assert EmojPersonJointPosition.FOOT_RIGHT == "FOOT_RIGHT"


def test_emoj_person_joint_position_fields():
    """EmojPersonJointPosition can be constructed with name, positions, and confidence."""
    msg = EmojPersonJointPosition()
    msg.name = "ELBOW_LEFT"
    msg.confidence = 0.95
    assert msg.name == "ELBOW_LEFT"
    assert msg.position_2d.x == 0.0
    assert msg.position_3d.x == 0.0
    assert msg.confidence == 0.95


def test_emoj_detected_person_fields():
    """EmojDetectedPerson has camera_id, position_2d, joints, confidence, and ergonomic_risk."""
    msg = EmojDetectedPerson()
    msg.camera_id = "cam_side"
    msg.confidence = 0.88
    msg.ergonomic_risk = 1
    assert msg.camera_id == "cam_side"
    assert msg.confidence == 0.88
    assert msg.ergonomic_risk == 1


def test_emoj_detected_person_nested_joints():
    """EmojDetectedPerson can hold a list of EmojPersonJointPosition messages."""
    joint = EmojPersonJointPosition()
    joint.name = "KNEE_RIGHT"
    joint.confidence = 0.9
    person = EmojDetectedPerson()
    person.joints = [joint]
    assert len(person.joints) == 1
    assert person.joints[0].name == "KNEE_RIGHT"


def test_emoj_detection_result_fields():
    """EmojDetectionResult contains header and detected_persons."""
    msg = EmojDetectionResult()
    assert len(msg.detected_persons) == 0
    msg.header.stamp.sec = 1000
    assert msg.header.stamp.sec == 1000


# --- Pumacy ---


def test_pumacy_activity_constants():
    """PumacyActivity has all activity string constants."""
    assert PumacyActivity.STANDING_STILL == "STANDING_STILL"
    assert PumacyActivity.SITTING == "SITTING"
    assert PumacyActivity.LAYING_DOWN == "LAYING_DOWN"
    assert PumacyActivity.WALKING == "WALKING"
    assert PumacyActivity.RUNNING == "RUNNING"
    assert PumacyActivity.BENDING_OVER == "BENDING_OVER"
    assert PumacyActivity.FALLING == "FALLING"


def test_pumacy_activity_fields():
    """PumacyActivity can be constructed with type, confidence, and anomalous."""
    msg = PumacyActivity()
    msg.type = PumacyActivity.FALLING
    msg.confidence = 0.99
    msg.anomalous = True
    assert msg.type == "FALLING"
    assert msg.confidence == 0.99
    assert msg.anomalous is True


# --- Rulex/UniTo ---


def test_rulex_area_score_constants():
    """RulexAreaScore has all area string constants."""
    assert RulexAreaScore.AREA_A == "AREA_A"
    assert RulexAreaScore.AREA_B == "AREA_B"
    assert RulexAreaScore.AREA_C == "AREA_C"
    assert RulexAreaScore.AREA_D == "AREA_D"


def test_rulex_area_score_fields():
    """RulexAreaScore has area and anomaly fields."""
    msg = RulexAreaScore()
    msg.area = RulexAreaScore.AREA_B
    msg.anomaly = True
    assert msg.area == "AREA_B"
    assert msg.anomaly is True


def test_rulex_detection_result_fields():
    """RulexDetectionResult contains area_scores and image."""
    msg = RulexDetectionResult()
    assert len(msg.area_scores) == 0
    score = RulexAreaScore()
    score.area = RulexAreaScore.AREA_A
    msg.area_scores = [score]
    assert len(msg.area_scores) == 1


# --- UniGra ---


def test_unigra_result_fields():
    """UnigraResult has collision_risk field."""
    msg = UnigraResult()
    assert msg.collision_risk == 0
    msg.collision_risk = 2
    assert msg.collision_risk == 2


# --- Smart Robotics ---


def test_sr_pallet_state_fields():
    """SrPalletState has side, layers_done, boxes_on_current_layer, and status."""
    msg = SrPalletState()
    msg.side = "left"
    msg.layers_done = 3
    msg.boxes_on_current_layer = 5
    msg.status = "PROGRESS"
    assert msg.side == "left"
    assert msg.layers_done == 3
    assert msg.boxes_on_current_layer == 5
    assert msg.status == "PROGRESS"


def test_sr_robot_system_state_fields():
    """SrRobotSystemState has joint_states, is_holding_box, current_pallet_side, lift_position, and pallet_states."""
    msg = SrRobotSystemState()
    msg.is_holding_box = True
    msg.current_pallet_side = "right"
    msg.lift_position = 1.5
    assert msg.is_holding_box is True
    assert msg.current_pallet_side == "right"
    assert msg.lift_position == 1.5
    assert len(msg.pallet_states) == 0


def test_sr_robot_system_state_nested_pallets():
    """SrRobotSystemState can hold a list of SrPalletState messages."""
    pallet = SrPalletState()
    pallet.side = "left"
    pallet.status = "FULL"
    msg = SrRobotSystemState()
    msg.pallet_states = [pallet]
    assert len(msg.pallet_states) == 1
    assert msg.pallet_states[0].status == "FULL"


def test_sr_area_activity_fields():
    """SrAreaActivity has name, engaged, operator_present, and operator_anomaly."""
    msg = SrAreaActivity()
    msg.name = "A"
    msg.engaged = True
    msg.operator_present = True
    msg.operator_anomaly = False
    assert msg.name == "A"
    assert msg.engaged is True
    assert msg.operator_present is True
    assert msg.operator_anomaly is False


def test_sr_fusion_model_output_fields():
    """SrFusionModelOutput has area_activities and robot_speed."""
    msg = SrFusionModelOutput()
    msg.robot_speed = "NORMAL"
    assert msg.robot_speed == "NORMAL"
    assert len(msg.area_activities) == 0


def test_sr_fusion_model_output_nested_activities():
    """SrFusionModelOutput can hold a list of SrAreaActivity messages."""
    activity = SrAreaActivity()
    activity.name = "B"
    activity.operator_present = True
    msg = SrFusionModelOutput()
    msg.area_activities = [activity]
    assert len(msg.area_activities) == 1
    assert msg.area_activities[0].name == "B"


# --- Relab/HMI ---


def test_relab_pallet_status_update_fields():
    """RelabPalletStatusUpdate has name and pallet_restored."""
    msg = RelabPalletStatusUpdate()
    msg.name = "left"
    msg.pallet_restored = True
    assert msg.name == "left"
    assert msg.pallet_restored is True


def test_relab_operator_input_fields():
    """RelabOperatorInput has operator_is_operational and pallet_status_update."""
    msg = RelabOperatorInput()
    msg.operator_is_operational = True
    msg.pallet_status_update.name = "right"
    msg.pallet_status_update.pallet_restored = False
    assert msg.operator_is_operational is True
    assert msg.pallet_status_update.name == "right"
    assert msg.pallet_status_update.pallet_restored is False
