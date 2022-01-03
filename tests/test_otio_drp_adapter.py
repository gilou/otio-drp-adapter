import opentimelineio as otio


def test_adapter():
    raw = """{
        "timeline": {
            "name": "my_timeline"
        },
        "track": {
            "name": "v1"
        },
        "clip": {
            "name": "my_clip",
            "in": 0,
            "out": 100,
            "rate": 30
        }
    }"""
    timeline = otio.adapters.read_from_string(raw, 'otio_drp_adapter')
    assert isinstance(timeline, otio.schema.Timeline)
