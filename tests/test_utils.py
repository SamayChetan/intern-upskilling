from utils import process_detections, build_payload


def test_no_low_confidence():
    detections = [
        {"class": "mask", "confidence": 0.91},
        {"class": "no_mask", "confidence": 0.82},
    ]

    result = process_detections(detections)

    assert result["low_conf_count"] == 0
    assert result["uncertain"] is False

def test_one_low_confidence():
    detections = [
            {"class": "mask", "confidence": 0.91},
            {"class": "no_mask", "confidence": 0.32},
    ]

    result = process_detections(detections)

    assert result["low_conf_count"] == 1
    assert result["uncertain"] is True

def test_multiple_low_confidence():
    detections = [
            {"class": "mask", "confidence": 0.25},
            {"class": "no_mask", "confidence": 0.31},
            {"class": "mask", "confidence": 0.49},
    ]

    result = process_detections(detections)

    assert result["low_conf_count"] == 3
    assert result["uncertain"] is True

def test_empty_detections():
    detections = []

    result = process_detections(detections)

    assert result["low_conf_count"] == 0
    assert result["uncertain"] is False

def test_payload_contains_frame_id():
    payload = build_payload(
        frame_id=10,
        detections=[],
        uncertain=False,
        low_conf_count=0
    )

    assert payload["frame_id"] == 10


def test_payload_contains_timestamp():
    payload = build_payload(
        frame_id=1,
        detections=[],
        uncertain=False,
        low_conf_count=0
    )

    assert "timestamp" in payload


def test_payload_structure():
    payload = build_payload(
        frame_id=5,
        detections=[
            {"class": "mask", "confidence": 0.95}
        ],
        uncertain=False,
        low_conf_count=0
    )

    assert "frame_id" in payload
    assert "timestamp" in payload
    assert "detections" in payload
    assert "uncertain" in payload
    assert "low_conf_count" in payload