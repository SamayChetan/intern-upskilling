from datetime import datetime


def process_detections(detections):
    low_conf_count = 0

    for detection in detections:
        if detection["confidence"] < 0.5:
            low_conf_count += 1

    uncertain = low_conf_count > 0

    return {
        "detections": detections,
        "uncertain": uncertain,
        "low_conf_count": low_conf_count
    }


def build_payload(frame_id, detections, uncertain, low_conf_count):
    return {
        "timestamp": datetime.now().isoformat(),
        "frame_id": frame_id,
        "detections": detections,
        "uncertain": uncertain,
        "low_conf_count": low_conf_count
    }