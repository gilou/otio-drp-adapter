import os
import opentimelineio as otio

SAMPLE_DATA_DIR = os.path.join(os.path.dirname(__file__), "sample_data")
DRP_EXAMPLE_PATH = os.path.join(SAMPLE_DATA_DIR, "sample.drp")


def test_adapter():
    timeline = otio.adapters.read_from_file(DRP_EXAMPLE_PATH, "otio_drp_adapter")
    assert isinstance(timeline, otio.schema.Timeline)
