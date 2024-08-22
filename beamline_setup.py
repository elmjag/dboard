from pydantic import BaseModel
from enum import Enum

"""
Defines a model for expressing use specified beamline setup.

The model captures the user changeable aspects of the beamline.
"""


class Detector(str, Enum):
    eiger = "eiger"
    jungfrau = "jungfrau"


class SampleDelivery(str, Enum):
    osc = "osc"
    hve = "hve"


class BeamlineSetup(BaseModel):
    detector: Detector = Detector.eiger
    sampleDelivery: SampleDelivery = SampleDelivery.hve
