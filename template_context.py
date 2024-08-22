from pathlib import Path
from beamline_setup import BeamlineSetup, Detector, SampleDelivery

CONTEXT_DIR = Path("micromax-context")

DETECTOR_CONFS = {
    Detector.eiger: "eiger_detector.xml",
    Detector.jungfrau: "jungfrau_detector.xml",
}

DETECTOR_DISTANCE_MOTORS = {
    Detector.eiger: "tabd_zi",
    Detector.jungfrau: "tabd_zo",
}

DETECTOR_COVER_DEVICES = {
    Detector.eiger: "b312a-eh/dia/detc-01",
    Detector.jungfrau: "b312a-eh/dia/detc-02",
}


def _read_ctx_file(file_name: str) -> str:
    return Path(CONTEXT_DIR, file_name).read_text()


def _detector_configuration_xml(beamline_setup: BeamlineSetup):
    file_name = DETECTOR_CONFS[beamline_setup.detector]
    return _read_ctx_file(file_name)


def _ssx_methods(beamline_setup: BeamlineSetup):
    if beamline_setup.sampleDelivery == SampleDelivery.osc:
        return ""

    assert beamline_setup.sampleDelivery == SampleDelivery.hve
    return "    ssx_injector: True\n    ssx_tr_injector: True"


def generate_template_context(beamline_setup):
    return dict(
        detector_configuration_xml=_detector_configuration_xml(beamline_setup),
        detector_distance_motor=DETECTOR_DISTANCE_MOTORS[beamline_setup.detector],
        detector_cover_device=DETECTOR_COVER_DEVICES[beamline_setup.detector],
        ssx_methods=_ssx_methods(beamline_setup),
    )
