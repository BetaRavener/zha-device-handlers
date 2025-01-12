"""Philips Hue Go device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import PHILIPS, PhilipsEffectCluster

(
    QuirkBuilder(PHILIPS, "7602031P7")
    .also_applies_to(PHILIPS, "7602031U7")
    .replaces(PhilipsEffectCluster, endpoint_id=11)
    .add_to_registry()
)
