# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_catalog_priorities 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'application/json', 'Access-Control-Allow-Origin': '*'}

CONTENT:[
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "RESURS P3",
        "object_norad_number": 41386,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": "",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 77",
        "object_norad_number": 21809,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS O-5",
        "object_norad_number": 40538,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ELYSIUM STAR 2 & LFF",
        "object_norad_number": 43760,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "PLEIADES 1A",
        "object_norad_number": 38012,
        "object_observation_quality": "99",
        "object_origin": "FR/IT",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 25",
        "object_norad_number": 18025,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "YAOGAN 26",
        "object_norad_number": 40362,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "HELIOS 1A",
        "object_norad_number": 23605,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C DEB",
        "object_norad_number": 43534,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 3",
        "object_norad_number": 15071,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 5A",
        "object_norad_number": 36104,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SPOT 7",
        "object_norad_number": 40053,
        "object_observation_quality": "99",
        "object_origin": "FR/BE/SE",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 7A",
        "object_norad_number": 37954,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 11511,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPTSAT-3000",
        "object_norad_number": 42900,
        "object_observation_quality": "99",
        "object_origin": "IT",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "High resolution electro-optical images.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "VOLGA R/B",
        "object_norad_number": 44425,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS R-5",
        "object_norad_number": 42072,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ATLAS 5 CENTAUR R/B",
        "object_norad_number": 40978,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "STPSAT-2 (USA 217)",
        "object_norad_number": 37222,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "LACMA ENOCH",
        "object_norad_number": 43777,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 21419,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "TOPEX/POSEIDON",
        "object_norad_number": 22076,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ELYSIUM STAR 2 & LFF",
        "object_norad_number": 43760,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "YAOGAN 18",
        "object_norad_number": 39363,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Carries Synthetic Aperture Radar (SAR) sensor",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IRIDIUM 120",
        "object_norad_number": 42805,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Next generation expected to last to 2030",
        "object_type": "Communications",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-16 R/B",
        "object_norad_number": 17590,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-3B R/B",
        "object_norad_number": 40750,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ATLAS 5 CENTAUR R/B",
        "object_norad_number": 40978,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 38246,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 7A",
        "object_norad_number": 37954,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS R-5",
        "object_norad_number": 42072,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 38246,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "STPSAT-2 (USA 217)",
        "object_norad_number": 37222,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 40 R/B",
        "object_norad_number": 20344,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IRIDIUM 96",
        "object_norad_number": 27376,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "\\"Spare; stored in 670 km storage orbit, not raised to 780 km operational orbit until needed\\"",
        "object_type": "Communications",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPS 5721 (DMSP 5D-1 F1)",
        "object_norad_number": 9415,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "HELIOS 1A",
        "object_norad_number": 23605,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "RESURS P1",
        "object_norad_number": 39186,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "To replace first Resurs.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 5A",
        "object_norad_number": 36104,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A R/B",
        "object_norad_number": 40382,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SAUDISAT 5A",
        "object_norad_number": 43831,
        "object_observation_quality": "99",
        "object_origin": "SA",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical imaging.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-16 R/B",
        "object_norad_number": 20625,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-14 R/B",
        "object_norad_number": 20511,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C R/B",
        "object_norad_number": 31114,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-16 R/B",
        "object_norad_number": 17590,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 9444,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "PW-SAT2",
        "object_norad_number": 43814,
        "object_observation_quality": "99",
        "object_origin": "PL",
        "object_primary_purpose": "",
        "object_secondary_purpose": "\\"Various tests, including deorbitation devices.\\"",
        "object_type": "Technology Development",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "PLEIADES 1A",
        "object_norad_number": 38012,
        "object_observation_quality": "99",
        "object_origin": "FR/IT",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CAPELLA-1",
        "object_norad_number": 43791,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "First of a planned 30-satellite constellation using radar imaging. Pathfinder.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SJ 16-02",
        "object_norad_number": 41634,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Conducting space environment exploration and technological experiments.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C R/B",
        "object_norad_number": 39625,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "DELTA 1 R/B(CEP 1)",
        "object_norad_number": 4794,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ARIANE 5 R/B",
        "object_norad_number": 36125,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ASTEX 1",
        "object_norad_number": 5560,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "YZ-1S DEB",
        "object_norad_number": 43644,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IRIDIUM 172",
        "object_norad_number": 43927,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "",
        "object_type": "Communications",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SUPERVIEW-1 04",
        "object_norad_number": 43100,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 7A",
        "object_norad_number": 37954,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "DMSP 5D-2 F9 (USA 29)",
        "object_norad_number": 18822,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 74",
        "object_norad_number": 21799,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-3 R/B",
        "object_norad_number": 13819,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPS 5721 (DMSP 5D-1 F1)",
        "object_norad_number": 9415,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "AJISAI (EGS)",
        "object_norad_number": 16908,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 281",
        "object_norad_number": 43145,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-KM R/B",
        "object_norad_number": 41336,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS O-5",
        "object_norad_number": 40538,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-27 R/B",
        "object_norad_number": 40354,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 11511,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "STPSAT-2 (USA 217)",
        "object_norad_number": 37222,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "GEOSAT",
        "object_norad_number": 15595,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ZIYUAN 3 (ZY 3)",
        "object_norad_number": 38046,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Land survey satellite.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "COSMOS 1666",
        "object_norad_number": 15889,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 11112,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPTSAT-3000",
        "object_norad_number": 42900,
        "object_observation_quality": "99",
        "object_origin": "IT",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "High resolution electro-optical images.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 23432,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS R-5",
        "object_norad_number": 42072,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 21419,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-KM R/B",
        "object_norad_number": 39454,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A R/B",
        "object_norad_number": 40382,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 11112,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C R/B",
        "object_norad_number": 31114,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 32",
        "object_norad_number": 19460,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "WORLDVIEW-2 (WV-2)",
        "object_norad_number": 35946,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Will provide earth imaging  in eight color bands; 0.5 m resolution for panchromatic images and 1.8 m for multi-spectral.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS R-5",
        "object_norad_number": 42072,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 5A",
        "object_norad_number": 36104,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    }
]'''

snapshots['test_catalog_undisclosed 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'application/json', 'Access-Control-Allow-Origin': '*'}

CONTENT:[
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CSO-1",
        "object_norad_number": 43866,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Multispectral Imaging",
        "object_secondary_purpose": "\\"Part of the MUSIS (Multinational Space-based Imaging System) programme, is resolutely open to European partnerships through bilateral agreements.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 15, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ELISA E24",
        "object_norad_number": 38008,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS O-6",
        "object_norad_number": 43223,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "June 21, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS R-6",
        "object_norad_number": 43495,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "June 17, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "April 21, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 281",
        "object_norad_number": 43145,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "January 19, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPTSAT-3000",
        "object_norad_number": 42900,
        "object_observation_quality": "99",
        "object_origin": "IT",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "High resolution electro-optical images.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 09, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "FASTRAC 1 (USA 222)",
        "object_norad_number": 37227,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Consists of two satellites that will be launched together -- Sara Lily and Emma.",
        "object_type": "Technology Development",
        "time_last_tracked": "July 31, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "May 26, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 274",
        "object_norad_number": 42058,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 02, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 274 DEB",
        "object_norad_number": 42065,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 02, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 267",
        "object_norad_number": 41334,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 06, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SAR-LUPE 4",
        "object_norad_number": 32750,
        "object_observation_quality": "99",
        "object_origin": "DE",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "\\"Synthetic Aperture Radar, 4th in a five-satellite fleet. Will be shared with the French military.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "October 22, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "October 12, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "October 08, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 25, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS O-5",
        "object_norad_number": 40538,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 05, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SAR-LUPE 2",
        "object_norad_number": 31797,
        "object_observation_quality": "99",
        "object_origin": "DE",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "January 12, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "STSS DEMO 2 (USA 209)",
        "object_norad_number": 35938,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Dathfinusrs for Missile Defense Ggency\'s 200 Capellite LEO minstellation.",
        "object_type": "Technology Development",
        "time_last_tracked": "November 21, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ELISA W23",
        "object_norad_number": 38009,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "September 06, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ELISA E12",
        "object_norad_number": 38010,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 181",
        "object_norad_number": 28537,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 15, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 181 DEB",
        "object_norad_number": 28541,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 15, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SAR-LUPE 1",
        "object_norad_number": 29658,
        "object_observation_quality": "99",
        "object_origin": "DE",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "First of five Germany surveillance satellites; 1-m resolution images.",
        "object_type": "Earth Observation",
        "time_last_tracked": "July 17, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "STSS ATRR (USA 205)",
        "object_norad_number": 34903,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Detect and track missile flights.",
        "object_type": "Technology Development",
        "time_last_tracked": "July 05, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 238",
        "object_norad_number": 38758,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "June 11, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 215",
        "object_norad_number": 37162,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Amateur observers speculate that this is part of the FIA.",
        "object_type": "Earth Observation",
        "time_last_tracked": "May 30, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 194",
        "object_norad_number": 31701,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "May 13, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 224",
        "object_norad_number": 37348,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "May 09, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "April 14, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 6A",
        "object_norad_number": 37813,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 10, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 8A",
        "object_norad_number": 39061,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 10, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ELISA W11",
        "object_norad_number": 38007,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 07, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 194 DEB",
        "object_norad_number": 31708,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 05, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "HELIOS 2B",
        "object_norad_number": 36124,
        "object_observation_quality": "99",
        "object_origin": "FR/IT/BE/ES/GR",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "\\"Optical reconnaissance, independent military intelligence capability for the EU (France has financed 90% of the B series).\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 05, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 229",
        "object_norad_number": 37386,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 05, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 182",
        "object_norad_number": 28646,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "$1 billion range.",
        "object_type": "Earth Observation",
        "time_last_tracked": "April 05, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 234",
        "object_norad_number": 38109,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Amateur observers speculate that this is part of the FIA.",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 26, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 229 DEB",
        "object_norad_number": 37391,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 26, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "HELIOS 2A",
        "object_norad_number": 28492,
        "object_observation_quality": "99",
        "object_origin": "FR/IT/BE/ES/GR",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance; independent military intelligence capability for the EU (France has financed 90% of the B series).",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 26, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 7A",
        "object_norad_number": 37954,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 22, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SAR-LUPE 3",
        "object_norad_number": 32283,
        "object_observation_quality": "99",
        "object_origin": "DE",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 22, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 5A",
        "object_norad_number": 36104,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 20, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "STSS DEMO 1 (USA 208)",
        "object_norad_number": 35937,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Use sensors on the two spacecraft to track ballistic missiles.",
        "object_type": "Technology Development",
        "time_last_tracked": "March 11, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 247",
        "object_norad_number": 39462,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "\\"US reconnaissance satellite, part of the only remaining element of the Future Imaging Architecture programme, equipped with an imaging radar. Orbit plane is 90\\u00c2\\u00b0 away in RA from each of the two earlier launches.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 10, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 10, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SAR-LUPE 5",
        "object_norad_number": 33244,
        "object_observation_quality": "99",
        "object_origin": "DE",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 10, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 238 DEB",
        "object_norad_number": 38773,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 10, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 186",
        "object_norad_number": 28888,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "$1 billion satellite; last use of Titan IV as launch vehicle.",
        "object_type": "Earth Observation",
        "time_last_tracked": "March 08, 2014",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SMDC ONE 1.2",
        "object_norad_number": 38759,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Mission unknown.",
        "object_type": "Technology Development",
        "time_last_tracked": "September 15, 2012",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 152",
        "object_norad_number": 26473,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "$1 billion range; 3-10 ft. image resolution.",
        "object_type": "Earth Observation",
        "time_last_tracked": "September 01, 2000",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 119",
        "object_norad_number": 23893,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Provides tactical intelligence focused support to broad community of users consisting of uniformed military services and government agencies for both exercises and operations.",
        "object_type": "Communications",
        "time_last_tracked": "September 09, 1998",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 133",
        "object_norad_number": 25017,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "\\"$1 billion range; space-based imaging radar, uses radar pulses to see through clouds, fog, haze, darkness and generate images.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "February 07, 1998",
        "username_last_tracked": "Russell Eberst"
    }
]'''

snapshots['test_catalog_debris 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'application/json', 'Access-Control-Allow-Origin': '*'}

CONTENT:[
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 40366,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 07, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 41583,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 07, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "FALCON 9 DEB",
        "object_norad_number": 44296,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 02, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A DEB",
        "object_norad_number": 43673,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "June 20, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "FALCON 9 DEB",
        "object_norad_number": 44295,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CREW DRAGON DEMO-1 DEB",
        "object_norad_number": 44064,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 23, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A DEB",
        "object_norad_number": 43675,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 22, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A DEB",
        "object_norad_number": 43674,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C DEB",
        "object_norad_number": 43534,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 17, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IRIDIUM 33 DEB",
        "object_norad_number": 33773,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 13, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "PSLV DEB",
        "object_norad_number": 41792,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "March 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "YAOGAN 4 DEB",
        "object_norad_number": 35575,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "February 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 37828,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "February 09, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 39010,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "January 29, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-23 DEB",
        "object_norad_number": 37756,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "January 02, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-24 DEB",
        "object_norad_number": 40537,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "November 27, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPS 4682 DEB",
        "object_norad_number": 1316,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "November 01, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "AVUM DEB [ADAPTOR]",
        "object_norad_number": 39162,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 28, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "DELTA 1 DEB",
        "object_norad_number": 7838,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 21, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "DELTA 1 DEB",
        "object_norad_number": 7054,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 18, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "YZ-1S DEB",
        "object_norad_number": 43644,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 10, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "THOR ABLESTAR DEB",
        "object_norad_number": 122,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 30, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 42751,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 23, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C DEB",
        "object_norad_number": 43531,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 29, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 39129,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 21, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "THORAD AGENA D DEB",
        "object_norad_number": 4217,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "July 25, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB",
        "object_norad_number": 32026,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "July 05, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 36794,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 18, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 39024,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 18, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 39174,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 14, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-4C DEB",
        "object_norad_number": 43281,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 14, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 39287,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 10, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 42936,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 28, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-4C DEB",
        "object_norad_number": 43261,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 25, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-4C DEB",
        "object_norad_number": 43265,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 20, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 37260,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 09, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "PSLV DEB",
        "object_norad_number": 43112,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "March 28, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A DEB",
        "object_norad_number": 43068,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "March 13, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-4 DEB",
        "object_norad_number": 20853,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "February 11, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "THORAD AGENA D DEB",
        "object_norad_number": 4216,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "January 27, 2018",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 42944,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 29, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-14 DEB",
        "object_norad_number": 22845,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 10, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-24 DEB",
        "object_norad_number": 28812,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 05, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-4 DEB",
        "object_norad_number": 20846,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 02, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 33374,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 31, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "AVUM DEB [ADAPTOR]",
        "object_norad_number": 42902,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 29, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "DELTA 1 DEB",
        "object_norad_number": 8956,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 29, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 28528,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 15, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-12 DEB",
        "object_norad_number": 18765,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 12, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "FREGAT DEB [TANK]",
        "object_norad_number": 41108,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 07, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 36594,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "July 20, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 33279,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "July 16, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 39124,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "June 19, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 28395,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 16, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-24 DEB",
        "object_norad_number": 35689,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 05, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "NOAA 14 DEB",
        "object_norad_number": 38732,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 25, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 274 DEB",
        "object_norad_number": 42065,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "",
        "time_last_tracked": "March 02, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-4 DEB",
        "object_norad_number": 20855,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "January 26, 2017",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A DEB",
        "object_norad_number": 38345,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "December 10, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 37604,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "November 19, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 36103,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 04, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 27646,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 27, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 37845,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 19, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "AVUM DEB [ADAPTOR]",
        "object_norad_number": 41775,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 16, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IRIDIUM 33 DEB",
        "object_norad_number": 33967,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 11, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 28116,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 11, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-4 DEB",
        "object_norad_number": 20849,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 02, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "METEOR 1-10 DEB",
        "object_norad_number": 8826,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 26, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 41193,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 06, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 35495,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 01, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "THORAD AGENA D DEB",
        "object_norad_number": 4719,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 01, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-23 DEB",
        "object_norad_number": 37347,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "July 27, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-24 DEB",
        "object_norad_number": 31791,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "July 02, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "THOR ABLESTAR DEB",
        "object_norad_number": 119,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "May 16, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 34712,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "March 31, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPS 4682 DEB",
        "object_norad_number": 1389,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "March 09, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IRIDIUM 33 DEB",
        "object_norad_number": 33876,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "February 10, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 40986,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "January 14, 2016",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SHIYAN 7 DEB",
        "object_norad_number": 39357,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "December 10, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-4 DEB",
        "object_norad_number": 20877,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "December 02, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-24 DEB",
        "object_norad_number": 28374,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "December 02, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A DEB",
        "object_norad_number": 38346,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "November 16, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 39615,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 14, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 34943,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 12, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-24 DEB",
        "object_norad_number": 37797,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 09, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "time_last_tracked": "October 08, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A DEB",
        "object_norad_number": 38347,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "October 08, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 28926,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 25, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-24 DEB",
        "object_norad_number": 29256,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 16, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 37871,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "September 07, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 DEB",
        "object_norad_number": 1392,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "August 06, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 DEB",
        "object_norad_number": 1335,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "July 26, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 39362,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "July 01, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 38089,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "June 23, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 15 DEB",
        "object_norad_number": 16623,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 25, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-24 DEB",
        "object_norad_number": 37796,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 17, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "FREGAT DEB",
        "object_norad_number": 40078,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "April 05, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "THORAD AGENA D DEB",
        "object_norad_number": 4607,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "March 11, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ARIANE 1 DEB",
        "object_norad_number": 17153,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "February 18, 2015",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 144 DEB",
        "object_norad_number": 25746,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "time_last_tracked": "February 16, 2015",
        "username_last_tracked": "Russell Eberst"
    }
]'''

snapshots['test_catalog_latest 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'application/json', 'Access-Control-Allow-Origin': '*'}

CONTENT:[
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "RESURS P3",
        "object_norad_number": 41386,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": "",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 77",
        "object_norad_number": 21809,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS O-5",
        "object_norad_number": 40538,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ELYSIUM STAR 2 & LFF",
        "object_norad_number": 43760,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "PLEIADES 1A",
        "object_norad_number": 38012,
        "object_observation_quality": "99",
        "object_origin": "FR/IT",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 25",
        "object_norad_number": 18025,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "YAOGAN 26",
        "object_norad_number": 40362,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "HELIOS 1A",
        "object_norad_number": 23605,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C DEB",
        "object_norad_number": 43534,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 3",
        "object_norad_number": 15071,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 5A",
        "object_norad_number": 36104,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SPOT 7",
        "object_norad_number": 40053,
        "object_observation_quality": "99",
        "object_origin": "FR/BE/SE",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 7A",
        "object_norad_number": 37954,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 11511,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPTSAT-3000",
        "object_norad_number": 42900,
        "object_observation_quality": "99",
        "object_origin": "IT",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "High resolution electro-optical images.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "VOLGA R/B",
        "object_norad_number": 44425,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS R-5",
        "object_norad_number": 42072,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ATLAS 5 CENTAUR R/B",
        "object_norad_number": 40978,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "STPSAT-2 (USA 217)",
        "object_norad_number": 37222,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "LACMA ENOCH",
        "object_norad_number": 43777,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 21419,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "TOPEX/POSEIDON",
        "object_norad_number": 22076,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ELYSIUM STAR 2 & LFF",
        "object_norad_number": 43760,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "YAOGAN 18",
        "object_norad_number": 39363,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Carries Synthetic Aperture Radar (SAR) sensor",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IRIDIUM 120",
        "object_norad_number": 42805,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Next generation expected to last to 2030",
        "object_type": "Communications",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-16 R/B",
        "object_norad_number": 17590,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-3B R/B",
        "object_norad_number": 40750,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 28, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ATLAS 5 CENTAUR R/B",
        "object_norad_number": 40978,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 38246,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 7A",
        "object_norad_number": 37954,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS R-5",
        "object_norad_number": 42072,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-M DEB [TANK]",
        "object_norad_number": 38246,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "STPSAT-2 (USA 217)",
        "object_norad_number": 37222,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 40 R/B",
        "object_norad_number": 20344,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IRIDIUM 96",
        "object_norad_number": 27376,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "\\"Spare; stored in 670 km storage orbit, not raised to 780 km operational orbit until needed\\"",
        "object_type": "Communications",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPS 5721 (DMSP 5D-1 F1)",
        "object_norad_number": 9415,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "HELIOS 1A",
        "object_norad_number": 23605,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "RESURS P1",
        "object_norad_number": 39186,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "To replace first Resurs.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 5A",
        "object_norad_number": 36104,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A R/B",
        "object_norad_number": 40382,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SAUDISAT 5A",
        "object_norad_number": 43831,
        "object_observation_quality": "99",
        "object_origin": "SA",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical imaging.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-16 R/B",
        "object_norad_number": 20625,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-14 R/B",
        "object_norad_number": 20511,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C R/B",
        "object_norad_number": 31114,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-16 R/B",
        "object_norad_number": 17590,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 9444,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "PW-SAT2",
        "object_norad_number": 43814,
        "object_observation_quality": "99",
        "object_origin": "PL",
        "object_primary_purpose": "",
        "object_secondary_purpose": "\\"Various tests, including deorbitation devices.\\"",
        "object_type": "Technology Development",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "PLEIADES 1A",
        "object_norad_number": 38012,
        "object_observation_quality": "99",
        "object_origin": "FR/IT",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CAPELLA-1",
        "object_norad_number": 43791,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "First of a planned 30-satellite constellation using radar imaging. Pathfinder.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SJ 16-02",
        "object_norad_number": 41634,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Conducting space environment exploration and technological experiments.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C R/B",
        "object_norad_number": 39625,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "DELTA 1 R/B(CEP 1)",
        "object_norad_number": 4794,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ARIANE 5 R/B",
        "object_norad_number": 36125,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ASTEX 1",
        "object_norad_number": 5560,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "YZ-1S DEB",
        "object_norad_number": 43644,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 26, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IRIDIUM 172",
        "object_norad_number": 43927,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "",
        "object_type": "Communications",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SUPERVIEW-1 04",
        "object_norad_number": 43100,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 7A",
        "object_norad_number": 37954,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "DMSP 5D-2 F9 (USA 29)",
        "object_norad_number": 18822,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 74",
        "object_norad_number": 21799,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-3 R/B",
        "object_norad_number": 13819,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPS 5721 (DMSP 5D-1 F1)",
        "object_norad_number": 9415,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "AJISAI (EGS)",
        "object_norad_number": 16908,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 281",
        "object_norad_number": 43145,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-KM R/B",
        "object_norad_number": 41336,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS O-5",
        "object_norad_number": 40538,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-27 R/B",
        "object_norad_number": 40354,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 11511,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "STPSAT-2 (USA 217)",
        "object_norad_number": 37222,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "GEOSAT",
        "object_norad_number": 15595,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "ZIYUAN 3 (ZY 3)",
        "object_norad_number": 38046,
        "object_observation_quality": "99",
        "object_origin": "CN",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Land survey satellite.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "COSMOS 1666",
        "object_norad_number": 15889,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 11112,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "OPTSAT-3000",
        "object_norad_number": 42900,
        "object_observation_quality": "99",
        "object_origin": "IT",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "High resolution electro-optical images.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 23432,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS R-5",
        "object_norad_number": 42072,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 21419,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "BREEZE-KM R/B",
        "object_norad_number": 39454,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "H-2A R/B",
        "object_norad_number": 40382,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 25, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "SL-8 R/B",
        "object_norad_number": 11112,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "CZ-2C R/B",
        "object_norad_number": 31114,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 9A",
        "object_norad_number": 40381,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Radar reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "USA 32",
        "object_norad_number": 19460,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "WORLDVIEW-2 (WV-2)",
        "object_norad_number": 35946,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Will provide earth imaging  in eight color bands; 0.5 m resolution for panchromatic images and 1.8 m for multi-spectral.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS R-5",
        "object_norad_number": 42072,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    },
    {
        "address_last_tracked": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "object_name": "IGS 5A",
        "object_norad_number": 36104,
        "object_observation_quality": "99",
        "object_origin": "JP",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Optical reconnaissance.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 24, 2019",
        "username_last_tracked": "Russell Eberst"
    }
]'''

snapshots['test_catalog_all 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'application/json', 'Access-Control-Allow-Origin': '*'}

CONTENT:[
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "MINOTAUR 4 R/B",
        "object_norad_number": 37228,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E24",
        "object_norad_number": 38008,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E24",
        "object_norad_number": 38008,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E12",
        "object_norad_number": 38010,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E12",
        "object_norad_number": 38010,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E24",
        "object_norad_number": 38008,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E12",
        "object_norad_number": 38010,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E24",
        "object_norad_number": 38008,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E12",
        "object_norad_number": 38010,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E24",
        "object_norad_number": 38008,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E24",
        "object_norad_number": 38008,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E12",
        "object_norad_number": 38010,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "ELISA E12",
        "object_norad_number": 38010,
        "object_observation_quality": "99",
        "object_origin": "FR",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "In-orbit elint demonstration project. Will identify ground-based radars and other telecommunications sources; to be replaced by operational ELINT system by end of decade.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 245",
        "object_norad_number": 39232,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Optical Imaging",
        "object_secondary_purpose": "Believed to be KH-11 class.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 22",
        "object_norad_number": 17997,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 22",
        "object_norad_number": 17997,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 22",
        "object_norad_number": 17997,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 22",
        "object_norad_number": 17997,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 22",
        "object_norad_number": 17997,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264 DEB",
        "object_norad_number": 40981,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 264",
        "object_norad_number": 40964,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Electronic Intelligence",
        "object_secondary_purpose": "\\"ELINT system; wide area ocean surveillance, primarily for the Navy and surveillance of shipping.\\"",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 234",
        "object_norad_number": 38109,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Amateur observers speculate that this is part of the FIA.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 234",
        "object_norad_number": 38109,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Amateur observers speculate that this is part of the FIA.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 234",
        "object_norad_number": 38109,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Amateur observers speculate that this is part of the FIA.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 234",
        "object_norad_number": 38109,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Amateur observers speculate that this is part of the FIA.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 234",
        "object_norad_number": 38109,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Amateur observers speculate that this is part of the FIA.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 234",
        "object_norad_number": 38109,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Amateur observers speculate that this is part of the FIA.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 234",
        "object_norad_number": 38109,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "Amateur observers speculate that this is part of the FIA.",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "OTV 5 (USA 277)",
        "object_norad_number": 42932,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Fifth flight of X37-B.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 160 DEB",
        "object_norad_number": 26907,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "SBSS (USA 216)",
        "object_norad_number": 37168,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Designed to track and detect other spacecraft in orbit.",
        "object_type": "Space Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 32",
        "object_norad_number": 19460,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 32",
        "object_norad_number": 19460,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 32",
        "object_norad_number": 19460,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 32",
        "object_norad_number": 19460,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 276",
        "object_norad_number": 42689,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "",
        "object_secondary_purpose": "Believed to be a technology demonstration satellite for a future project.",
        "object_type": "Technology Development",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "FASTRAC 2 (USA 228)",
        "object_norad_number": 37380,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "FASTRAC 2 (USA 228)",
        "object_norad_number": 37380,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "FASTRAC 2 (USA 228)",
        "object_norad_number": 37380,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "FASTRAC 2 (USA 228)",
        "object_norad_number": 37380,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 267",
        "object_norad_number": 41334,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 267",
        "object_norad_number": 41334,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 267",
        "object_norad_number": 41334,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 267",
        "object_norad_number": 41334,
        "object_observation_quality": "99",
        "object_origin": "US",
        "object_primary_purpose": "Radar Imaging",
        "object_secondary_purpose": "",
        "object_type": "Earth Observation",
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 122",
        "object_norad_number": 23862,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 122",
        "object_norad_number": 23862,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 122",
        "object_norad_number": 23862,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    },
    {
        "address_last_tracked": "0x77E365e4BdCEF3e0C513d2ADbFC09B829ad24Ac8",
        "object_name": "USA 122",
        "object_norad_number": 23862,
        "object_observation_quality": "99",
        "object_origin": "",
        "object_primary_purpose": null,
        "object_secondary_purpose": null,
        "object_type": null,
        "time_last_tracked": "August 29, 2019",
        "username_last_tracked": "Cees Bassa"
    }
]'''

snapshots['test_tle_trusat_all 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'text/plain', 'Access-Control-Allow-Origin': '*'}

CONTENT:Canyon 1
1 03334U 68063A   10123.40009905 0.00000000  00000-0  00000-0 0    03
2 03334  15.3109 349.9077 0930186  62.8827 306.3130  0.99244310    01
Canyon 2
1 03889U 69036A   10123.85895608 0.00000000  00000-0  00000-0 0    01
2 03889   2.1240 154.2443 0941406 326.6324  27.8335  1.00368037    08
Intelsat 3F7
1 04376U 70032A   09043.49870956 0.00000000  00000-0  00000-0 0    09
2 04376  10.3292 321.4666 0004451 284.3056  75.6570  1.00281526    04
Rhyolite 1
1 04418U 70046A   11005.40772169 0.00000000  00000-0  00000-0 0    00
2 04418   9.3696 318.3178 0011896  57.3581 302.7686  1.00251116    06
Canyon 3
1 04510U 70069A   11008.55443638 0.00000000  00000-0  00000-0 0    03
2 04510  17.7662 292.6247 0869018 244.5444 106.2216  1.00243524    01
DSP F2
1 05204U 71039A   08086.15413223 0.00000000  00000-0  00000-0 0    07
2 05204  10.7656 324.2652 0007863  26.4922 333.5601  1.00266212    02
DSP F2 r
1 05205U 71039B   11005.53095150 0.00000000  00000-0  00000-0 0    00
2 05205   9.7468 321.1078 0032465 323.0265  36.7621  1.00414555    01
NOSS 0 (A)
1 05678U 71110A   06021.74281767 0.00000020  00000-0  21364-4 0    02
2 05678  69.9820 260.2836 0006000 164.1547 195.8453 13.73783199    09
NOSS 0 r
1 05679U 71110B   05365.76203398 0.00000030  00000-0  26500-4 0    07
2 05679  70.0000 210.4505 0015000 293.5570  66.4430 13.84958551    02
NOSS 0 (C)
1 05680U 71110C   06020.75411501 0.00000030  00000-0  31803-4 0    06
2 05680  69.9810 254.0019 0008000 161.0640 198.9360 13.74231084    00
NOSS 0 (D)
1 05681U 71110D   06021.76087966 0.00000030  00000-0  31852-4 0    07
2 05681  69.9900 253.0594 0004000 210.9628 149.0372 13.74150281    03
NOSS 0 (E)
1 05682U 71110E   06010.89007426 0.00000020  00000-0  21229-4 0    09
2 05682  69.9803 275.1969 0010000 175.2520 184.7480 13.74147571    02
DSP F3
1 05851U 62010A   08086.20613198 0.00000000  00000-0  00000-0 0    03
2 05851  12.2906 334.7519 0018455  92.8538 267.3695  1.00270317    00
DSP F3 r
1 05854U 72010B   11005.43225509 0.00000000  00000-0  00000-0 0    02
2 05854  10.3342 324.0683 0063364 357.7199   2.2635  1.00673084    03
Canyon 5
1 06317U 72101A   11008.54416051 0.00000000  00000-0  00000-0 0    07
2 06317  20.0936 334.3235 1324186 283.8601  61.7469  1.00221794    04
Canyon 5 r
1 06318U 72101B   10239.11847001 0.00000000  00000-0  00000-0 0    09
2 06318  19.3177 331.9150 1282609 333.9047  20.1530  1.02309316    03
Rhyolite 2
1 06380U 73013A   11005.41574207 0.00000000  00000-0  00000-0 0    01
2 06380  11.3440 327.9270 0021169 109.4382 250.8027  1.00264876    06
DSP F4
1 06691U 73040A   08098.37693189 0.00000000  00000-0  00000-0 0    00
2 06691  12.9189 334.4397 0007787 208.6198 151.3495  0.99825195    06
DMSP 7
1 07816U 75043A   06004.26317354 0.00000070  00000-0  31254-4 0    01
2 07816  98.5820 203.1249 0053000 225.1915 134.8084 14.22025303    00
Canyon 6
1 07963U 75055A   11221.82705374 0.00000000  00000-0  00000-0 0    03
2 07963  20.8266 336.9310 1291601 251.9194  93.6187  1.00161775    09
Canyon 6 r
1 07964U 75055B   10122.60104465 0.00000000  00000-0  00000-0 0    03
2 07964  20.3166 338.6817 1312086 297.0392  50.1742  1.02091197    04
DSP F5
1 08482U 75118A   08096.39725032 0.00000000  00000-0  00000-0 0    01
2 08482  14.2089 345.0303 0004294 353.2314   6.7748  0.99469072    04
DSP F5 r2
1 08516U 75118C   10122.76384947 0.00000000  00000-0  00000-0 0    09
2 08516  13.0312 335.7526 0014254  26.1951 333.8889  1.00537189    09
NOSS 1 (A)
1 08818U 76038A   06009.27071717 0.00000910  00000-0  93106-4 0    02
2 08818  63.3050  84.6572 0875000  53.9584 306.0416 13.53455271    06
NOSS 1 (C)
1 08835U 76038C   06009.27537296 0.00000900  00000-0  94452-4 0    04
2 08835  63.3040  85.2586 0871500  58.5500 301.4500 13.53464917    06
NOSS 1 (D)
1 08836U 76038D   06001.23692537 0.00000900  00000-0  92190-4 0    00
2 08836  63.3045 116.3278 0878000  53.6809 306.3191 13.52814296    04
NOSS 1 (J)
1 08884U 76038J   06004.24488934 0.00000900  00000-0  94391-4 0    06
2 08884  63.3070  98.1516 0871500  58.2759 301.7241 13.53482768    01
DSP F6
1 08916U 76059A   07079.50377131 0.00000000  00000-0  00000-0 0    04
2 08916  13.8181 344.4747 0029627 177.9250 182.0994  1.00452685    02
DSP F6 r2
1 08918U 76059C   10122.52944398 0.00000000  00000-0  00000-0 0    06
2 08918  13.3364 337.3635 0012322  64.7732 295.3666  1.00562065    09
AMS 1(DMSP F1)
1 09415U 76091A   06001.25011777 0.00000070  00000-0  29618-4 0    09
2 09415  98.9850 210.8688 0012000 137.6036 222.3963 14.25525199    02
DSP F7
1 09803U 77007A   08114.44862472 0.00000000  00000-0  00000-0 0    05
2 09803  14.7754 349.6778 0080086 225.1035 134.2558  0.97530801    05
DSP F7 r2
1 09855U 77007C   11001.84593791 0.00000000  00000-0  00000-0 0    00
2 09855  13.6141 337.9179 0012657 249.6341 110.2420  1.00250495    00
DSP F7 Cover
1 09856U 77007D   11008.58424549 0.00000000  00000-0  00000-0 0    03
2 09856  13.5082 335.8751 0280774 338.3763  20.7070  1.00562393    07
Canyon 7
1 10016U 77038A   11210.94542121 0.00000000  00000-0  00000-0 0    09
2 10016  11.2708   6.6753 1234411 353.9543   4.6847  1.00230764    06
AMS 2(DMSP F2)
1 10033U 77044A   06009.20947247 0.00000055  00000-0  22039-4 0    02
2 10033  99.1150 341.8062 0041000 195.1400 164.8599 14.27901766    08
NOSS 2 (A)
1 10502U 77112A   06009.76375048 0.00000250  00000-0  50559-4 0    09
2 10502  63.3360  98.9638 0815500  28.7167 331.2833 13.44798729    01
Rhyolite 3
1 10508U 77114A   11008.74855715 0.00000000  00000-0  00000-0 0    09
2 10508  19.0226 351.8409 0020259 213.5990 146.2844  1.00289870    07
NOSS 2 (D)
1 10529U 77112D   06012.22156335 0.00000250  00000-0  49488-4 0    08
2 10529  63.3330  91.3147 0818500  35.0169 324.9831 13.44914612    03
NOSS 2 (E)
1 10544U 77112E   06012.24981873 0.00000240  00000-0  48080-4 0    06
2 10544  63.3280  91.6270 0816500  34.9837 325.0163 13.44913427    05
NOSS 2 (F)
1 10594U 77112F   06021.23098060 0.00000180  00000-0  36089-4 0    06
2 10594  63.3373  73.9008 0818000  28.9052 331.0948 13.44595788    08
FleetSatCom 1
1 10669U 78016A   08291.77004869 0.00000000  00000-0  00000-0 0    08
2 10669  15.3166 359.1225 0003786 189.3854 170.6196  0.99001209    05
Rhyolite 4
1 10787U 78038A   10154.31636398 0.00000000  00000-0  00000-0 0    02
2 10787  10.9051 348.3458 0009044 140.3101 219.7682  1.00463900    01
Vortex 1
1 10941U 78058A   08090.45486010 0.00000000  00000-0  00000-0 0    01
2 10941   7.6350 355.8693 1079347 280.1798  67.8410  1.00276373    08
Vortex 1 r
1 10942U 78058B   11005.78215515 0.00000000  00000-0  00000-0 0    08
2 10942   4.1414  29.4797 1477379  17.7038 346.9449  0.99630870    05
AMS 4(DMSP F4)
1 11389U 79050A   06003.72990493 0.00000060  00000-0  24677-4 0    04
2 11389  98.8730  44.0192 0014000 100.7336 259.2663 14.26974127    00
DSP F8
1 11397U 79053A   08090.53814964 0.00000000  00000-0  00000-0 0    05
2 11397  14.8450   2.2863 0005860 133.4590 226.6018  0.98746460    09
DSP F8 r2
1 11436U 79053C   10186.45711167 0.00000000  00000-0  00000-0 0    00
2 11436  14.9061 354.8558 0054070 136.1219 224.3289  0.99437731    08
Vortex B
1 11558U 79086A   08086.38392276 0.00000000  00000-0  00000-0 0    05
2 11558   5.5456   9.1846 0949142 216.9956 136.0829  1.00270000    01
Vortex 2 r2
1 11560U 79086C   10163.55770832 0.00000000  00000-0  00000-0 0    04
2 11560   6.9789 352.5593 1298164  38.3842 330.1857  0.99674722    08
NOSS 3 (A)
1 11720U 80019A   06012.26008070 0.00000100  00000-0  41590-4 0    08
2 11720  63.4061  63.2060 0689094 339.9632  20.0368 13.42277773    03
NOSS 3 (C)
1 11731U 80019C   06002.19803734 0.00000100  00000-0  31733-4 0    09
2 11731  63.3990  75.3164 0744500 347.7610  12.2390 13.42586373    08
NOSS 3 (D)
1 11732U 80019D   06002.19206682 0.00000110  00000-0  35134-4 0    09
2 11732  63.3970  75.5233 0743500 347.9431  12.0569 13.42531475    07
NOSS 3 (G)
1 11745U 80019G   06012.20310123 0.00000100  00000-0  42507-4 0    03
2 11745  63.4122  71.4502 0686500 339.2665  20.7335 13.41864885    04
KH 9-16 Elint
1 11852U 80052C   06039.21206398 0.00000017  00000-0  71475-4 0    00
2 11852  96.6040  17.8887 0001500  51.8884 308.1115 12.83309062    06
Ekran 5
1 11890U 80060A   11087.45687140 0.00000000  00000-0  00000-0 0    08
2 11890  14.3967 346.5687 0018148  37.1907 322.9468  1.00283477    05
DSP F4 r
1 11940U 73040B   11001.96298108 0.00000000  00000-0  00000-0 0    08
2 11940  12.1271 327.7115 0028171 267.2785  92.4171  0.99556133    08
FleetSatCom 4
1 12046U 80087A   08048.55787839 0.00000000  00000-0  00000-0 0    01
2 12046  14.3411   7.6528 0000303 216.0758 143.9342  0.98954925    09
DSP F9
1 12339U 81025A   07313.15890331 0.00000000  00000-0  00000-0 0    01
2 12339  14.3160   8.7296 0016263 108.4172 251.7717  0.98821615    08
DSP F9 r2
1 12371U 81025C   11008.65766043 0.00000000  00000-0  00000-0 0    00
2 12371  14.0354 356.4170 0050104 158.5486 201.6742  1.01328057    05
Vortex 3
1 12930U 81107A   08256.17620449 0.00000000  00000-0  00000-0 0    09
2 12930   7.2702 358.1588 0937156 264.7361  84.5292  1.00196143    08
Vortex 3 r2
1 12932U 81107C   11002.00572033 0.00000000  00000-0  00000-0 0    01
2 12932   7.7252 351.7751 0964737  28.0144 336.8851  0.99598272    01
DSP F10
1 13086U 82019A   08064.36790061 0.00000000  00000-0  00000-0 0    01
2 13086  14.6381  12.2070 0003547 192.0567 167.9468  0.98187064    08
DSP F10 r
1 13089U 82019B   10122.67457340 0.00000000  00000-0  00000-0 0    06
2 13089  14.2542   2.0245 0015158 336.6330  23.3102  1.01259794    07
KH 9-17 Elint
1 13172U 82041C   06021.77836867 0.00000380  00000-0  48262-4 0    00
2 13172  95.9810  59.5302 0003003 148.0009 211.9990 14.81752848    09
DSCS 3-1
1 13637U 82106B   09086.57587271 0.00000000  00000-0  00000-0 0    05
2 13637  12.8363  29.5893 0014471  24.5147 335.5789  0.97822440    07
NOSS 4 (A)
1 13791U 83008A   05365.75640978 0.00000240  00000-0  11426-3 0    01
2 13791  63.3680 326.6365 0661000  13.3522 346.6478 13.41737496    02
NOSS 4 (E)
1 13844U 83008E   05365.75151752 0.00000200  00000-0  96629-4 0    02
2 13844  63.3690 333.2877 0659500  13.2795 346.7205 13.41384743    09
NOSS 4 (F)
1 13845U 83008F   05365.78563490 0.00000180  00000-0  85077-4 0    04
2 13845  63.3660 332.2210 0664500  18.6956 341.3044 13.41422712    02
NOSS 4 (H)
1 13874U 83008H   06003.75362458 0.00000160  00000-0  74156-4 0    08
2 13874  63.3690 324.6016 0669000  18.2405 341.7596 13.41442010    00
NOSS 5 (A)
1 14112U 83056A   06012.20716683 0.00000100  00000-0  50482-4 0    00
2 14112  63.3690 152.9751 0648000  11.5924 348.4076 13.41544224    00
KH 9-18 Elint
1 14139U 83060C   06017.76197650 -.00000010  00000-0 -36357-4 0    04
2 14139  96.6545 212.5709 0001500 215.9289 144.0710 12.93723529    03
NOSS 5 (C)
1 14143U 83056C   06012.25073528 0.00000060  00000-0  29173-4 0    01
2 14143  63.3670 155.4097 0658000  16.3428 343.6572 13.41381711    04
NOSS 5 (D)
1 14144U 83056D   06012.26535057 0.00000030  00000-0  14479-4 0    03
2 14144  63.3700 156.2478 0660000  16.5321 343.4679 13.41342763    08
NOSS 5 (G)
1 14180U 83056G   06012.25830263 0.00000030  00000-0  14961-4 0    05
2 14180  63.3700 157.2054 0652500  11.3842 348.6158 13.41275153    03
Vortex 4
1 14675U 84009A   08254.00611331 0.00000000  00000-0  00000-0 0    01
2 14675   7.6479 356.0872 1075535 282.8383  65.3832  1.00270000    06
Vortex 4 r2
1 14677U 84009C   11005.54089154 0.00000000  00000-0  00000-0 0    02
2 14677   7.9119 358.7188 0973592   1.3230 358.9621  0.99442161    08
NOSS 6 (A)
1 14690U 84012A   05365.79376013 0.00000150  00000-0  83314-4 0    02
2 14690  63.3780 249.4662 0625000   7.9287 352.0713 13.41396801    05
NOSS 6 P/S
1 14691U 84012B   15157.92364826 0.00030000  00000-0  49029-2 0    07
2 14691  63.2063 101.5270 0508509  92.9460 267.6227 14.10126907    09
NOSS 6 (C)
1 14728U 84012C   05365.82802004 0.00000140  00000-0  76072-4 0    04
2 14728  63.3730 255.3263 0634500  15.1951 344.8049 13.40721876    03
NOSS 6 (D)
1 14729U 84012D   05365.82148756 0.00000140  00000-0  76387-4 0    01
2 14729  63.3730 254.7782 0633000  15.3266 344.6734 13.40800738    02
NOSS 6 (F)
1 14795U 84012F   05365.76390722 0.00000110  00000-0  61830-4 0    03
2 14795  63.3770 258.4890 0626000   7.7191 352.2809 13.40703219    08
DSP F11
1 14930U 84037A   08090.56650089 0.00000000  00000-0  00000-0 0    08
2 14930  14.0419  18.2076 0005398 121.6795 238.3852  0.98681548    08
DSP F11 r
1 14931U 84037B   10122.64908370 0.00000000  00000-0  00000-0 0    06
2 14931  14.0201   9.2730 0027160 163.5370 196.5700  1.01165890    09
USA 3
1 15071U 84065C   06004.24535974 0.00000500  00000-0  60160-4 0    01
2 15071  95.8872 199.5948 0003000 160.1409 199.8589 14.84003314    01
Canyon 7 r2?
1 15422U 77038C   10191.67764865 0.00000000  00000-0  00000-0 0    03
2 15422  10.5096   7.4978 1472221  32.1671 336.0317  1.02333119    07
DSP F12 USA 7
1 15453U 84129A   08100.43318721 0.00000000  00000-0  00000-0 0    03
2 15453  13.8988  24.8677 0003138 220.2659 139.7229  0.98851744    01
DSP F12 r
1 15454U 84129B   10191.65064750 0.00000000  00000-0  00000-0 0    01
2 15454  14.4335  15.4732 0004626   5.5645 354.4527  1.01159923    07
Magnum 1 USA 8
1 15543U 85010B   08086.36389186 0.00000000  00000-0  00000-0 0    01
2 15543  15.5902  26.8044 0016419 255.3492 104.4758  1.00270000    06
Magnum 1 r2
1 15545U 85010D   11001.85767895 0.00000000  00000-0  00000-0 0    05
2 15545  16.9666  17.2390 0024810 132.4417 227.7805  1.00811075    09
DSCS 3-2
1 16116U 85092B   11002.02934994 0.00000000  00000-0  00000-0 0    06
2 16116  12.5337  40.0812 0005992 320.9918  38.9771  0.98986082    05
DSCS 3-3
1 16117U 85092C   11002.02521120 0.00000000  00000-0  00000-0 0    00
2 16117  12.3047  41.8378 0003933  42.3089 317.7264  0.99321201    07
DSCS 3-2 r2
1 16119U 85092E   11001.86215215 0.00000000  00000-0  00000-0 0    08
2 16119  14.5985  12.3049 0060958  24.0546 336.2479  1.01082978    00
NOSS 7 (A)
1 16591U 86014A   05365.73722074 0.00000070  00000-0  49561-4 0    01
2 16591  63.3900 210.5319 0560502   2.3116 357.6884 13.41103355    04
NOSS 1-7 PS
1 16592U 86014B   15105.10231904 0.00001500  00000-0  68791-3 0    07
2 16592  63.3160  10.7169 0540649  97.1787 262.8213 13.64013249    02
NOSS 7 (D)
1 16623U 86014D   05365.73886567 0.00000080  00000-0  56334-4 0    02
2 16623  63.3842 214.0383 0566000  11.2966 348.7034 13.40471088    04
NOSS 7 (E)
1 16624U 86014E   05365.73905480 0.00000080  00000-0  55849-4 0    09
2 16624  63.3830 214.1538 0568500  11.2175 348.7825 13.40470702    04
NOSS 7 (H)
1 16631U 86014H   05365.73927053 0.00000070  00000-0  51003-4 0    04
2 16631  63.3890 217.8019 0556000   2.1894 357.8106 13.40471184    09
FleetSatCom 7
1 17181U 86096A   16266.74107602 0.00000000  00000-0  00000-0 0    08
2 17181  14.7111   9.1749 0023795 159.0970 201.0142  1.00270000    02
NOSS 8 (A)
1 17997U 87043A   06009.24674221 0.00000050  00000-0  36703-4 0    09
2 17997  63.3950  96.3688 0548500   2.8452 357.1548 13.41315349    01
NOSS 8 (E)
1 18009U 87043E   06011.25757371 0.00000050  00000-0  39153-4 0    08
2 18009  63.3960 104.7865 0532000   5.9063 354.0938 13.40811205    08
NOSS 8 (F)
1 18010U 87043F   06012.23104210 0.00000030  00000-0  23342-4 0    08
2 18010  63.3950 102.2883 0534000   6.2713 353.7287 13.40809255    05
NOSS 8 (H)
1 18025U 87043H   06002.17263149 0.00000040  00000-0  32346-4 0    08
2 18025  63.3940 128.2963 0522000 359.7676   0.2324 13.40795143    04
DSP F13 USA 28
1 18583U 87097A   08030.76666845 0.00000000  00000-0  00000-0 0    08
2 18583  11.0074  34.8814 0021881 107.0759 253.1760  0.98386091    05
DSP F13 r
1 18584U 87097B   11154.57379289 0.00000000  00000-0  00000-0 0    02
2 18584  12.4519  22.5409 0005636  88.0849 271.9918  1.01240645    09
USA 32
1 19460U 88078A   06010.87279986 0.00000050  00000-0  18408-4 0    07
2 19460  84.9840 123.8525 0004000 235.1365 124.8634 14.32693695    06
Vortex 6 USA 37
1 19976U 89035A   08254.92982997 0.00000000  00000-0  00000-0 0    04
2 19976   5.6687  10.8577 0957500 218.1037 134.7383  1.00270000    01
Vortex 6 r2
1 19983U 89035C   11002.10744857 0.00000000  00000-0  00000-0 0    08
2 19983   6.8705  13.8944 1025712 297.2868  52.6590  0.99428067    09
USA 39 (DSP)
1 20066U 89046A   06008.23830112 0.00000000  00000-0  00000-0 0    08
2 20066   8.9654  47.9789 0012000 312.8426  47.1608  1.00270000    07
DSP F14 r3
1 20069U 89046D   10191.67588769 0.00000000  00000-0  00000-0 0    05
2 20069  11.9707  33.5320 0046338 215.8917 143.8083  1.01304169    09
DSCS 2-15
1 20202U 89069A   10220.38055627 0.00000000  00000-0  00000-0 0    02
2 20202  13.2973  29.8468 0011478  95.6547 264.4849  0.98613270    00
DSCS 3-4
1 20203U 89069B   10122.71740873 0.00000000  00000-0  00000-0 0    05
2 20203   8.6420  60.0767 0006037 253.8998 106.0458  0.99114991    02
DSCS 2-15 r2
1 20205U 89069D   11001.90521396 0.00000000  00000-0  00000-0 0    02
2 20205  13.3566  21.9145 0065448 194.7902 165.0577  1.01242289    06
FleetSatCom 8 USA 46
1 20253U 89077A   08090.65047492 0.00000000  00000-0  00000-0 0    00
2 20253   8.2319  47.4526 0008934 267.8261  92.0783  1.00270000    00
USA 40 r
1 20344U 89061D   05365.75227907 0.00000080  00000-0  74094-4 0    04
2 20344  57.0097 333.9693 3552000  50.5787 309.4213  7.85782853    01
Magnum 2 USA 48
1 20355U 89090B   08224.02190055 0.00000000  00000-0  00000-0 0    02
2 20355  13.2472  57.6713 0261787 276.6026  80.4301  1.00270000    01
Magnum 2 r2
1 20357U 89090D   10154.45931574 0.00000000  00000-0  00000-0 0    05
2 20357  14.8484  49.1417 0320218 295.8635  60.8843  0.99522508    07
USA 58
1 20562U 90031C   14217.03818759 0.00000000  00000-0  00000-0 0    07
2 20562  89.7939 335.9734 0001983 235.6846 124.3153 14.59434657    08
NOSS 2-1 (A)
1 20641U 90050A   07060.70300488 0.00000000  00000-0  00000-0 0    03
2 20641  63.4172  96.2736 4033400 268.3644  91.6356  6.02572519    05
NOSS 2-1 (E)
1 20642U 90050E   06012.26882069 0.00000010  00000-0  10763-4 0    03
2 20642  63.4060 119.1582 0423000 358.1103   1.8897 13.40460764    00
NOSS 2-1 (C)
1 20691U 90050C   06002.19768306 0.00000010  00000-0  10628-4 0    05
2 20691  63.4080 145.4648 0428000   2.3923 357.6077 13.40463970    08
NOSS 2-1 (D)
1 20692U 90050D   06002.19775123 0.00000010  00000-0  10628-4 0    01
2 20692  63.4060 145.1925 0428000   2.4392 357.5608 13.40462948    06
DSP 15 (USA 65
1 20929U 90095A   08059.52443716 0.00000000  00000-0  00000-0 0    02
2 20929  10.7927  46.6862 0007936 247.2447 112.6835  0.98391988    08
DSP F15 r3
1 20932U 90095D   11055.88946838 0.00000000  00000-0  00000-0 0    08
2 20932  12.9195  36.6967 0072353 302.6888  56.6275  0.99915351    00
SDS2 F2 Magnum 3 USA 67
1 20963U 90097B   07232.00023005 0.00000000  00000-0  00000-0 0    02
2 20963  12.3782  43.6309 0129130  94.7845 265.2341  1.00270000    06
Lacrosse 2
1 21147U 91017A   06002.17048373 0.00000160  00000-0  23506-4 0    04
2 21147  67.9940 150.6437 0005000 254.4290 105.5710 14.75374457    05
NOSS 2-2 (A)
1 21775U 91076A   07074.65642862 0.00000000  00000-0  00000-0 0    05
2 21775  63.3589 225.0012 3325559 266.6830  93.3170  5.53394968    08
DMSP B5D2-6
1 21798U 91082A   05365.79588958 0.00000090  00000-0  45971-4 0    07
2 21798  98.6393  16.1728 0013000  20.6178 339.3821 14.15631006    06
NOSS 2-2 (C)
1 21799U 91076C   06002.15198731 0.00000020  00000-0  23751-4 0    01
2 21799  63.4120  33.7995 0381500   1.6448 358.3552 13.40476112    02
DSP F16 USA 75
1 21805U 91080B   08088.72882587 0.00000000  00000-0  00000-0 0    08
2 21805  10.3736  50.6365 0011224 177.2610 182.7582  1.00270000    00
DSP F16 r2
1 21807U 91080D   11002.01305000 0.00000000  00000-0  00000-0 0    02
2 21807  12.3044  39.1416 0019700 201.2681 158.6621  1.01277059    06
NOSS 2-2 (D)
1 21808U 91076D   06002.15211711 0.00000020  00000-0  23697-4 0    05
2 21808  63.4130  34.0652 0382500   1.3918 358.6082 13.40475952    00
NOSS 2-2 (E)
1 21809U 91076E   06002.15200984 0.00000020  00000-0  23938-4 0    04
2 21809  63.4140  33.6286 0378000 356.1064   3.8936 13.40476059    09
DSCS 3-5
1 21873U 92006A   11001.19697838 0.00000000  00000-0  00000-0 0    05
2 21873   9.5882  56.0610 0003064 235.6309 124.3521  0.99032102    08
DSCS 3-5 r2
1 21877U 92006C   11002.20253967 0.00000000  00000-0  00000-0 0    03
2 21877  10.2452  22.1501 0648096 278.9656  73.7723  1.10779583    08
USA 81
1 21949U 92023A   05364.75195687 0.00000040  00000-0  15305-4 0    02
2 21949  85.0070  58.6990 0002000 125.3078 234.6920 14.30742967    01
DSCS 3-6
1 22009U 92037A   11148.79132668 0.00000000  00000-0  00000-0 0    04
2 22009   8.2184  58.4688 0002761 263.7119  96.2686  1.00452281    02
DSCS 3-6 r2
1 22011U 92037C   10163.59337545 0.00000000  00000-0  00000-0 0    02
2 22011  12.5364  31.4773 0025384 280.7688  78.9577  1.01646308    07
USA 89 r
1 22519U 92086C   06002.16731662 0.00001900  00000-0  32267-3 0    00
2 22519  56.9280  45.0522 3218246 309.2593  50.7407  8.76398053    08
Alexis
1 22638U 93026A   06008.04402818 0.00000100  00000-0  36599-4 0    02
2 22638  69.9176  29.4719 0061000 285.0361  74.9639 14.31805374    09
Alexis r
1 22639U 93026B   06009.24935143 0.00000070  00000-0  26102-4 0    03
2 22639  69.9190  48.0928 0064000 302.0895  57.9105 14.30763043    04
DSCS 3-7
1 22719U 93046A   11055.93398839 0.00000000  00000-0  00000-0 0    00
2 22719   6.8249  63.1383 0005558 302.6320  57.3264  0.99006663    01
DSCS 3-7 r2
1 22738U 93046C   10163.69616747 0.00000000  00000-0  00000-0 0    04
2 22738  12.1950  35.6416 0079059 336.3576  23.2839  1.02122163    05
UFO F2 USA 95
1 22787U 93056A   08086.54301158 0.00000000  00000-0  00000-0 0    01
2 22787   5.5241  48.5394 0007510 232.6485 127.2925  1.00270000    09
DSCS III B10 USA 97
1 22915U 93074A   08086.54366224 0.00000000  00000-0  00000-0 0    09
2 22915   3.9939  77.0038 0011292 232.3070 127.6000  1.00270000    07
DSCS 3-8 r
1 22916U 93074B   10186.49616209 0.00000000  00000-0  00000-0 0    09
2 22916  12.6587  38.0691 0008701 275.5345  84.3780  0.99249324    07
Milstar 1 USA 99
1 22988U 94009A   08126.87731780 0.00000000  00000-0  00000-0 0    02
2 22988   5.6904 141.0599 0010295 273.5206  86.3680  1.00270000    07
Milstar 1 r
1 22989U 94009B   10122.91088427 0.00000000  00000-0  00000-0 0    00
2 22989   6.7942 104.0615 0009881  53.7279 306.3753  1.00595740    04
USA 102
1 23031U 94017B   06001.05606452 0.00002450  00000-0  10644-3 0    07
2 23031 105.0348 197.9572 0016000 126.6818 233.3181 15.22131729    05
Trumpet 1
1 23097U 94026A   14301.56449094 0.00000264  00000-0  00000-0 0    07
2 23097  64.0600 221.8444 6447805 273.5901  20.0715  2.00616570    07
UFO F3 USA 104
1 23132U 94035A   08297.50944147 0.00000000  00000-0  00000-0 0    05
2 23132   5.7058  54.4158 0004958 209.2649 150.7194  1.00332118    09
Mercury 1 USA 105
1 23223U 94054A   08098.72636622 0.00000000  00000-0  00000-0 0    06
2 23223   4.5914  70.5938 0046177 192.8760 167.0182  1.00270000    02
DMSP B5D2-7
1 23233U 94057A   06001.23996751 0.00000090  00000-0  46824-4 0    07
2 23233  98.5560 347.5658 0012000 299.9347  60.0652 14.14656230    03
Mercury 1 r
1 23247U 94054B   11005.77075415 0.00000000  00000-0  00000-0 0    06
2 23247   9.6741  38.3676 0122820 209.8320 149.4835  0.99588186    07
DSP F17 USA 107
1 23435U 94084A   08255.32935064 0.00000000  00000-0  00000-0 0    07
2 23435   8.9380  59.9535 0027817  16.4882 343.6267  1.00270000    08
DSP F17 r3
1 23438U 94084D   10214.62345466 0.00000000  00000-0  00000-0 0    02
2 23438  10.4068  51.4622 0004460 329.9707  30.0084  1.01180360    07
UFO F4 USA 108
1 23467U 95003A   09004.33456456 0.00000000  00000-0  00000-0 0    01
2 23467   4.7731  47.6367 0006000 221.7153 138.2785  1.00270000    00
DMSP B5D2-8
1 23533U 95015A   05365.74221147 0.00000080  00000-0  41460-4 0    03
2 23533  98.8056  18.3941 0007000 250.8729 109.1270 14.14886173    03
Mentor 1
1 23567U 95022A   11212.97783719 0.00000000  00000-0  00000-0 0    02
2 23567  10.0373  68.5437 0121312  21.6476 338.8609  1.00273447    03
Mentor 1 r
1 23568U 95022B   10170.81502268 0.00000000  00000-0  00000-0 0    06
2 23568  10.9214  79.3584 0011176 188.1995 171.8066  1.00559637    01
UFO F5 USA 111
1 23589U 95027A   08184.63450042 0.00000000  00000-0  00000-0 0    08
2 23589   4.7805  49.0518 0005954 237.0213 122.9306  1.00270000    04
Helios 1A
1 23605U 95033A   10097.11731295 0.00000000  00000-0 -14523-3 0    04
2 23605  98.1038  33.6397 0002499 104.4270 255.5729 14.63844028    05
Trumpet 2
1 23609U 95034A   14301.66813519 0.00000046  00000-0  00000-0 0    02
2 23609  63.4451 255.3436 6933054 268.9888  17.8027  2.00608837    01
DSCS 3-9
1 23628U 95038A   16329.64722082 0.00000000  00000-0  00000-0 0    01
2 23628  10.0654  40.6121 0003516 111.6319 248.4234  1.00270000    07
DSCS 3-9 r2
1 23648U 95038C   10155.58771574 0.00000000  00000-0  00000-0 0    07
2 23648  11.5522  44.2078 0015192 165.7499 194.3050  1.01266427    06
UFO F6 USA 114
1 23696U 95057A   08217.55569624 0.00000000  00000-0  00000-0 0    05
2 23696   4.0529  48.3448 0005132 245.6947 114.2602  1.00270000    03
Milstar 2 USA 115
1 23712U 95060A   08086.55593646 0.00000000  00000-0  00000-0 0    03
2 23712   7.1392  68.5502 0007556 190.5725 169.4235  0.99034856    01
Milstar 2 r
1 23713U 95060B   10122.81724332 0.00000000  00000-0  00000-0 0    05
2 23713   9.3135  57.1125 0033938  48.2190 312.0826  1.00597069    09
USA 116
1 23728U 95066A   06108.05776286 0.00001000  00000-0  51035-4 0    06
2 23728  97.8800 241.3477 0282154  48.8003 311.1996 14.88264379    01
MSX
1 23851U 96024A   06010.81985590 0.00000060  00000-0  42438-4 0    06
2 23851  99.1184  89.5662 0007000 352.2393   7.7606 13.97829114    04
Mercury 2
1 23855U 96026A   08105.54515348 0.00000000  00000-0  00000-0 0    08
2 23855   7.3324  15.8034 0501103 176.6202 183.7537  1.00270000    03
NOSS 2-3 (D)
1 23862U 96029D   05365.77515009 0.00000030  00000-0  46515-4 0    01
2 23862  63.4170 313.5618 0234000   0.8115 359.1885 13.40476571    02
NOSS 2-3 (A)
1 23893U 96029A   07060.82206468 0.00000000  00000-0  00000-0 0    03
2 23893  63.4733 352.7942 3314138 264.6933  95.3067  5.52843875    08
NOSS 2-3 (C)
1 23908U 96029C   05365.77520912 0.00000030  00000-0  46482-4 0    04
2 23908  63.4190 313.4749 0234500 357.6241   2.3759 13.40477541    02
NOSS 2-3 (E)
1 23936U 96029E   05365.77526370 0.00000030  00000-0  46450-4 0    04
2 23936  63.4210 313.6991 0235000   0.3324 359.6676 13.40477576    01
TiPS
1 23937U 96029F   05365.81682843 0.00001000  00000-0  73955-3 0    05
2 23937  63.4005 236.3733 0323997   4.2196 355.7804 13.73082070    09
SDS 2F4 USA 125
1 23945U 96038A   08057.84877624 0.00001355  00000-0  00000-0 0    02
2 23945  64.0583 290.0161 7425694 255.4767  18.8791  2.00624178    07
USA 125 r
1 23947U 96038C   06002.80292820 0.00000070  00000-0  17014-3 0    06
2 23947  55.3758 221.6783 4893500 174.2271 185.7729  5.48310268    08
UFO 7
1 23967U 96042A   07053.75412736 0.00000000  00000-0  00000-0 0    01
2 23967   2.8276  41.8670 0008000 200.9769 159.0231  1.00270000    02
USA 129
1 24680U 96072A   05364.85222684 0.00011000  00000-0  15375-3 0    08
2 24680  97.9382  65.5364 0514056 244.8119 115.1880 14.74984649    09
DSP F18 USA 130
1 24737U 97008A   09002.49706237 0.00000000  00000-0  00000-0 0    09
2 24737   7.3728  66.6604 0000496 258.3498 101.6521  1.00270000    04
DSP F18 r3
1 24740U 97008D   11002.19332744 0.00000000  00000-0  00000-0 0    01
2 24740   9.1536  57.5687 0025271  30.7570 329.4030  0.99490376    08
DMSP F14
1 24753U 97012A   06003.72450074 0.00000080  00000-0  41276-4 0    03
2 24753  98.5480  19.8760 0009000 139.4492 220.5507 14.15118092    02
Lacrosse 3
1 25017U 97064A   06011.27682724 0.00000140  00000-0  22468-4 0    01
2 25017  57.0100 167.8106 0005000 108.4515 251.5485 14.71324217    00
DSCS 3-10 USA 135
1 25019U 97065A   08271.55834468 0.00000000  00000-0  00000-0 0    08
2 25019   2.4599  77.9836 0006877 344.1851  15.7946  1.00270000    04
Trumpet 3
1 25034U 97068A   14203.73894686 -.00001155  00000-0  00000-0 0    01
2 25034  63.2760 326.0072 6828663 284.1592  13.6226  2.00610838    08
USA 137
1 25148U 98005A   08105.89470532 0.00001391  00000-0  00000-0 0    01
2 25148  64.2508 175.7217 7145485 255.3197  21.8969  2.00594627    03
Geosat FO
1 25157U 98007A   06001.01381868 0.00000050  00000-0  18797-4 0    00
2 25157 108.0561 183.2132 0001965 319.6116  40.3884 14.31515516    00
UFO F8
1 25258U 98016A   16329.45184925 0.00000000  00000-0  00000-0 0    08
2 25258   7.3145  39.0000 0004809 204.6795 155.3088  1.00270000    00
Mentor 5 USA 139
1 25336U 98029A   08094.37073255 0.00000000  00000-0  00000-0 0    03
2 25336   7.5221  10.0919 0052658 214.9992 144.6642  1.00270000    07
Mentor 2 r
1 25337U 98029B   11005.72886267 0.00000000  00000-0  00000-0 0    04
2 25337   9.9060  10.2291 0050559  44.2198 316.2053  1.00269978    05
Mercury 2 r
1 25349U 96026B   11005.59407392 0.00000000  00000-0  00000-0 0    05
2 25349   8.9424   5.3872 0468483 275.3341  79.3626  0.99563671    04
STEX
1 25489U 98055A   06030.73270506 0.00000110  00000-0  30596-4 0    06
2 25489  84.9825  81.8375 0008000 315.1152  44.8847 14.46509155    09
UFO F9 USA 140
1 25501U 98058A   08047.63563391 0.00000000  00000-0  00000-0 0    01
2 25501   2.4697  28.0195 0016339 255.5349 104.2965  0.98179571    07
USA 141 (ATEX)
1 25615U 98055C   06002.84052518 0.00000150  00000-0  44352-4 0    08
2 25615  84.9820 104.9407 0007000  46.9351 313.0648 14.43555225    03
DSP F19 USA 142
1 25669U 99017A   07324.02276106 0.00000000  00000-0  00000-0 0    07
2 25669  29.0657 245.4422 7091527 341.3340  18.6658  2.32920751    06
Milstar 3
1 25724U 99023A   06005.78692418 0.00000080  00000-0  10081-2 0    02
2 25724  28.2355 206.3189 2132000 174.9652 185.0343  9.37434718    08
Milstar 3 Cn r
1 25725U 99023B   06018.02416152 0.00000130  00000-0  29077-3 0    05
2 25725  28.3070 308.1593 2388000  91.5240 268.4755  9.67067529    02
USA 144 Deb
1 25746U 99028C   06002.14793056 0.00000060  00000-0  92484-2 0    03
2 25746  63.4412  85.4913 0242000 294.0968  65.9032  9.69821966    03
UFO F10 USA 146
1 25967U 99063A   08098.31161688 0.00000000  00000-0  00000-0 0    08
2 25967   1.6695  21.0153 0016980 267.7109  92.1015  1.00270000    04
DMSP F15
1 25991U 99067A   06010.71545390 0.00000100  00000-0  50644-4 0    05
2 25991  98.5989  58.3927 0013001 112.0755 247.9244 14.16086491    08
DSCS 3-11 USA 148
1 26052U 00001A   08274.63870388 0.00000000  00000-0  00000-0 0    03
2 26052   0.0382 104.3705 0019368 128.4344 231.7569  1.00270000    06
DSCS 3-11 r2
1 26054U 00001C   10122.76136962 0.00000000  00000-0  00000-0 0    07
2 26054   8.9107  57.9538 0015899 210.1349 149.7857  1.01179694    02
JAWSAT
1 26065U 00004E   15054.09556197 0.00000000  00000-0  00000-0 0    03
2 26065 100.2306 253.2202 0037976 171.2560 188.7439 14.36618221    07
DSP F20 USA 149
1 26356U 00024A   08066.83903380 -.00000166  00000-0  00000-0 0 00009
2 26356 004.0836 070.1118 0001346 296.7291 063.8756 00.99855931000007
DSP F20 r3
1 26359U 00024D   11002.08177633 0.00000000  00000-0  00000-0 0    03
2 26359   6.6356  59.5431 0009443  13.1812 346.8556  0.99699248    09
Lacrosse 4
1 26473U 00047A   05365.73533576 0.00000100  00000-0  18922-4 0    01
2 26473  67.9950 310.5724 0006000 273.8098  86.1902 14.64250326    04
DSCS 3-12 USA 153
1 26575U 00065A   08029.90854415 0.00000000  00000-0  00000-0 0    04
2 26575   0.0400  83.5695 0003000 191.3683 168.6317  1.00270000    03
DSCS 3-12 r2
1 26577U 00065C   10163.77567858 0.00000000  00000-0  00000-0 0    05
2 26577   8.5277  58.6293 0050772 116.0677 244.4680  1.01179455    01
SDS 3F2 USA 155
1 26635U 00080A   08084.63045670 0.00000000  00000-0  00000-0 0    04
2 26635   2.1120  39.4865 0012830 188.2367 171.7550  1.00270000    00
Sicral 1
1 26694U 01005A   13214.20728829 0.00000000  00000-0  00000-0 0    05
2 26694   4.8244  62.5072 0004226 116.2035 243.8645  1.00270000    07
Milstar 4 USA 157
1 26715U 01009A   09004.42726648 0.00000000  00000-0  00000-0 0    06
2 26715   2.8864  50.0981 0001000 205.9101 154.0822  1.00270000    05
Milstar 4 r
1 26716U 01009B   11001.24367419 0.00000000  00000-0  00000-0 0    04
2 26716   6.2596  56.2099 0017452 348.0440  11.9266  1.00468874    08
GeoLite
1 26770U 01020A   11349.95867440 0.00000000  00000-0  00000-0 0    09
2 26770   2.7931  51.9289 0018954 357.4321   2.5909  0.98843605    00
DSP F21 USA 159
1 26880U 01033A   08043.61029153 0.00000000  00000-0  00000-0 0    06
2 26880   3.0088  71.2071 0014726 185.6100 174.3900  1.00270000    08
DSP F21 r3
1 26883U 01033D   11002.06214617 0.00000000  00000-0  00000-0 0    08
2 26883   5.5905  61.5661 0006246 248.1881 111.7576  0.99888268    04
NOSS 3-1 (A)
1 26905U 01040A   05365.82917860 0.00000020  00000-0  36402-4 0    01
2 26905  63.4370 252.6798 0005000  66.7155 293.2845 13.40482888    00
NOSS 3-1 r
1 26906U 01040B   05365.81442981 0.00000010  00000-0  17328-4 0    03
2 26906  63.4746 235.6115 0010500 169.7159 190.2841 13.43638197    02
NOSS 3-1 (C)
1 26907U 01040C   05365.82908481 0.00000020  00000-0  36402-4 0    02
2 26907  63.4290 252.4506 0005000  90.4103 269.5897 13.40483196    01
USA 161
1 26934U 01044A   05364.93732890 0.00000900  00000-0  51180-4 0    03
2 26934  97.9180 109.5229 0343693 129.9356 230.0642 14.74398653    08
SDS 3F3 AQUILA USA 162
1 26948U 01046A   08263.73192277 0.00000000  00000-0  00000-0 0    00
2 26948   2.4912 118.5410 0007986 166.4257 193.6102  1.00270000    02
Milstar 5
1 27168U 02001A   06010.59487748 0.00000000  00000-0  00000-0 0    09
2 27168   1.6801 327.9695 0006833  20.2919 339.7081  1.00270000    07
Milstar 5 Cn r
1 27169U 02001B   07164.98349897 0.00000000  00000-0  00000-0 0    06
2 27169   2.2751 323.3619 0049349  78.2542 287.0261  1.00137794    06
Ofeq 5
1 27434U 02025A   11039.78070777 0.00001700  00000-0  11165-3 0    04
2 27434 143.4626 301.4704 0026074 352.9413   7.0579 15.06461984    05
DSP F18 Cover
1 27680U 97008E   10273.49042398 0.00000000  00000-0  00000-0 0    02
2 27680   8.8526  57.3275 0148455  25.4214 335.3707  0.99519054    08
DSCS 3-13 USA 167
1 27691U 03008A   08042.98221351 0.00000000  00000-0  00000-0 0    04
2 27691   0.0165 194.9748 0000100 227.3477 132.6621  1.00270000    05
DSCS 3-13 r2
1 27693U 03008C   11002.07825266 0.00000000  00000-0  00000-0 0    01
2 27693   7.0061  62.1537 0004810  43.4018 316.6682  1.01116496    01
IGS 1A
1 27698U 03009A   06002.84702713 0.00000000  00000-0  00000-0 0    07
2 27698  97.4061  78.8833 0001000 346.0767  13.9232 15.25957369    04
IGS 1B
1 27699U 03009B   06002.82136744 0.00000000  00000-0  00000-0 0    01
2 27699  97.4011  78.8328 0001500 337.8526  22.1473 15.25959078    03
Milstar 6
1 27711U 03012A   06005.70465450 0.00000000  00000-0  00000-0 0    09
2 27711   1.9200 268.8640 0003000 300.5910  59.4134  1.00270200    05
Milstar 6 Cr
1 27712U 03012B   06059.79819916 0.00000000  00000-0  00000-0 0    08
2 27712   1.5656 328.5041 0038437 140.3392 219.9544  1.00554043    00
Canyon 1 r
1 27785U 68063B   11002.69552116 0.00000000  00000-0  00000-0 0    04
2 27785  14.4213 342.8047 1095502  87.5165 284.9585  1.01773464    02
Canyon 2 r
1 27786U 69036B   10163.00168806 0.00000000  00000-0  00000-0 0    07
2 27786   4.1309 116.8438 0969700  46.5985 321.0825  1.03853244    09
Canyon 3 r
1 27787U 70069B   10170.36389558 0.00000000  00000-0  00000-0 0    02
2 27787  16.6678 285.4757 1264801 311.7085  38.1336  1.01706096    06
DSCS 3-14 USA 170
1 27875U 03040A   07274.36836055 0.00000000  00000-0  00000-0 0    05
2 27875   0.0200  90.0004 0001000 180.0001 179.9999  1.00270000    00
DSCS 3-14 r2
1 27877U 03040C   10224.65989715 0.00000000  00000-0  00000-0 0    00
2 27877   6.2418  64.9054 0017404 154.3367 205.7796  1.00749133    01
Adv Orion 3 USA 171
1 27937U 03041A   08224.27606074 0.00000000  00000-0  00000-0 0    07
2 27937   3.1995 154.8696 0046919 127.2981 233.1479  1.00270000    04
USA 171 r
1 27938U 03041B   06002.16161718 0.00000000  00000-0  00000-0 0    09
2 27938   4.8448 219.9329 0036325 166.7110 193.3965  1.00857694    01
DMSP F16
1 28054U 03048A   06011.79395072 -.00000020  00000-0 -10654-4 0    01
2 28054  98.8208  54.4827 0010000 116.4122 243.5877 14.13401246    06
NOSS 3-2 (A)
1 28095U 03054A   06012.28078454 0.00000030  00000-0  54013-4 0    06
2 28095  63.4350 140.3003 0061000 175.2463 184.7537 13.40484330    08
NOSS 3-2 r
1 28096U 03054B   06004.26667110 0.00000020  00000-0  35653-4 0    07
2 28096  63.6760 176.3028 0082000 131.1629 228.8371 13.40560965    05
NOSS 3-2 (C)
1 28097U 03054C   06012.28086606 0.00000030  00000-0  53974-4 0    01
2 28097  63.4380 140.5002 0063000 175.7481 184.2519 13.40484583    06
UFO F11 USA 174
1 28117U 03057A   08086.20850047 0.00000000  00000-0  00000-0 0    05
2 28117   2.2933 330.1377 0005154 119.9365 240.1326  1.00270000    01
DSP F20 Cover
1 28156U 00024E   10219.54841720 0.00000000  00000-0  00000-0 0    05
2 28156   6.5337  61.3504 0236099 220.3280 137.8983  0.99704389    01
DSP F22 USA 176
1 28158U 04004A   08292.82125469 0.00000000  00000-0  00000-0 0    03
2 28158   1.4073  67.1299 0010770  51.8717 308.2483  1.00270000    07
DSP F22 r3
1 28161U 04004D   10194.17389645 0.00000000  00000-0  00000-0 0    07
2 28161   2.9900  66.4668 0004829 255.6058 104.3420  0.99812515    04
USA 179
1 28384U 04034A   08105.57031399 0.00001405  00000-0  00000-0 0    00
2 28384  63.1359  58.7451 7286209 271.8820  14.0454  2.00613917    03
USA 179 Cn r
1 28385U 04034B   05365.77545288 0.00002300  00000-0  69736-3 0    04
2 28385  57.3912 281.7272 5245781  61.4870 298.5130  5.17267731    09
Helios 2A
1 28492U 04049A   10087.08779818 0.00000000  00000-0  39215-3 0    02
2 28492  98.1112  24.1031 0001504 132.1829 227.8169 14.63842742    02
Essaim 1
1 28494U 04049C   10078.14361211 0.00000090  00000-0  14966-4 0    01
2 28494  98.3005  46.2035 0003783  98.9520 261.0479 14.70180409    01
Essaim 2
1 28495U 04049D   10078.14406910 0.00000010  00000-0  16636-5 0    07
2 28495  98.2815  46.0980 0004617  92.5141 267.4857 14.70158428    09
Essaim 3
1 28496U 04049E   10091.34788348 0.00000020  00000-0  33248-5 0    02
2 28496  98.3032  64.3619 0009789  59.9821 300.0177 14.70164628    09
Essaim 4
1 28497U 04049F   10091.34742217 0.00000020  00000-0  33229-5 0    07
2 28497  98.3046  64.4188 0012914  55.6010 304.3989 14.70165884    07
Delta4 Demo
1 28500U 04050A   07030.25879883 0.00000000  00000-0  00000-0 0    07
2 28500  11.9212 199.6328 2887341 244.8710 115.1442  1.41309200    08
NOSS 3-3 (A)
1 28537U 05004A   06002.15441714 0.00000010  00000-0  17645-4 0    00
2 28537  63.4340  35.7759 0103000 177.7610 182.2391 13.40481310    07
NOSS 3-3 r
1 28538U 05004B   06002.19553970 0.00000010  00000-0  16881-4 0    04
2 28538  63.8281  43.9989 0114000 147.8157 212.1843 13.42859142    07
NOSS 3-3 (C)
1 28541U 05004C   06002.15450342 0.00000020  00000-0  35290-4 0    09
2 28541  63.4340  35.9774 0103000 177.6416 182.3585 13.40481471    08
Delta4 Demo r
1 28546U 04050B   07028.57971064 0.00000000  00000-0  00000-0 0    03
2 28546  12.2910 202.7945 2680736 239.2158 120.7992  1.37842000    08
XSS-11
1 28636U 05011A   06001.24510227 0.00000070  00000-0  38934-4 0    03
2 28636  98.8526 356.0685 0013000 178.6393 181.3606 14.11055223    08
XSS-11 r
1 28637U 05011B   06001.24515133 0.00000060  00000-0  33380-4 0    04
2 28637  98.8516 356.0730 0010997 169.6387 190.3612 14.11054175    06
Lacrosse 5
1 28646U 05016A   05365.76346897 0.00000040  00000-0  95517-5 0    06
2 28646  57.0110 293.2429 0007000 187.6750 172.3250 14.53349022    07
Lacrosse 5 r
1 28647U 05016B   06001.68331250 0.00000600  00000-0  44507-4 0    07
2 28647  56.9980 231.2148 0164000  89.6177 270.3822 14.92462870    03
USA 186
1 28888U 05042A   06012.74211712 0.00010500  00000-0  10732-3 0    04
2 28888  97.8724  77.6223 0550578 269.8685  90.1314 14.72977790    05
MiTEX1 USA 187
1 29240U 06024A   08048.86864532 0.00000000  00000-0  00000-0 0    04
2 29240   1.2647  81.3384 0003038 154.6375 205.3903  1.04000000    08
Unknown 090123
1 29241U 06024B   09043.13578394 0.00000000  00000-0  00000-0 0    09
2 29241   0.0930 268.8956 0001722  79.0749 280.9526  1.00600180    02
MiTEx NRL U/S USA 189
1 29242U 06024C   09034.74688303 0.00000000  00000-0  00000-0 0    09
2 29242   2.0973  77.0138 0001706 153.1240 206.8902  1.04004000    04
USA 184
1 29249U 06027A   06200.42851878 0.00000700  00000-0  15249-0 0    03
2 29249  63.2108  44.0449 7162774 268.3637  91.6363  2.00508383    09
USA 184 r
1 29250U 06027B   08082.02503547 0.00000000  00000-0  00000-0 0    00
2 29250  62.3743 309.7803 7050465 274.7610  14.8472  2.17595297    02
IGS 2A
1 29393U 06037A   06255.94050995 0.00000000  00000-0  00000-0 0    04
2 29393  97.3059  14.6731 0005460 350.5714   9.4284 15.25871519    04
DMSP F17
1 29522U 06050A   06313.22739550 0.00000062  00000-0  33121-4 0    02
2 29522  98.7877 311.9526 0009224 249.9390 110.0609 14.13250636    06
USA 193
1 29651U 06057A   06351.27314032  .00012066  00000-0  10000-3 0    00
2 29651  58.5075 109.9880 0009237 103.8726 256.3387 15.69650945    02
SAR Lupe 1
1 29658U 06060A   11070.12965775 0.00001600  00000-0  59766-4 0    00
2 29658  98.1769 237.9832 0015428 236.5024 123.4974 15.27285723    00
IGS R2
1 30586U 07005A   07108.00162496 0.00001600  00000-0  62349-4 0    06
2 30586  97.3219 228.6634 0004789 117.0927 242.9071 15.25995200    04
IGS OVS
1 30587U 07005B   07106.97556309 0.00000000  00000-0  19730-2 0    08
2 30587  97.2818 227.5525 0001804  89.7710 270.2288 15.26031287    07
IGS R2 r
1 30588U 07005C   07107.99867309 0.00004000  00000-0  78749-4 0    08
2 30588  97.2912 229.6846 0095798 294.2453  65.7546 15.42260292    06
IGS-R2 adapter
1 30589U 07005D   07107.98881854 0.00005000  00000-0  18693-3 0    01
2 30589  97.2372 228.3467 0007973 199.6670 160.3328 15.27351491    04
IGS R1 shroud1
1 30590U 07005E   07107.99315165 0.00007300  00000-0  27229-3 0    01
2 30590  97.2211 228.2657 0008108 233.2259 126.7740 15.27426208    00
IGS R2 shroud2
1 30591U 07005F   07107.99494023 0.00007000  00000-0  26144-3 0    05
2 30591  97.2300 228.3472 0007979 235.7727 124.2272 15.27384068    08
Ofeq 7
1 31601U 07025A   11041.01942323 0.00001650  00000-0  74097-4 0    02
2 31601 141.7491 116.2780 0091897 282.8335  77.1657 15.16476805    06
NOSS 3-4 (A)
1 31701U 07027A   07170.06953822 0.00000000  00000-0  00000-0 0    01
2 31701  63.4491  37.1181 0234547 144.6382 215.4221 13.65677834    02
NOSS 3-4 r
1 31702U 07027B   07211.98602379 0.00000483  00000-0  20711-3 0    06
2 31702  63.3731 274.4572 0163620 189.3552 170.3056 14.17708429    05
NOSS 3-4 (C)
1 31708U 07027C   07193.35731252 0.00000000  00000-0  00000-0 0    06
2 31708  63.4300 335.2216 0234817 150.8127 209.1873 13.65500000    08
SAR Lupe 2
1 31797U 07030A   11039.78731563 0.00001500  00000-0  56307-4 0    05
2 31797  98.1084 273.2461 0009814 290.2418  69.7581 15.27193401    01
WGS 1
1 32258U 07046A   17015.41718039 0.00000000  00000-0  00000-0 0    07
2 32258   0.0448  84.9221 0003453 246.9285 113.0715  1.00270000    03
SAR Lupe 3
1 32283U 07053A   11203.31709745 0.00001300  00000-0  48521-4 0    07
2 32283  98.1293 149.8191 0005557 188.9386 171.0613 15.27414496    02
USA 197
1 32287U 07054A   07317.90389715 0.00000000  00000-0  00000-0 0    01
2 32287   3.9960 273.0734 0003000  60.0268 299.9732  0.99731100    03
USA 197 Cn r
1 32288U 07054B   07315.89571404 0.00000000  00000-0  00000-0 0    06
2 32288   3.9650 272.1000 0001000 154.0000 206.0000  0.99676600    02
USA 198
1 32378U 07060A   07346.89533062 0.00001757  00000-0  17534-3 0    08
2 32378  60.0106 317.1239 5543977 287.1515  72.8485  4.77580618    03
USA 198 Cn r
1 32379U 07060B   07346.84730914 0.00069200  00000-0  28374-2 0    09
2 32379  60.7629 318.0027 5493200 285.4805  74.5049  4.90067973    06
TecSAR
1 32476U 08002A   11049.05080476 0.00003000  00000-0  68921-4 0    03
2 32476  41.0264  26.3829 0077736 116.4231 243.5763 15.38583238    05
USA 200
1 32706U 08010A   08080.11461581 0.00000000  00000-0  00000-0 0    03
2 32706  63.5619  40.8769 7095838 271.6711  15.8320  2.10156510    09
USA 200 r
1 32707U 08010B   14290.43525739 0.00000400  00000-0  11525-2 0    05
2 32707  63.5611  67.2355 7356940 250.7816  21.9391  2.11366141    04
SAR Lupe 4
1 32750U 08014A   11077.19385881 0.00002300  00000-0  86015-4 0    01
2 32750  98.1839 246.5658 0017316  10.7656 349.2342 15.27216362    08
SAR Lupe 5
1 33244U 08036A   11098.02690432 0.00001200  00000-0  44740-4 0    07
2 33244  98.1680  35.7157 0016319 346.4017  13.5981 15.27334359    02
USA 202
1 33490U 09001A   09046.30328249 0.00000000  00000-0  00000-0 0    02
2 33490   2.8915 337.5826 0024996 190.8227 169.2084  1.00130520    01
USA 202 r
1 33491U 09001B   09023.53756835 0.00000000  00000-0  00000-0 0    09
2 33491   2.9844 334.0731 0246632  12.9987 347.6968  0.96057197    06
WGS F2 USA 204
1 34713U 09017A   09141.35810465 0.00000000  00000-0  00000-0 0    05
2 34713   0.0915 245.2475 0004000  23.0065 336.9754  1.00317756    01
Sicral 1B
1 34810U 09020A   13141.79392576 0.00000000  00000-0  00000-0 0    08
2 34810   0.1028  82.0406 0005392  27.2992  68.0656  1.00270000    00
STSS-ATRR
1 34903U 09023A   09127.88488268 0.00000000  00000-0  00000-0 0    07
2 34903  98.9513 226.1446 0007714 220.9054 139.0944 14.06067719    03
STSS-ATRR r
1 34904U 09023B   09130.12101793 0.00480000  00000-0  68103-2 0    06
2 34904 112.7678 228.4968 0309489 290.6359  68.9977 15.16282514    01
PAN USA 207
1 35815U 09047A   09263.63810579 0.00000000  00000-0  00000-0 0    04
2 35815   0.0533 274.1181 0003730  63.1363 286.5617  1.00270000    09
PAN r
1 35816U 09047B   18282.71996110 0.00000000  00000-0  00000-0 0    01
2 35816  22.9471 142.3146 5167264  91.1611 325.7804  1.94974253    04
STSS Demo 1
1 35937U 09052A   09271.78649380 0.00000000  00000-0  00000-0 0    00
2 35937  57.9904  82.1205 0013359 323.1724  36.8701 12.79625382    04
STSS Demo 2
1 35938U 09052B   09270.77181345 0.00000000  00000-0  00000-0 0    01
2 35938  57.9922  84.8776 0007193 297.9025  62.0975 12.79020022    02
STSS Demo r
1 35939U 09052C   09337.06590627 0.00243000  00000-0  24874-3 0    02
2 35939  59.6643 210.1386 0654620 289.3240  70.6760 14.79164575    01
DMSP F18
1 35951U 09057A   09292.07608029 0.00000000  00000-0  00000-0 0    01
2 35951  98.9336 326.0730 0010024 295.5843  64.4156 14.12545987    09
IGS 5A
1 36104U 09066A   10079.86836021 0.00000000  00000-0  00000-0 0    09
2 36104  97.8129 153.1807 0001000   4.2748 355.7250 14.93388774    04
IGS 5A r
1 36105U 09066B   10072.86172539 0.00000803  00000-0  65607-4 0    09
2 36105  97.6507 144.6866 0043019  43.1528 317.3053 14.98708889    00
WGS F3
1 36108U 09068A   11005.02353592 0.00000000  00000-0  00000-0 0    00
2 36108   0.0026 100.5215 0004229  21.4235 338.6194  1.00270000    00
WGS 3 r
1 36109U 09068B   14053.01007272 0.00000000  00000-0  00000-0 0    07
2 36109  24.6755   3.9597 8162708 292.0115 296.9198  1.18380000    00
Helios 2B
1 36124U 09073A   10239.07282622 0.00000000  00000-0  00000-0 0    02
2 36124  98.1220 173.9535 0003000  68.3825 291.7697 14.63824605    08
Helios 2B r
1 36125U 09073B   10237.02021578 0.00000102  00000-0  15029-4 0    01
2 36125  98.0401 175.1666 0040933   2.2543 357.8842 14.74859328    06
OTV-1
1 36514U 10015A   10143.39927771 0.00001500  00000-0  23465-4 0    03
2 36514  39.9923 169.4404 0015696 208.7785 151.2208 15.52671083    05
Ofeq 9
1 36608U 10031A   11062.70774936 0.00002800  00000-0  95322-4 0    09
2 36608 141.7685   4.6085 0165306 274.0977  85.9015 15.17341025    04
AEHF 1
1 36868U 10039A   11001.20444344 0.00000000  00000-0  00000-0 0    05
2 36868  10.5699 284.5336 5611939 219.6849 343.0000  1.23768400    08
AEHF 1 r
1 36869U 10039B   11002.48493822 0.00000200  00000-0  17139-3 0    08
2 36869  21.0322 277.4191 7885107 240.4423  21.6745  1.55587975    07
FIA Radar 1
1 37162U 10046A   10365.68598779 0.00000000  00000-0  00000-0 0    07
2 37162 122.9944  52.8158 0005000 102.1579 257.8421 13.41452514    00
SBSS 1
1 37168U 10048A   11005.27810923 0.00000150  00000-0  20380-4 0    03
2 37168  98.0154 231.9758 0002500  27.7937 332.2061 14.78900661    00
SBSS 1 r
1 37169U 10048B   10273.80860640 0.00000000  00000-0  00000-0 0    07
2 37169  98.0000 135.5082 0008000  44.9343 315.0656 15.10164263    09
STPSat 2
1 37222U 10062A   12232.94555056 0.00000320  00000-0  45657-4 0    03
2 37222  71.9651 172.3631 0018000 196.5016 163.4984 14.76589784    01
RAX
1 37223U 10062B   11047.27696737 0.00000210  00000-0  00000-0 0    02
2 37223  71.9744 305.5778 0020243 156.1195 204.0952 14.77236729    05
O/OREOS
1 37224U 10062C   11043.43618410 0.00000219  00000-0  00000-0 0    08
2 37224  71.9758 314.1598 0019424 162.0076 198.1778 14.76892599    01
FASTSAT
1 37225U 10062D   11014.05373812 0.00000060  00000-0  85753-5 0    06
2 37225  71.9620  19.0237 0019965 207.0682 152.9317 14.76490180    01
FAST 1
1 37227U 10062F   11057.21878648 0.00000076  00000-0  00000-0 0    04
2 37227  71.9724 283.9188 0016148 131.5768 228.6802 14.76395401    01
STPSAT 2 r
1 37228U 10062G   11022.74152336 0.00000000  00000-0  00000-0 0    01
2 37228  71.9734 359.9669 0010000 194.6902 165.3098 14.76000000    04
HAPS r
1 37229U 10062H   11062.78081731 0.00000150  00000-0  21631-4 0    03
2 37229  71.9874 271.7369 0017000 117.2072 242.7927 14.76146611    04
Mentor 5
1 37232U 10063A   11213.60548493 0.00000000  00000-0  00000-0 0    07
2 37232   6.4453 263.4062 0035159 336.2384  23.5997  1.00277406    08
Mentor 5 r
1 37233U 10063B   11001.68520661 0.00000000  00000-0  00000-0 0    08
2 37233   6.9953 266.8852 0220851 140.0576 221.6006  1.04031629    03
USA 224
1 37348U 11002A   11023.83162841 0.00008800  00000-0  50440-4 0    05
2 37348  97.9000 139.0368 0563457 277.2512  82.7487 14.79617543    01
NanoSail-D
1 37361U 10062L   11053.18324610 0.00045000  00000-0  60443-2 0    05
2 37361  71.9732 292.6219 0023333  99.1733 261.2301 14.79073791    01
OTV 2
1 37375U 11010A   11073.71563114 0.00007980  00000-0  39958-4 0    03
2 37375  42.8585 237.5217 0018908 356.6571   3.2257 15.80528259    09
USA 227
1 37377U 11011A   11098.49400289 0.00000000  00000-0  00000-0 0    09
2 37377   4.9151 343.8190 0001043  15.4298 344.5885  1.00270000    01
FAST 2
1 37380U 10062M   11155.19780612 0.00000130  00000-0  18663-4 0    02
2 37380  71.9889  68.1025 0017205 296.9102  63.0897 14.76335623    04
NOSS 3-5 (A)
1 37386U 11014A   11107.10689160 0.00000000  00000-0  00000-0 0    08
2 37386  63.4238 346.0103 0128090 179.8530 180.1470 13.34368235    04
NOSS 3-5 (B)
1 37387U 11014B   11109.03548857 0.00000000  00000-0  00000-0 0    00
2 37387  63.4167 342.7331 0128413 180.9847 179.0943 13.39251023    08
NOSS 3-5 (B)
1 37391U 11014B   11110.75281113 0.00000000  00000-0  00000-0 0    05
2 37391  63.4047 338.3792 0127413 180.4827 179.5173 13.39341423    08
SBIRS GEO 1
1 37481U 11019A   11154.45872124 0.00000000  00000-0  00000-0 0    03
2 37481   6.4830 319.9777 0001300 143.8525 216.1475  1.00270000    07
ORS 1
1 37728U 11029A   11183.10603239 0.00006852  00000-0  10000-3 0    06
2 37728  40.0000 125.8626 0009897 284.9325  75.0391 15.54660733    04
RadioAstron
1 37755U 11037A   11343.96971181 0.00000000  00000-0  00000-0 0    06
2 37755  74.9673 308.4764 8612669 316.2510   3.7923  0.11953359    03
IGS 6A
1 37813U 11050A   11272.94111109 0.00000619  00000-0  60047-4 0    08
2 37813  97.6931  31.0490 0002497 291.0367  69.0585 14.92733754    04
IGS 6A r
1 37814U 11050B   11272.85741330 0.00000455  00000-0  39984-4 0    08
2 37814  97.6540  31.0070 0019112   2.8113 357.3213 14.96485088    03
IGS 7A
1 37954U 11075A   12198.09926076 0.00000000  00000-0  00000-0 0    05
2 37954  97.5197 269.8670 0010529 310.4530  49.5784 15.17603387    07
IGS 7A r
1 37955U 11075B   12082.87443186 0.00005600  00000-0  21802-3 0    07
2 37955  97.4180 155.2591 0027670  42.0496 317.9502 15.25664235    01
Elisa W11
1 38007U 11076A   12199.27377032 0.00000200  00000-0  38982-4 0    05
2 38007  98.1589 272.9104 0010685 143.9017 216.2908 14.63069705    09
Elisa E24
1 38008U 11076B   12196.19622887 0.00000257  00000-0  50093-4 0    04
2 38008  98.1589 272.4606 0010692 121.7407 238.4838 14.63068126    01
Elisa W23
1 38009U 11076C   12199.27393649 0.00000200  00000-0  39016-4 0    08
2 38009  98.1819 272.9488 0001486 102.4077 257.7291 14.63066078    02
Elisa E12
1 38010U 11076D   12196.19638590 0.00000256  00000-0  49937-4 0    09
2 38010  98.1819 272.4855 0001493 112.0474 248.0886 14.63069469    03
WGS 4
1 38070U 12003A   12063.65981561  .00000000  00000-0  00000-0 0    00
2 38070   0.0541 274.4832 0549995 184.8475 175.1525  1.00180033    00
WGS 4 r
1 38071U 12003B   15053.99435768 0.00000008  00000-0  19809-3 0    01
2 38071  22.0934 101.0464 8200411 170.2769 234.7800  1.15520163    03
MUOS 1
1 38093U 12009A   15278.37810261 0.00000000  00000-0  00000-0 0    09
2 38093   3.8500 332.8334 0059750 180.1670 179.8329  1.00270000    05
Muos r
1 38094U 12009B   12319.41029435 0.00000000  00000-0  00000-0 0    03
2 38094  18.0821 266.9340 6213463 273.3248  22.1483  2.11710260    00
FIA Radar 2
1 38109U 12014A   12097.24217641 0.00000000  00000-0  00000-0 0    08
2 38109 122.9914 224.3990 0009283 284.9437  75.1044 13.45794928    02
AEHF 2
1 38254U 12019A   13058.76513473 0.00000000  00000-0  00000-0 0    01
2 38254   3.1694 313.1993 0006856 338.0255  21.9467  1.00270000    06
USA 236
1 38466U 12033A   12201.02221518 0.00000000  00000-0  00000-0 0    06
2 38466   4.9082 274.5087 0005000 175.6170 184.6492  1.00273922    07
USA 237
1 38528U 12034A   12197.78746808 0.00000000  00000-0  00000-0 0    07
2 38528   3.5184 299.5137 0050303 310.7722  48.7936  0.99909995    04
USA 237 r
1 38529U 12034B   12201.16401249 0.00000000  00000-0  00000-0 0    03
2 38529   3.5829 299.0775 0197347 196.4398 163.3022  1.03226679    09
NOSS 3-6 (A)
1 38758U 12048A   12260.11019213 0.00000000  00000-0  00000-0 0    08
2 38758  63.4386  36.1321 0127783 180.8284 179.1715 13.40501612    02
NOSS 3-6 r
1 38770U 12048N   12260.17511925 0.00068242  00000-0  54452-2 0    09
2 38770  64.6150  33.5493 0214551 293.7818  66.2662 14.83675255    06
NOSS 3-6 (P)
1 38771U 12048P   12260.11029461 0.00000000  00000-0  00000-0 0    09
2 38771  63.4386  36.1322 0127783 180.4284 179.5715 13.40441112    06
NOSS 3-6 (P)
1 38773U 12048P   12263.16874014 0.00000000  00000-0  00000-0 0    01
2 38773  63.4386  28.3553 0127283 180.8086 179.1914 13.40519112    09
Pleiades 1B
1 39019U 12068A   13089.90057915 0.00000000  00000-0  00000-0 0    09
2 39019  98.2085 166.2336 0001000   0.0000  57.5005 14.58553606    09
OTV 3
1 39025U 12071A   12348.51262355 0.00015000  00000-0  10571-3 0    03
2 39025  43.4959 127.0411 0012422 332.5991  27.4004 15.73041223    09
IGS 8A
1 39061U 13002A   13121.97756745 0.00000000  00000-0  00000-0 0    06
2 39061  97.4279 242.7329 0003000 129.2047 230.7951 15.17643370    00
IGS 8B
1 39062U 13002B   13122.01510889 0.00049000  00000-0  20498-2 0    08
2 39062  97.4912 243.9044 0001752 178.8640 181.1358 15.23623977    01
IGS 8 r
1 39063U 13002C   13120.00020091 0.00002800  00000-0  22745-3 0    02
2 39063  97.6606 239.5592 0016692 194.3256 165.6742 14.99562829    02
IGS 8 Db D
1 39064U 13002D   13124.04353781 0.00028336  00000-0  12595-2 0    09
2 39064  97.6067 245.9456 0025211 326.1169  33.2972 15.21264961    06
IGS 8 Db E
1 39065U 13002E   13122.03288079 0.00041000  00000-0  17432-2 0    02
2 39065  97.4942 243.7765 0002996 272.3416  87.6582 15.23070998    05
IGS 8 Db F
1 39066U 13002F   13122.01706688 0.00020500  00000-0  63916-3 0    03
2 39066  97.5213 244.8534 0048335 174.3422 185.6576 15.32084308    01
SBIRS GEO 2
1 39120U 13011A   14055.40411744 0.00000000  00000-0  00000-0 0    04
2 39120   5.2166 320.3571 0003941 228.4966 131.4792  1.00270000    09
SBIRS GEO 2 r
1 39121U 13011B   13206.14342780 0.00002225  00000-0  10769-2 0    02
2 39121  21.9142 267.5106 7256990 274.7545   7.9326  2.29613940    09
WGS 5
1 39168U 13024A   13317.25465817 0.00000000  00000-0  00000-0 0    03
2 39168   0.0350  91.4850 0002000 180.0000 180.0000  1.00270000    04
WGS 5 r
1 39169U 13024B   14005.12611120 0.00000000  00000-0  00000-0 0    05
2 39169  25.4033  39.8556 8235545 234.2618  26.0965  1.08104166    06
MUOS 2
1 39206U 13036A   14019.85792968 0.00000000  00000-0  00000-0 0    05
2 39206   4.9431 328.0286 0057037 359.3804   0.6127  1.00270000    02
MUOS 2 r
1 39207U 13036B   13282.13634292 0.00000000  00000-0  00000-0 0    03
2 39207  18.6538 310.2079 6155019 204.8400 104.9075  2.09952624    06
WGS 6
1 39222U 13041A   14320.90546396 0.00000000  00000-0  00000-0 0    02
2 39222   0.0150 270.3700 0001000 210.8973 125.3893  1.00270000    07
WGS 6 r
1 39223U 13041B   14052.84022525 0.00000000  00000-0  00000-0 0    01
2 39223  23.8998 115.7659 8281093 230.7244  23.7049  1.09740000    03
USA 245
1 39232U 13043A   13241.13429432 0.00025000  00000-0  21639-3 0    03
2 39232  97.8732 304.6187 0528234 192.3915 167.7736 14.80683858    08
AEHF 3
1 39256U 13050A   13362.30780316 0.00000000  00000-0  00000-0 0    00
2 39256   4.8845 304.1814 0345112 179.9578 336.7311  0.99205949    00
FIA Radar 3
1 39462U 13072A   13344.12994719 0.00000000  00000-0  00000-0 0    07
2 39462 123.0082 236.8229 0012759 307.2947  52.7053 13.47778591    04
FIA Radar 3 r
1 39475U 13072P   13345.20809444 0.00000000  00000-0  00000-0 0    01
2 39475 120.4582 244.1978 0286404 342.8858  17.1141 14.61081031    09
DMSP F19
1 39630U 14015A   14095.71497852 0.00000000  00000-0  00000-0 0    07
2 39630  98.8700 111.1816 0009822 285.0801  74.9198 14.13792356    08
Ofeq 10
1 39650U 14019A   14106.07914909 0.00070000  00000-0  19916-2 0    07
2 39650 140.9470 242.8354 0162954 123.9544 237.6834 15.22939887    00
USA 250
1 39652U 14020A   17015.02195921 0.00000000  00000-0  00000-0 0    08
2 39652   2.8469 319.5183 0003455 332.8264  27.1575  1.00270006    04
USA 250 r
1 39653U 14020B   15290.00159653 0.00000000  00000-0  00000-0 0    02
2 39653  10.9881 261.7799 4853383 283.0181  28.8166  1.86026107    05
GPS 70 r
1 39742U 14026B   14262.60191257 0.00000000  00000-0  00000-0 0    07
2 39742  54.9489 140.2888 0043262 346.5976  13.4024  1.95489795    05
USA 252
1 39751U 14027A   14144.03015972 0.00000000  00000-0  00000-0 0    03
2 39751  20.6956 263.7634 7074111 178.0121  96.0401  2.24037956    05
GSSAP 1
1 40099U 14043A   15075.15735905 0.00000000  00000-0  00000-0 0    00
2 40099   0.1049 100.4273 0004545 328.1692  31.8192  1.00139487    01
GSSAP 2
1 40100U 14043B   15253.07958315 0.00000000  00000-0  00000-0 0    04
2 40100   0.0581   5.0168 0002000 174.4752 185.4978  1.00270000    05
ANGELS
1 40101U 14043C   15047.61959938 0.00000000  00000-0  00000-0 0    08
2 40101   0.2861   6.6268 0010708 280.8296  79.0674  0.98918407    03
GSSAP r
1 40102U 14043D   14213.29410491 0.00000000  00000-0  00000-0 0    03
2 40102   0.4803 306.6432 0009502   3.3829 356.6355  0.98907512    03
CLIO ISON 143663
1 40208U 14055A   15133.18330974 0.00000000  00000-0  00000-0 0    00
2 40208   0.0440  44.7375 0011405 315.6929  44.2191  1.00270000    01
CLIO r
1 40209U 14055B   15044.70114305 0.00000000  00000-0  00000-0 0    08
2 40209  20.6201 168.7594 4753934 201.2359 129.5757  1.84619428    04
USA 259
1 40344U 14081A   14350.26041667 0.00000000  00000-0  00000-0 0    07
2 40344  62.8515 212.5009 6775547 266.7169 108.1768  2.03519385    08
MUOS 3
1 40374U 15002A   15250.99325315 0.00000000  00000-0  00000-0 0    09
2 40374   4.8951 328.7601 0058632 178.7298 181.2702  1.00270000    01
MUOS 3 r
1 40375U 15002B   15253.71322792 0.00000000  00000-0  00000-0 0    09
2 40375  18.5498 286.0940 6083604 254.8778  33.8705  2.08929700    06
IGS 9
1 40381U 15004A   15116.92747674 0.00000000  00000-0  00000-0 0    09
2 40381  97.4995 188.9595 0006379  74.2520 285.7480 15.27764783    05
IGS 9 r
1 40382U 15004B   15111.89449586 0.00015000  00000-0  56321-3 0    08
2 40382  97.4877 184.9834 0012862 106.5662 253.4337 15.27156191    08
IGS Opt 5
1 40538U 15015A   15095.89867762 0.00000000  00000-0  00000-0 0    08
2 40538  97.5000 168.3467 0003000 146.0759 213.9239 15.17587539    03
IGS Opt 5 r
1 40539U 15015B   15091.90843653 0.00012500  00000-0  42829-3 0    06
2 40539  97.2694 164.0290 0054534 346.4875  12.9436 15.28766798    04
Sicral 2
1 40614U 15022B   15182.22211214 0.00000000  00000-0  00000-0 0    00
2 40614   0.0470  35.8635 0001000 157.7440 202.2560  1.00270000    04
OTV 4
1 40651U 15025A   15153.41113187 0.00000000  00000-0  00000-0 0    03
2 40651  38.0218 255.0262 0009791   9.5017 350.5955 15.85156401    08
LightSail-A
1 40661U 15025L   15159.06218063 0.02648498  00000-0  67226-1 0    05
2 40661  55.0136 260.3261 0243391 227.2228 135.1229 15.14087982    04
WGS 7
1 40746U 15036A   16212.98877681 0.00000000  00000-0  00000-0 0    05
2 40746   0.0220  79.1171 0004580 133.4127 226.5873  1.00270000    04
MUOS 4
1 40887U 15044A   15259.40453690 0.00000000  00000-0  00000-0 0    07
2 40887   5.0430 328.7371 0001000 140.0000 220.0000  1.00270000    02
MUOS 4 r
1 40888U 15044B   15251.42355530 0.00000000  00000-0  00000-0 0    06
2 40888  19.0850 326.7373 6080000 179.7900 180.2000  2.08796000    04
NOSS 3-7 (A)
1 40964U 15058A   15282.84746112 0.00000000  00000-0  00000-0 0    06
2 40964  63.4349 289.4988 0126612 179.0834 180.9166 13.40379204    06
NOSS 3-7 r
1 40978U 15058Q   15282.12325980 0.00000000  00000-0  00000-0 0    08
2 40978  64.7704 289.8805 0219834 284.4137  73.2663 14.78941654    00
NOSS 3-7 (R)
1 40979U 15058R   15282.84751800 0.00000000  00000-0  00000-0 0    02
2 40979  63.4350 289.4959 0126213 179.4631 180.5064 13.40312760    05
NOSS 3-7 (R)
1 40981U 15058R   15286.05573889 0.00000000  00000-0  00000-0 0    01
2 40981  63.4353 281.3310 0124989 179.3855 180.6145 13.40311788    08
FIA Radar 4
1 41334U 16010A   16042.12521527 0.00000000  00000-0  00000-0 0    04
2 41334 122.9820 357.1748 0001000   0.6468 359.3531 13.46533695    05
Mentor 7
1 41584U 16036A   16167.96105997  .00000000  00000-0  00000-0 0    08
2 41584   7.5055 353.7008 0046333  41.2140 319.1375  1.00195548    05
Mentor 7 r
1 41585U 16036B   16206.24457998 0.00000000  00000-0  00000-0 0    05
2 41585   7.6093 354.1663 0215708 185.2147 174.5696  1.04075044    02
MUOS 5
1 41622U 16041A   16191.51826304 0.00000000  00000-0  00000-0 0    07
2 41622   9.8109 324.2407 3211951 178.9804 181.9317  1.52735617    02
MUOS 5 r
1 41623U 16041B   16177.33159821 0.00000000  00000-0  00000-0 0    05
2 41623  19.1010 322.8427 6092785 178.1097 181.9138  2.09515519    06
USA 269
1 41724U 16047A   16211.22686712 0.00000000  00000-0  00000-0 0    04
2 41724  18.6851 325.1617 6992826 178.8357 185.2363  2.21876674    06
GSSAP 3
1 41744U 16052A   16239.71177259 0.00000000  00000-0  00000-0 0    07
2 41744   0.0040 120.2942 0008000 355.4515   4.5217  1.00274330    01
GSSAP 4
1 41745U 16052B   16239.71428764 0.00000000  00000-0  00000-0 0    08
2 41745   0.0190 120.2942 0010000 300.4515  59.5217  1.00104330    03
GSSAP 3 r
1 41746U 16052C   16233.50208616 0.00000000  00000-0  00000-0 0    02
2 41746   0.8621  50.2917 0005920 265.4971  95.1165  0.98987562    06
Ofeq 11
1 41759U 16056A   16262.10113449 0.00138035  00000-0  24500-2 0    00
2 41759 142.5282 325.3519 0184795  50.1757 311.5128 15.32477128    00
WGS 8
1 41879U 16075A   16358.21353247 0.00000000  00000-0  00000-0 0    01
2 41879   3.6003  66.5855 0199996 312.3102   7.7135  1.00270000    06
SBIRS GEO 3
1 41937U 17004A   17052.51326561 0.00000000  00000-0  00000-0 0    03
2 41937   0.0150  69.4353 0001880 223.4955 136.5045  1.00270000    03
SBIRS GEO 3 r
1 41938U 17004B   17226.86044573 0.00013236  00000-0  82035-3 0    01
2 41938  22.5837 222.2595 6958881 345.2570   1.9162  2.72948754    09
DSN 2
1 41940U 17005A   17107.36097467 0.00000000  00000-0  00000-0 0    02
2 41940   0.0150  68.6994 0005459 225.0038 134.9962  1.00270000    05
DSN 2 r
1 41941U 17005B   18213.56543130 0.00000100  00000-0  15139-3 0    00
2 41941  21.3100  61.4050 7218605 205.1470  87.0456  2.30389691    03
NOSS 3-8 (A)
1 42058U 17011A   17161.02542692 0.00000000  00000-0  00000-0 0    08
2 42058  63.4408 255.6854 0118000 179.5102 180.4898 13.40819991    09
NOSS 3-8 (B)
1 42065U 17011B   17161.02534667 0.00000000  00000-0  00000-0 0    09
2 42065  63.4428 255.5230 0119000 180.6735 179.3265 13.40812568    00
IGS Radar 5
1 42071U 17015A   17087.84954211 0.00000000  00000-0  00000-0 0    08
2 42071  97.3495 160.2996 0004000 334.5310  25.4688 15.24496229    06
IGS Radar 5
1 42072U 17015A   17094.87269383 0.00000000  00000-0  00000-0 0    09
2 42072  97.2241 166.8028 0009000 343.9402  16.0596 15.24523891    04
IGS Radar 5 r
1 42073U 17015B   17261.88630936 0.00002200  00000-0  87991-4 0    05
2 42073  97.1831 326.9887 0009000  83.0370 276.9629 15.25098569    01
WGS 9
1 42075U 17016A   17106.28782418 0.00000000  00000-0  00000-0 0    01
2 42075   0.1945 260.0954 2063413 295.8864 351.4187  1.00270000    05
USA 276
1 42689U 17022A   17144.32054585 0.00000000  00000-0  00000-0 0    03
2 42689  50.0027 163.4501 0016976  69.7427 279.9823 15.56120259    05
OPTSAT 3000
1 42900U 17044A   17218.89724819 0.00000000  00000-0  00000-0 0    01
2 42900  97.2000 293.1140 0002000 329.8206  30.1792 15.38252000    05
ORS 5
1 42921U 17050A   18110.27452846 0.00000000  00000-0  00000-0 0    03
2 42921   0.0238 169.0721 0001130 355.4093   4.5880 14.90503959    03
OTV 5
1 42932U 17052A   18103.08332516 0.00000000  00000-0  00000-0 0    09
2 42932  54.4848 135.8907 0003000 305.5090  54.4909 15.71190888    02
USA 278
1 42941U 17056A   17273.78255542 -.00000501  00000-0  00000-0 0    07
2 42941  63.7330 167.0642 6776181 269.6298  90.1889  2.03452428    03
USA 279
1 42949U 17066A   17292.89738262 0.00000000  00000-0  00000-0 0    07
2 42949   8.1392 324.6522 2991000 180.5487 179.0910  1.48414800    08
USA 281
1 43145U 18005A   18016.73232019 0.00000000  00000-0  00000-0 0    07
2 43145 105.9827 142.3843 0008357 272.9216  87.0812 13.55444999    07
SBIRS GEO 4
1 43162U 18009A   18095.79099802 0.00000000  00000-0  00000-0 0    04
2 43162   6.3252 319.8752 0006791 124.1827 235.8990  1.00270000    05
GovSat 1
1 43178U 18013A   18046.24058247 0.00000000  00000-0  00000-0 0    00
2 43178   0.0460 254.8293 0002003  88.6147 271.3689  1.00089661    04
IGS Opt 6
1 43223U 18021A   18168.30056652 0.00000000  00000-0  00000-0 0    00
2 43223  97.4607 288.1271 0001238 165.0178 184.2919 15.27661121    06
IGS Opt 6 r
1 43224U 18021B   18148.12499854 0.00002000  00000-0  84250-4 0    09
2 43224  97.2158 265.9641 0003245  71.2932 288.5103 15.23386603    04
CBAS 1
1 43339U 18036A   18117.06594243 0.00000000  00000-0  00000-0 0    04
2 43339   0.0547  66.4252 0005088 125.6918 234.3082  1.02201461    07
EAGLE
1 43340U 18036B   18117.06441580 0.00000000  00000-0  00000-0 0    01
2 43340   0.0596  64.2796 0003439 116.7817 243.2183  1.02131320    06
CBAS 1 r
1 43341U 18036C   18115.04896991 0.00000000  00000-0  00000-0 0    08
2 43341   0.0551  79.6538 0417135 135.0141  46.6646  1.08312763    05
CBAS 1 r Db
1 43342U 18036D   18133.73566022 0.00000000  00000-0  00000-0 0    04
2 43342   0.0566  93.6184 0016521  99.4573 260.7382  1.02326553    03
USA 287
1 43465U 18036G   18139.83833779 0.00000000  00000-0  00000-0 0    03
2 43465   0.0749  83.9927 0003505 288.3053  71.7431  1.00928636    02
IGS Radar 6
1 43495U 18052A   18163.22499904 0.00000000  00000-0  00000-0 0    02
2 43495  97.2624 279.4803 0014129  53.7498 304.7202 15.25130130    02
IGS Radar 6 r
1 43496U 18052B   18167.95995151 0.00000000  00000-0  00000-0 0    02
2 43496  97.3785 284.1465 0011502 266.9348  93.0651 15.21683580    07
AEHF 4
1 43651U 18079A   18300.25858909 0.00000000  00000-0  00000-0 0    05
2 43651   7.6748 299.5509 1927334 182.3182 177.6818  1.32745226    06
AEHF 4 r
1 43652U 18079B   18292.01091487 0.00000000  00000-0  00000-0 0    00
2 43652  12.4468 299.9219 4706018 177.9937 135.5054  1.83429526    00
ESHAIL 2
1 43700U 18090A   18330.87536882 0.00000000  00000-0  00000-0 0    07
2 43700   0.0750 318.0416 0005000 318.9982 127.3114  1.00270000    05
CSO 1
1 43866U 18106A   19104.02036166 0.00000000  00000-0  00000-0 0    05
2 43866  98.6110  44.4325 0001684 162.5259 197.5005 14.26738299    03
USA 290
1 43941U 19004A   19034.25038896 0.00000000  00000-0  00000-0 0    06
2 43941  73.6099  86.4526 0018729  44.6193 315.3807 15.53160071    08
SAR Lupe 3or5
1 70002U 08036A   12090.39115859 0.00004000  00000-0  14855-3 0    02
2 70002  98.1320  66.2797 0014999 187.0872 172.9126 15.27484427    08
USA NEW
1 70003U          18014.81341543 0.00000000  00000-0  00000-0 0    06
2 70003 105.9998 139.2840 0006265 275.9232  84.0647 13.55404211    04
ISON 37600
1 70036U          14314.68605640 0.00000000  00000-0  00000-0 0    07
2 70036   4.5600 111.6760 5662209  63.5018 295.3748  3.99208818    04
ISON 59501
1 70184U          14317.09270388 0.00000000  00000-0  00000-0 0    06
2 70184  10.7796 334.9840 6996980 142.3878 218.4241  2.41793291    03
ISON 64800
1 70283U          14320.49456760 0.00000000  00000-0  00000-0 0    04
2 70283  63.9317 197.8354 6523714 261.0625  25.2811  2.21894000    03
ISON 144402
1 71171U          14313.95572657 0.00000000  00000-0  00000-0 0    08
2 71171   9.6970  44.0880 0220655 176.3869 183.8703  0.99723473    08
NOSS 3-4 (C)
1 71703U 07027C   07170.06971504 0.00000000  00000-0  00000-0 0    04
2 71703  63.4300  37.1342 0234817 144.7322 215.3563 13.65609061    06
DMSP F19
1 72910U          14093.66263531 0.00000000  00000-0  00000-0 0    01
2 72910  98.8700 109.1454 0009822 295.9013  64.2057 14.13825356    09
2010-062 UNID
1 78701U 10062X   11120.10505598 0.00000400  00000-0  57405-4 0    02
2 78701  71.9574 145.3579 0017000 355.7358   4.2641 14.76352554    05
FIA Radar 3
1 78817U 13072A   13341.53383309 0.00000000  00000-0  00000-0 0    03
2 78817 122.9957 228.6601 0014502 298.6008  61.3992 13.47753224    06
FIA Radar 3 r
1 78820U 13072P   13341.44424121 0.00000000  00000-0  00000-0 0    05
2 78820 120.4883 230.9287 0276875 339.4109  19.5967 14.61190032    02
NOSS 3-6 (P)
1 79603U 12048P   12261.45298345 0.00000000  00000-0  00000-0 0    05
2 79603  63.4386  32.7196 0127283 180.8197 179.1803 13.40494112    00
FIA Radar 2
1 79701U 12014A   12095.23647071 0.00000000  00000-0  00000-0 0    02
2 79701 123.0192 218.2476 0016360 317.0451  42.9234 13.45650207    08
NOSS 3-5 (B)
1 79937U 11014B   11110.75281113 0.00000000  00000-0  00000-0 0    07
2 79937  63.4047 338.3792 0127413 180.4827 179.5173 13.39341423    00
Unknown 981016
1 90002U 98789A   06006.92648003 0.00000000  00000-0  00000-0 0    09
2 90002  13.7831 340.5774 0016555 305.1111  54.7458  0.99808667    06
Unknown 990103
1 90003U 99503A   06018.00710268 0.00000000  00000-0  00000-0 0    00
2 90003  13.1475  24.2150 0009180 116.4066 243.6997  0.98677698    01
Unknown 990907
1 90004U 99750A   06097.80600307 -.00000505  00000-0 -18863-0 0    00
2 90004  64.5291 350.4796 7084586 279.3597  80.6391  2.01495310    08
Unknown 991031
1 90005U 99804A   06018.73290965 0.00000000  00000-0  00000-0 0    03
2 90005   7.9806   6.3675 0472424 243.4249 111.6810  0.99563483    09
Unknown 000405
1 90006U 00596A   06145.29819421 0.00000095  00000-0  23938-0 0    09
2 90006  63.3529 199.9244 6752207 283.4119  76.5881  2.00555791    09
Unknown 000601
1 90007U 00653A   06098.95306970 0.00000000  00000-0  00000-0 0    05
2 90007   9.8323  48.0204 0047144  54.8546 305.5982  1.00239154    00
Unknown 001203
1 90008U 00838A   05362.95530853 0.00000000  00000-0  00000-0 0    03
2 90008   6.9461 114.1948 0019914 174.6606 185.3725  1.00547382    08
Unknown 010313
1 90009U 01572A   06140.74274119 0.00000000  00000-0  00000-0 0    02
2 90009   2.9314  45.9265 0015000 339.4929  20.5071  1.00270000    00
Unknown 030305
1 90013U 03564A   05365.62255760 0.00000000  00000-0  00000-0 0    06
2 90013   7.1137   8.3672 0042091 213.9246 146.0754  1.00270000    00
Unknown 030923
1 90016U 03766A   06198.19827141 0.00000000  00000-0  00000-0 0    08
2 90016   6.8666  13.8494 0583335 183.1413 176.5626  1.00270000    00
Unknown 040208
1 90020U 04539A   05257.20527666 -.00000371  00000-0 -79704-0 0    08
2 90020  64.7204 285.9802 6783484 266.9398  93.0589  2.00951372    06
Unknown 040920
1 90022U 04764A   06269.06199207 0.00000000  00000-0  00000-0 0    04
2 90022  11.6732  66.9434 0316489 252.0766 104.4603  0.99514325    02
Unknown 041002
1 90023U 04776A   06006.38858888 0.00000000  00000-0  00000-0 0    09
2 90023   5.0100 177.7034 0004000 205.7851 154.2263  1.00270000    06
Unknown 041011
1 90024U 04785A   05274.35638107 0.00000000  00000-0  00000-0 0    03
2 90024   0.0500  85.8960 0001000   9.5595 350.4405  1.00270000    03
Unknown 041026
1 90025U 04800A   06183.53789828 0.00001050  00000-0  14709-0 0    06
2 90025  64.1225 256.4894 7210093 262.9974  99.0174  2.00587000    09
Unknown 041206
1 90027U 04841A   06071.55035598 0.00001113  00000-0  11045+1 0    09
2 90027  62.3773 158.6750 6940454 268.4454  91.5512  2.00728666    05
Unknown 041211
1 90028U 04846A   06159.43062649 0.00000000  00000-0  00000-0 0    09
2 90028  64.0772  29.4966 7382273 261.9243  98.0757  2.00625000    03
Unknown 050112
1 90029U 05512A   06018.63718640 0.00000000  00000-0  00000-0 0    06
2 90029  13.8738  13.1142 0003995  71.2329 288.8224  0.98951704    01
Unknown 050213
1 90030U 05544A   06007.24787862 0.00000000  00000-0  00000-0 0    00
2 90030   6.0118  48.8949 0114617 166.7998 193.5150  0.99578393    05
Unknown 050215
1 90031U 05546A   06018.65572539 0.00000000  00000-0  00000-0 0    03
2 90031   1.1000  63.5709 0010222 179.2424 180.7576  1.00270000    07
Unknown 050318
1 90032U 05577A   05116.46023920 0.00000411  00000-0  00000-0 0    06
2 90032  63.5256 327.4948 7380134 263.0325  96.9675  2.00614585    00
Unknown 050227
1 90033U 05558A   06018.85731161 0.00000000  00000-0  00000-0 0    08
2 90033   2.0160  74.6800 0030000  33.1612 326.8388  1.00270000    08
Unknown 050402
1 90034U 05592A   06018.71910417 0.00000000  00000-0  00000-0 0    05
2 90034   3.8000  45.6702 0007491 106.8854 253.1146  1.00270000    08
Unknown 050505
1 90035U 05625A   05362.54974897 0.00000000  00000-0  00000-0 0    07
2 90035   0.0200 354.9914 0003000  95.6060 264.3940  1.00270000    03
Unknown 050509
1 90036U 05629A   06010.40206371 0.00000000  00000-0  00000-0 0    03
2 90036   1.8500 326.9206 0020000 308.9433  51.0567  1.00270000    08
Unknown 050518
1 90037U 05638A   06079.40180517 0.00000000  00000-0  00000-0 0    02
2 90037  14.2982  33.7953 0021888 235.5780 124.4306  1.00271000    05
Unknown 050518
1 90038U 05638B   06010.36547102 0.00000000  00000-0  00000-0 0    00
2 90038   3.6133 312.7763 0010000 263.6647  96.3353  1.00270400    05
Unknown 050708
1 90039U 05689A   05346.40921668 0.00001052  00000-0  00000-0 0    04
2 90039  63.8308  12.1969 7098024 260.2953  99.7042  2.00744639    02
Unknown 050702
1 90040U 05683A   06010.57318895 0.00000407  00000-0  31110-3 0    01
2 90040  27.5239 114.8635 7016479 266.8135  93.2557  2.58073078    07
Unknown 051002
1 90041U 05775A   06024.52102519 0.00000000  00000-0  00000-0 0    08
2 90041  14.1180 347.6590 0030902 162.3863 197.7332  1.00479337    04
Unknown 051124
1 90042U 05828A   05364.80475198 0.00000000  00000-0  00000-0 0    01
2 90042   1.8300  85.8634 0002000 213.9437 146.0563  1.00270000    09
Unknown 051201
1 90043U 05835A   05364.71370386 0.00000000  00000-0  00000-0 0    03
2 90043   1.5656 346.0967 0007000 148.2516 211.7484  1.00270000    07
Unknown 051225
1 90044U 05859A   06002.82944993 0.00020000  00000-0  96959-3 0    06
2 90044  63.2528 236.8413 4261404 294.7048  65.2952  6.98670114    08
Unknown 051228
1 90045U 05862B   06002.66182344 0.00000000  00000-0  00000-0 0    04
2 90045   8.5203 186.2035 5754874  27.5269 332.4727  4.22727690    01
Unknown 051230
1 90046U 05864A   06009.57536690 0.00000112  00000-0  10215-0 0    04
2 90046  63.4777 260.4332 6956666 276.0373  83.9628  2.00613732    07
Unknown 060121
1 90047U 06521A   06024.72702083 0.00000000  00000-0  00000-0 0    08
2 90047  25.7535 308.6171 7207107 335.9939  24.0059  2.28274700    02
Unknown 050415
1 90048U 05605B   06038.05573991 0.00000000  00000-0  00000-0 0    06
2 90048   5.5634  76.0751 0032072  14.1134 345.9977  1.00594285    08
Unknown 050415
1 90049U 05605C   06037.27383977 0.00000000  00000-0  00000-0 0    03
2 90049   4.1640 161.3551 0011879 324.0805  35.8513  1.00595721    04
Unknown 050227
1 90050U 05558C   06059.93910082 0.00000000  00000-0  00000-0 0    02
2 90050  13.9238  13.1234 0018764  91.5995 268.6274  0.98818813    01
Unknown 050415
1 90051U 05605A   05241.35118712 0.00000000  00000-0  00000-0 0    04
2 90051   7.2179 348.6914 1295010 314.1949  35.8646  1.00150951    01
Unknown 060419
1 90052U 04109A   06109.85366700 0.00000000  00000-0  00000-0 0    04
2 90052   9.3679  53.1385 0012000 315.6230  44.3770  1.00270000    05
Unknown 050220
1 90053U 05551A   06143.34198075 0.00000000  00000-0  00000-0 0    07
2 90053   7.8144 353.9381 1073396 272.0437  87.9563  1.00270000    07
Unknown 950327
1 90054U 95586A   06198.46725162 0.00000000  00000-0  00000-0 0    01
2 90054   3.0358  76.0091 0039416 175.6179 184.2812  1.00270000    07
Unknown 960906
1 90055U 96750A   06199.08002185 0.00000000  00000-0  00000-0 0    08
2 90055   5.2943   3.1498 0925710 210.8082 149.1923  1.00270000    03
Unknown 060503
1 90056U 06623A   06322.94510516 0.00000000  00000-0  00000-0 0    04
2 90056   7.2520 356.1980 0932075 255.9116 104.0884  1.00270000    00
Unknown 060625
1 90057U 06676A   06207.01005982 0.00000000  00000-0  00000-0 0    09
2 90057  26.9476  68.1456 7173774  54.7817 305.4409  2.34416859    02
Unknown 060617
1 90058U 06668A   06213.87615521 0.00110000  00000-0  70237-3 0    02
2 90058  26.4049 222.4175 5435308 258.1896 101.8100  5.06142444    00
Unknown 060624
1 90059U 06675A   06213.40370816 0.00000542  00000-0  14233-3 0    08
2 90059  28.7365 286.3203 7286371 158.7000 201.2761  2.27620548    00
Unknown 060520
1 90060U 06640A   06213.63054290 0.00000000  00000-0  00000-0 0    05
2 90060  29.2763  47.7373 7093583  80.6305 279.3694  2.32913910    04
Unknown 060616
1 90061U 06667A   06222.02218586 0.00003000  00000-0  37574-3 0    00
2 90061  27.3823 233.4744 6875518 226.8912 133.1086  2.82348878    02
Unknown 060718
1 90062U 06199A   06223.76547498 0.00000000  00000-0  00000-0 0    08
2 90062   7.2890 189.8930 6839993 283.3245  76.6751  2.77430457    08
Unknown 060802
1 90063U 06214A   06227.02166296 0.00000000  00000-0  00000-0 0    03
2 90063  11.6391  47.0304 0126000  81.1450 278.8550  1.00270000    02
Unknown 060320
1 90064U 06579A   06239.69337876 0.00000000  00000-0  00000-0 0    08
2 90064  63.4467  68.5584 3305539 264.7788  95.2212  5.52842574    00
Unknown 060509
1 90065U 06629B   06239.61902766 0.00004000  00000-0  30340+1 0    07
2 90065  63.3895 300.5325 3358959 269.6587  90.3414  5.54462256    09
Unknown 050616
1 90066U 05667A   06264.54841245 0.00000000  00000-0  00000-0 0    09
2 90066   2.5399  65.1529 0013926 309.9507  49.9391  1.00475347    09
Unknown 060326
1 90067U 06085A   06346.15791963 0.00000000  00000-0  00000-0 0    04
2 90067  14.9277 353.2022 0078968 211.7528 147.7807  0.97525542    08
Unknown 061108
1 90068U 06812A   06315.12171652 0.00000000  00000-0  00000-0 0    03
2 90068   9.2728  55.6347 0002000 340.3244  19.6756  1.00270000    09
Unknown 050301
1 90069U 05560A   06316.23065343 0.00000000  00000-0  00000-0 0    05
2 90069  14.6843   5.9956 0008122 115.5975 244.4985  0.98741716    01
Unknown 061125
1 90070U 06829A   06336.25247557 0.00013000  00000-0  57382-3 0    01
2 90070  27.4667  75.3817 4799897 331.0516  28.9480  6.04892999    00
Unknown 050227
1 90071U 05558B   08030.76647236 0.00000000  00000-0  00000-0 0    05
2 90071  10.9841  34.8099 0021503 106.0371 254.2119  0.98385359    08
Unknown 050301
1 90072U 05560C   07063.31680326 0.00000000  00000-0  00000-0 0    02
2 90072  14.4214 348.0660 0002296  16.0318 343.9875  0.99461249    04
Unknown 070310
1 90073U 07569A   07218.27701724 0.00000000  00000-0  00000-0 0    07
2 90073  12.3375 333.6121 0016032 220.0822 139.8115  0.98152425    03
Unknown 060326
1 90074U 06585B   08271.90138811 0.00000000  00000-0  00000-0 0    06
2 90074  14.7436   0.1190 0055910 121.5737 238.9855  0.99437823    09
Unknown 050415
1 90075U 05605D   08320.72470970 0.00000000  00000-0  00000-0 0    09
2 90075   6.9467 351.1744 1279846  28.4373 338.0007  0.99676604    02
Unknown 070918
1 90076U 07761A   07261.14212025 0.00000000  00000-0  00000-0 0    09
2 90076  18.7352   4.4643 0024056 177.2573 182.7789  1.00217190    03
Unknown 070914
1 90077U 07757A   07272.02679788 0.00000700  00000-0  53965-3 0    05
2 90077  28.1149 223.4027 7211623  34.5532 325.4466  2.33718986    01
Unknown 071201
1 90078U 07835A   07337.91338451 0.00000000  00000-0  00000-0 0    04
2 90078   1.0439  81.5551 0002593 163.2956 196.7247  1.04000377    07
Unknown 071225
1 90079U 07859A   08005.82782101 0.00000000  00000-0  00000-0 0    09
2 90079  62.4173 321.5587 7063071 273.7666  86.2334  2.17597297    07
Unknown 080331
1 90080U 08591A   08114.89787183 0.00000000  00000-0  00000-0 0    08
2 90080  63.3561 169.3958 4938027 292.2456  67.7544  5.52688554    08
Unknown 080507
1 90081U 08628A   08137.07694771 -.00000848  00000-0  00000-0 0    06
2 90081  62.8133 214.3140 6808239 276.9167  16.0088  2.00573006    08
Unknown 080818
1 90082U 08731A   08238.36640692 0.00000000  00000-0  00000-0 0    08
2 90082  64.1000  87.1676 6500000 260.3687  14.3594  2.00600500    09
Unknown 000405
1 90083U 09526A   09041.61082110 -.00000043  00000-0  00000-0 0    06
2 90083  63.9971 336.2962 7172924 278.6846  12.8961  2.00612597    00
Unknown 9O0DC57
1 90084U 09710A   09244.64721928 0.00000000  00000-0  00000-0 0    09
2 90084  41.8425 356.8152 7570669 190.1322 133.6279  0.44275082    08
Unknown 091017
1 90085U 09790A   09292.01577191  .00000000  00000-0  00000+0 0    02
2 90085  25.3410  12.0524 6961417 187.5746 150.4904  2.73606553    05
Unknown 101019
1 90086U 10792A   10293.40767197  .01192144  00000-0  74211-3 0    01
2 90086  26.3644  16.4586 2095633 273.6405  94.8735 11.57122578    00
Unknown 110623
1 90087U 11674A   11177.96275344 0.00000100  00000-0  00000-0 0    04
2 90087  26.7578 123.5582 7347027 137.0879 222.9119  2.00830285    06
Unknown 111101
1 90088U 11805A   11309.06268930 0.00195000  00000-0  52546-3 0    01
2 90088  24.0237  18.9989 6960288 186.2817 155.5822  2.76778641    07
Unknown 120723
1 90089U 12705A   12220.02431339 0.00023389  00000-0  95520-3 0    05
2 90089  25.6421 131.8563 7019888 177.3023 191.5831  2.65684060    04
Unknown 120530
1 90090U 12651A   12310.78408745 0.00000452  00000-0  21111-3 0    06
2 90090  63.3240 192.1322 0669187  50.1557 309.7753 13.41089659    08
Unknown 131121
1 90091U 13825A   13341.95489258 -.00001113  00000-0  00000-0 0    00
2 90091  62.6309  14.1059 7269922 270.7699  14.5171  2.00560139    09
Unknown 140824
1 90092U 14735A   14242.95503590 0.00000000  00000-0  00000-0 0    02
2 90092  15.1286   9.3792 0089042  56.2201 304.3016  0.99531895    00
Unknown141003A
1 90093U 14576A   14276.74591757 0.00003373  00000-0  13244-0 0    02
2 90093   3.8791 318.8159 7248031 272.6482  14.1023  2.08151131    05
Unknown141003B
1 90094U 14776B   14283.36769152 0.00000000  00000-0  00000-0 0    07
2 90094  24.2135 306.5490 5129031 168.6285 210.0496  1.94990330    05
Unknown 141011
1 90095U 14784A   14284.61299940 0.00000000  00000-0  00000-0 0    09
2 90095  63.1946 229.8784 6997432 265.8347  18.5519  2.38687000    02
Unknown 141017
1 90096U 14790A   14290.32717842 0.00001216  00000-0  00000-0 0    08
2 90096  63.5519 329.1665 7278087 274.7780  13.2468  2.04981299    09
ISON 37600
1 90097U 14792A   14324.22065240 0.00000000  00000-0  00000-0 0    06
2 90097   4.5567 104.4372 5658746  77.6790 337.3548  3.99368491    07
ISON 63200
1 90099U 14792C   15253.75900097 0.00000300  00000-0  56680-3 0    07
2 90099  28.8113 318.4133 7231764 181.9215 173.1245  2.27903210    01
ISON 144402
1 90100U 14798A   16094.39398747 0.00000000  00000-0  00000-0 0    02
2 90100  10.4683  39.0470 0206359 312.6121  45.6776  0.99706215    02
ISON 64800
1 90103U 14820A   14329.50798226 0.00000000  00000-0  00000-0 0    09
2 90103  63.9343 196.8175 6524807 260.9662  25.3221  2.21892500    07
ISON 77400
1 90104U 14735A   14311.60381953 0.00000000  00000-0  00000-0 0    02
2 90104  11.4240 296.6895 4859083 216.4018  97.9237  1.86027107    01
ISON 81600
1 90105U 14824A   14324.50091989 0.00000000  00000-0  00000-0 0    02
2 90105  20.9494 158.0091 5607648 162.1109 197.8891  1.76312000    08
ISON  59700
1 90106U 14844A   14344.93775833 0.00001037  00000-0  11372-2 0    08
2 90106   1.7288 107.8123 7133426  65.2861 350.7480  2.42060426    03
ISON 68600
1 90107U 14844B   14344.56595229 0.00000000  00000-0  00000-0 0    00
2 90107   5.9532  78.8720 6279691 158.2173 249.7319  2.09703600    04
ISON 47601
1 90108U 14845A   14345.78155113 0.00130000  00000-0  18587-2 0    06
2 90108  26.1828  35.4683 6439223 226.4502  57.9456  3.48344430    05
ISON 54102
1 90109U 15523A   15029.57905560 0.00005800  00000-0  46958-2 0    09
2 90109  10.4211 317.0590 6904054 338.7542   2.8690  2.72178709    03
ISON 20100
1 90110U 15545A   15045.04292572 0.00000901  00000-0  94884-3 0    06
2 90110  63.6259 336.8399 3953340 298.9469  27.1475  7.14307836    04
ISON 60601
1 90111U 15607A   15107.89871643 0.00001000  00000-0  13050-1 0    05
2 90111  10.6896  53.7508 7057175 341.8331   1.9904  2.37655470    09
ISON 62200
1 90112U 15614A   15114.81795662 0.00000505  00000-0  12336-2 0    06
2 90112   5.6630 163.6807 7185228 168.6699 227.4237  2.32366316    03
ISON 32000
1 90113U 16535A   16035.80645369 0.00022000  00000-0  12036-2 0    01
2 90113  25.7492 289.9636 5615007  15.7724 356.3818  4.69385969    01
ISON 49200
1 90114U 16591A   16091.06076050 0.00017500  00000-0  11494-2 0    05
2 90114  63.3298 353.0721 6721151 268.3028  19.9584  3.04943579    01
ISON 63700
1 90115U 16612A   16112.02101776 0.00001839  00000-0  54920-1 0    02
2 90115   5.5953  41.9123 7102035   6.8645 358.9886  2.26165691    07
ISON 51100
1 90116U 16697A   16197.02271432 0.00000000  00000-0  00000-0 0    04
2 90116   3.9248 273.8998 6620303 223.5734 136.4263  2.80970031    02
ISON 35200
1 90117U 16707A   16207.35955033 0.00000000  00000-0  00000-0 0    01
2 90117  63.4918 231.6878 5884284 265.7474  29.0451  4.09304115    08
ISON 42000
1 90118U 16730A   16230.35935117 0.00011366  00000-0  14734-2 0    03
2 90118  26.0225 336.1134 6270391 200.1137 116.5868  3.66447608    00
ISON 61100
1 90119U 16843A   16343.42987787 0.00000142  00000-0  27797-3 0    06
2 90119  28.7816 227.6741 7149883 333.5099   3.3944  2.37617559    03
ISON 41700
1 90120U 17538A   18038.90025342 0.00003500  00000-0  29034-2 0    02
2 90120  24.9795  43.0554 6138627 225.9473 152.0618  3.75473860    02
ISON 69600
1 90121U 18773A   18273.06751200 0.00000000  00000-0  00000-0 0    04
2 90121  62.8485 202.2860 6638524 253.8350 106.1650  2.06880107    09
Unknown 070914
1 90177U 07757A   19142.11009172 0.00000000  00000-0  00000-0 0    01
2 90177  28.6405  55.6760 7139573 123.6282 325.0221  2.39943421    01
Unknown 061210
1 91090U 06844A   06344.94929672 0.00000000  00000-0  00000-0 0    09
2 91090   2.7000  38.7258 0001000 341.1643  18.8357  1.00270000    08
Unknown 070511
1 91117U 07631A   07139.26722877  .00000000  00000-0  00000+0 0    09
2 91117  50.7032 157.3669 4804844 248.9007 111.6171  5.07303637    09
Unknown 081224
1 91132U 08859A   08363.85226720 0.00000000  00000-0  00000-0 0    01
2 91132   0.1956  67.6540 0002292 197.1192 162.8932  0.99949073    03
Unknown 090123
1 91141U 09523A   09023.27786493 0.00000000  00000-0  00000-0 0    08
2 91141   0.1465 277.1835 0001045 113.3174 246.6826  1.00566977    02
Unknown 090215
1 96002U 96502A   09046.73183017 0.00000000  00000-0  00000-0 0    01
2 96002   4.9583  72.2162 0020199 137.2073 222.9621  1.00738930    07
Unknown 090103
1 96005U 96505A   09003.90602467 0.00000000  00000-0  00000-0 0    04
2 96005   5.1196  67.1652 0239868 214.2204 144.2231  0.99716871    07
Unknown 080229
1 96006U 96506A   08060.77423349 0.00000000  00000-0  00000-0 0    07
2 96006   4.5303  75.9027 0002291 319.4726  40.5224  1.01113961    04
Unknown 080229
1 96009U 96509A   08096.51286366 0.00000000  00000-0  00000-0 0    06
2 96009   2.8307  21.8640 1452369 290.8193  54.2771  1.00124605    04
Unknown 081022
1 96010U 96510A   08296.77355037 0.00000000  00000-0  00000-0 0    02
2 96010   2.9182  15.4739 1442354  15.8083 348.2633  0.99618090    08
Unknown 050627
1 96011U 96511A   08064.64212642 0.00000000  00000-0  00000-0 0    07
2 96011   6.5684  69.5637 0053365  96.6612 263.9586  1.01183929    09
Unknown 050406
1 96012U 96512A   08096.86498368 0.00000000  00000-0  00000-0 0    09
2 96012   3.0349 157.4932 0998767 349.8187   8.2990  1.03851217    02
Unknown 081021
1 96015U 96515A   08294.41062971 0.00000000  00000-0  00000-0 0    03
2 96015   7.5933  65.0334 0020417 222.4009 137.4533  1.01182968    06
Unknown 081021
1 96019U 96519A   08294.35649347 0.00000000  00000-0  00000-0 0    02
2 96019   8.9308  59.2425 0003407 253.9774 105.9972  1.01182092    00
Unknown 081118
1 96020U 96520A   08323.70749973 0.00000000  00000-0  00000-0 0    04
2 96020   6.1839  11.7069 1043244 284.6255  64.0509  0.99426703    04
Unknown 080408
1 96022U 96522A   08099.61641082 0.00000000  00000-0  00000-0 0    00
2 96022   9.8980  52.9806 0016445 145.2103 214.9094  1.01259033    04
Unknown 080926
1 96025U 96525A   08270.96309031 0.00000000  00000-0  00000-0 0    00
2 96025   7.6389 358.4193 0975000 344.5655  12.6679  0.99444016    01
Unknown 080229
1 96027U 96527A   08098.39106334 0.00000000  00000-0  00000-0 0    00
2 96027   9.0026  13.9951 0045502  22.0048 338.2019  1.00351012    02
Unknown 050301
1 96028U 96528A   08100.58033098 0.00000000  00000-0  00000-0 0    03
2 96028  10.7066  43.8128 0082752 306.4114  52.8402  1.02110481    05
Unknown 080911
1 96029U 96529A   08255.93880784 0.00000000  00000-0  00000-0 0    07
2 96029  10.9471  31.4307 0004599 107.2756 252.7868  1.01242586    00
Unknown 050612
1 96031U 96531A   08064.36769844 0.00000000  00000-0  00000-0 0    01
2 96031   8.7338 322.6710 0224048 198.1654 161.0338  1.01903049    04
Unknown 080302
1 96032U 96532A   08062.64872644 0.00000000  00000-0  00000-0 0    05
2 96032  13.4036  23.3941 0001000 125.9163 234.1039  1.01155123    00
Unknown 090420
1 96033U 96533A   09110.63239993 0.00000000  00000-0  00000-0 0    05
2 96033  13.9432  18.2202 0057566   3.7749 356.2802  1.01080704    06
Unknown 080304
1 96038U 96538A   08064.40626317 0.00000000  00000-0  00000-0 0    07
2 96038  11.4764 330.8618 0065894 331.1138  28.5350  1.00659910    06
Unknown 080304
1 96039U 96539A   08064.62138421 0.00000000  00000-0  00000-0 0    07
2 96039  13.8130   8.7463 0013569 304.8716  55.0129  1.01251536    02
Unknown 080304
1 96040U 96540A   08064.58411234 0.00000000  00000-0  00000-0 0    02
2 96040  13.6458   5.0879 0052131 138.0675 222.3450  1.01329548    00
Unknown 100202
1 96041U 96541A   10033.50617528 0.00000000  00000-0  00000-0 0    09
2 96041  14.1070 359.5358 0044918 231.0381 128.5729  1.00224248    04
Unknown 090720
1 96044U 96544A   09201.96545740 0.00000000  00000-0  00000-0 0    06
2 96044  14.3745   1.0263 0053649 298.1383  61.3327  1.00336036    06
Unknown 090128
1 96047U 96547A   09028.63032334 0.00000000  00000-0  00000-0 0    03
2 96047  16.0654  24.9673 0024383 122.3340 237.9143  1.00815221    05
Unknown 080304
1 96049U 96549A   08064.44685507 0.00000000  00000-0  00000-0 0    01
2 96049  13.1088 335.3875 0031824 238.9238 120.7755  0.99556421    06
Unknown 080911
1 96050U 96550A   08255.02233796 0.00000000  00000-0  00000-0 0    00
2 96050  13.4137 340.5469 0012896   2.9643 357.0553  1.00524592    08
Unknown 080911
1 96054U 96554A   08255.87927744 0.00000000  00000-0  00000-0 0    04
2 96054  13.6860 342.2216 0010151  46.8918 313.2051  1.00552224    00
Unknown 050227
1 96055U 96555A   08100.44212720 0.00000000  00000-0  00000-0 0    09
2 96055  14.6318 351.7468 1080958  59.5789 310.6741  1.01770851    00
Unknown 050403
1 96058U 96558A   08086.39376577 0.00000000  00000-0  00000-0 0    03
2 96058  16.8187   5.3065 0036070 257.7007 101.9200  0.94327282    05
Unknown 081019
1 96059U 96559A   08293.81340330 0.00000000  00000-0  00000-0 0    00
2 96059  19.8602 340.0457 1275710 313.4680  36.5967  1.02314755    02
Unknown 080304
1 96060U 96560A   08064.39018608 0.00000000  00000-0  00000-0 0    03
2 96060  21.2625 351.7156 1302320 215.7121 134.8443  1.00184598    02
Unknown 080926
1 96061U 96561A   08270.24471407 0.00000000  00000-0  00000-0 0    08
2 96061   3.5773  70.0911 0009000 203.4988 156.4722  0.99905530    07
Unknown 080304
1 96062U 96562A   08100.71696554 0.00000000  00000-0  00000-0 0    06
2 96062   0.9611  64.2132 0006150 222.5308 137.4336  0.99820367    05
Unknown 090220
1 96067U 96567A   09061.15788108 0.00000000  00000-0  00000-0 0    08
2 96067   5.0689  67.0894 0005392 347.9646  12.0344  0.99703848    02
Unknown 080304
1 96070U 96570A   08101.00872691 0.00000000  00000-0  00000-0 0    05
2 96070   2.4964 215.8648 0985398 253.4186  95.5602  1.00368077    03
Unknown 080927
1 96071U 96571A   08277.13303548 0.00000000  00000-0  00000-0 0    05
2 96071   7.1630  67.9520 0024000  10.2236 349.8262  0.99498363    06
Unknown 081021
1 96076U 96576A   08301.85393732 0.00000000  00000-0  00000-0 0    06
2 96076   7.7179 351.1443 0960487  12.7427 349.4839  0.99600970    09
Unknown 081120
1 96077U 96577A   08325.85800704 0.00000000  00000-0  00000-0 0    06
2 96077  10.7161  50.2040 0004288 267.6007  92.3622  0.99322423    06
Unknown 080501
1 96078U 96078A   08122.54349808 0.00000000  00000-0  00000-0 0    07
2 96078  10.3461  49.7125 0024235 179.3373 180.6780  1.01274257    03
Unknown 080309
1 96079U 96579A   08069.69673970 0.00000000  00000-0  00000-0 0    05
2 96079  10.3707  50.9256 0007270 261.4505  98.4791  0.98989015    04
Unknown 081022
1 96080U 96580A   08296.85496185 0.00000000  00000-0  00000-0 0    05
2 96080  10.8549  39.4838 0048453 198.5563 161.2785  1.01304710    05
Unknown 081021
1 96081U 96581A   08294.25232584 0.00000000  00000-0  00000-0 0    00
2 96081  11.2450  45.7120 0077703 275.0046  84.1210  0.99906934    01
Unknown 080309
1 96082U 96582A   08122.37762015 0.00000000  00000-0  00000-0 0    02
2 96082   9.8078  12.1480 1460039  12.0363 351.1134  1.02326597    06
Unknown 081022
1 96084U 96584A   08302.94748073 0.00000000  00000-0  00000-0 0    07
2 96084  11.4187  44.2975 0009022 232.7367 127.1884  0.99248500    03
Unknown 080409
1 96085U 96585A   08100.69892177 0.00000000  00000-0  00000-0 0    02
2 96085  11.1264  39.3093 0026169 252.4349 107.2911  1.01639621    05
Unknown 090214
1 96087U 96587A   09044.89525712 0.00000000  00000-0  00000-0 0    04
2 96087  12.3775  34.9456 0011397  90.8437 269.2989  0.98605782    00
Unknown 081019
1 96088U 96588A   08292.96283639 0.00000000  00000-0  00000-0 0    07
2 96088  12.1705  29.4325 0069691 174.4171 185.6732  1.01239903    00
Unknown 080229
1 96089U 96589A   08060.53498818 0.00000000  00000-0  00000-0 0    02
2 96089   9.6611 330.6652 0185997 220.1976 138.4244  1.00699880    05
Unknown 080229
1 96091U 96591A   08060.32446549 0.00000000  00000-0  00000-0 0    09
2 96091  10.9952 352.4674 0014798 154.6112 205.4736  1.00501009    06
Unknown 080803
1 96093U 96593A   08215.28997837 0.00000000  00000-0  00000-0 0    01
2 96093  10.8328 326.6735 0038054 304.7776  54.8767  1.00434895    08
Unknown 080911
1 96094U 96594A   08255.89252771 0.00000000  00000-0  00000-0 0    05
2 96094  12.9829   8.6765 0696377  99.3668 268.5795  0.93696548    04
Unknown 081021
1 96095U 96595A   08294.18251905 0.00000000  00000-0  00000-0 0    00
2 96095  13.5257  14.1909 0031472 154.1760 205.9936  1.01164980    03
Unknown 080927
1 96098U 96598A   08277.88170435 0.00000000  00000-0  00000-0 0    02
2 96098  14.5448 354.0857 0008392  26.0996 333.9717  1.00198879    02
Unknown 080229
1 96101U 96601A   08062.49629351 0.00000000  00000-0  00000-0 0    07
2 96101  15.2567   1.0345 0004633 173.2996 186.7187  0.99004765    09
Unknown 080302
1 96102U 96602A   08062.41228654 0.00000000  00000-0  00000-0 0    02
2 96102  15.2927 356.6593 0914988  41.9981 324.6887  0.99235365    04
Unknown 080920
1 96103U 96603A   08264.92829330 0.00000000  00000-0  00000-0 0    02
2 96103  20.6123 345.7805 1312167 279.6206  65.8356  1.02087560    02
Unknown 090104
1 96104U 96604A   09004.46041200 0.00000000  00000-0  00000-0 0    08
2 96104   0.0050  84.9509 0001000 173.8940 186.1060  1.00270000    07
Unknown 080229
1 96126U 96626A   08060.78546095 0.00000000  00000-0  00000-0 0    04
2 96126   6.7593  70.1253 0007953 192.3467 167.6458  0.99119499    08
Unknown 090215
1 96127U 96627A   09046.66695530 0.00000000  00000-0  00000-0 0    07
2 96127   7.9678  64.6583 0006567 199.8241 160.1623  0.99036302    05
Unknown 080920
1 96132U 96632A   08264.17193122 0.00000000  00000-0  00000-0 0    06
2 96132   9.1149  30.8425 0655443 252.7264 100.0146  1.10773811    05
Unknown 090220
1 96135U 96635A   09061.02229998 0.00000000  00000-0  00000-0 0    03
2 96135  12.8109  29.8292 0032281  35.1712 324.9230  0.97828162    00
Unknown 081022
1 96137U 96637A   08301.95162800 0.00000000  00000-0  00000-0 0    03
2 96137  14.4606 353.6224 0013800 171.0170 189.0197  1.00329687    04
DSP F15 Cover
1 96143U 90095E   12252.35954447 0.00000000  00000-0  00000-0 0    02
2 96143  14.1584  29.3941 0086528 131.4655 229.2929  0.99285540    07
Unknown 090103
1 96144U 96644A   09003.50600162 0.00000000  00000-0  00000-0 0    08
2 96144  11.6034 330.3545 0008228 236.2970 123.6365  0.99765774    03
Unknown 080930
1 96145U 96645A   08277.05017666 0.00000000  00000-0  00000-0 0    03
2 96145  18.0058 294.7849 1246854 290.1798  56.8594  1.01708854    09
Unknown 090222
1 96151U 96651A   09061.26213363 0.00000000  00000-0  00000-0 0    03
2 96151   2.8722 110.6502 0007024 173.3904 186.6327  1.00271000    04
Unknown 090222
1 96153U 96653A   09052.88999143 0.00000000  00000-0  00000-0 0    03
2 96153   2.2340  34.5244 0255638 191.4014 168.0085  0.95121995    07
Unknown 120530
1 99015U 12651A   12169.31301658 0.00001300  00000-0  15136-3 0    01
2 99015  98.1973 111.5061 0010333 298.8158  61.1840 14.85307145    07
99046
1 99046U          13115.97760364 0.00000090  00000-0  44798-5 0    00
2 99046  97.4409 236.8971 0003000 170.0754 189.9244 15.17645170    00
99047
1 99047U 13595B   13115.98761716 0.00023000  00000-0  99272-3 0    08
2 99047  97.4882 237.6643 0002996 353.5123   6.4875 15.22560744    04
99048
1 99048U          13118.00841701 0.00036500  00000-0  15440-2 0    08
2 99048  97.4912 239.8975 0001752 142.9081 217.0918 15.23247676    08
99049
1 99049U          13116.98765167 0.00012800  00000-0  39776-3 0    01
2 99049  97.5373 239.8673 0054335 195.1828 164.8171 15.31880471    05
99050
1 99050U          13117.99836650 0.00002000  00000-0  16259-3 0    03
2 99050  97.6576 237.5699 0015692 204.0608 155.9391 14.99547427    04
Unknown 130608
1 99064U 13659A   13171.34611362 0.00000000  00000-0  00000-0 0    04
2 99064   4.7115  62.4659 0004148   8.0943 351.9292  1.00427101    08
SAR Lupe3or5
1 99068U 13770A   13271.79560051 0.00000000  00000-0  00000-0 0    00
2 99068  98.1752 308.5386 0003602   0.3543 359.6456 15.27557102    08
Unknown 130929
1 99069U 13772A   13273.75224919 0.00000138  00000-0  00000-0 0    03
2 99069  64.0272 258.5812 6654330 276.1244  16.1326  2.00614452    03
Unknown 131001
1 99070U 13774A   13278.79023945 0.00000000  00000-0  00000-0 0    00
2 99070   5.2985 319.5957 0005819 266.2397  93.7006  1.00270000    08
Unknown 131021
1 99075U 13794A   13296.82824030 0.00000000  00000-0  00000-0 0    05
2 99075   2.9784 314.0976 0002683 308.1391  51.8406  1.00270000    00
Unknown 131120
1 99079U 13825A   13335.71953869 0.00002800  00000-0  12676-2 0    03
2 99079  28.4923   5.3250 7184644 218.6097  57.5864  2.38762084    01
Unknown131229B
1 99085U 13863B   14003.80411560 0.00000000  00000-0  00000-0 0    08
2 99085   0.1713  81.5121 0003189 144.4001 215.5999  1.00376385    01
Unknown 140103
1 99086U 14503A   14003.81258995 0.00000000  00000-0  00000-0 0    03
2 99086  11.2184  44.0392 0005179 296.4846  63.4155  1.00270000    08
Essaim 14547A
1 99091U 14547A   14052.77390121 0.00000000  00000-0  00000-0 0    04
2 99091  98.3277  94.6861 0003236  86.3983 273.6664 14.78500946    09
Unknown140221E
1 99096U 14552E   14061.90935522 0.00002026  00000-0  23663-2 0    02
2 99096  63.2369  22.5189 7322465 270.6871 330.9436  2.18857743    04
Unknown 140303
1 99099U 14562A   14064.88053226 0.00910809  00000-0  25276-3 0    08
2 99099  21.5237 107.5170 4930158 197.9328 135.9812  5.98574706    08
Unknown 130428
1 99143U 13618A   13129.37386472 0.00000000  00000-0  00000-0 0    04
2 99143  97.1534 250.2405 0005719 244.0786 172.8044 15.46470036    00
Unknown 131224
1 99155U 13858A   13358.26109368 0.00000000  00000-0  00000-0 0    02
2 99155   4.9439 303.9995 0480203 182.4544 328.4754  0.99493725    04
Object 10062X
1 99207U 10062X   13155.25626156 0.00000000  00000-0  00000-0 0    07
2 99207  72.0259 255.5944 0020000 337.6259  66.2618 14.77170909    09
Unk 130404
1 99208U 13594A   13196.65856129 0.00430000  00000-0  27787-2 0    05
2 99208  20.2342 280.8648 5993339 159.4367 242.7508  4.16919351    02
Unknown 130704
1 99210U 13685A   13199.96892181 0.00001150  00000-0  92963-3 0    03
2 99210  63.3059 191.0441 0405425 116.8184 243.1816 13.57884301    03
Unknown 130725
1 99212U 13706A   13248.88429323 0.00000200  00000-0  51524-3 0    02
2 99212  27.9553 235.4646 7168230 359.9657 359.9774  2.34151114    03
Unknown 131012
1 99218U 13785A   13295.97738589 0.00001000  00000-0  13232-3 0    07
2 99218  98.3481 327.0658 0000500  25.7826  20.4778 14.80017172    09
Essaim 14544A
1 99221U 14544A   14052.75428076 0.00000500  00000-0  71134-4 0    00
2 99221  98.3503  87.4467 0000628   9.4204 350.5794 14.76943147    03
Unknown 140607
1 99224U 14658A   14158.05870913 0.00000000  00000-0  00000-0 0    05
2 99224  63.2984  59.7602 0649136  78.7674 281.2326 13.86763379    04
Unk
1 99406U 14602A   14109.95853628 0.00001600  00000-0  51820-3 0    01
2 99406  63.2995  78.8961 0737856  80.7875 279.2125 13.43060588    00
Unknown 140823
1 99424U 14735B   14291.72435747 0.00000000  00000-0  00000-0 0    07
2 99424  11.4451 298.6308 4870003 212.6338 104.7926  1.86027107    00
Essaim 99449
1 99449U 15720A   15220.86620070 0.00000000  00000-0  00000-0 0    02
2 99449  98.2702 294.2724 0001261 247.1290 112.8708 14.63067828    02
Elisa 99450
1 99450U 15720B   15224.89694404 0.00000500  00000-0  94309-4 0    07
2 99450  98.0802 297.9838 0005267 322.6356  37.3643 14.64577524    00
Unknown 101208
1 99991U 10742A   10345.69214651 0.00000000  00000-0  00000-0 0    01
2 99991   0.0668  12.3384 0002903 145.4049 214.6472  1.00404895    08

1 99992U          18078.78364164  .00000000  00000-0  00000-0 0    04
2 99992  63.3235 341.7709 0800761 110.5196 252.1151 13.49010610    00

1 99993U 11674A   11176.08369001 0.00000000  00000-0  00000-0 0    04
2 99993  26.1166 131.3682 6781610 145.7450 274.2928  3.01235994    02

1 99994U 11674A   11176.13115708 0.00000000  00000-0  00000-0 0    03
2 99994  26.2366 130.3455 6105404 148.2332 313.8428  4.01632994    07

1 99995U 11674A   11176.12751252 0.00000000  00000-0  00000-0 0    02
2 99995  26.4366 129.5536 5483915 149.7695 295.2928  5.02022994    05

1 99996U 11674A   11176.12140414 0.00000000  00000-0  00000-0 0    04
2 99996  26.5366 129.1682 4902726 151.7450 268.2928  6.02405994    07

1 99999U 14736A   14236.81819308  .00000000  00000-0  00000-0 0    03
2 99999  15.2395   9.6197 1034942 127.6835 195.0717  1.21226772    09
'''

snapshots['test_tle_trusat_priorities 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'text/plain', 'Access-Control-Allow-Origin': '*'}

CONTENT:Unknown 070914
1 90177U 07757A   19142.11009172 0.00000000  00000-0  00000-0 0    01
2 90177  28.6405  55.6760 7139573 123.6282 325.0221  2.39943421    01
CSO 1
1 43866U 18106A   19104.02036166 0.00000000  00000-0  00000-0 0    05
2 43866  98.6110  44.4325 0001684 162.5259 197.5005 14.26738299    03
USA 290
1 43941U 19004A   19034.25038896 0.00000000  00000-0  00000-0 0    06
2 43941  73.6099  86.4526 0018729  44.6193 315.3807 15.53160071    08
ESHAIL 2
1 43700U 18090A   18330.87536882 0.00000000  00000-0  00000-0 0    07
2 43700   0.0750 318.0416 0005000 318.9982 127.3114  1.00270000    05
AEHF 4
1 43651U 18079A   18300.25858909 0.00000000  00000-0  00000-0 0    05
2 43651   7.6748 299.5509 1927334 182.3182 177.6818  1.32745226    06
AEHF 4 r
1 43652U 18079B   18292.01091487 0.00000000  00000-0  00000-0 0    00
2 43652  12.4468 299.9219 4706018 177.9937 135.5054  1.83429526    00
PAN r
1 35816U 09047B   18282.71996110 0.00000000  00000-0  00000-0 0    01
2 35816  22.9471 142.3146 5167264  91.1611 325.7804  1.94974253    04
ISON 69600
1 90121U 18773A   18273.06751200 0.00000000  00000-0  00000-0 0    04
2 90121  62.8485 202.2860 6638524 253.8350 106.1650  2.06880107    09
DSN 2 r
1 41941U 17005B   18213.56543130 0.00000100  00000-0  15139-3 0    00
2 41941  21.3100  61.4050 7218605 205.1470  87.0456  2.30389691    03
IGS Opt 6
1 43223U 18021A   18168.30056652 0.00000000  00000-0  00000-0 0    00
2 43223  97.4607 288.1271 0001238 165.0178 184.2919 15.27661121    06
IGS Radar 6 r
1 43496U 18052B   18167.95995151 0.00000000  00000-0  00000-0 0    02
2 43496  97.3785 284.1465 0011502 266.9348  93.0651 15.21683580    07
IGS Radar 6
1 43495U 18052A   18163.22499904 0.00000000  00000-0  00000-0 0    02
2 43495  97.2624 279.4803 0014129  53.7498 304.7202 15.25130130    02
IGS Opt 6 r
1 43224U 18021B   18148.12499854 0.00002000  00000-0  84250-4 0    09
2 43224  97.2158 265.9641 0003245  71.2932 288.5103 15.23386603    04
USA 287
1 43465U 18036G   18139.83833779 0.00000000  00000-0  00000-0 0    03
2 43465   0.0749  83.9927 0003505 288.3053  71.7431  1.00928636    02
CBAS 1 r Db
1 43342U 18036D   18133.73566022 0.00000000  00000-0  00000-0 0    04
2 43342   0.0566  93.6184 0016521  99.4573 260.7382  1.02326553    03
CBAS 1
1 43339U 18036A   18117.06594243 0.00000000  00000-0  00000-0 0    04
2 43339   0.0547  66.4252 0005088 125.6918 234.3082  1.02201461    07
EAGLE
1 43340U 18036B   18117.06441580 0.00000000  00000-0  00000-0 0    01
2 43340   0.0596  64.2796 0003439 116.7817 243.2183  1.02131320    06
CBAS 1 r
1 43341U 18036C   18115.04896991 0.00000000  00000-0  00000-0 0    08
2 43341   0.0551  79.6538 0417135 135.0141  46.6646  1.08312763    05
ORS 5
1 42921U 17050A   18110.27452846 0.00000000  00000-0  00000-0 0    03
2 42921   0.0238 169.0721 0001130 355.4093   4.5880 14.90503959    03
OTV 5
1 42932U 17052A   18103.08332516 0.00000000  00000-0  00000-0 0    09
2 42932  54.4848 135.8907 0003000 305.5090  54.4909 15.71190888    02
SBIRS GEO 4
1 43162U 18009A   18095.79099802 0.00000000  00000-0  00000-0 0    04
2 43162   6.3252 319.8752 0006791 124.1827 235.8990  1.00270000    05

1 99992U          18078.78364164  .00000000  00000-0  00000-0 0    04
2 99992  63.3235 341.7709 0800761 110.5196 252.1151 13.49010610    00
GovSat 1
1 43178U 18013A   18046.24058247 0.00000000  00000-0  00000-0 0    00
2 43178   0.0460 254.8293 0002003  88.6147 271.3689  1.00089661    04
ISON 41700
1 90120U 17538A   18038.90025342 0.00003500  00000-0  29034-2 0    02
2 90120  24.9795  43.0554 6138627 225.9473 152.0618  3.75473860    02
USA 281
1 43145U 18005A   18016.73232019 0.00000000  00000-0  00000-0 0    07
2 43145 105.9827 142.3843 0008357 272.9216  87.0812 13.55444999    07
USA NEW
1 70003U          18014.81341543 0.00000000  00000-0  00000-0 0    06
2 70003 105.9998 139.2840 0006265 275.9232  84.0647 13.55404211    04
USA 279
1 42949U 17066A   17292.89738262 0.00000000  00000-0  00000-0 0    07
2 42949   8.1392 324.6522 2991000 180.5487 179.0910  1.48414800    08
USA 278
1 42941U 17056A   17273.78255542 -.00000501  00000-0  00000-0 0    07
2 42941  63.7330 167.0642 6776181 269.6298  90.1889  2.03452428    03
IGS Radar 5 r
1 42073U 17015B   17261.88630936 0.00002200  00000-0  87991-4 0    05
2 42073  97.1831 326.9887 0009000  83.0370 276.9629 15.25098569    01
SBIRS GEO 3 r
1 41938U 17004B   17226.86044573 0.00013236  00000-0  82035-3 0    01
2 41938  22.5837 222.2595 6958881 345.2570   1.9162  2.72948754    09
OPTSAT 3000
1 42900U 17044A   17218.89724819 0.00000000  00000-0  00000-0 0    01
2 42900  97.2000 293.1140 0002000 329.8206  30.1792 15.38252000    05
NOSS 3-8 (A)
1 42058U 17011A   17161.02542692 0.00000000  00000-0  00000-0 0    08
2 42058  63.4408 255.6854 0118000 179.5102 180.4898 13.40819991    09
NOSS 3-8 (B)
1 42065U 17011B   17161.02534667 0.00000000  00000-0  00000-0 0    09
2 42065  63.4428 255.5230 0119000 180.6735 179.3265 13.40812568    00
USA 276
1 42689U 17022A   17144.32054585 0.00000000  00000-0  00000-0 0    03
2 42689  50.0027 163.4501 0016976  69.7427 279.9823 15.56120259    05
DSN 2
1 41940U 17005A   17107.36097467 0.00000000  00000-0  00000-0 0    02
2 41940   0.0150  68.6994 0005459 225.0038 134.9962  1.00270000    05
WGS 9
1 42075U 17016A   17106.28782418 0.00000000  00000-0  00000-0 0    01
2 42075   0.1945 260.0954 2063413 295.8864 351.4187  1.00270000    05
IGS Radar 5
1 42072U 17015A   17094.87269383 0.00000000  00000-0  00000-0 0    09
2 42072  97.2241 166.8028 0009000 343.9402  16.0596 15.24523891    04
IGS Radar 5
1 42071U 17015A   17087.84954211 0.00000000  00000-0  00000-0 0    08
2 42071  97.3495 160.2996 0004000 334.5310  25.4688 15.24496229    06
SBIRS GEO 3
1 41937U 17004A   17052.51326561 0.00000000  00000-0  00000-0 0    03
2 41937   0.0150  69.4353 0001880 223.4955 136.5045  1.00270000    03
WGS 1
1 32258U 07046A   17015.41718039 0.00000000  00000-0  00000-0 0    07
2 32258   0.0448  84.9221 0003453 246.9285 113.0715  1.00270000    03
USA 250
1 39652U 14020A   17015.02195921 0.00000000  00000-0  00000-0 0    08
2 39652   2.8469 319.5183 0003455 332.8264  27.1575  1.00270006    04
WGS 8
1 41879U 16075A   16358.21353247 0.00000000  00000-0  00000-0 0    01
2 41879   3.6003  66.5855 0199996 312.3102   7.7135  1.00270000    06
ISON 61100
1 90119U 16843A   16343.42987787 0.00000142  00000-0  27797-3 0    06
2 90119  28.7816 227.6741 7149883 333.5099   3.3944  2.37617559    03
DSCS 3-9
1 23628U 95038A   16329.64722082 0.00000000  00000-0  00000-0 0    01
2 23628  10.0654  40.6121 0003516 111.6319 248.4234  1.00270000    07
UFO F8
1 25258U 98016A   16329.45184925 0.00000000  00000-0  00000-0 0    08
2 25258   7.3145  39.0000 0004809 204.6795 155.3088  1.00270000    00
FleetSatCom 7
1 17181U 86096A   16266.74107602 0.00000000  00000-0  00000-0 0    08
2 17181  14.7111   9.1749 0023795 159.0970 201.0142  1.00270000    02
Ofeq 11
1 41759U 16056A   16262.10113449 0.00138035  00000-0  24500-2 0    00
2 41759 142.5282 325.3519 0184795  50.1757 311.5128 15.32477128    00
GSSAP 4
1 41745U 16052B   16239.71428764 0.00000000  00000-0  00000-0 0    08
2 41745   0.0190 120.2942 0010000 300.4515  59.5217  1.00104330    03
GSSAP 3
1 41744U 16052A   16239.71177259 0.00000000  00000-0  00000-0 0    07
2 41744   0.0040 120.2942 0008000 355.4515   4.5217  1.00274330    01
GSSAP 3 r
1 41746U 16052C   16233.50208616 0.00000000  00000-0  00000-0 0    02
2 41746   0.8621  50.2917 0005920 265.4971  95.1165  0.98987562    06
ISON 42000
1 90118U 16730A   16230.35935117 0.00011366  00000-0  14734-2 0    03
2 90118  26.0225 336.1134 6270391 200.1137 116.5868  3.66447608    00
WGS 7
1 40746U 15036A   16212.98877681 0.00000000  00000-0  00000-0 0    05
2 40746   0.0220  79.1171 0004580 133.4127 226.5873  1.00270000    04
USA 269
1 41724U 16047A   16211.22686712 0.00000000  00000-0  00000-0 0    04
2 41724  18.6851 325.1617 6992826 178.8357 185.2363  2.21876674    06
ISON 35200
1 90117U 16707A   16207.35955033 0.00000000  00000-0  00000-0 0    01
2 90117  63.4918 231.6878 5884284 265.7474  29.0451  4.09304115    08
Mentor 7 r
1 41585U 16036B   16206.24457998 0.00000000  00000-0  00000-0 0    05
2 41585   7.6093 354.1663 0215708 185.2147 174.5696  1.04075044    02
ISON 51100
1 90116U 16697A   16197.02271432 0.00000000  00000-0  00000-0 0    04
2 90116   3.9248 273.8998 6620303 223.5734 136.4263  2.80970031    02
MUOS 5
1 41622U 16041A   16191.51826304 0.00000000  00000-0  00000-0 0    07
2 41622   9.8109 324.2407 3211951 178.9804 181.9317  1.52735617    02
MUOS 5 r
1 41623U 16041B   16177.33159821 0.00000000  00000-0  00000-0 0    05
2 41623  19.1010 322.8427 6092785 178.1097 181.9138  2.09515519    06
Mentor 7
1 41584U 16036A   16167.96105997  .00000000  00000-0  00000-0 0    08
2 41584   7.5055 353.7008 0046333  41.2140 319.1375  1.00195548    05
ISON 63700
1 90115U 16612A   16112.02101776 0.00001839  00000-0  54920-1 0    02
2 90115   5.5953  41.9123 7102035   6.8645 358.9886  2.26165691    07
ISON 144402
1 90100U 14798A   16094.39398747 0.00000000  00000-0  00000-0 0    02
2 90100  10.4683  39.0470 0206359 312.6121  45.6776  0.99706215    02
ISON 49200
1 90114U 16591A   16091.06076050 0.00017500  00000-0  11494-2 0    05
2 90114  63.3298 353.0721 6721151 268.3028  19.9584  3.04943579    01
FIA Radar 4
1 41334U 16010A   16042.12521527 0.00000000  00000-0  00000-0 0    04
2 41334 122.9820 357.1748 0001000   0.6468 359.3531 13.46533695    05
ISON 32000
1 90113U 16535A   16035.80645369 0.00022000  00000-0  12036-2 0    01
2 90113  25.7492 289.9636 5615007  15.7724 356.3818  4.69385969    01
USA 250 r
1 39653U 14020B   15290.00159653 0.00000000  00000-0  00000-0 0    02
2 39653  10.9881 261.7799 4853383 283.0181  28.8166  1.86026107    05
NOSS 3-7 (R)
1 40981U 15058R   15286.05573889 0.00000000  00000-0  00000-0 0    01
2 40981  63.4353 281.3310 0124989 179.3855 180.6145 13.40311788    08
NOSS 3-7 (R)
1 40979U 15058R   15282.84751800 0.00000000  00000-0  00000-0 0    02
2 40979  63.4350 289.4959 0126213 179.4631 180.5064 13.40312760    05
NOSS 3-7 (A)
1 40964U 15058A   15282.84746112 0.00000000  00000-0  00000-0 0    06
2 40964  63.4349 289.4988 0126612 179.0834 180.9166 13.40379204    06
NOSS 3-7 r
1 40978U 15058Q   15282.12325980 0.00000000  00000-0  00000-0 0    08
2 40978  64.7704 289.8805 0219834 284.4137  73.2663 14.78941654    00
MUOS 1
1 38093U 12009A   15278.37810261 0.00000000  00000-0  00000-0 0    09
2 38093   3.8500 332.8334 0059750 180.1670 179.8329  1.00270000    05
MUOS 4
1 40887U 15044A   15259.40453690 0.00000000  00000-0  00000-0 0    07
2 40887   5.0430 328.7371 0001000 140.0000 220.0000  1.00270000    02
ISON 63200
1 90099U 14792C   15253.75900097 0.00000300  00000-0  56680-3 0    07
2 90099  28.8113 318.4133 7231764 181.9215 173.1245  2.27903210    01
MUOS 3 r
1 40375U 15002B   15253.71322792 0.00000000  00000-0  00000-0 0    09
2 40375  18.5498 286.0940 6083604 254.8778  33.8705  2.08929700    06
GSSAP 2
1 40100U 14043B   15253.07958315 0.00000000  00000-0  00000-0 0    04
2 40100   0.0581   5.0168 0002000 174.4752 185.4978  1.00270000    05
MUOS 4 r
1 40888U 15044B   15251.42355530 0.00000000  00000-0  00000-0 0    06
2 40888  19.0850 326.7373 6080000 179.7900 180.2000  2.08796000    04
MUOS 3
1 40374U 15002A   15250.99325315 0.00000000  00000-0  00000-0 0    09
2 40374   4.8951 328.7601 0058632 178.7298 181.2702  1.00270000    01
Elisa 99450
1 99450U 15720B   15224.89694404 0.00000500  00000-0  94309-4 0    07
2 99450  98.0802 297.9838 0005267 322.6356  37.3643 14.64577524    00
Essaim 99449
1 99449U 15720A   15220.86620070 0.00000000  00000-0  00000-0 0    02
2 99449  98.2702 294.2724 0001261 247.1290 112.8708 14.63067828    02
Sicral 2
1 40614U 15022B   15182.22211214 0.00000000  00000-0  00000-0 0    00
2 40614   0.0470  35.8635 0001000 157.7440 202.2560  1.00270000    04
LightSail-A
1 40661U 15025L   15159.06218063 0.02648498  00000-0  67226-1 0    05
2 40661  55.0136 260.3261 0243391 227.2228 135.1229 15.14087982    04
NOSS 6 P/S
1 14691U 84012B   15157.92364826 0.00030000  00000-0  49029-2 0    07
2 14691  63.2063 101.5270 0508509  92.9460 267.6227 14.10126907    09
OTV 4
1 40651U 15025A   15153.41113187 0.00000000  00000-0  00000-0 0    03
2 40651  38.0218 255.0262 0009791   9.5017 350.5955 15.85156401    08
CLIO ISON 143663
1 40208U 14055A   15133.18330974 0.00000000  00000-0  00000-0 0    00
2 40208   0.0440  44.7375 0011405 315.6929  44.2191  1.00270000    01
IGS 9
1 40381U 15004A   15116.92747674 0.00000000  00000-0  00000-0 0    09
2 40381  97.4995 188.9595 0006379  74.2520 285.7480 15.27764783    05
ISON 62200
1 90112U 15614A   15114.81795662 0.00000505  00000-0  12336-2 0    06
2 90112   5.6630 163.6807 7185228 168.6699 227.4237  2.32366316    03
IGS 9 r
1 40382U 15004B   15111.89449586 0.00015000  00000-0  56321-3 0    08
2 40382  97.4877 184.9834 0012862 106.5662 253.4337 15.27156191    08
ISON 60601
1 90111U 15607A   15107.89871643 0.00001000  00000-0  13050-1 0    05
2 90111  10.6896  53.7508 7057175 341.8331   1.9904  2.37655470    09
NOSS 1-7 PS
1 16592U 86014B   15105.10231904 0.00001500  00000-0  68791-3 0    07
2 16592  63.3160  10.7169 0540649  97.1787 262.8213 13.64013249    02
IGS Opt 5
1 40538U 15015A   15095.89867762 0.00000000  00000-0  00000-0 0    08
2 40538  97.5000 168.3467 0003000 146.0759 213.9239 15.17587539    03
IGS Opt 5 r
1 40539U 15015B   15091.90843653 0.00012500  00000-0  42829-3 0    06
2 40539  97.2694 164.0290 0054534 346.4875  12.9436 15.28766798    04
GSSAP 1
1 40099U 14043A   15075.15735905 0.00000000  00000-0  00000-0 0    00
2 40099   0.1049 100.4273 0004545 328.1692  31.8192  1.00139487    01
JAWSAT
1 26065U 00004E   15054.09556197 0.00000000  00000-0  00000-0 0    03
2 26065 100.2306 253.2202 0037976 171.2560 188.7439 14.36618221    07
WGS 4 r
1 38071U 12003B   15053.99435768 0.00000008  00000-0  19809-3 0    01
2 38071  22.0934 101.0464 8200411 170.2769 234.7800  1.15520163    03
ANGELS
1 40101U 14043C   15047.61959938 0.00000000  00000-0  00000-0 0    08
2 40101   0.2861   6.6268 0010708 280.8296  79.0674  0.98918407    03
ISON 20100
1 90110U 15545A   15045.04292572 0.00000901  00000-0  94884-3 0    06
2 90110  63.6259 336.8399 3953340 298.9469  27.1475  7.14307836    04
CLIO r
1 40209U 14055B   15044.70114305 0.00000000  00000-0  00000-0 0    08
2 40209  20.6201 168.7594 4753934 201.2359 129.5757  1.84619428    04
ISON 54102
1 90109U 15523A   15029.57905560 0.00005800  00000-0  46958-2 0    09
2 90109  10.4211 317.0590 6904054 338.7542   2.8690  2.72178709    03
USA 259
1 40344U 14081A   14350.26041667 0.00000000  00000-0  00000-0 0    07
2 40344  62.8515 212.5009 6775547 266.7169 108.1768  2.03519385    08
ISON 47601
1 90108U 14845A   14345.78155113 0.00130000  00000-0  18587-2 0    06
2 90108  26.1828  35.4683 6439223 226.4502  57.9456  3.48344430    05
ISON  59700
1 90106U 14844A   14344.93775833 0.00001037  00000-0  11372-2 0    08
2 90106   1.7288 107.8123 7133426  65.2861 350.7480  2.42060426    03
ISON 68600
1 90107U 14844B   14344.56595229 0.00000000  00000-0  00000-0 0    00
2 90107   5.9532  78.8720 6279691 158.2173 249.7319  2.09703600    04
ISON 64800
1 90103U 14820A   14329.50798226 0.00000000  00000-0  00000-0 0    09
2 90103  63.9343 196.8175 6524807 260.9662  25.3221  2.21892500    07
ISON 81600
1 90105U 14824A   14324.50091989 0.00000000  00000-0  00000-0 0    02
2 90105  20.9494 158.0091 5607648 162.1109 197.8891  1.76312000    08
ISON 37600
1 90097U 14792A   14324.22065240 0.00000000  00000-0  00000-0 0    06
2 90097   4.5567 104.4372 5658746  77.6790 337.3548  3.99368491    07
WGS 6
1 39222U 13041A   14320.90546396 0.00000000  00000-0  00000-0 0    02
2 39222   0.0150 270.3700 0001000 210.8973 125.3893  1.00270000    07
ISON 64800
1 70283U          14320.49456760 0.00000000  00000-0  00000-0 0    04
2 70283  63.9317 197.8354 6523714 261.0625  25.2811  2.21894000    03
ISON 59501
1 70184U          14317.09270388 0.00000000  00000-0  00000-0 0    06
2 70184  10.7796 334.9840 6996980 142.3878 218.4241  2.41793291    03
ISON 37600
1 70036U          14314.68605640 0.00000000  00000-0  00000-0 0    07
2 70036   4.5600 111.6760 5662209  63.5018 295.3748  3.99208818    04
ISON 144402
1 71171U          14313.95572657 0.00000000  00000-0  00000-0 0    08
2 71171   9.6970  44.0880 0220655 176.3869 183.8703  0.99723473    08
ISON 77400
1 90104U 14735A   14311.60381953 0.00000000  00000-0  00000-0 0    02
2 90104  11.4240 296.6895 4859083 216.4018  97.9237  1.86027107    01
Trumpet 2
1 23609U 95034A   14301.66813519 0.00000046  00000-0  00000-0 0    02
2 23609  63.4451 255.3436 6933054 268.9888  17.8027  2.00608837    01
Trumpet 1
1 23097U 94026A   14301.56449094 0.00000264  00000-0  00000-0 0    07
2 23097  64.0600 221.8444 6447805 273.5901  20.0715  2.00616570    07
Unknown 140823
1 99424U 14735B   14291.72435747 0.00000000  00000-0  00000-0 0    07
2 99424  11.4451 298.6308 4870003 212.6338 104.7926  1.86027107    00
USA 200 r
1 32707U 08010B   14290.43525739 0.00000400  00000-0  11525-2 0    05
2 32707  63.5611  67.2355 7356940 250.7816  21.9391  2.11366141    04
Unknown 141017
1 90096U 14790A   14290.32717842 0.00001216  00000-0  00000-0 0    08
2 90096  63.5519 329.1665 7278087 274.7780  13.2468  2.04981299    09
Unknown 141011
1 90095U 14784A   14284.61299940 0.00000000  00000-0  00000-0 0    09
2 90095  63.1946 229.8784 6997432 265.8347  18.5519  2.38687000    02
Unknown141003B
1 90094U 14776B   14283.36769152 0.00000000  00000-0  00000-0 0    07
2 90094  24.2135 306.5490 5129031 168.6285 210.0496  1.94990330    05
Unknown141003A
1 90093U 14576A   14276.74591757 0.00003373  00000-0  13244-0 0    02
2 90093   3.8791 318.8159 7248031 272.6482  14.1023  2.08151131    05
GPS 70 r
1 39742U 14026B   14262.60191257 0.00000000  00000-0  00000-0 0    07
2 39742  54.9489 140.2888 0043262 346.5976  13.4024  1.95489795    05
Unknown 140824
1 90092U 14735A   14242.95503590 0.00000000  00000-0  00000-0 0    02
2 90092  15.1286   9.3792 0089042  56.2201 304.3016  0.99531895    00

1 99999U 14736A   14236.81819308  .00000000  00000-0  00000-0 0    03
2 99999  15.2395   9.6197 1034942 127.6835 195.0717  1.21226772    09
USA 58
1 20562U 90031C   14217.03818759 0.00000000  00000-0  00000-0 0    07
2 20562  89.7939 335.9734 0001983 235.6846 124.3153 14.59434657    08
GSSAP r
1 40102U 14043D   14213.29410491 0.00000000  00000-0  00000-0 0    03
2 40102   0.4803 306.6432 0009502   3.3829 356.6355  0.98907512    03
Trumpet 3
1 25034U 97068A   14203.73894686 -.00001155  00000-0  00000-0 0    01
2 25034  63.2760 326.0072 6828663 284.1592  13.6226  2.00610838    08
Unknown 140607
1 99224U 14658A   14158.05870913 0.00000000  00000-0  00000-0 0    05
2 99224  63.2984  59.7602 0649136  78.7674 281.2326 13.86763379    04
USA 252
1 39751U 14027A   14144.03015972 0.00000000  00000-0  00000-0 0    03
2 39751  20.6956 263.7634 7074111 178.0121  96.0401  2.24037956    05
Unk
1 99406U 14602A   14109.95853628 0.00001600  00000-0  51820-3 0    01
2 99406  63.2995  78.8961 0737856  80.7875 279.2125 13.43060588    00
Ofeq 10
1 39650U 14019A   14106.07914909 0.00070000  00000-0  19916-2 0    07
2 39650 140.9470 242.8354 0162954 123.9544 237.6834 15.22939887    00
DMSP F19
1 39630U 14015A   14095.71497852 0.00000000  00000-0  00000-0 0    07
2 39630  98.8700 111.1816 0009822 285.0801  74.9198 14.13792356    08
DMSP F19
1 72910U          14093.66263531 0.00000000  00000-0  00000-0 0    01
2 72910  98.8700 109.1454 0009822 295.9013  64.2057 14.13825356    09
Unknown 140303
1 99099U 14562A   14064.88053226 0.00910809  00000-0  25276-3 0    08
2 99099  21.5237 107.5170 4930158 197.9328 135.9812  5.98574706    08
Unknown140221E
1 99096U 14552E   14061.90935522 0.00002026  00000-0  23663-2 0    02
2 99096  63.2369  22.5189 7322465 270.6871 330.9436  2.18857743    04
SBIRS GEO 2
1 39120U 13011A   14055.40411744 0.00000000  00000-0  00000-0 0    04
2 39120   5.2166 320.3571 0003941 228.4966 131.4792  1.00270000    09
WGS 3 r
1 36109U 09068B   14053.01007272 0.00000000  00000-0  00000-0 0    07
2 36109  24.6755   3.9597 8162708 292.0115 296.9198  1.18380000    00
WGS 6 r
1 39223U 13041B   14052.84022525 0.00000000  00000-0  00000-0 0    01
2 39223  23.8998 115.7659 8281093 230.7244  23.7049  1.09740000    03
Essaim 14547A
1 99091U 14547A   14052.77390121 0.00000000  00000-0  00000-0 0    04
2 99091  98.3277  94.6861 0003236  86.3983 273.6664 14.78500946    09
Essaim 14544A
1 99221U 14544A   14052.75428076 0.00000500  00000-0  71134-4 0    00
2 99221  98.3503  87.4467 0000628   9.4204 350.5794 14.76943147    03
MUOS 2
1 39206U 13036A   14019.85792968 0.00000000  00000-0  00000-0 0    05
2 39206   4.9431 328.0286 0057037 359.3804   0.6127  1.00270000    02
WGS 5 r
1 39169U 13024B   14005.12611120 0.00000000  00000-0  00000-0 0    05
2 39169  25.4033  39.8556 8235545 234.2618  26.0965  1.08104166    06
Unknown 140103
1 99086U 14503A   14003.81258995 0.00000000  00000-0  00000-0 0    03
2 99086  11.2184  44.0392 0005179 296.4846  63.4155  1.00270000    08
Unknown131229B
1 99085U 13863B   14003.80411560 0.00000000  00000-0  00000-0 0    08
2 99085   0.1713  81.5121 0003189 144.4001 215.5999  1.00376385    01
AEHF 3
1 39256U 13050A   13362.30780316 0.00000000  00000-0  00000-0 0    00
2 39256   4.8845 304.1814 0345112 179.9578 336.7311  0.99205949    00
Unknown 131224
1 99155U 13858A   13358.26109368 0.00000000  00000-0  00000-0 0    02
2 99155   4.9439 303.9995 0480203 182.4544 328.4754  0.99493725    04
FIA Radar 3 r
1 39475U 13072P   13345.20809444 0.00000000  00000-0  00000-0 0    01
2 39475 120.4582 244.1978 0286404 342.8858  17.1141 14.61081031    09
FIA Radar 3
1 39462U 13072A   13344.12994719 0.00000000  00000-0  00000-0 0    07
2 39462 123.0082 236.8229 0012759 307.2947  52.7053 13.47778591    04
Unknown 131121
1 90091U 13825A   13341.95489258 -.00001113  00000-0  00000-0 0    00
2 90091  62.6309  14.1059 7269922 270.7699  14.5171  2.00560139    09
FIA Radar 3
1 78817U 13072A   13341.53383309 0.00000000  00000-0  00000-0 0    03
2 78817 122.9957 228.6601 0014502 298.6008  61.3992 13.47753224    06
FIA Radar 3 r
1 78820U 13072P   13341.44424121 0.00000000  00000-0  00000-0 0    05
2 78820 120.4883 230.9287 0276875 339.4109  19.5967 14.61190032    02
Unknown 131120
1 99079U 13825A   13335.71953869 0.00002800  00000-0  12676-2 0    03
2 99079  28.4923   5.3250 7184644 218.6097  57.5864  2.38762084    01
WGS 5
1 39168U 13024A   13317.25465817 0.00000000  00000-0  00000-0 0    03
2 39168   0.0350  91.4850 0002000 180.0000 180.0000  1.00270000    04
Unknown 131021
1 99075U 13794A   13296.82824030 0.00000000  00000-0  00000-0 0    05
2 99075   2.9784 314.0976 0002683 308.1391  51.8406  1.00270000    00
Unknown 131012
1 99218U 13785A   13295.97738589 0.00001000  00000-0  13232-3 0    07
2 99218  98.3481 327.0658 0000500  25.7826  20.4778 14.80017172    09
MUOS 2 r
1 39207U 13036B   13282.13634292 0.00000000  00000-0  00000-0 0    03
2 39207  18.6538 310.2079 6155019 204.8400 104.9075  2.09952624    06
Unknown 131001
1 99070U 13774A   13278.79023945 0.00000000  00000-0  00000-0 0    00
2 99070   5.2985 319.5957 0005819 266.2397  93.7006  1.00270000    08
Unknown 130929
1 99069U 13772A   13273.75224919 0.00000138  00000-0  00000-0 0    03
2 99069  64.0272 258.5812 6654330 276.1244  16.1326  2.00614452    03
SAR Lupe3or5
1 99068U 13770A   13271.79560051 0.00000000  00000-0  00000-0 0    00
2 99068  98.1752 308.5386 0003602   0.3543 359.6456 15.27557102    08
Unknown 130725
1 99212U 13706A   13248.88429323 0.00000200  00000-0  51524-3 0    02
2 99212  27.9553 235.4646 7168230 359.9657 359.9774  2.34151114    03
USA 245
1 39232U 13043A   13241.13429432 0.00025000  00000-0  21639-3 0    03
2 39232  97.8732 304.6187 0528234 192.3915 167.7736 14.80683858    08
Sicral 1
1 26694U 01005A   13214.20728829 0.00000000  00000-0  00000-0 0    05
2 26694   4.8244  62.5072 0004226 116.2035 243.8645  1.00270000    07
SBIRS GEO 2 r
1 39121U 13011B   13206.14342780 0.00002225  00000-0  10769-2 0    02
2 39121  21.9142 267.5106 7256990 274.7545   7.9326  2.29613940    09
Unknown 130704
1 99210U 13685A   13199.96892181 0.00001150  00000-0  92963-3 0    03
2 99210  63.3059 191.0441 0405425 116.8184 243.1816 13.57884301    03
Unk 130404
1 99208U 13594A   13196.65856129 0.00430000  00000-0  27787-2 0    05
2 99208  20.2342 280.8648 5993339 159.4367 242.7508  4.16919351    02
Unknown 130608
1 99064U 13659A   13171.34611362 0.00000000  00000-0  00000-0 0    04
2 99064   4.7115  62.4659 0004148   8.0943 351.9292  1.00427101    08
Object 10062X
1 99207U 10062X   13155.25626156 0.00000000  00000-0  00000-0 0    07
2 99207  72.0259 255.5944 0020000 337.6259  66.2618 14.77170909    09
Sicral 1B
1 34810U 09020A   13141.79392576 0.00000000  00000-0  00000-0 0    08
2 34810   0.1028  82.0406 0005392  27.2992  68.0656  1.00270000    00
Unknown 130428
1 99143U 13618A   13129.37386472 0.00000000  00000-0  00000-0 0    04
2 99143  97.1534 250.2405 0005719 244.0786 172.8044 15.46470036    00
IGS 8 Db D
1 39064U 13002D   13124.04353781 0.00028336  00000-0  12595-2 0    09
2 39064  97.6067 245.9456 0025211 326.1169  33.2972 15.21264961    06
IGS 8 Db E
1 39065U 13002E   13122.03288079 0.00041000  00000-0  17432-2 0    02
2 39065  97.4942 243.7765 0002996 272.3416  87.6582 15.23070998    05
IGS 8 Db F
1 39066U 13002F   13122.01706688 0.00020500  00000-0  63916-3 0    03
2 39066  97.5213 244.8534 0048335 174.3422 185.6576 15.32084308    01
IGS 8B
1 39062U 13002B   13122.01510889 0.00049000  00000-0  20498-2 0    08
2 39062  97.4912 243.9044 0001752 178.8640 181.1358 15.23623977    01
IGS 8A
1 39061U 13002A   13121.97756745 0.00000000  00000-0  00000-0 0    06
2 39061  97.4279 242.7329 0003000 129.2047 230.7951 15.17643370    00
IGS 8 r
1 39063U 13002C   13120.00020091 0.00002800  00000-0  22745-3 0    02
2 39063  97.6606 239.5592 0016692 194.3256 165.6742 14.99562829    02
99048
1 99048U          13118.00841701 0.00036500  00000-0  15440-2 0    08
2 99048  97.4912 239.8975 0001752 142.9081 217.0918 15.23247676    08
99050
1 99050U          13117.99836650 0.00002000  00000-0  16259-3 0    03
2 99050  97.6576 237.5699 0015692 204.0608 155.9391 14.99547427    04
99049
1 99049U          13116.98765167 0.00012800  00000-0  39776-3 0    01
2 99049  97.5373 239.8673 0054335 195.1828 164.8171 15.31880471    05
99047
1 99047U 13595B   13115.98761716 0.00023000  00000-0  99272-3 0    08
2 99047  97.4882 237.6643 0002996 353.5123   6.4875 15.22560744    04
99046
1 99046U          13115.97760364 0.00000090  00000-0  44798-5 0    00
2 99046  97.4409 236.8971 0003000 170.0754 189.9244 15.17645170    00
Pleiades 1B
1 39019U 12068A   13089.90057915 0.00000000  00000-0  00000-0 0    09
2 39019  98.2085 166.2336 0001000   0.0000  57.5005 14.58553606    09
AEHF 2
1 38254U 12019A   13058.76513473 0.00000000  00000-0  00000-0 0    01
2 38254   3.1694 313.1993 0006856 338.0255  21.9467  1.00270000    06
OTV 3
1 39025U 12071A   12348.51262355 0.00015000  00000-0  10571-3 0    03
2 39025  43.4959 127.0411 0012422 332.5991  27.4004 15.73041223    09
Muos r
1 38094U 12009B   12319.41029435 0.00000000  00000-0  00000-0 0    03
2 38094  18.0821 266.9340 6213463 273.3248  22.1483  2.11710260    00
Unknown 120530
1 90090U 12651A   12310.78408745 0.00000452  00000-0  21111-3 0    06
2 90090  63.3240 192.1322 0669187  50.1557 309.7753 13.41089659    08
NOSS 3-6 (P)
1 38773U 12048P   12263.16874014 0.00000000  00000-0  00000-0 0    01
2 38773  63.4386  28.3553 0127283 180.8086 179.1914 13.40519112    09
NOSS 3-6 (P)
1 79603U 12048P   12261.45298345 0.00000000  00000-0  00000-0 0    05
2 79603  63.4386  32.7196 0127283 180.8197 179.1803 13.40494112    00
NOSS 3-6 r
1 38770U 12048N   12260.17511925 0.00068242  00000-0  54452-2 0    09
2 38770  64.6150  33.5493 0214551 293.7818  66.2662 14.83675255    06
NOSS 3-6 (P)
1 38771U 12048P   12260.11029461 0.00000000  00000-0  00000-0 0    09
2 38771  63.4386  36.1322 0127783 180.4284 179.5715 13.40441112    06
NOSS 3-6 (A)
1 38758U 12048A   12260.11019213 0.00000000  00000-0  00000-0 0    08
2 38758  63.4386  36.1321 0127783 180.8284 179.1715 13.40501612    02
DSP F15 Cover
1 96143U 90095E   12252.35954447 0.00000000  00000-0  00000-0 0    02
2 96143  14.1584  29.3941 0086528 131.4655 229.2929  0.99285540    07
STPSat 2
1 37222U 10062A   12232.94555056 0.00000320  00000-0  45657-4 0    03
2 37222  71.9651 172.3631 0018000 196.5016 163.4984 14.76589784    01
Unknown 120723
1 90089U 12705A   12220.02431339 0.00023389  00000-0  95520-3 0    05
2 90089  25.6421 131.8563 7019888 177.3023 191.5831  2.65684060    04
USA 237 r
1 38529U 12034B   12201.16401249 0.00000000  00000-0  00000-0 0    03
2 38529   3.5829 299.0775 0197347 196.4398 163.3022  1.03226679    09
USA 236
1 38466U 12033A   12201.02221518 0.00000000  00000-0  00000-0 0    06
2 38466   4.9082 274.5087 0005000 175.6170 184.6492  1.00273922    07
Elisa W23
1 38009U 11076C   12199.27393649 0.00000200  00000-0  39016-4 0    08
2 38009  98.1819 272.9488 0001486 102.4077 257.7291 14.63066078    02
Elisa W11
1 38007U 11076A   12199.27377032 0.00000200  00000-0  38982-4 0    05
2 38007  98.1589 272.9104 0010685 143.9017 216.2908 14.63069705    09
IGS 7A
1 37954U 11075A   12198.09926076 0.00000000  00000-0  00000-0 0    05
2 37954  97.5197 269.8670 0010529 310.4530  49.5784 15.17603387    07
USA 237
1 38528U 12034A   12197.78746808 0.00000000  00000-0  00000-0 0    07
2 38528   3.5184 299.5137 0050303 310.7722  48.7936  0.99909995    04
Elisa E12
1 38010U 11076D   12196.19638590 0.00000256  00000-0  49937-4 0    09
2 38010  98.1819 272.4855 0001493 112.0474 248.0886 14.63069469    03
Elisa E24
1 38008U 11076B   12196.19622887 0.00000257  00000-0  50093-4 0    04
2 38008  98.1589 272.4606 0010692 121.7407 238.4838 14.63068126    01
Unknown 120530
1 99015U 12651A   12169.31301658 0.00001300  00000-0  15136-3 0    01
2 99015  98.1973 111.5061 0010333 298.8158  61.1840 14.85307145    07
FIA Radar 2
1 38109U 12014A   12097.24217641 0.00000000  00000-0  00000-0 0    08
2 38109 122.9914 224.3990 0009283 284.9437  75.1044 13.45794928    02
FIA Radar 2
1 79701U 12014A   12095.23647071 0.00000000  00000-0  00000-0 0    02
2 79701 123.0192 218.2476 0016360 317.0451  42.9234 13.45650207    08
SAR Lupe 3or5
1 70002U 08036A   12090.39115859 0.00004000  00000-0  14855-3 0    02
2 70002  98.1320  66.2797 0014999 187.0872 172.9126 15.27484427    08
IGS 7A r
1 37955U 11075B   12082.87443186 0.00005600  00000-0  21802-3 0    07
2 37955  97.4180 155.2591 0027670  42.0496 317.9502 15.25664235    01
WGS 4
1 38070U 12003A   12063.65981561  .00000000  00000-0  00000-0 0    00
2 38070   0.0541 274.4832 0549995 184.8475 175.1525  1.00180033    00
GeoLite
1 26770U 01020A   11349.95867440 0.00000000  00000-0  00000-0 0    09
2 26770   2.7931  51.9289 0018954 357.4321   2.5909  0.98843605    00
RadioAstron
1 37755U 11037A   11343.96971181 0.00000000  00000-0  00000-0 0    06
2 37755  74.9673 308.4764 8612669 316.2510   3.7923  0.11953359    03
Unknown 111101
1 90088U 11805A   11309.06268930 0.00195000  00000-0  52546-3 0    01
2 90088  24.0237  18.9989 6960288 186.2817 155.5822  2.76778641    07
IGS 6A
1 37813U 11050A   11272.94111109 0.00000619  00000-0  60047-4 0    08
2 37813  97.6931  31.0490 0002497 291.0367  69.0585 14.92733754    04
IGS 6A r
1 37814U 11050B   11272.85741330 0.00000455  00000-0  39984-4 0    08
2 37814  97.6540  31.0070 0019112   2.8113 357.3213 14.96485088    03
Canyon 6
1 07963U 75055A   11221.82705374 0.00000000  00000-0  00000-0 0    03
2 07963  20.8266 336.9310 1291601 251.9194  93.6187  1.00161775    09
Mentor 5
1 37232U 10063A   11213.60548493 0.00000000  00000-0  00000-0 0    07
2 37232   6.4453 263.4062 0035159 336.2384  23.5997  1.00277406    08
Mentor 1
1 23567U 95022A   11212.97783719 0.00000000  00000-0  00000-0 0    02
2 23567  10.0373  68.5437 0121312  21.6476 338.8609  1.00273447    03
Canyon 7
1 10016U 77038A   11210.94542121 0.00000000  00000-0  00000-0 0    09
2 10016  11.2708   6.6753 1234411 353.9543   4.6847  1.00230764    06
SAR Lupe 3
1 32283U 07053A   11203.31709745 0.00001300  00000-0  48521-4 0    07
2 32283  98.1293 149.8191 0005557 188.9386 171.0613 15.27414496    02
ORS 1
1 37728U 11029A   11183.10603239 0.00006852  00000-0  10000-3 0    06
2 37728  40.0000 125.8626 0009897 284.9325  75.0391 15.54660733    04
Unknown 110623
1 90087U 11674A   11177.96275344 0.00000100  00000-0  00000-0 0    04
2 90087  26.7578 123.5582 7347027 137.0879 222.9119  2.00830285    06

1 99994U 11674A   11176.13115708 0.00000000  00000-0  00000-0 0    03
2 99994  26.2366 130.3455 6105404 148.2332 313.8428  4.01632994    07

1 99995U 11674A   11176.12751252 0.00000000  00000-0  00000-0 0    02
2 99995  26.4366 129.5536 5483915 149.7695 295.2928  5.02022994    05

1 99996U 11674A   11176.12140414 0.00000000  00000-0  00000-0 0    04
2 99996  26.5366 129.1682 4902726 151.7450 268.2928  6.02405994    07

1 99993U 11674A   11176.08369001 0.00000000  00000-0  00000-0 0    04
2 99993  26.1166 131.3682 6781610 145.7450 274.2928  3.01235994    02
FAST 2
1 37380U 10062M   11155.19780612 0.00000130  00000-0  18663-4 0    02
2 37380  71.9889  68.1025 0017205 296.9102  63.0897 14.76335623    04
DSP F13 r
1 18584U 87097B   11154.57379289 0.00000000  00000-0  00000-0 0    02
2 18584  12.4519  22.5409 0005636  88.0849 271.9918  1.01240645    09
SBIRS GEO 1
1 37481U 11019A   11154.45872124 0.00000000  00000-0  00000-0 0    03
2 37481   6.4830 319.9777 0001300 143.8525 216.1475  1.00270000    07
DSCS 3-6
1 22009U 92037A   11148.79132668 0.00000000  00000-0  00000-0 0    04
2 22009   8.2184  58.4688 0002761 263.7119  96.2686  1.00452281    02
2010-062 UNID
1 78701U 10062X   11120.10505598 0.00000400  00000-0  57405-4 0    02
2 78701  71.9574 145.3579 0017000 355.7358   4.2641 14.76352554    05
NOSS 3-5 (B)
1 37391U 11014B   11110.75281113 0.00000000  00000-0  00000-0 0    05
2 37391  63.4047 338.3792 0127413 180.4827 179.5173 13.39341423    08
NOSS 3-5 (B)
1 79937U 11014B   11110.75281113 0.00000000  00000-0  00000-0 0    07
2 79937  63.4047 338.3792 0127413 180.4827 179.5173 13.39341423    00
NOSS 3-5 (B)
1 37387U 11014B   11109.03548857 0.00000000  00000-0  00000-0 0    00
2 37387  63.4167 342.7331 0128413 180.9847 179.0943 13.39251023    08
NOSS 3-5 (A)
1 37386U 11014A   11107.10689160 0.00000000  00000-0  00000-0 0    08
2 37386  63.4238 346.0103 0128090 179.8530 180.1470 13.34368235    04
USA 227
1 37377U 11011A   11098.49400289 0.00000000  00000-0  00000-0 0    09
2 37377   4.9151 343.8190 0001043  15.4298 344.5885  1.00270000    01
SAR Lupe 5
1 33244U 08036A   11098.02690432 0.00001200  00000-0  44740-4 0    07
2 33244  98.1680  35.7157 0016319 346.4017  13.5981 15.27334359    02
Ekran 5
1 11890U 80060A   11087.45687140 0.00000000  00000-0  00000-0 0    08
2 11890  14.3967 346.5687 0018148  37.1907 322.9468  1.00283477    05
SAR Lupe 4
1 32750U 08014A   11077.19385881 0.00002300  00000-0  86015-4 0    01
2 32750  98.1839 246.5658 0017316  10.7656 349.2342 15.27216362    08
OTV 2
1 37375U 11010A   11073.71563114 0.00007980  00000-0  39958-4 0    03
2 37375  42.8585 237.5217 0018908 356.6571   3.2257 15.80528259    09
SAR Lupe 1
1 29658U 06060A   11070.12965775 0.00001600  00000-0  59766-4 0    00
2 29658  98.1769 237.9832 0015428 236.5024 123.4974 15.27285723    00
HAPS r
1 37229U 10062H   11062.78081731 0.00000150  00000-0  21631-4 0    03
2 37229  71.9874 271.7369 0017000 117.2072 242.7927 14.76146611    04
Ofeq 9
1 36608U 10031A   11062.70774936 0.00002800  00000-0  95322-4 0    09
2 36608 141.7685   4.6085 0165306 274.0977  85.9015 15.17341025    04
FAST 1
1 37227U 10062F   11057.21878648 0.00000076  00000-0  00000-0 0    04
2 37227  71.9724 283.9188 0016148 131.5768 228.6802 14.76395401    01
DSCS 3-7
1 22719U 93046A   11055.93398839 0.00000000  00000-0  00000-0 0    00
2 22719   6.8249  63.1383 0005558 302.6320  57.3264  0.99006663    01
DSP F15 r3
1 20932U 90095D   11055.88946838 0.00000000  00000-0  00000-0 0    08
2 20932  12.9195  36.6967 0072353 302.6888  56.6275  0.99915351    00
NanoSail-D
1 37361U 10062L   11053.18324610 0.00045000  00000-0  60443-2 0    05
2 37361  71.9732 292.6219 0023333  99.1733 261.2301 14.79073791    01
TecSAR
1 32476U 08002A   11049.05080476 0.00003000  00000-0  68921-4 0    03
2 32476  41.0264  26.3829 0077736 116.4231 243.5763 15.38583238    05
RAX
1 37223U 10062B   11047.27696737 0.00000210  00000-0  00000-0 0    02
2 37223  71.9744 305.5778 0020243 156.1195 204.0952 14.77236729    05
O/OREOS
1 37224U 10062C   11043.43618410 0.00000219  00000-0  00000-0 0    08
2 37224  71.9758 314.1598 0019424 162.0076 198.1778 14.76892599    01
Ofeq 7
1 31601U 07025A   11041.01942323 0.00001650  00000-0  74097-4 0    02
2 31601 141.7491 116.2780 0091897 282.8335  77.1657 15.16476805    06
SAR Lupe 2
1 31797U 07030A   11039.78731563 0.00001500  00000-0  56307-4 0    05
2 31797  98.1084 273.2461 0009814 290.2418  69.7581 15.27193401    01
Ofeq 5
1 27434U 02025A   11039.78070777 0.00001700  00000-0  11165-3 0    04
2 27434 143.4626 301.4704 0026074 352.9413   7.0579 15.06461984    05
USA 224
1 37348U 11002A   11023.83162841 0.00008800  00000-0  50440-4 0    05
2 37348  97.9000 139.0368 0563457 277.2512  82.7487 14.79617543    01
STPSAT 2 r
1 37228U 10062G   11022.74152336 0.00000000  00000-0  00000-0 0    01
2 37228  71.9734 359.9669 0010000 194.6902 165.3098 14.76000000    04
FASTSAT
1 37225U 10062D   11014.05373812 0.00000060  00000-0  85753-5 0    06
2 37225  71.9620  19.0237 0019965 207.0682 152.9317 14.76490180    01
Rhyolite 3
1 10508U 77114A   11008.74855715 0.00000000  00000-0  00000-0 0    09
2 10508  19.0226 351.8409 0020259 213.5990 146.2844  1.00289870    07
DSP F9 r2
1 12371U 81025C   11008.65766043 0.00000000  00000-0  00000-0 0    00
2 12371  14.0354 356.4170 0050104 158.5486 201.6742  1.01328057    05
DSP F7 Cover
1 09856U 77007D   11008.58424549 0.00000000  00000-0  00000-0 0    03
2 09856  13.5082 335.8751 0280774 338.3763  20.7070  1.00562393    07
Canyon 3
1 04510U 70069A   11008.55443638 0.00000000  00000-0  00000-0 0    03
2 04510  17.7662 292.6247 0869018 244.5444 106.2216  1.00243524    01
Canyon 5
1 06317U 72101A   11008.54416051 0.00000000  00000-0  00000-0 0    07
2 06317  20.0936 334.3235 1324186 283.8601  61.7469  1.00221794    04
Vortex 1 r
1 10942U 78058B   11005.78215515 0.00000000  00000-0  00000-0 0    08
2 10942   4.1414  29.4797 1477379  17.7038 346.9449  0.99630870    05
Mercury 1 r
1 23247U 94054B   11005.77075415 0.00000000  00000-0  00000-0 0    06
2 23247   9.6741  38.3676 0122820 209.8320 149.4835  0.99588186    07
Mentor 2 r
1 25337U 98029B   11005.72886267 0.00000000  00000-0  00000-0 0    04
2 25337   9.9060  10.2291 0050559  44.2198 316.2053  1.00269978    05
Mercury 2 r
1 25349U 96026B   11005.59407392 0.00000000  00000-0  00000-0 0    05
2 25349   8.9424   5.3872 0468483 275.3341  79.3626  0.99563671    04
Vortex 4 r2
1 14677U 84009C   11005.54089154 0.00000000  00000-0  00000-0 0    02
2 14677   7.9119 358.7188 0973592   1.3230 358.9621  0.99442161    08
DSP F2 r
1 05205U 71039B   11005.53095150 0.00000000  00000-0  00000-0 0    00
2 05205   9.7468 321.1078 0032465 323.0265  36.7621  1.00414555    01
DSP F3 r
1 05854U 72010B   11005.43225509 0.00000000  00000-0  00000-0 0    02
2 05854  10.3342 324.0683 0063364 357.7199   2.2635  1.00673084    03
Rhyolite 2
1 06380U 73013A   11005.41574207 0.00000000  00000-0  00000-0 0    01
2 06380  11.3440 327.9270 0021169 109.4382 250.8027  1.00264876    06
Rhyolite 1
1 04418U 70046A   11005.40772169 0.00000000  00000-0  00000-0 0    00
2 04418   9.3696 318.3178 0011896  57.3581 302.7686  1.00251116    06
SBSS 1
1 37168U 10048A   11005.27810923 0.00000150  00000-0  20380-4 0    03
2 37168  98.0154 231.9758 0002500  27.7937 332.2061 14.78900661    00
WGS F3
1 36108U 09068A   11005.02353592 0.00000000  00000-0  00000-0 0    00
2 36108   0.0026 100.5215 0004229  21.4235 338.6194  1.00270000    00
Canyon 1 r
1 27785U 68063B   11002.69552116 0.00000000  00000-0  00000-0 0    04
2 27785  14.4213 342.8047 1095502  87.5165 284.9585  1.01773464    02
AEHF 1 r
1 36869U 10039B   11002.48493822 0.00000200  00000-0  17139-3 0    08
2 36869  21.0322 277.4191 7885107 240.4423  21.6745  1.55587975    07
DSCS 3-5 r2
1 21877U 92006C   11002.20253967 0.00000000  00000-0  00000-0 0    03
2 21877  10.2452  22.1501 0648096 278.9656  73.7723  1.10779583    08
DSP F18 r3
1 24740U 97008D   11002.19332744 0.00000000  00000-0  00000-0 0    01
2 24740   9.1536  57.5687 0025271  30.7570 329.4030  0.99490376    08
Vortex 6 r2
1 19983U 89035C   11002.10744857 0.00000000  00000-0  00000-0 0    08
2 19983   6.8705  13.8944 1025712 297.2868  52.6590  0.99428067    09
DSP F20 r3
1 26359U 00024D   11002.08177633 0.00000000  00000-0  00000-0 0    03
2 26359   6.6356  59.5431 0009443  13.1812 346.8556  0.99699248    09
DSCS 3-13 r2
1 27693U 03008C   11002.07825266 0.00000000  00000-0  00000-0 0    01
2 27693   7.0061  62.1537 0004810  43.4018 316.6682  1.01116496    01
DSP F21 r3
1 26883U 01033D   11002.06214617 0.00000000  00000-0  00000-0 0    08
2 26883   5.5905  61.5661 0006246 248.1881 111.7576  0.99888268    04
DSCS 3-2
1 16116U 85092B   11002.02934994 0.00000000  00000-0  00000-0 0    06
2 16116  12.5337  40.0812 0005992 320.9918  38.9771  0.98986082    05
DSCS 3-3
1 16117U 85092C   11002.02521120 0.00000000  00000-0  00000-0 0    00
2 16117  12.3047  41.8378 0003933  42.3089 317.7264  0.99321201    07
DSP F16 r2
1 21807U 91080D   11002.01305000 0.00000000  00000-0  00000-0 0    02
2 21807  12.3044  39.1416 0019700 201.2681 158.6621  1.01277059    06
Vortex 3 r2
1 12932U 81107C   11002.00572033 0.00000000  00000-0  00000-0 0    01
2 12932   7.7252 351.7751 0964737  28.0144 336.8851  0.99598272    01
DSP F4 r
1 11940U 73040B   11001.96298108 0.00000000  00000-0  00000-0 0    08
2 11940  12.1271 327.7115 0028171 267.2785  92.4171  0.99556133    08
DSCS 2-15 r2
1 20205U 89069D   11001.90521396 0.00000000  00000-0  00000-0 0    02
2 20205  13.3566  21.9145 0065448 194.7902 165.0577  1.01242289    06
DSCS 3-2 r2
1 16119U 85092E   11001.86215215 0.00000000  00000-0  00000-0 0    08
2 16119  14.5985  12.3049 0060958  24.0546 336.2479  1.01082978    00
Magnum 1 r2
1 15545U 85010D   11001.85767895 0.00000000  00000-0  00000-0 0    05
2 15545  16.9666  17.2390 0024810 132.4417 227.7805  1.00811075    09
DSP F7 r2
1 09855U 77007C   11001.84593791 0.00000000  00000-0  00000-0 0    00
2 09855  13.6141 337.9179 0012657 249.6341 110.2420  1.00250495    00
Mentor 5 r
1 37233U 10063B   11001.68520661 0.00000000  00000-0  00000-0 0    08
2 37233   6.9953 266.8852 0220851 140.0576 221.6006  1.04031629    03
Milstar 4 r
1 26716U 01009B   11001.24367419 0.00000000  00000-0  00000-0 0    04
2 26716   6.2596  56.2099 0017452 348.0440  11.9266  1.00468874    08
AEHF 1
1 36868U 10039A   11001.20444344 0.00000000  00000-0  00000-0 0    05
2 36868  10.5699 284.5336 5611939 219.6849 343.0000  1.23768400    08
DSCS 3-5
1 21873U 92006A   11001.19697838 0.00000000  00000-0  00000-0 0    05
2 21873   9.5882  56.0610 0003064 235.6309 124.3521  0.99032102    08
FIA Radar 1
1 37162U 10046A   10365.68598779 0.00000000  00000-0  00000-0 0    07
2 37162 122.9944  52.8158 0005000 102.1579 257.8421 13.41452514    00
Unknown 101208
1 99991U 10742A   10345.69214651 0.00000000  00000-0  00000-0 0    01
2 99991   0.0668  12.3384 0002903 145.4049 214.6472  1.00404895    08
Unknown 101019
1 90086U 10792A   10293.40767197  .01192144  00000-0  74211-3 0    01
2 90086  26.3644  16.4586 2095633 273.6405  94.8735 11.57122578    00
SBSS 1 r
1 37169U 10048B   10273.80860640 0.00000000  00000-0  00000-0 0    07
2 37169  98.0000 135.5082 0008000  44.9343 315.0656 15.10164263    09
DSP F18 Cover
1 27680U 97008E   10273.49042398 0.00000000  00000-0  00000-0 0    02
2 27680   8.8526  57.3275 0148455  25.4214 335.3707  0.99519054    08
Canyon 5 r
1 06318U 72101B   10239.11847001 0.00000000  00000-0  00000-0 0    09
2 06318  19.3177 331.9150 1282609 333.9047  20.1530  1.02309316    03
Helios 2B
1 36124U 09073A   10239.07282622 0.00000000  00000-0  00000-0 0    02
2 36124  98.1220 173.9535 0003000  68.3825 291.7697 14.63824605    08
Helios 2B r
1 36125U 09073B   10237.02021578 0.00000102  00000-0  15029-4 0    01
2 36125  98.0401 175.1666 0040933   2.2543 357.8842 14.74859328    06
DSCS 3-14 r2
1 27877U 03040C   10224.65989715 0.00000000  00000-0  00000-0 0    00
2 27877   6.2418  64.9054 0017404 154.3367 205.7796  1.00749133    01
DSCS 2-15
1 20202U 89069A   10220.38055627 0.00000000  00000-0  00000-0 0    02
2 20202  13.2973  29.8468 0011478  95.6547 264.4849  0.98613270    00
DSP F20 Cover
1 28156U 00024E   10219.54841720 0.00000000  00000-0  00000-0 0    05
2 28156   6.5337  61.3504 0236099 220.3280 137.8983  0.99704389    01
DSP F17 r3
1 23438U 94084D   10214.62345466 0.00000000  00000-0  00000-0 0    02
2 23438  10.4068  51.4622 0004460 329.9707  30.0084  1.01180360    07
DSP F22 r3
1 28161U 04004D   10194.17389645 0.00000000  00000-0  00000-0 0    07
2 28161   2.9900  66.4668 0004829 255.6058 104.3420  0.99812515    04
Canyon 7 r2?
1 15422U 77038C   10191.67764865 0.00000000  00000-0  00000-0 0    03
2 15422  10.5096   7.4978 1472221  32.1671 336.0317  1.02333119    07
DSP F14 r3
1 20069U 89046D   10191.67588769 0.00000000  00000-0  00000-0 0    05
2 20069  11.9707  33.5320 0046338 215.8917 143.8083  1.01304169    09
DSP F12 r
1 15454U 84129B   10191.65064750 0.00000000  00000-0  00000-0 0    01
2 15454  14.4335  15.4732 0004626   5.5645 354.4527  1.01159923    07
DSCS 3-8 r
1 22916U 93074B   10186.49616209 0.00000000  00000-0  00000-0 0    09
2 22916  12.6587  38.0691 0008701 275.5345  84.3780  0.99249324    07
DSP F8 r2
1 11436U 79053C   10186.45711167 0.00000000  00000-0  00000-0 0    00
2 11436  14.9061 354.8558 0054070 136.1219 224.3289  0.99437731    08
Mentor 1 r
1 23568U 95022B   10170.81502268 0.00000000  00000-0  00000-0 0    06
2 23568  10.9214  79.3584 0011176 188.1995 171.8066  1.00559637    01
Canyon 3 r
1 27787U 70069B   10170.36389558 0.00000000  00000-0  00000-0 0    02
2 27787  16.6678 285.4757 1264801 311.7085  38.1336  1.01706096    06
DSCS 3-12 r2
1 26577U 00065C   10163.77567858 0.00000000  00000-0  00000-0 0    05
2 26577   8.5277  58.6293 0050772 116.0677 244.4680  1.01179455    01
DSCS 3-7 r2
1 22738U 93046C   10163.69616747 0.00000000  00000-0  00000-0 0    04
2 22738  12.1950  35.6416 0079059 336.3576  23.2839  1.02122163    05
DSCS 3-6 r2
1 22011U 92037C   10163.59337545 0.00000000  00000-0  00000-0 0    02
2 22011  12.5364  31.4773 0025384 280.7688  78.9577  1.01646308    07
Vortex 2 r2
1 11560U 79086C   10163.55770832 0.00000000  00000-0  00000-0 0    04
2 11560   6.9789 352.5593 1298164  38.3842 330.1857  0.99674722    08
Canyon 2 r
1 27786U 69036B   10163.00168806 0.00000000  00000-0  00000-0 0    07
2 27786   4.1309 116.8438 0969700  46.5985 321.0825  1.03853244    09
DSCS 3-9 r2
1 23648U 95038C   10155.58771574 0.00000000  00000-0  00000-0 0    07
2 23648  11.5522  44.2078 0015192 165.7499 194.3050  1.01266427    06
Magnum 2 r2
1 20357U 89090D   10154.45931574 0.00000000  00000-0  00000-0 0    05
2 20357  14.8484  49.1417 0320218 295.8635  60.8843  0.99522508    07
Rhyolite 4
1 10787U 78038A   10154.31636398 0.00000000  00000-0  00000-0 0    02
2 10787  10.9051 348.3458 0009044 140.3101 219.7682  1.00463900    01
OTV-1
1 36514U 10015A   10143.39927771 0.00001500  00000-0  23465-4 0    03
2 36514  39.9923 169.4404 0015696 208.7785 151.2208 15.52671083    05
Canyon 2
1 03889U 69036A   10123.85895608 0.00000000  00000-0  00000-0 0    01
2 03889   2.1240 154.2443 0941406 326.6324  27.8335  1.00368037    08
Canyon 1
1 03334U 68063A   10123.40009905 0.00000000  00000-0  00000-0 0    03
2 03334  15.3109 349.9077 0930186  62.8827 306.3130  0.99244310    01
Milstar 1 r
1 22989U 94009B   10122.91088427 0.00000000  00000-0  00000-0 0    00
2 22989   6.7942 104.0615 0009881  53.7279 306.3753  1.00595740    04
Milstar 2 r
1 23713U 95060B   10122.81724332 0.00000000  00000-0  00000-0 0    05
2 23713   9.3135  57.1125 0033938  48.2190 312.0826  1.00597069    09
DSP F5 r2
1 08516U 75118C   10122.76384947 0.00000000  00000-0  00000-0 0    09
2 08516  13.0312 335.7526 0014254  26.1951 333.8889  1.00537189    09
DSCS 3-11 r2
1 26054U 00001C   10122.76136962 0.00000000  00000-0  00000-0 0    07
2 26054   8.9107  57.9538 0015899 210.1349 149.7857  1.01179694    02
DSCS 3-4
1 20203U 89069B   10122.71740873 0.00000000  00000-0  00000-0 0    05
2 20203   8.6420  60.0767 0006037 253.8998 106.0458  0.99114991    02
DSP F10 r
1 13089U 82019B   10122.67457340 0.00000000  00000-0  00000-0 0    06
2 13089  14.2542   2.0245 0015158 336.6330  23.3102  1.01259794    07
DSP F11 r
1 14931U 84037B   10122.64908370 0.00000000  00000-0  00000-0 0    06
2 14931  14.0201   9.2730 0027160 163.5370 196.5700  1.01165890    09
Canyon 6 r
1 07964U 75055B   10122.60104465 0.00000000  00000-0  00000-0 0    03
2 07964  20.3166 338.6817 1312086 297.0392  50.1742  1.02091197    04
DSP F6 r2
1 08918U 76059C   10122.52944398 0.00000000  00000-0  00000-0 0    06
2 08918  13.3364 337.3635 0012322  64.7732 295.3666  1.00562065    09
Helios 1A
1 23605U 95033A   10097.11731295 0.00000000  00000-0 -14523-3 0    04
2 23605  98.1038  33.6397 0002499 104.4270 255.5729 14.63844028    05
Essaim 3
1 28496U 04049E   10091.34788348 0.00000020  00000-0  33248-5 0    02
2 28496  98.3032  64.3619 0009789  59.9821 300.0177 14.70164628    09
Essaim 4
1 28497U 04049F   10091.34742217 0.00000020  00000-0  33229-5 0    07
2 28497  98.3046  64.4188 0012914  55.6010 304.3989 14.70165884    07
Helios 2A
1 28492U 04049A   10087.08779818 0.00000000  00000-0  39215-3 0    02
2 28492  98.1112  24.1031 0001504 132.1829 227.8169 14.63842742    02
IGS 5A
1 36104U 09066A   10079.86836021 0.00000000  00000-0  00000-0 0    09
2 36104  97.8129 153.1807 0001000   4.2748 355.7250 14.93388774    04
Essaim 2
1 28495U 04049D   10078.14406910 0.00000010  00000-0  16636-5 0    07
2 28495  98.2815  46.0980 0004617  92.5141 267.4857 14.70158428    09
Essaim 1
1 28494U 04049C   10078.14361211 0.00000090  00000-0  14966-4 0    01
2 28494  98.3005  46.2035 0003783  98.9520 261.0479 14.70180409    01
IGS 5A r
1 36105U 09066B   10072.86172539 0.00000803  00000-0  65607-4 0    09
2 36105  97.6507 144.6866 0043019  43.1528 317.3053 14.98708889    00
Unknown 100202
1 96041U 96541A   10033.50617528 0.00000000  00000-0  00000-0 0    09
2 96041  14.1070 359.5358 0044918 231.0381 128.5729  1.00224248    04
STSS Demo r
1 35939U 09052C   09337.06590627 0.00243000  00000-0  24874-3 0    02
2 35939  59.6643 210.1386 0654620 289.3240  70.6760 14.79164575    01
DMSP F18
1 35951U 09057A   09292.07608029 0.00000000  00000-0  00000-0 0    01
2 35951  98.9336 326.0730 0010024 295.5843  64.4156 14.12545987    09
Unknown 091017
1 90085U 09790A   09292.01577191  .00000000  00000-0  00000+0 0    02
2 90085  25.3410  12.0524 6961417 187.5746 150.4904  2.73606553    05
STSS Demo 1
1 35937U 09052A   09271.78649380 0.00000000  00000-0  00000-0 0    00
2 35937  57.9904  82.1205 0013359 323.1724  36.8701 12.79625382    04
STSS Demo 2
1 35938U 09052B   09270.77181345 0.00000000  00000-0  00000-0 0    01
2 35938  57.9922  84.8776 0007193 297.9025  62.0975 12.79020022    02
PAN USA 207
1 35815U 09047A   09263.63810579 0.00000000  00000-0  00000-0 0    04
2 35815   0.0533 274.1181 0003730  63.1363 286.5617  1.00270000    09
Unknown 9O0DC57
1 90084U 09710A   09244.64721928 0.00000000  00000-0  00000-0 0    09
2 90084  41.8425 356.8152 7570669 190.1322 133.6279  0.44275082    08
Unknown 090720
1 96044U 96544A   09201.96545740 0.00000000  00000-0  00000-0 0    06
2 96044  14.3745   1.0263 0053649 298.1383  61.3327  1.00336036    06
WGS F2 USA 204
1 34713U 09017A   09141.35810465 0.00000000  00000-0  00000-0 0    05
2 34713   0.0915 245.2475 0004000  23.0065 336.9754  1.00317756    01
STSS-ATRR r
1 34904U 09023B   09130.12101793 0.00480000  00000-0  68103-2 0    06
2 34904 112.7678 228.4968 0309489 290.6359  68.9977 15.16282514    01
STSS-ATRR
1 34903U 09023A   09127.88488268 0.00000000  00000-0  00000-0 0    07
2 34903  98.9513 226.1446 0007714 220.9054 139.0944 14.06067719    03
Unknown 090420
1 96033U 96533A   09110.63239993 0.00000000  00000-0  00000-0 0    05
2 96033  13.9432  18.2202 0057566   3.7749 356.2802  1.01080704    06
DSCS 3-1
1 13637U 82106B   09086.57587271 0.00000000  00000-0  00000-0 0    05
2 13637  12.8363  29.5893 0014471  24.5147 335.5789  0.97822440    07
Unknown 090222
1 96151U 96651A   09061.26213363 0.00000000  00000-0  00000-0 0    03
2 96151   2.8722 110.6502 0007024 173.3904 186.6327  1.00271000    04
Unknown 090220
1 96067U 96567A   09061.15788108 0.00000000  00000-0  00000-0 0    08
2 96067   5.0689  67.0894 0005392 347.9646  12.0344  0.99703848    02
Unknown 090220
1 96135U 96635A   09061.02229998 0.00000000  00000-0  00000-0 0    03
2 96135  12.8109  29.8292 0032281  35.1712 324.9230  0.97828162    00
Unknown 090222
1 96153U 96653A   09052.88999143 0.00000000  00000-0  00000-0 0    03
2 96153   2.2340  34.5244 0255638 191.4014 168.0085  0.95121995    07
Unknown 090215
1 96002U 96502A   09046.73183017 0.00000000  00000-0  00000-0 0    01
2 96002   4.9583  72.2162 0020199 137.2073 222.9621  1.00738930    07
Unknown 090215
1 96127U 96627A   09046.66695530 0.00000000  00000-0  00000-0 0    07
2 96127   7.9678  64.6583 0006567 199.8241 160.1623  0.99036302    05
USA 202
1 33490U 09001A   09046.30328249 0.00000000  00000-0  00000-0 0    02
2 33490   2.8915 337.5826 0024996 190.8227 169.2084  1.00130520    01
Unknown 090214
1 96087U 96587A   09044.89525712 0.00000000  00000-0  00000-0 0    04
2 96087  12.3775  34.9456 0011397  90.8437 269.2989  0.98605782    00
Intelsat 3F7
1 04376U 70032A   09043.49870956 0.00000000  00000-0  00000-0 0    09
2 04376  10.3292 321.4666 0004451 284.3056  75.6570  1.00281526    04
Unknown 090123
1 29241U 06024B   09043.13578394 0.00000000  00000-0  00000-0 0    09
2 29241   0.0930 268.8956 0001722  79.0749 280.9526  1.00600180    02
Unknown 000405
1 90083U 09526A   09041.61082110 -.00000043  00000-0  00000-0 0    06
2 90083  63.9971 336.2962 7172924 278.6846  12.8961  2.00612597    00
MiTEx NRL U/S USA 189
1 29242U 06024C   09034.74688303 0.00000000  00000-0  00000-0 0    09
2 29242   2.0973  77.0138 0001706 153.1240 206.8902  1.04004000    04
Unknown 090128
1 96047U 96547A   09028.63032334 0.00000000  00000-0  00000-0 0    03
2 96047  16.0654  24.9673 0024383 122.3340 237.9143  1.00815221    05
USA 202 r
1 33491U 09001B   09023.53756835 0.00000000  00000-0  00000-0 0    09
2 33491   2.9844 334.0731 0246632  12.9987 347.6968  0.96057197    06
Unknown 090123
1 91141U 09523A   09023.27786493 0.00000000  00000-0  00000-0 0    08
2 91141   0.1465 277.1835 0001045 113.3174 246.6826  1.00566977    02
Unknown 090104
1 96104U 96604A   09004.46041200 0.00000000  00000-0  00000-0 0    08
2 96104   0.0050  84.9509 0001000 173.8940 186.1060  1.00270000    07
Milstar 4 USA 157
1 26715U 01009A   09004.42726648 0.00000000  00000-0  00000-0 0    06
2 26715   2.8864  50.0981 0001000 205.9101 154.0822  1.00270000    05
UFO F4 USA 108
1 23467U 95003A   09004.33456456 0.00000000  00000-0  00000-0 0    01
2 23467   4.7731  47.6367 0006000 221.7153 138.2785  1.00270000    00
Unknown 090103
1 96005U 96505A   09003.90602467 0.00000000  00000-0  00000-0 0    04
2 96005   5.1196  67.1652 0239868 214.2204 144.2231  0.99716871    07
Unknown 090103
1 96144U 96644A   09003.50600162 0.00000000  00000-0  00000-0 0    08
2 96144  11.6034 330.3545 0008228 236.2970 123.6365  0.99765774    03
DSP F18 USA 130
1 24737U 97008A   09002.49706237 0.00000000  00000-0  00000-0 0    09
2 24737   7.3728  66.6604 0000496 258.3498 101.6521  1.00270000    04
Unknown 081224
1 91132U 08859A   08363.85226720 0.00000000  00000-0  00000-0 0    01
2 91132   0.1956  67.6540 0002292 197.1192 162.8932  0.99949073    03
Unknown 081120
1 96077U 96577A   08325.85800704 0.00000000  00000-0  00000-0 0    06
2 96077  10.7161  50.2040 0004288 267.6007  92.3622  0.99322423    06
Unknown 081118
1 96020U 96520A   08323.70749973 0.00000000  00000-0  00000-0 0    04
2 96020   6.1839  11.7069 1043244 284.6255  64.0509  0.99426703    04
Unknown 050415
1 90075U 05605D   08320.72470970 0.00000000  00000-0  00000-0 0    09
2 90075   6.9467 351.1744 1279846  28.4373 338.0007  0.99676604    02
Unknown 081022
1 96084U 96584A   08302.94748073 0.00000000  00000-0  00000-0 0    07
2 96084  11.4187  44.2975 0009022 232.7367 127.1884  0.99248500    03
Unknown 081022
1 96137U 96637A   08301.95162800 0.00000000  00000-0  00000-0 0    03
2 96137  14.4606 353.6224 0013800 171.0170 189.0197  1.00329687    04
Unknown 081021
1 96076U 96576A   08301.85393732 0.00000000  00000-0  00000-0 0    06
2 96076   7.7179 351.1443 0960487  12.7427 349.4839  0.99600970    09
UFO F3 USA 104
1 23132U 94035A   08297.50944147 0.00000000  00000-0  00000-0 0    05
2 23132   5.7058  54.4158 0004958 209.2649 150.7194  1.00332118    09
Unknown 081022
1 96080U 96580A   08296.85496185 0.00000000  00000-0  00000-0 0    05
2 96080  10.8549  39.4838 0048453 198.5563 161.2785  1.01304710    05
Unknown 081022
1 96010U 96510A   08296.77355037 0.00000000  00000-0  00000-0 0    02
2 96010   2.9182  15.4739 1442354  15.8083 348.2633  0.99618090    08
Unknown 081021
1 96015U 96515A   08294.41062971 0.00000000  00000-0  00000-0 0    03
2 96015   7.5933  65.0334 0020417 222.4009 137.4533  1.01182968    06
Unknown 081021
1 96019U 96519A   08294.35649347 0.00000000  00000-0  00000-0 0    02
2 96019   8.9308  59.2425 0003407 253.9774 105.9972  1.01182092    00
Unknown 081021
1 96081U 96581A   08294.25232584 0.00000000  00000-0  00000-0 0    00
2 96081  11.2450  45.7120 0077703 275.0046  84.1210  0.99906934    01
Unknown 081021
1 96095U 96595A   08294.18251905 0.00000000  00000-0  00000-0 0    00
2 96095  13.5257  14.1909 0031472 154.1760 205.9936  1.01164980    03
Unknown 081019
1 96059U 96559A   08293.81340330 0.00000000  00000-0  00000-0 0    00
2 96059  19.8602 340.0457 1275710 313.4680  36.5967  1.02314755    02
Unknown 081019
1 96088U 96588A   08292.96283639 0.00000000  00000-0  00000-0 0    07
2 96088  12.1705  29.4325 0069691 174.4171 185.6732  1.01239903    00
DSP F22 USA 176
1 28158U 04004A   08292.82125469 0.00000000  00000-0  00000-0 0    03
2 28158   1.4073  67.1299 0010770  51.8717 308.2483  1.00270000    07
FleetSatCom 1
1 10669U 78016A   08291.77004869 0.00000000  00000-0  00000-0 0    08
2 10669  15.3166 359.1225 0003786 189.3854 170.6196  0.99001209    05
Unknown 080927
1 96098U 96598A   08277.88170435 0.00000000  00000-0  00000-0 0    02
2 96098  14.5448 354.0857 0008392  26.0996 333.9717  1.00198879    02
Unknown 080927
1 96071U 96571A   08277.13303548 0.00000000  00000-0  00000-0 0    05
2 96071   7.1630  67.9520 0024000  10.2236 349.8262  0.99498363    06
Unknown 080930
1 96145U 96645A   08277.05017666 0.00000000  00000-0  00000-0 0    03
2 96145  18.0058 294.7849 1246854 290.1798  56.8594  1.01708854    09
DSCS 3-11 USA 148
1 26052U 00001A   08274.63870388 0.00000000  00000-0  00000-0 0    03
2 26052   0.0382 104.3705 0019368 128.4344 231.7569  1.00270000    06
Unknown 060326
1 90074U 06585B   08271.90138811 0.00000000  00000-0  00000-0 0    06
2 90074  14.7436   0.1190 0055910 121.5737 238.9855  0.99437823    09
DSCS 3-10 USA 135
1 25019U 97065A   08271.55834468 0.00000000  00000-0  00000-0 0    08
2 25019   2.4599  77.9836 0006877 344.1851  15.7946  1.00270000    04
Unknown 080926
1 96025U 96525A   08270.96309031 0.00000000  00000-0  00000-0 0    00
2 96025   7.6389 358.4193 0975000 344.5655  12.6679  0.99444016    01
Unknown 080926
1 96061U 96561A   08270.24471407 0.00000000  00000-0  00000-0 0    08
2 96061   3.5773  70.0911 0009000 203.4988 156.4722  0.99905530    07
Unknown 080920
1 96103U 96603A   08264.92829330 0.00000000  00000-0  00000-0 0    02
2 96103  20.6123 345.7805 1312167 279.6206  65.8356  1.02087560    02
Unknown 080920
1 96132U 96632A   08264.17193122 0.00000000  00000-0  00000-0 0    06
2 96132   9.1149  30.8425 0655443 252.7264 100.0146  1.10773811    05
SDS 3F3 AQUILA USA 162
1 26948U 01046A   08263.73192277 0.00000000  00000-0  00000-0 0    00
2 26948   2.4912 118.5410 0007986 166.4257 193.6102  1.00270000    02
Vortex 3
1 12930U 81107A   08256.17620449 0.00000000  00000-0  00000-0 0    09
2 12930   7.2702 358.1588 0937156 264.7361  84.5292  1.00196143    08
Unknown 080911
1 96029U 96529A   08255.93880784 0.00000000  00000-0  00000-0 0    07
2 96029  10.9471  31.4307 0004599 107.2756 252.7868  1.01242586    00
Unknown 080911
1 96094U 96594A   08255.89252771 0.00000000  00000-0  00000-0 0    05
2 96094  12.9829   8.6765 0696377  99.3668 268.5795  0.93696548    04
Unknown 080911
1 96054U 96554A   08255.87927744 0.00000000  00000-0  00000-0 0    04
2 96054  13.6860 342.2216 0010151  46.8918 313.2051  1.00552224    00
DSP F17 USA 107
1 23435U 94084A   08255.32935064 0.00000000  00000-0  00000-0 0    07
2 23435   8.9380  59.9535 0027817  16.4882 343.6267  1.00270000    08
Unknown 080911
1 96050U 96550A   08255.02233796 0.00000000  00000-0  00000-0 0    00
2 96050  13.4137 340.5469 0012896   2.9643 357.0553  1.00524592    08
Vortex 6 USA 37
1 19976U 89035A   08254.92982997 0.00000000  00000-0  00000-0 0    04
2 19976   5.6687  10.8577 0957500 218.1037 134.7383  1.00270000    01
Vortex 4
1 14675U 84009A   08254.00611331 0.00000000  00000-0  00000-0 0    01
2 14675   7.6479 356.0872 1075535 282.8383  65.3832  1.00270000    06
Unknown 080818
1 90082U 08731A   08238.36640692 0.00000000  00000-0  00000-0 0    08
2 90082  64.1000  87.1676 6500000 260.3687  14.3594  2.00600500    09
Adv Orion 3 USA 171
1 27937U 03041A   08224.27606074 0.00000000  00000-0  00000-0 0    07
2 27937   3.1995 154.8696 0046919 127.2981 233.1479  1.00270000    04
Magnum 2 USA 48
1 20355U 89090B   08224.02190055 0.00000000  00000-0  00000-0 0    02
2 20355  13.2472  57.6713 0261787 276.6026  80.4301  1.00270000    01
UFO F6 USA 114
1 23696U 95057A   08217.55569624 0.00000000  00000-0  00000-0 0    05
2 23696   4.0529  48.3448 0005132 245.6947 114.2602  1.00270000    03
Unknown 080803
1 96093U 96593A   08215.28997837 0.00000000  00000-0  00000-0 0    01
2 96093  10.8328 326.6735 0038054 304.7776  54.8767  1.00434895    08
UFO F5 USA 111
1 23589U 95027A   08184.63450042 0.00000000  00000-0  00000-0 0    08
2 23589   4.7805  49.0518 0005954 237.0213 122.9306  1.00270000    04
Unknown 080507
1 90081U 08628A   08137.07694771 -.00000848  00000-0  00000-0 0    06
2 90081  62.8133 214.3140 6808239 276.9167  16.0088  2.00573006    08
Milstar 1 USA 99
1 22988U 94009A   08126.87731780 0.00000000  00000-0  00000-0 0    02
2 22988   5.6904 141.0599 0010295 273.5206  86.3680  1.00270000    07
Unknown 080501
1 96078U 96078A   08122.54349808 0.00000000  00000-0  00000-0 0    07
2 96078  10.3461  49.7125 0024235 179.3373 180.6780  1.01274257    03
Unknown 080309
1 96082U 96582A   08122.37762015 0.00000000  00000-0  00000-0 0    02
2 96082   9.8078  12.1480 1460039  12.0363 351.1134  1.02326597    06
Unknown 080331
1 90080U 08591A   08114.89787183 0.00000000  00000-0  00000-0 0    08
2 90080  63.3561 169.3958 4938027 292.2456  67.7544  5.52688554    08
DSP F7
1 09803U 77007A   08114.44862472 0.00000000  00000-0  00000-0 0    05
2 09803  14.7754 349.6778 0080086 225.1035 134.2558  0.97530801    05
USA 137
1 25148U 98005A   08105.89470532 0.00001391  00000-0  00000-0 0    01
2 25148  64.2508 175.7217 7145485 255.3197  21.8969  2.00594627    03
USA 179
1 28384U 04034A   08105.57031399 0.00001405  00000-0  00000-0 0    00
2 28384  63.1359  58.7451 7286209 271.8820  14.0454  2.00613917    03
Mercury 2
1 23855U 96026A   08105.54515348 0.00000000  00000-0  00000-0 0    08
2 23855   7.3324  15.8034 0501103 176.6202 183.7537  1.00270000    03
Unknown 080304
1 96070U 96570A   08101.00872691 0.00000000  00000-0  00000-0 0    05
2 96070   2.4964 215.8648 0985398 253.4186  95.5602  1.00368077    03
Unknown 080304
1 96062U 96562A   08100.71696554 0.00000000  00000-0  00000-0 0    06
2 96062   0.9611  64.2132 0006150 222.5308 137.4336  0.99820367    05
Unknown 080409
1 96085U 96585A   08100.69892177 0.00000000  00000-0  00000-0 0    02
2 96085  11.1264  39.3093 0026169 252.4349 107.2911  1.01639621    05
Unknown 050301
1 96028U 96528A   08100.58033098 0.00000000  00000-0  00000-0 0    03
2 96028  10.7066  43.8128 0082752 306.4114  52.8402  1.02110481    05
Unknown 050227
1 96055U 96555A   08100.44212720 0.00000000  00000-0  00000-0 0    09
2 96055  14.6318 351.7468 1080958  59.5789 310.6741  1.01770851    00
DSP F12 USA 7
1 15453U 84129A   08100.43318721 0.00000000  00000-0  00000-0 0    03
2 15453  13.8988  24.8677 0003138 220.2659 139.7229  0.98851744    01
Unknown 080408
1 96022U 96522A   08099.61641082 0.00000000  00000-0  00000-0 0    00
2 96022   9.8980  52.9806 0016445 145.2103 214.9094  1.01259033    04
Mercury 1 USA 105
1 23223U 94054A   08098.72636622 0.00000000  00000-0  00000-0 0    06
2 23223   4.5914  70.5938 0046177 192.8760 167.0182  1.00270000    02
Unknown 080229
1 96027U 96527A   08098.39106334 0.00000000  00000-0  00000-0 0    00
2 96027   9.0026  13.9951 0045502  22.0048 338.2019  1.00351012    02
DSP F4
1 06691U 73040A   08098.37693189 0.00000000  00000-0  00000-0 0    00
2 06691  12.9189 334.4397 0007787 208.6198 151.3495  0.99825195    06
UFO F10 USA 146
1 25967U 99063A   08098.31161688 0.00000000  00000-0  00000-0 0    08
2 25967   1.6695  21.0153 0016980 267.7109  92.1015  1.00270000    04
Unknown 050406
1 96012U 96512A   08096.86498368 0.00000000  00000-0  00000-0 0    09
2 96012   3.0349 157.4932 0998767 349.8187   8.2990  1.03851217    02
Unknown 080229
1 96009U 96509A   08096.51286366 0.00000000  00000-0  00000-0 0    06
2 96009   2.8307  21.8640 1452369 290.8193  54.2771  1.00124605    04
DSP F5
1 08482U 75118A   08096.39725032 0.00000000  00000-0  00000-0 0    01
2 08482  14.2089 345.0303 0004294 353.2314   6.7748  0.99469072    04
Mentor 5 USA 139
1 25336U 98029A   08094.37073255 0.00000000  00000-0  00000-0 0    03
2 25336   7.5221  10.0919 0052658 214.9992 144.6642  1.00270000    07
FleetSatCom 8 USA 46
1 20253U 89077A   08090.65047492 0.00000000  00000-0  00000-0 0    00
2 20253   8.2319  47.4526 0008934 267.8261  92.0783  1.00270000    00
DSP F11
1 14930U 84037A   08090.56650089 0.00000000  00000-0  00000-0 0    08
2 14930  14.0419  18.2076 0005398 121.6795 238.3852  0.98681548    08
DSP F8
1 11397U 79053A   08090.53814964 0.00000000  00000-0  00000-0 0    05
2 11397  14.8450   2.2863 0005860 133.4590 226.6018  0.98746460    09
Vortex 1
1 10941U 78058A   08090.45486010 0.00000000  00000-0  00000-0 0    01
2 10941   7.6350 355.8693 1079347 280.1798  67.8410  1.00276373    08
DSP F16 USA 75
1 21805U 91080B   08088.72882587 0.00000000  00000-0  00000-0 0    08
2 21805  10.3736  50.6365 0011224 177.2610 182.7582  1.00270000    00
Milstar 2 USA 115
1 23712U 95060A   08086.55593646 0.00000000  00000-0  00000-0 0    03
2 23712   7.1392  68.5502 0007556 190.5725 169.4235  0.99034856    01
DSCS III B10 USA 97
1 22915U 93074A   08086.54366224 0.00000000  00000-0  00000-0 0    09
2 22915   3.9939  77.0038 0011292 232.3070 127.6000  1.00270000    07
UFO F2 USA 95
1 22787U 93056A   08086.54301158 0.00000000  00000-0  00000-0 0    01
2 22787   5.5241  48.5394 0007510 232.6485 127.2925  1.00270000    09
Unknown 050403
1 96058U 96558A   08086.39376577 0.00000000  00000-0  00000-0 0    03
2 96058  16.8187   5.3065 0036070 257.7007 101.9200  0.94327282    05
Vortex B
1 11558U 79086A   08086.38392276 0.00000000  00000-0  00000-0 0    05
2 11558   5.5456   9.1846 0949142 216.9956 136.0829  1.00270000    01
Magnum 1 USA 8
1 15543U 85010B   08086.36389186 0.00000000  00000-0  00000-0 0    01
2 15543  15.5902  26.8044 0016419 255.3492 104.4758  1.00270000    06
UFO F11 USA 174
1 28117U 03057A   08086.20850047 0.00000000  00000-0  00000-0 0    05
2 28117   2.2933 330.1377 0005154 119.9365 240.1326  1.00270000    01
DSP F3
1 05851U 62010A   08086.20613198 0.00000000  00000-0  00000-0 0    03
2 05851  12.2906 334.7519 0018455  92.8538 267.3695  1.00270317    00
DSP F2
1 05204U 71039A   08086.15413223 0.00000000  00000-0  00000-0 0    07
2 05204  10.7656 324.2652 0007863  26.4922 333.5601  1.00266212    02
SDS 3F2 USA 155
1 26635U 00080A   08084.63045670 0.00000000  00000-0  00000-0 0    04
2 26635   2.1120  39.4865 0012830 188.2367 171.7550  1.00270000    00
USA 184 r
1 29250U 06027B   08082.02503547 0.00000000  00000-0  00000-0 0    00
2 29250  62.3743 309.7803 7050465 274.7610  14.8472  2.17595297    02
USA 200
1 32706U 08010A   08080.11461581 0.00000000  00000-0  00000-0 0    03
2 32706  63.5619  40.8769 7095838 271.6711  15.8320  2.10156510    09
Unknown 080309
1 96079U 96579A   08069.69673970 0.00000000  00000-0  00000-0 0    05
2 96079  10.3707  50.9256 0007270 261.4505  98.4791  0.98989015    04
DSP F20 USA 149
1 26356U 00024A   08066.83903380 -.00000166  00000-0  00000-0 0 00009
2 26356 004.0836 070.1118 0001346 296.7291 063.8756 00.99855931000007
Unknown 050627
1 96011U 96511A   08064.64212642 0.00000000  00000-0  00000-0 0    07
2 96011   6.5684  69.5637 0053365  96.6612 263.9586  1.01183929    09
Unknown 080304
1 96039U 96539A   08064.62138421 0.00000000  00000-0  00000-0 0    07
2 96039  13.8130   8.7463 0013569 304.8716  55.0129  1.01251536    02
Unknown 080304
1 96040U 96540A   08064.58411234 0.00000000  00000-0  00000-0 0    02
2 96040  13.6458   5.0879 0052131 138.0675 222.3450  1.01329548    00
Unknown 080304
1 96049U 96549A   08064.44685507 0.00000000  00000-0  00000-0 0    01
2 96049  13.1088 335.3875 0031824 238.9238 120.7755  0.99556421    06
Unknown 080304
1 96038U 96538A   08064.40626317 0.00000000  00000-0  00000-0 0    07
2 96038  11.4764 330.8618 0065894 331.1138  28.5350  1.00659910    06
Unknown 080304
1 96060U 96560A   08064.39018608 0.00000000  00000-0  00000-0 0    03
2 96060  21.2625 351.7156 1302320 215.7121 134.8443  1.00184598    02
DSP F10
1 13086U 82019A   08064.36790061 0.00000000  00000-0  00000-0 0    01
2 13086  14.6381  12.2070 0003547 192.0567 167.9468  0.98187064    08
Unknown 050612
1 96031U 96531A   08064.36769844 0.00000000  00000-0  00000-0 0    01
2 96031   8.7338 322.6710 0224048 198.1654 161.0338  1.01903049    04
Unknown 080302
1 96032U 96532A   08062.64872644 0.00000000  00000-0  00000-0 0    05
2 96032  13.4036  23.3941 0001000 125.9163 234.1039  1.01155123    00
Unknown 080229
1 96101U 96601A   08062.49629351 0.00000000  00000-0  00000-0 0    07
2 96101  15.2567   1.0345 0004633 173.2996 186.7187  0.99004765    09
Unknown 080302
1 96102U 96602A   08062.41228654 0.00000000  00000-0  00000-0 0    02
2 96102  15.2927 356.6593 0914988  41.9981 324.6887  0.99235365    04
Unknown 080229
1 96126U 96626A   08060.78546095 0.00000000  00000-0  00000-0 0    04
2 96126   6.7593  70.1253 0007953 192.3467 167.6458  0.99119499    08
Unknown 080229
1 96006U 96506A   08060.77423349 0.00000000  00000-0  00000-0 0    07
2 96006   4.5303  75.9027 0002291 319.4726  40.5224  1.01113961    04
Unknown 080229
1 96089U 96589A   08060.53498818 0.00000000  00000-0  00000-0 0    02
2 96089   9.6611 330.6652 0185997 220.1976 138.4244  1.00699880    05
Unknown 080229
1 96091U 96591A   08060.32446549 0.00000000  00000-0  00000-0 0    09
2 96091  10.9952 352.4674 0014798 154.6112 205.4736  1.00501009    06
DSP 15 (USA 65
1 20929U 90095A   08059.52443716 0.00000000  00000-0  00000-0 0    02
2 20929  10.7927  46.6862 0007936 247.2447 112.6835  0.98391988    08
SDS 2F4 USA 125
1 23945U 96038A   08057.84877624 0.00001355  00000-0  00000-0 0    02
2 23945  64.0583 290.0161 7425694 255.4767  18.8791  2.00624178    07
MiTEX1 USA 187
1 29240U 06024A   08048.86864532 0.00000000  00000-0  00000-0 0    04
2 29240   1.2647  81.3384 0003038 154.6375 205.3903  1.04000000    08
FleetSatCom 4
1 12046U 80087A   08048.55787839 0.00000000  00000-0  00000-0 0    01
2 12046  14.3411   7.6528 0000303 216.0758 143.9342  0.98954925    09
UFO F9 USA 140
1 25501U 98058A   08047.63563391 0.00000000  00000-0  00000-0 0    01
2 25501   2.4697  28.0195 0016339 255.5349 104.2965  0.98179571    07
DSP F21 USA 159
1 26880U 01033A   08043.61029153 0.00000000  00000-0  00000-0 0    06
2 26880   3.0088  71.2071 0014726 185.6100 174.3900  1.00270000    08
DSCS 3-13 USA 167
1 27691U 03008A   08042.98221351 0.00000000  00000-0  00000-0 0    04
2 27691   0.0165 194.9748 0000100 227.3477 132.6621  1.00270000    05
DSP F13 USA 28
1 18583U 87097A   08030.76666845 0.00000000  00000-0  00000-0 0    08
2 18583  11.0074  34.8814 0021881 107.0759 253.1760  0.98386091    05
Unknown 050227
1 90071U 05558B   08030.76647236 0.00000000  00000-0  00000-0 0    05
2 90071  10.9841  34.8099 0021503 106.0371 254.2119  0.98385359    08
DSCS 3-12 USA 153
1 26575U 00065A   08029.90854415 0.00000000  00000-0  00000-0 0    04
2 26575   0.0400  83.5695 0003000 191.3683 168.6317  1.00270000    03
Unknown 071225
1 90079U 07859A   08005.82782101 0.00000000  00000-0  00000-0 0    09
2 90079  62.4173 321.5587 7063071 273.7666  86.2334  2.17597297    07
USA 198
1 32378U 07060A   07346.89533062 0.00001757  00000-0  17534-3 0    08
2 32378  60.0106 317.1239 5543977 287.1515  72.8485  4.77580618    03
USA 198 Cn r
1 32379U 07060B   07346.84730914 0.00069200  00000-0  28374-2 0    09
2 32379  60.7629 318.0027 5493200 285.4805  74.5049  4.90067973    06
Unknown 071201
1 90078U 07835A   07337.91338451 0.00000000  00000-0  00000-0 0    04
2 90078   1.0439  81.5551 0002593 163.2956 196.7247  1.04000377    07
DSP F19 USA 142
1 25669U 99017A   07324.02276106 0.00000000  00000-0  00000-0 0    07
2 25669  29.0657 245.4422 7091527 341.3340  18.6658  2.32920751    06
USA 197
1 32287U 07054A   07317.90389715 0.00000000  00000-0  00000-0 0    01
2 32287   3.9960 273.0734 0003000  60.0268 299.9732  0.99731100    03
USA 197 Cn r
1 32288U 07054B   07315.89571404 0.00000000  00000-0  00000-0 0    06
2 32288   3.9650 272.1000 0001000 154.0000 206.0000  0.99676600    02
DSP F9
1 12339U 81025A   07313.15890331 0.00000000  00000-0  00000-0 0    01
2 12339  14.3160   8.7296 0016263 108.4172 251.7717  0.98821615    08
DSCS 3-14 USA 170
1 27875U 03040A   07274.36836055 0.00000000  00000-0  00000-0 0    05
2 27875   0.0200  90.0004 0001000 180.0001 179.9999  1.00270000    00
Unknown 070914
1 90077U 07757A   07272.02679788 0.00000700  00000-0  53965-3 0    05
2 90077  28.1149 223.4027 7211623  34.5532 325.4466  2.33718986    01
Unknown 070918
1 90076U 07761A   07261.14212025 0.00000000  00000-0  00000-0 0    09
2 90076  18.7352   4.4643 0024056 177.2573 182.7789  1.00217190    03
SDS2 F2 Magnum 3 USA 67
1 20963U 90097B   07232.00023005 0.00000000  00000-0  00000-0 0    02
2 20963  12.3782  43.6309 0129130  94.7845 265.2341  1.00270000    06
Unknown 070310
1 90073U 07569A   07218.27701724 0.00000000  00000-0  00000-0 0    07
2 90073  12.3375 333.6121 0016032 220.0822 139.8115  0.98152425    03
NOSS 3-4 r
1 31702U 07027B   07211.98602379 0.00000483  00000-0  20711-3 0    06
2 31702  63.3731 274.4572 0163620 189.3552 170.3056 14.17708429    05
NOSS 3-4 (C)
1 31708U 07027C   07193.35731252 0.00000000  00000-0  00000-0 0    06
2 31708  63.4300 335.2216 0234817 150.8127 209.1873 13.65500000    08
NOSS 3-4 (C)
1 71703U 07027C   07170.06971504 0.00000000  00000-0  00000-0 0    04
2 71703  63.4300  37.1342 0234817 144.7322 215.3563 13.65609061    06
NOSS 3-4 (A)
1 31701U 07027A   07170.06953822 0.00000000  00000-0  00000-0 0    01
2 31701  63.4491  37.1181 0234547 144.6382 215.4221 13.65677834    02
Milstar 5 Cn r
1 27169U 02001B   07164.98349897 0.00000000  00000-0  00000-0 0    06
2 27169   2.2751 323.3619 0049349  78.2542 287.0261  1.00137794    06
Unknown 070511
1 91117U 07631A   07139.26722877  .00000000  00000-0  00000+0 0    09
2 91117  50.7032 157.3669 4804844 248.9007 111.6171  5.07303637    09
IGS R2
1 30586U 07005A   07108.00162496 0.00001600  00000-0  62349-4 0    06
2 30586  97.3219 228.6634 0004789 117.0927 242.9071 15.25995200    04
IGS R2 r
1 30588U 07005C   07107.99867309 0.00004000  00000-0  78749-4 0    08
2 30588  97.2912 229.6846 0095798 294.2453  65.7546 15.42260292    06
IGS R2 shroud2
1 30591U 07005F   07107.99494023 0.00007000  00000-0  26144-3 0    05
2 30591  97.2300 228.3472 0007979 235.7727 124.2272 15.27384068    08
IGS R1 shroud1
1 30590U 07005E   07107.99315165 0.00007300  00000-0  27229-3 0    01
2 30590  97.2211 228.2657 0008108 233.2259 126.7740 15.27426208    00
IGS-R2 adapter
1 30589U 07005D   07107.98881854 0.00005000  00000-0  18693-3 0    01
2 30589  97.2372 228.3467 0007973 199.6670 160.3328 15.27351491    04
IGS OVS
1 30587U 07005B   07106.97556309 0.00000000  00000-0  19730-2 0    08
2 30587  97.2818 227.5525 0001804  89.7710 270.2288 15.26031287    07
DSP F6
1 08916U 76059A   07079.50377131 0.00000000  00000-0  00000-0 0    04
2 08916  13.8181 344.4747 0029627 177.9250 182.0994  1.00452685    02
NOSS 2-2 (A)
1 21775U 91076A   07074.65642862 0.00000000  00000-0  00000-0 0    05
2 21775  63.3589 225.0012 3325559 266.6830  93.3170  5.53394968    08
Unknown 050301
1 90072U 05560C   07063.31680326 0.00000000  00000-0  00000-0 0    02
2 90072  14.4214 348.0660 0002296  16.0318 343.9875  0.99461249    04
NOSS 2-3 (A)
1 23893U 96029A   07060.82206468 0.00000000  00000-0  00000-0 0    03
2 23893  63.4733 352.7942 3314138 264.6933  95.3067  5.52843875    08
NOSS 2-1 (A)
1 20641U 90050A   07060.70300488 0.00000000  00000-0  00000-0 0    03
2 20641  63.4172  96.2736 4033400 268.3644  91.6356  6.02572519    05
UFO 7
1 23967U 96042A   07053.75412736 0.00000000  00000-0  00000-0 0    01
2 23967   2.8276  41.8670 0008000 200.9769 159.0231  1.00270000    02
Delta4 Demo
1 28500U 04050A   07030.25879883 0.00000000  00000-0  00000-0 0    07
2 28500  11.9212 199.6328 2887341 244.8710 115.1442  1.41309200    08
Delta4 Demo r
1 28546U 04050B   07028.57971064 0.00000000  00000-0  00000-0 0    03
2 28546  12.2910 202.7945 2680736 239.2158 120.7992  1.37842000    08
USA 193
1 29651U 06057A   06351.27314032  .00012066  00000-0  10000-3 0    00
2 29651  58.5075 109.9880 0009237 103.8726 256.3387 15.69650945    02
Unknown 060326
1 90067U 06085A   06346.15791963 0.00000000  00000-0  00000-0 0    04
2 90067  14.9277 353.2022 0078968 211.7528 147.7807  0.97525542    08
Unknown 061210
1 91090U 06844A   06344.94929672 0.00000000  00000-0  00000-0 0    09
2 91090   2.7000  38.7258 0001000 341.1643  18.8357  1.00270000    08
Unknown 061125
1 90070U 06829A   06336.25247557 0.00013000  00000-0  57382-3 0    01
2 90070  27.4667  75.3817 4799897 331.0516  28.9480  6.04892999    00
Unknown 060503
1 90056U 06623A   06322.94510516 0.00000000  00000-0  00000-0 0    04
2 90056   7.2520 356.1980 0932075 255.9116 104.0884  1.00270000    00
Unknown 050301
1 90069U 05560A   06316.23065343 0.00000000  00000-0  00000-0 0    05
2 90069  14.6843   5.9956 0008122 115.5975 244.4985  0.98741716    01
Unknown 061108
1 90068U 06812A   06315.12171652 0.00000000  00000-0  00000-0 0    03
2 90068   9.2728  55.6347 0002000 340.3244  19.6756  1.00270000    09
DMSP F17
1 29522U 06050A   06313.22739550 0.00000062  00000-0  33121-4 0    02
2 29522  98.7877 311.9526 0009224 249.9390 110.0609 14.13250636    06
Unknown 040920
1 90022U 04764A   06269.06199207 0.00000000  00000-0  00000-0 0    04
2 90022  11.6732  66.9434 0316489 252.0766 104.4603  0.99514325    02
Unknown 050616
1 90066U 05667A   06264.54841245 0.00000000  00000-0  00000-0 0    09
2 90066   2.5399  65.1529 0013926 309.9507  49.9391  1.00475347    09
IGS 2A
1 29393U 06037A   06255.94050995 0.00000000  00000-0  00000-0 0    04
2 29393  97.3059  14.6731 0005460 350.5714   9.4284 15.25871519    04
Unknown 060320
1 90064U 06579A   06239.69337876 0.00000000  00000-0  00000-0 0    08
2 90064  63.4467  68.5584 3305539 264.7788  95.2212  5.52842574    00
Unknown 060509
1 90065U 06629B   06239.61902766 0.00004000  00000-0  30340+1 0    07
2 90065  63.3895 300.5325 3358959 269.6587  90.3414  5.54462256    09
Unknown 060802
1 90063U 06214A   06227.02166296 0.00000000  00000-0  00000-0 0    03
2 90063  11.6391  47.0304 0126000  81.1450 278.8550  1.00270000    02
Unknown 060718
1 90062U 06199A   06223.76547498 0.00000000  00000-0  00000-0 0    08
2 90062   7.2890 189.8930 6839993 283.3245  76.6751  2.77430457    08
Unknown 060616
1 90061U 06667A   06222.02218586 0.00003000  00000-0  37574-3 0    00
2 90061  27.3823 233.4744 6875518 226.8912 133.1086  2.82348878    02
Unknown 060617
1 90058U 06668A   06213.87615521 0.00110000  00000-0  70237-3 0    02
2 90058  26.4049 222.4175 5435308 258.1896 101.8100  5.06142444    00
Unknown 060520
1 90060U 06640A   06213.63054290 0.00000000  00000-0  00000-0 0    05
2 90060  29.2763  47.7373 7093583  80.6305 279.3694  2.32913910    04
Unknown 060624
1 90059U 06675A   06213.40370816 0.00000542  00000-0  14233-3 0    08
2 90059  28.7365 286.3203 7286371 158.7000 201.2761  2.27620548    00
Unknown 060625
1 90057U 06676A   06207.01005982 0.00000000  00000-0  00000-0 0    09
2 90057  26.9476  68.1456 7173774  54.7817 305.4409  2.34416859    02
USA 184
1 29249U 06027A   06200.42851878 0.00000700  00000-0  15249-0 0    03
2 29249  63.2108  44.0449 7162774 268.3637  91.6363  2.00508383    09
Unknown 960906
1 90055U 96750A   06199.08002185 0.00000000  00000-0  00000-0 0    08
2 90055   5.2943   3.1498 0925710 210.8082 149.1923  1.00270000    03
Unknown 950327
1 90054U 95586A   06198.46725162 0.00000000  00000-0  00000-0 0    01
2 90054   3.0358  76.0091 0039416 175.6179 184.2812  1.00270000    07
Unknown 030923
1 90016U 03766A   06198.19827141 0.00000000  00000-0  00000-0 0    08
2 90016   6.8666  13.8494 0583335 183.1413 176.5626  1.00270000    00
Unknown 041026
1 90025U 04800A   06183.53789828 0.00001050  00000-0  14709-0 0    06
2 90025  64.1225 256.4894 7210093 262.9974  99.0174  2.00587000    09
Unknown 041211
1 90028U 04846A   06159.43062649 0.00000000  00000-0  00000-0 0    09
2 90028  64.0772  29.4966 7382273 261.9243  98.0757  2.00625000    03
Unknown 000405
1 90006U 00596A   06145.29819421 0.00000095  00000-0  23938-0 0    09
2 90006  63.3529 199.9244 6752207 283.4119  76.5881  2.00555791    09
Unknown 050220
1 90053U 05551A   06143.34198075 0.00000000  00000-0  00000-0 0    07
2 90053   7.8144 353.9381 1073396 272.0437  87.9563  1.00270000    07
Unknown 010313
1 90009U 01572A   06140.74274119 0.00000000  00000-0  00000-0 0    02
2 90009   2.9314  45.9265 0015000 339.4929  20.5071  1.00270000    00
Unknown 060419
1 90052U 04109A   06109.85366700 0.00000000  00000-0  00000-0 0    04
2 90052   9.3679  53.1385 0012000 315.6230  44.3770  1.00270000    05
USA 116
1 23728U 95066A   06108.05776286 0.00001000  00000-0  51035-4 0    06
2 23728  97.8800 241.3477 0282154  48.8003 311.1996 14.88264379    01
Unknown 000601
1 90007U 00653A   06098.95306970 0.00000000  00000-0  00000-0 0    05
2 90007   9.8323  48.0204 0047144  54.8546 305.5982  1.00239154    00
Unknown 990907
1 90004U 99750A   06097.80600307 -.00000505  00000-0 -18863-0 0    00
2 90004  64.5291 350.4796 7084586 279.3597  80.6391  2.01495310    08
Unknown 050518
1 90037U 05638A   06079.40180517 0.00000000  00000-0  00000-0 0    02
2 90037  14.2982  33.7953 0021888 235.5780 124.4306  1.00271000    05
Unknown 041206
1 90027U 04841A   06071.55035598 0.00001113  00000-0  11045+1 0    09
2 90027  62.3773 158.6750 6940454 268.4454  91.5512  2.00728666    05
Unknown 050227
1 90050U 05558C   06059.93910082 0.00000000  00000-0  00000-0 0    02
2 90050  13.9238  13.1234 0018764  91.5995 268.6274  0.98818813    01
Milstar 6 Cr
1 27712U 03012B   06059.79819916 0.00000000  00000-0  00000-0 0    08
2 27712   1.5656 328.5041 0038437 140.3392 219.9544  1.00554043    00
KH 9-16 Elint
1 11852U 80052C   06039.21206398 0.00000017  00000-0  71475-4 0    00
2 11852  96.6040  17.8887 0001500  51.8884 308.1115 12.83309062    06
Unknown 050415
1 90048U 05605B   06038.05573991 0.00000000  00000-0  00000-0 0    06
2 90048   5.5634  76.0751 0032072  14.1134 345.9977  1.00594285    08
Unknown 050415
1 90049U 05605C   06037.27383977 0.00000000  00000-0  00000-0 0    03
2 90049   4.1640 161.3551 0011879 324.0805  35.8513  1.00595721    04
STEX
1 25489U 98055A   06030.73270506 0.00000110  00000-0  30596-4 0    06
2 25489  84.9825  81.8375 0008000 315.1152  44.8847 14.46509155    09
Unknown 060121
1 90047U 06521A   06024.72702083 0.00000000  00000-0  00000-0 0    08
2 90047  25.7535 308.6171 7207107 335.9939  24.0059  2.28274700    02
Unknown 051002
1 90041U 05775A   06024.52102519 0.00000000  00000-0  00000-0 0    08
2 90041  14.1180 347.6590 0030902 162.3863 197.7332  1.00479337    04
KH 9-17 Elint
1 13172U 82041C   06021.77836867 0.00000380  00000-0  48262-4 0    00
2 13172  95.9810  59.5302 0003003 148.0009 211.9990 14.81752848    09
NOSS 0 (D)
1 05681U 71110D   06021.76087966 0.00000030  00000-0  31852-4 0    07
2 05681  69.9900 253.0594 0004000 210.9628 149.0372 13.74150281    03
NOSS 0 (A)
1 05678U 71110A   06021.74281767 0.00000020  00000-0  21364-4 0    02
2 05678  69.9820 260.2836 0006000 164.1547 195.8453 13.73783199    09
NOSS 2 (F)
1 10594U 77112F   06021.23098060 0.00000180  00000-0  36089-4 0    06
2 10594  63.3373  73.9008 0818000  28.9052 331.0948 13.44595788    08
NOSS 0 (C)
1 05680U 71110C   06020.75411501 0.00000030  00000-0  31803-4 0    06
2 05680  69.9810 254.0019 0008000 161.0640 198.9360 13.74231084    00
Unknown 050227
1 90033U 05558A   06018.85731161 0.00000000  00000-0  00000-0 0    08
2 90033   2.0160  74.6800 0030000  33.1612 326.8388  1.00270000    08
Unknown 991031
1 90005U 99804A   06018.73290965 0.00000000  00000-0  00000-0 0    03
2 90005   7.9806   6.3675 0472424 243.4249 111.6810  0.99563483    09
Unknown 050402
1 90034U 05592A   06018.71910417 0.00000000  00000-0  00000-0 0    05
2 90034   3.8000  45.6702 0007491 106.8854 253.1146  1.00270000    08
Unknown 050215
1 90031U 05546A   06018.65572539 0.00000000  00000-0  00000-0 0    03
2 90031   1.1000  63.5709 0010222 179.2424 180.7576  1.00270000    07
Unknown 050112
1 90029U 05512A   06018.63718640 0.00000000  00000-0  00000-0 0    06
2 90029  13.8738  13.1142 0003995  71.2329 288.8224  0.98951704    01
Milstar 3 Cn r
1 25725U 99023B   06018.02416152 0.00000130  00000-0  29077-3 0    05
2 25725  28.3070 308.1593 2388000  91.5240 268.4755  9.67067529    02
Unknown 990103
1 90003U 99503A   06018.00710268 0.00000000  00000-0  00000-0 0    00
2 90003  13.1475  24.2150 0009180 116.4066 243.6997  0.98677698    01
KH 9-18 Elint
1 14139U 83060C   06017.76197650 -.00000010  00000-0 -36357-4 0    04
2 14139  96.6545 212.5709 0001500 215.9289 144.0710 12.93723529    03
USA 186
1 28888U 05042A   06012.74211712 0.00010500  00000-0  10732-3 0    04
2 28888  97.8724  77.6223 0550578 269.8685  90.1314 14.72977790    05
NOSS 3-2 (C)
1 28097U 03054C   06012.28086606 0.00000030  00000-0  53974-4 0    01
2 28097  63.4380 140.5002 0063000 175.7481 184.2519 13.40484583    06
NOSS 3-2 (A)
1 28095U 03054A   06012.28078454 0.00000030  00000-0  54013-4 0    06
2 28095  63.4350 140.3003 0061000 175.2463 184.7537 13.40484330    08
NOSS 2-1 (E)
1 20642U 90050E   06012.26882069 0.00000010  00000-0  10763-4 0    03
2 20642  63.4060 119.1582 0423000 358.1103   1.8897 13.40460764    00
NOSS 5 (D)
1 14144U 83056D   06012.26535057 0.00000030  00000-0  14479-4 0    03
2 14144  63.3700 156.2478 0660000  16.5321 343.4679 13.41342763    08
NOSS 3 (A)
1 11720U 80019A   06012.26008070 0.00000100  00000-0  41590-4 0    08
2 11720  63.4061  63.2060 0689094 339.9632  20.0368 13.42277773    03
NOSS 5 (G)
1 14180U 83056G   06012.25830263 0.00000030  00000-0  14961-4 0    05
2 14180  63.3700 157.2054 0652500  11.3842 348.6158 13.41275153    03
NOSS 5 (C)
1 14143U 83056C   06012.25073528 0.00000060  00000-0  29173-4 0    01
2 14143  63.3670 155.4097 0658000  16.3428 343.6572 13.41381711    04
NOSS 2 (E)
1 10544U 77112E   06012.24981873 0.00000240  00000-0  48080-4 0    06
2 10544  63.3280  91.6270 0816500  34.9837 325.0163 13.44913427    05
NOSS 8 (F)
1 18010U 87043F   06012.23104210 0.00000030  00000-0  23342-4 0    08
2 18010  63.3950 102.2883 0534000   6.2713 353.7287 13.40809255    05
NOSS 2 (D)
1 10529U 77112D   06012.22156335 0.00000250  00000-0  49488-4 0    08
2 10529  63.3330  91.3147 0818500  35.0169 324.9831 13.44914612    03
NOSS 5 (A)
1 14112U 83056A   06012.20716683 0.00000100  00000-0  50482-4 0    00
2 14112  63.3690 152.9751 0648000  11.5924 348.4076 13.41544224    00
NOSS 3 (G)
1 11745U 80019G   06012.20310123 0.00000100  00000-0  42507-4 0    03
2 11745  63.4122  71.4502 0686500 339.2665  20.7335 13.41864885    04
DMSP F16
1 28054U 03048A   06011.79395072 -.00000020  00000-0 -10654-4 0    01
2 28054  98.8208  54.4827 0010000 116.4122 243.5877 14.13401246    06
Lacrosse 3
1 25017U 97064A   06011.27682724 0.00000140  00000-0  22468-4 0    01
2 25017  57.0100 167.8106 0005000 108.4515 251.5485 14.71324217    00
NOSS 8 (E)
1 18009U 87043E   06011.25757371 0.00000050  00000-0  39153-4 0    08
2 18009  63.3960 104.7865 0532000   5.9063 354.0938 13.40811205    08
NOSS 0 (E)
1 05682U 71110E   06010.89007426 0.00000020  00000-0  21229-4 0    09
2 05682  69.9803 275.1969 0010000 175.2520 184.7480 13.74147571    02
USA 32
1 19460U 88078A   06010.87279986 0.00000050  00000-0  18408-4 0    07
2 19460  84.9840 123.8525 0004000 235.1365 124.8634 14.32693695    06
MSX
1 23851U 96024A   06010.81985590 0.00000060  00000-0  42438-4 0    06
2 23851  99.1184  89.5662 0007000 352.2393   7.7606 13.97829114    04
DMSP F15
1 25991U 99067A   06010.71545390 0.00000100  00000-0  50644-4 0    05
2 25991  98.5989  58.3927 0013001 112.0755 247.9244 14.16086491    08
Milstar 5
1 27168U 02001A   06010.59487748 0.00000000  00000-0  00000-0 0    09
2 27168   1.6801 327.9695 0006833  20.2919 339.7081  1.00270000    07
Unknown 050702
1 90040U 05683A   06010.57318895 0.00000407  00000-0  31110-3 0    01
2 90040  27.5239 114.8635 7016479 266.8135  93.2557  2.58073078    07
Unknown 050509
1 90036U 05629A   06010.40206371 0.00000000  00000-0  00000-0 0    03
2 90036   1.8500 326.9206 0020000 308.9433  51.0567  1.00270000    08
Unknown 050518
1 90038U 05638B   06010.36547102 0.00000000  00000-0  00000-0 0    00
2 90038   3.6133 312.7763 0010000 263.6647  96.3353  1.00270400    05
NOSS 2 (A)
1 10502U 77112A   06009.76375048 0.00000250  00000-0  50559-4 0    09
2 10502  63.3360  98.9638 0815500  28.7167 331.2833 13.44798729    01
Unknown 051230
1 90046U 05864A   06009.57536690 0.00000112  00000-0  10215-0 0    04
2 90046  63.4777 260.4332 6956666 276.0373  83.9628  2.00613732    07
NOSS 1 (C)
1 08835U 76038C   06009.27537296 0.00000900  00000-0  94452-4 0    04
2 08835  63.3040  85.2586 0871500  58.5500 301.4500 13.53464917    06
NOSS 1 (A)
1 08818U 76038A   06009.27071717 0.00000910  00000-0  93106-4 0    02
2 08818  63.3050  84.6572 0875000  53.9584 306.0416 13.53455271    06
Alexis r
1 22639U 93026B   06009.24935143 0.00000070  00000-0  26102-4 0    03
2 22639  69.9190  48.0928 0064000 302.0895  57.9105 14.30763043    04
NOSS 8 (A)
1 17997U 87043A   06009.24674221 0.00000050  00000-0  36703-4 0    09
2 17997  63.3950  96.3688 0548500   2.8452 357.1548 13.41315349    01
AMS 2(DMSP F2)
1 10033U 77044A   06009.20947247 0.00000055  00000-0  22039-4 0    02
2 10033  99.1150 341.8062 0041000 195.1400 164.8599 14.27901766    08
USA 39 (DSP)
1 20066U 89046A   06008.23830112 0.00000000  00000-0  00000-0 0    08
2 20066   8.9654  47.9789 0012000 312.8426  47.1608  1.00270000    07
Alexis
1 22638U 93026A   06008.04402818 0.00000100  00000-0  36599-4 0    02
2 22638  69.9176  29.4719 0061000 285.0361  74.9639 14.31805374    09
Unknown 050213
1 90030U 05544A   06007.24787862 0.00000000  00000-0  00000-0 0    00
2 90030   6.0118  48.8949 0114617 166.7998 193.5150  0.99578393    05
Unknown 981016
1 90002U 98789A   06006.92648003 0.00000000  00000-0  00000-0 0    09
2 90002  13.7831 340.5774 0016555 305.1111  54.7458  0.99808667    06
Unknown 041002
1 90023U 04776A   06006.38858888 0.00000000  00000-0  00000-0 0    09
2 90023   5.0100 177.7034 0004000 205.7851 154.2263  1.00270000    06
Milstar 3
1 25724U 99023A   06005.78692418 0.00000080  00000-0  10081-2 0    02
2 25724  28.2355 206.3189 2132000 174.9652 185.0343  9.37434718    08
Milstar 6
1 27711U 03012A   06005.70465450 0.00000000  00000-0  00000-0 0    09
2 27711   1.9200 268.8640 0003000 300.5910  59.4134  1.00270200    05
NOSS 3-2 r
1 28096U 03054B   06004.26667110 0.00000020  00000-0  35653-4 0    07
2 28096  63.6760 176.3028 0082000 131.1629 228.8371 13.40560965    05
DMSP 7
1 07816U 75043A   06004.26317354 0.00000070  00000-0  31254-4 0    01
2 07816  98.5820 203.1249 0053000 225.1915 134.8084 14.22025303    00
USA 3
1 15071U 84065C   06004.24535974 0.00000500  00000-0  60160-4 0    01
2 15071  95.8872 199.5948 0003000 160.1409 199.8589 14.84003314    01
NOSS 1 (J)
1 08884U 76038J   06004.24488934 0.00000900  00000-0  94391-4 0    06
2 08884  63.3070  98.1516 0871500  58.2759 301.7241 13.53482768    01
NOSS 4 (H)
1 13874U 83008H   06003.75362458 0.00000160  00000-0  74156-4 0    08
2 13874  63.3690 324.6016 0669000  18.2405 341.7596 13.41442010    00
AMS 4(DMSP F4)
1 11389U 79050A   06003.72990493 0.00000060  00000-0  24677-4 0    04
2 11389  98.8730  44.0192 0014000 100.7336 259.2663 14.26974127    00
DMSP F14
1 24753U 97012A   06003.72450074 0.00000080  00000-0  41276-4 0    03
2 24753  98.5480  19.8760 0009000 139.4492 220.5507 14.15118092    02
IGS 1A
1 27698U 03009A   06002.84702713 0.00000000  00000-0  00000-0 0    07
2 27698  97.4061  78.8833 0001000 346.0767  13.9232 15.25957369    04
USA 141 (ATEX)
1 25615U 98055C   06002.84052518 0.00000150  00000-0  44352-4 0    08
2 25615  84.9820 104.9407 0007000  46.9351 313.0648 14.43555225    03
Unknown 051225
1 90044U 05859A   06002.82944993 0.00020000  00000-0  96959-3 0    06
2 90044  63.2528 236.8413 4261404 294.7048  65.2952  6.98670114    08
IGS 1B
1 27699U 03009B   06002.82136744 0.00000000  00000-0  00000-0 0    01
2 27699  97.4011  78.8328 0001500 337.8526  22.1473 15.25959078    03
USA 125 r
1 23947U 96038C   06002.80292820 0.00000070  00000-0  17014-3 0    06
2 23947  55.3758 221.6783 4893500 174.2271 185.7729  5.48310268    08
Unknown 051228
1 90045U 05862B   06002.66182344 0.00000000  00000-0  00000-0 0    04
2 90045   8.5203 186.2035 5754874  27.5269 332.4727  4.22727690    01
NOSS 3 (C)
1 11731U 80019C   06002.19803734 0.00000100  00000-0  31733-4 0    09
2 11731  63.3990  75.3164 0744500 347.7610  12.2390 13.42586373    08
NOSS 2-1 (D)
1 20692U 90050D   06002.19775123 0.00000010  00000-0  10628-4 0    01
2 20692  63.4060 145.1925 0428000   2.4392 357.5608 13.40462948    06
NOSS 2-1 (C)
1 20691U 90050C   06002.19768306 0.00000010  00000-0  10628-4 0    05
2 20691  63.4080 145.4648 0428000   2.3923 357.6077 13.40463970    08
NOSS 3-3 r
1 28538U 05004B   06002.19553970 0.00000010  00000-0  16881-4 0    04
2 28538  63.8281  43.9989 0114000 147.8157 212.1843 13.42859142    07
NOSS 3 (D)
1 11732U 80019D   06002.19206682 0.00000110  00000-0  35134-4 0    09
2 11732  63.3970  75.5233 0743500 347.9431  12.0569 13.42531475    07
NOSS 8 (H)
1 18025U 87043H   06002.17263149 0.00000040  00000-0  32346-4 0    08
2 18025  63.3940 128.2963 0522000 359.7676   0.2324 13.40795143    04
Lacrosse 2
1 21147U 91017A   06002.17048373 0.00000160  00000-0  23506-4 0    04
2 21147  67.9940 150.6437 0005000 254.4290 105.5710 14.75374457    05
USA 89 r
1 22519U 92086C   06002.16731662 0.00001900  00000-0  32267-3 0    00
2 22519  56.9280  45.0522 3218246 309.2593  50.7407  8.76398053    08
USA 171 r
1 27938U 03041B   06002.16161718 0.00000000  00000-0  00000-0 0    09
2 27938   4.8448 219.9329 0036325 166.7110 193.3965  1.00857694    01
NOSS 3-3 (C)
1 28541U 05004C   06002.15450342 0.00000020  00000-0  35290-4 0    09
2 28541  63.4340  35.9774 0103000 177.6416 182.3585 13.40481471    08
NOSS 3-3 (A)
1 28537U 05004A   06002.15441714 0.00000010  00000-0  17645-4 0    00
2 28537  63.4340  35.7759 0103000 177.7610 182.2391 13.40481310    07
NOSS 2-2 (D)
1 21808U 91076D   06002.15211711 0.00000020  00000-0  23697-4 0    05
2 21808  63.4130  34.0652 0382500   1.3918 358.6082 13.40475952    00
NOSS 2-2 (E)
1 21809U 91076E   06002.15200984 0.00000020  00000-0  23938-4 0    04
2 21809  63.4140  33.6286 0378000 356.1064   3.8936 13.40476059    09
NOSS 2-2 (C)
1 21799U 91076C   06002.15198731 0.00000020  00000-0  23751-4 0    01
2 21799  63.4120  33.7995 0381500   1.6448 358.3552 13.40476112    02
USA 144 Deb
1 25746U 99028C   06002.14793056 0.00000060  00000-0  92484-2 0    03
2 25746  63.4412  85.4913 0242000 294.0968  65.9032  9.69821966    03
Lacrosse 5 r
1 28647U 05016B   06001.68331250 0.00000600  00000-0  44507-4 0    07
2 28647  56.9980 231.2148 0164000  89.6177 270.3822 14.92462870    03
AMS 1(DMSP F1)
1 09415U 76091A   06001.25011777 0.00000070  00000-0  29618-4 0    09
2 09415  98.9850 210.8688 0012000 137.6036 222.3963 14.25525199    02
XSS-11 r
1 28637U 05011B   06001.24515133 0.00000060  00000-0  33380-4 0    04
2 28637  98.8516 356.0730 0010997 169.6387 190.3612 14.11054175    06
XSS-11
1 28636U 05011A   06001.24510227 0.00000070  00000-0  38934-4 0    03
2 28636  98.8526 356.0685 0013000 178.6393 181.3606 14.11055223    08
DMSP B5D2-7
1 23233U 94057A   06001.23996751 0.00000090  00000-0  46824-4 0    07
2 23233  98.5560 347.5658 0012000 299.9347  60.0652 14.14656230    03
NOSS 1 (D)
1 08836U 76038D   06001.23692537 0.00000900  00000-0  92190-4 0    00
2 08836  63.3045 116.3278 0878000  53.6809 306.3191 13.52814296    04
USA 102
1 23031U 94017B   06001.05606452 0.00002450  00000-0  10644-3 0    07
2 23031 105.0348 197.9572 0016000 126.6818 233.3181 15.22131729    05
Geosat FO
1 25157U 98007A   06001.01381868 0.00000050  00000-0  18797-4 0    00
2 25157 108.0561 183.2132 0001965 319.6116  40.3884 14.31515516    00
NOSS 3-1 (A)
1 26905U 01040A   05365.82917860 0.00000020  00000-0  36402-4 0    01
2 26905  63.4370 252.6798 0005000  66.7155 293.2845 13.40482888    00
NOSS 3-1 (C)
1 26907U 01040C   05365.82908481 0.00000020  00000-0  36402-4 0    02
2 26907  63.4290 252.4506 0005000  90.4103 269.5897 13.40483196    01
NOSS 6 (C)
1 14728U 84012C   05365.82802004 0.00000140  00000-0  76072-4 0    04
2 14728  63.3730 255.3263 0634500  15.1951 344.8049 13.40721876    03
NOSS 6 (D)
1 14729U 84012D   05365.82148756 0.00000140  00000-0  76387-4 0    01
2 14729  63.3730 254.7782 0633000  15.3266 344.6734 13.40800738    02
TiPS
1 23937U 96029F   05365.81682843 0.00001000  00000-0  73955-3 0    05
2 23937  63.4005 236.3733 0323997   4.2196 355.7804 13.73082070    09
NOSS 3-1 r
1 26906U 01040B   05365.81442981 0.00000010  00000-0  17328-4 0    03
2 26906  63.4746 235.6115 0010500 169.7159 190.2841 13.43638197    02
DMSP B5D2-6
1 21798U 91082A   05365.79588958 0.00000090  00000-0  45971-4 0    07
2 21798  98.6393  16.1728 0013000  20.6178 339.3821 14.15631006    06
NOSS 6 (A)
1 14690U 84012A   05365.79376013 0.00000150  00000-0  83314-4 0    02
2 14690  63.3780 249.4662 0625000   7.9287 352.0713 13.41396801    05
NOSS 4 (F)
1 13845U 83008F   05365.78563490 0.00000180  00000-0  85077-4 0    04
2 13845  63.3660 332.2210 0664500  18.6956 341.3044 13.41422712    02
USA 179 Cn r
1 28385U 04034B   05365.77545288 0.00002300  00000-0  69736-3 0    04
2 28385  57.3912 281.7272 5245781  61.4870 298.5130  5.17267731    09
NOSS 2-3 (E)
1 23936U 96029E   05365.77526370 0.00000030  00000-0  46450-4 0    04
2 23936  63.4210 313.6991 0235000   0.3324 359.6676 13.40477576    01
NOSS 2-3 (C)
1 23908U 96029C   05365.77520912 0.00000030  00000-0  46482-4 0    04
2 23908  63.4190 313.4749 0234500 357.6241   2.3759 13.40477541    02
NOSS 2-3 (D)
1 23862U 96029D   05365.77515009 0.00000030  00000-0  46515-4 0    01
2 23862  63.4170 313.5618 0234000   0.8115 359.1885 13.40476571    02
NOSS 6 (F)
1 14795U 84012F   05365.76390722 0.00000110  00000-0  61830-4 0    03
2 14795  63.3770 258.4890 0626000   7.7191 352.2809 13.40703219    08
Lacrosse 5
1 28646U 05016A   05365.76346897 0.00000040  00000-0  95517-5 0    06
2 28646  57.0110 293.2429 0007000 187.6750 172.3250 14.53349022    07
NOSS 0 r
1 05679U 71110B   05365.76203398 0.00000030  00000-0  26500-4 0    07
2 05679  70.0000 210.4505 0015000 293.5570  66.4430 13.84958551    02
NOSS 4 (A)
1 13791U 83008A   05365.75640978 0.00000240  00000-0  11426-3 0    01
2 13791  63.3680 326.6365 0661000  13.3522 346.6478 13.41737496    02
USA 40 r
1 20344U 89061D   05365.75227907 0.00000080  00000-0  74094-4 0    04
2 20344  57.0097 333.9693 3552000  50.5787 309.4213  7.85782853    01
NOSS 4 (E)
1 13844U 83008E   05365.75151752 0.00000200  00000-0  96629-4 0    02
2 13844  63.3690 333.2877 0659500  13.2795 346.7205 13.41384743    09
DMSP B5D2-8
1 23533U 95015A   05365.74221147 0.00000080  00000-0  41460-4 0    03
2 23533  98.8056  18.3941 0007000 250.8729 109.1270 14.14886173    03
NOSS 7 (H)
1 16631U 86014H   05365.73927053 0.00000070  00000-0  51003-4 0    04
2 16631  63.3890 217.8019 0556000   2.1894 357.8106 13.40471184    09
NOSS 7 (E)
1 16624U 86014E   05365.73905480 0.00000080  00000-0  55849-4 0    09
2 16624  63.3830 214.1538 0568500  11.2175 348.7825 13.40470702    04
NOSS 7 (D)
1 16623U 86014D   05365.73886567 0.00000080  00000-0  56334-4 0    02
2 16623  63.3842 214.0383 0566000  11.2966 348.7034 13.40471088    04
NOSS 7 (A)
1 16591U 86014A   05365.73722074 0.00000070  00000-0  49561-4 0    01
2 16591  63.3900 210.5319 0560502   2.3116 357.6884 13.41103355    04
Lacrosse 4
1 26473U 00047A   05365.73533576 0.00000100  00000-0  18922-4 0    01
2 26473  67.9950 310.5724 0006000 273.8098  86.1902 14.64250326    04
Unknown 030305
1 90013U 03564A   05365.62255760 0.00000000  00000-0  00000-0 0    06
2 90013   7.1137   8.3672 0042091 213.9246 146.0754  1.00270000    00
USA 161
1 26934U 01044A   05364.93732890 0.00000900  00000-0  51180-4 0    03
2 26934  97.9180 109.5229 0343693 129.9356 230.0642 14.74398653    08
USA 129
1 24680U 96072A   05364.85222684 0.00011000  00000-0  15375-3 0    08
2 24680  97.9382  65.5364 0514056 244.8119 115.1880 14.74984649    09
Unknown 051124
1 90042U 05828A   05364.80475198 0.00000000  00000-0  00000-0 0    01
2 90042   1.8300  85.8634 0002000 213.9437 146.0563  1.00270000    09
USA 81
1 21949U 92023A   05364.75195687 0.00000040  00000-0  15305-4 0    02
2 21949  85.0070  58.6990 0002000 125.3078 234.6920 14.30742967    01
Unknown 051201
1 90043U 05835A   05364.71370386 0.00000000  00000-0  00000-0 0    03
2 90043   1.5656 346.0967 0007000 148.2516 211.7484  1.00270000    07
Unknown 001203
1 90008U 00838A   05362.95530853 0.00000000  00000-0  00000-0 0    03
2 90008   6.9461 114.1948 0019914 174.6606 185.3725  1.00547382    08
Unknown 050505
1 90035U 05625A   05362.54974897 0.00000000  00000-0  00000-0 0    07
2 90035   0.0200 354.9914 0003000  95.6060 264.3940  1.00270000    03
Unknown 050708
1 90039U 05689A   05346.40921668 0.00001052  00000-0  00000-0 0    04
2 90039  63.8308  12.1969 7098024 260.2953  99.7042  2.00744639    02
Unknown 041011
1 90024U 04785A   05274.35638107 0.00000000  00000-0  00000-0 0    03
2 90024   0.0500  85.8960 0001000   9.5595 350.4405  1.00270000    03
Unknown 040208
1 90020U 04539A   05257.20527666 -.00000371  00000-0 -79704-0 0    08
2 90020  64.7204 285.9802 6783484 266.9398  93.0589  2.00951372    06
Unknown 050415
1 90051U 05605A   05241.35118712 0.00000000  00000-0  00000-0 0    04
2 90051   7.2179 348.6914 1295010 314.1949  35.8646  1.00150951    01
Unknown 050318
1 90032U 05577A   05116.46023920 0.00000411  00000-0  00000-0 0    06
2 90032  63.5256 327.4948 7380134 263.0325  96.9675  2.00614585    00
'''

snapshots['test_tle_trusat_high_confidence 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'text/plain', 'Access-Control-Allow-Origin': '*'}

CONTENT:Elisa W11
1 38007U 11076A   19233.81751334 0.00000050  00000-0  93270-5 0    07
2 38007  97.9542 291.2812 0001000   8.2000 351.7998 14.65084869    05
Elisa W23
1 38009U 11076C   19233.81766668 0.00000050  00000-0  93268-5 0    02
2 38009  97.9522 291.2676 0002000   8.2051 351.7947 14.65084771    06
STPSat 2
1 37222U 10062A   19233.89996344 0.00000060  00000-0  82010-5 0    00
2 37222  71.9626 281.7722 0017000 107.8487 252.1512 14.78426929    01
SAR Lupe 3
1 32283U 07053A   19233.93367556 0.00000700  00000-0  26051-4 0    03
2 32283  98.0970 135.0123 0001500  88.0689 271.9309 15.27523941    03
IGS Radar 6 r
1 43496U 18052B   19233.94106000 0.00000750  00000-0  28999-4 0    06
2 43496  97.2501 339.6651 0020498 293.7918  66.2081 15.26062101    04
NOSS 2-1 (E)
1 20642U 90050E   19233.98038656 0.00000050  00000-0  89137-5 0    02
2 20642  63.3224 290.7529 0851003  40.0960 319.9040 13.41903111    06
NOSS 8 (A)
1 17997U 87043A   19234.81382666 0.00001053  00000-0  87824-4 0    09
2 17997  63.3024 148.8608 0924442  59.9273 300.0492 13.48788042    01
USA 276
1 42689U 17022A   19234.83728902 0.00002600  00000-0  33969-4 0    04
2 42689  49.9951 224.9231 0014740  18.1699 341.8299 15.57810374    08
USA 245
1 39232U 13043A   19234.83834021 0.00003100  00000-0  30962-4 0    09
2 39232  97.8930 296.2762 0527109 291.5919  68.4080 14.78437010    02
Elisa E12
1 38010U 11076D   19234.84196779 0.00000020  00000-0  37307-5 0    07
2 38010  97.9556 294.8290 0002002  11.0723 348.9276 14.65084753    09
Elisa E24
1 38008U 11076B   19234.84211828 0.00000010  00000-0  18652-5 0    08
2 38008  97.9499 294.8221 0003691  70.0740 289.9259 14.65084596    05
FIA Radar 2
1 38109U 12014A   19234.84887430 0.00000000  00000-0  00000-0 0    03
2 38109 123.0021 307.4858 0004248 229.5575 130.4424 13.41422979    00
IGS Radar 5 r
1 42073U 17015B   19234.85039334 0.00000750  00000-0  28453-4 0    05
2 42073  97.0815 277.4066 0008388  94.0956 265.9042 15.26864236    01
Optsat 3000
1 42900U 17044A   19234.85184977 0.00000800  00000-0  30831-4 0    09
2 42900  97.3128 305.5990 0024083  29.1462 330.8537 15.26093081    03
IGS 9 r
1 40382U 15004B   19234.86190339 0.00002000  00000-0  44028-4 0    02
2 40382  97.0479 287.5487 0010000  11.2958 348.7040 15.43923006    02
IGS 5A
1 36104U 09066A   19234.86706706 0.00000000  00000-0  00000-0 0    07
2 36104  97.6382 301.1924 0003129  26.3819 333.6180 14.93714755    05
NOSS 3-5 (B)
1 37391U 11014B   19234.87035831 0.00000000  00000-0  00000-0 0    07
2 37391  63.4378 148.7803 0138313 359.3143   0.6857 13.40785366    03
NOSS 3-5 (A)
1 37386U 11014A   19234.87044313 0.00000000  00000-0  00000-0 0    06
2 37386  63.4378 148.9683 0133840 358.9245   1.1223 13.40785063    00
USA 144 Deb
1 25746U 99028C   19234.90840927 0.00000000  00000-0  00000-0 0    03
2 25746  63.4437 244.2605 0272570 300.4677  59.5322  9.70006734    08
IGS Radar 5
1 42072U 17015A   19234.91130826 0.00000000  00000-0  00000-0 0    01
2 42072  97.3788 304.8067 0003002 313.5369  46.4629 15.25980423    02
Essaim 2
1 28495U 04049D   19234.92776645 0.00000100  00000-0  13590-4 0    06
2 28495  98.1881 340.3480 0001003   4.8946 355.1053 14.78890794    01
FAST 2
1 37380U 10062M   19234.93233072 0.00000000  00000-0  00000-0 0    01
2 37380  72.0080 278.6161 0010374  83.3009 276.7184 14.78262679    06
NOSS 2-2 (E)
1 21809U 91076E   19234.96119443 0.00000050  00000-0  11104-4 0    08
2 21809  63.3417 197.1596 0816560  31.7257 328.2743 13.41490402    02
NOSS 3-2 r
1 28096U 03054B   19234.98483547 0.00000000  00000-0  00000-0 0    07
2 28096  63.6753 203.9135 0245696 239.4246 120.5753 13.40854423    09
FIA Radar 5
1 43145U 18005A   19235.00782902 0.00000000  00000-0  00000-0 0    02
2 43145 106.0078 349.0491 0002164 318.2027  41.7527 13.48022848    03
IGS 6
1 37813U 11050A   19235.00961634 0.00000000  00000-0  00000-0 0    01
2 37813  97.7659 349.8974 0004090  51.7448 308.2551 14.93590513    07
CSO 1
1 43866U 18106A   19235.02293756 0.00000000  00000-0  00000-0 0    00
2 43866  98.6300 173.5412 0001000  41.3261 318.6737 14.26736535    03
IGS Opt 5 r
1 40539U 15015B   19235.02380884 0.00001700  00000-0  41445-4 0    09
2 40539  97.4577 347.6830 0006799 216.7257 143.2741 15.40889650    02
IGS Opt 6
1 43223U 18021A   19235.02748157 0.00000000  00000-0  00000-0 0    03
2 43223  97.3483 353.6509 0003313  14.1508 345.8490 15.27649836    04
Helios 2B
1 36124U 09073A   19235.03606046 0.00000100  00000-0  19178-4 0    04
2 36124  98.1353 170.2460 0001002  28.1864 331.8135 14.63837704    06
IGS 8A
1 39061U 13002A   19235.04311388 0.00000000  00000-0  00000-0 0    06
2 39061  97.4934 353.6113 0000928 359.4925   0.5785 15.17615180    05
USA 186
1 28888U 05042A   19235.09724505 0.00013000  00000-0  61609-4 0    00
2 28888  96.8838 271.8450 0137548 345.2143  14.8415 15.70087007    03
NOSS 3-8 (B)
1 42065U 17011B   19235.12281177 0.00000000  00000-0  00000-0 0    09
2 42065  63.4393   9.5013 0049783 172.0749 187.9251 13.40786766    07
NOSS 3-8 (A)
1 42058U 17011A   19235.12289715 0.00000000  00000-0  00000-0 0    07
2 42058  63.4405   9.6900 0051359 173.5585 186.4415 13.40786613    02
NOSS 3-1 (C)
1 26907U 01040C   19235.80155771 0.00000000  00000-0  00000-0 0    06
2 26907  63.4118 148.8883 0439452   0.1619 359.8381 13.41296102    09
NOSS 2-3 (C)
1 23908U 96029C   19235.80458357 0.00000020  00000-0  90925-5 0    03
2 23908  63.3643 162.1281 0676545  18.5322 341.4678 13.40899766    00
SBSS 1
1 37168U 10048A   19235.81890678 0.00000050  00000-0  63827-5 0    04
2 37168  97.8485  95.5314 0001212 126.8965 233.1034 14.81530025    03
USA 32
1 19460U 88078A   19235.82349060 0.00000000  00000-0  00000-0 0    06
2 19460  84.9841 119.0072 0004410 125.8957 234.1141 14.33476415    06
Alexis r
1 22639U 93026B   19235.82356043 0.00000080  00000-0  29235-4 0    09
2 22639  69.9168 253.1128 0065000 353.4532   6.5468 14.31741909    09
IGS 9
1 40381U 15004A   19235.84038004 0.00000000  00000-0  00000-0 0    06
2 40381  97.3380 305.9387 0004096  77.9114 282.0884 15.27652194    05
NOSS 3-1 (A)
1 26905U 01040A   19235.84371419 0.00000000  00000-0  00000-0 0    07
2 26905  63.4037 155.5465 0444353   0.0210 359.9789 13.40772344    09
NOSS 2-3 (E)
1 23936U 96029E   19235.84813439 0.00000030  00000-0  13332-4 0    01
2 23936  63.3684 161.8048 0681699  18.6588 341.3412 13.40915873    07
NOSS 2-3 (D)
1 23862U 96029D   19235.85141573 0.00000000  00000-0  00000-0 0    04
2 23862  63.3624 162.6568 0676378  19.4334 340.5666 13.40864882    06
IGS Opt 5
1 40538U 15015A   19235.85317892 0.00000000  00000-0  00000-0 0    08
2 40538  97.4630 309.8098 0001995 290.6915  69.3083 15.17628735    08
STPSat 2 r
1 37228U 10062G   19235.85722435 0.00000020  00000-0  26888-5 0    09
2 37228  71.9616 272.3370 0020766 108.2353 251.7646 14.79075828    03
AMS 1
1 09415U 76091A   19235.86609124 0.00000000  00000-0  00000-0 0    01
2 09415  98.4190 112.1735 0012874  34.3884 325.6115 14.26402195    01
USA 3
1 15071U 84065C   19235.87116000 0.00000150  00000-0  14519-4 0    03
2 15071  95.9396 311.9822 0006663 330.3168  29.6830 14.92818718    05
IGS 7A
1 37954U 11075A   19235.88073385 0.00000100  00000-0  49796-5 0    08
2 37954  97.4629 311.8031 0001913 336.3265  23.6733 15.17633148    09
STSS-ATRR
1 34903U 09023A   19235.89346253 0.00000090  00000-0  54334-4 0    08
2 34903  98.9318 332.2992 0009140 176.6714 183.3285 14.06613132    02
NOSS 2-2 (C)
1 21799U 91076C   19235.89629447 0.00000050  00000-0  11180-4 0    03
2 21799  63.3380 196.9185 0816611  34.5017 325.4982 13.41249738    00
NOSS 3-7 r
1 40978U 15058Q   19235.94380037 0.00000470  00000-0  43564-4 0    01
2 40978  64.7746 284.1486 0194050 184.7527 175.2311 14.80974929    03
NOSS 2-2 (D)
1 21808U 91076D   19235.94712433 0.00000100  00000-0  22159-4 0    02
2 21808  63.3418 196.9527 0818070  34.1220 325.8780 13.41270858    03
NOSS 2-1 (C)
1 20691U 90050C   19235.96141551 0.00000020  00000-0  35295-5 0    08
2 20691  63.3227 284.3071 0852500  42.2932 317.7068 13.41927435    01
NOSS 2-1 (D)
1 20692U 90050D   19235.96346764 0.00000000  00000-0  00000-0 0    01
2 20692  63.3273 284.1495 0852570  42.3146 317.6854 13.41922485    08
USA 224
1 37348U 11002A   19235.96376860 0.00009733  00000-0  87965-4 0    08
2 37348  97.9000 346.1115 0536016 144.5643 215.4217 14.78261821    03
NOSS 3-4 (A)
1 31701U 07027A   19236.00035838 0.00000000  00000-0  00000-0 0    09
2 31701  63.3997 208.7095 0259843  19.9787 340.0213 13.40781549    09
NOSS 3-4 (C)
1 31708U 07027C   19236.00044455 0.00000000  00000-0  00000-0 0    01
2 31708  63.4005 208.8889 0259694  19.9478 340.0522 13.40781980    02
FIA Radar 4
1 41334U 16010A   19236.00408868 0.00000000  00000-0  00000-0 0    01
2 41334 123.0030  41.2834 0007180  21.4122 338.5877 13.41415161    04
Helios 2A
1 28492U 04049A   19236.02582239 0.00000040  00000-0  76753-5 0    04
2 28492  98.1431 171.2664 0001000 176.4631 183.5367 14.63813430    05
SAR Lupe 4
1 32750U 08014A   19236.02971477 0.00000562  00000-0  20920-4 0    01
2 32750  98.1588   6.7625 0001929 359.3849   0.5875 15.27515059    01
NOSS 4 (A)
1 13791U 83008A   19236.03930158 0.00000641  00000-0  43805-4 0    08
2 13791  63.2920 229.5607 0902624  89.0328 270.9672 13.58313578    06
NOSS 3-7 (A)
1 40964U 15058A   19236.04157705 0.00000000  00000-0  00000-0 0    05
2 40964  63.4549 290.7852 0006805 114.0909 245.9091 13.40782893    07
NOSS 3-7 (R)
1 40981U 15058R   19236.04167702 0.00000000  00000-0  00000-0 0    02
2 40981  63.4562 290.9539 0006227  33.6322 326.3678 13.40783023    09
NOSS 7 (A)
1 16591U 86014A   19236.05800887 0.00000678  00000-0  52434-4 0    04
2 16591  63.2960 227.2409 0928830  64.0359 296.0003 13.49809166    00
KH 9-17 Elint
1 13172U 82041C   19236.06111293 -.00000080  00000-0 -84206-5 0    01
2 13172  95.9583 185.4547 0003003 276.0377  83.9621 14.89472611    09
USA 290
1 43941U 19004A   19236.07927356 0.00001059  00000-0  16300-4 0    07
2 43941  73.5811 349.1872 0024642 294.2471  65.6842 15.53718739    09
NOSS 3-3 (A)
1 28537U 05004A   19236.09486259 0.00000000  00000-0  00000-0 0    01
2 28537  63.4243 313.5773 0339059 358.1863   1.7879 13.40781380    08
NOSS 3-3 (C)
1 28541U 05004C   19236.09496488 0.00000000  00000-0  00000-0 0    01
2 28541  63.4288 313.7786 0339641 358.1247   1.9331 13.40781405    04
FIA Radar 1
1 37162U 10046A   19236.11593345 0.00000060  00000-0  10747-3 0    03
2 37162 123.0063 131.6499 0003001 113.2496 246.7504 13.41417312    04
FIA Radar 3 r
1 39475U 13072P   19236.14754364 0.00000200  00000-0  20322-4 0    04
2 39475 120.4596 104.1041 0255861 261.5169  98.4831 14.69157554    05
SAR Lupe 5
1 33244U 08036A   19236.95914019 0.00000500  00000-0  18593-4 0    00
2 33244  98.1018 139.0673 0001999 358.4641   1.5358 15.27549215    06
Helios 2B r
1 36125U 09073B   19238.84182692 0.00000000  00000-0  00000-0 0    02
2 36125  98.1996 285.0207 0036806 279.3818  80.3964 14.77090824    08
Milstar 3
1 25724U 99023A   19238.84650306 0.00000000  00000-0  00000-0 0    01
2 25724  28.2064 170.9797 2117261 214.5525 144.4338  9.37475376    06
OTV 5
1 42932U 17052A   19238.88528238 0.00000000  00000-0  00000-0 0    05
2 42932  54.5223 225.8601 0029693  80.6107 279.2999 15.84698239    00
Helios 1A
1 23605U 95033A   19238.95704674 0.00000200  00000-0  20098-4 0    09
2 23605  98.1828 327.4346 0015399 343.4349  16.5379 14.91233697    06
FAST 1
1 37227U 10062F   19239.18261053 0.00000500  00000-0  65483-4 0    08
2 37227  71.9329 262.3476 0005000  48.8959 311.1041 14.80324574    01
'''

snapshots['test_astriagraph 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'text/plain', 'Access-Control-Allow-Origin': '*'}

CONTENT:Unknown 070914
1 90177U 07757A   19142.11009172 0.00000000  00000-0  00000-0 0    01
2 90177  28.6405  55.6760 7139573 123.6282 325.0221  2.39943421    01
CSO 1
1 43866U 18106A   19104.02036166 0.00000000  00000-0  00000-0 0    05
2 43866  98.6110  44.4325 0001684 162.5259 197.5005 14.26738299    03
USA 290
1 43941U 19004A   19034.25038896 0.00000000  00000-0  00000-0 0    06
2 43941  73.6099  86.4526 0018729  44.6193 315.3807 15.53160071    08
ESHAIL 2
1 43700U 18090A   18330.87536882 0.00000000  00000-0  00000-0 0    07
2 43700   0.0750 318.0416 0005000 318.9982 127.3114  1.00270000    05
AEHF 4
1 43651U 18079A   18300.25858909 0.00000000  00000-0  00000-0 0    05
2 43651   7.6748 299.5509 1927334 182.3182 177.6818  1.32745226    06
AEHF 4 r
1 43652U 18079B   18292.01091487 0.00000000  00000-0  00000-0 0    00
2 43652  12.4468 299.9219 4706018 177.9937 135.5054  1.83429526    00
PAN r
1 35816U 09047B   18282.71996110 0.00000000  00000-0  00000-0 0    01
2 35816  22.9471 142.3146 5167264  91.1611 325.7804  1.94974253    04
ISON 69600
1 90121U 18773A   18273.06751200 0.00000000  00000-0  00000-0 0    04
2 90121  62.8485 202.2860 6638524 253.8350 106.1650  2.06880107    09
DSN 2 r
1 41941U 17005B   18213.56543130 0.00000100  00000-0  15139-3 0    00
2 41941  21.3100  61.4050 7218605 205.1470  87.0456  2.30389691    03
IGS Opt 6
1 43223U 18021A   18168.30056652 0.00000000  00000-0  00000-0 0    00
2 43223  97.4607 288.1271 0001238 165.0178 184.2919 15.27661121    06
IGS Radar 6 r
1 43496U 18052B   18167.95995151 0.00000000  00000-0  00000-0 0    02
2 43496  97.3785 284.1465 0011502 266.9348  93.0651 15.21683580    07
IGS Radar 6
1 43495U 18052A   18163.22499904 0.00000000  00000-0  00000-0 0    02
2 43495  97.2624 279.4803 0014129  53.7498 304.7202 15.25130130    02
IGS Opt 6 r
1 43224U 18021B   18148.12499854 0.00002000  00000-0  84250-4 0    09
2 43224  97.2158 265.9641 0003245  71.2932 288.5103 15.23386603    04
USA 287
1 43465U 18036G   18139.83833779 0.00000000  00000-0  00000-0 0    03
2 43465   0.0749  83.9927 0003505 288.3053  71.7431  1.00928636    02
CBAS 1 r Db
1 43342U 18036D   18133.73566022 0.00000000  00000-0  00000-0 0    04
2 43342   0.0566  93.6184 0016521  99.4573 260.7382  1.02326553    03
CBAS 1
1 43339U 18036A   18117.06594243 0.00000000  00000-0  00000-0 0    04
2 43339   0.0547  66.4252 0005088 125.6918 234.3082  1.02201461    07
EAGLE
1 43340U 18036B   18117.06441580 0.00000000  00000-0  00000-0 0    01
2 43340   0.0596  64.2796 0003439 116.7817 243.2183  1.02131320    06
CBAS 1 r
1 43341U 18036C   18115.04896991 0.00000000  00000-0  00000-0 0    08
2 43341   0.0551  79.6538 0417135 135.0141  46.6646  1.08312763    05
ORS 5
1 42921U 17050A   18110.27452846 0.00000000  00000-0  00000-0 0    03
2 42921   0.0238 169.0721 0001130 355.4093   4.5880 14.90503959    03
OTV 5
1 42932U 17052A   18103.08332516 0.00000000  00000-0  00000-0 0    09
2 42932  54.4848 135.8907 0003000 305.5090  54.4909 15.71190888    02
SBIRS GEO 4
1 43162U 18009A   18095.79099802 0.00000000  00000-0  00000-0 0    04
2 43162   6.3252 319.8752 0006791 124.1827 235.8990  1.00270000    05

1 99992U          18078.78364164  .00000000  00000-0  00000-0 0    04
2 99992  63.3235 341.7709 0800761 110.5196 252.1151 13.49010610    00
GovSat 1
1 43178U 18013A   18046.24058247 0.00000000  00000-0  00000-0 0    00
2 43178   0.0460 254.8293 0002003  88.6147 271.3689  1.00089661    04
ISON 41700
1 90120U 17538A   18038.90025342 0.00003500  00000-0  29034-2 0    02
2 90120  24.9795  43.0554 6138627 225.9473 152.0618  3.75473860    02
USA 281
1 43145U 18005A   18016.73232019 0.00000000  00000-0  00000-0 0    07
2 43145 105.9827 142.3843 0008357 272.9216  87.0812 13.55444999    07
USA NEW
1 70003U          18014.81341543 0.00000000  00000-0  00000-0 0    06
2 70003 105.9998 139.2840 0006265 275.9232  84.0647 13.55404211    04
USA 279
1 42949U 17066A   17292.89738262 0.00000000  00000-0  00000-0 0    07
2 42949   8.1392 324.6522 2991000 180.5487 179.0910  1.48414800    08
USA 278
1 42941U 17056A   17273.78255542 -.00000501  00000-0  00000-0 0    07
2 42941  63.7330 167.0642 6776181 269.6298  90.1889  2.03452428    03
IGS Radar 5 r
1 42073U 17015B   17261.88630936 0.00002200  00000-0  87991-4 0    05
2 42073  97.1831 326.9887 0009000  83.0370 276.9629 15.25098569    01
SBIRS GEO 3 r
1 41938U 17004B   17226.86044573 0.00013236  00000-0  82035-3 0    01
2 41938  22.5837 222.2595 6958881 345.2570   1.9162  2.72948754    09
OPTSAT 3000
1 42900U 17044A   17218.89724819 0.00000000  00000-0  00000-0 0    01
2 42900  97.2000 293.1140 0002000 329.8206  30.1792 15.38252000    05
NOSS 3-8 (A)
1 42058U 17011A   17161.02542692 0.00000000  00000-0  00000-0 0    08
2 42058  63.4408 255.6854 0118000 179.5102 180.4898 13.40819991    09
NOSS 3-8 (B)
1 42065U 17011B   17161.02534667 0.00000000  00000-0  00000-0 0    09
2 42065  63.4428 255.5230 0119000 180.6735 179.3265 13.40812568    00
USA 276
1 42689U 17022A   17144.32054585 0.00000000  00000-0  00000-0 0    03
2 42689  50.0027 163.4501 0016976  69.7427 279.9823 15.56120259    05
DSN 2
1 41940U 17005A   17107.36097467 0.00000000  00000-0  00000-0 0    02
2 41940   0.0150  68.6994 0005459 225.0038 134.9962  1.00270000    05
WGS 9
1 42075U 17016A   17106.28782418 0.00000000  00000-0  00000-0 0    01
2 42075   0.1945 260.0954 2063413 295.8864 351.4187  1.00270000    05
IGS Radar 5
1 42072U 17015A   17094.87269383 0.00000000  00000-0  00000-0 0    09
2 42072  97.2241 166.8028 0009000 343.9402  16.0596 15.24523891    04
IGS Radar 5
1 42071U 17015A   17087.84954211 0.00000000  00000-0  00000-0 0    08
2 42071  97.3495 160.2996 0004000 334.5310  25.4688 15.24496229    06
SBIRS GEO 3
1 41937U 17004A   17052.51326561 0.00000000  00000-0  00000-0 0    03
2 41937   0.0150  69.4353 0001880 223.4955 136.5045  1.00270000    03
WGS 1
1 32258U 07046A   17015.41718039 0.00000000  00000-0  00000-0 0    07
2 32258   0.0448  84.9221 0003453 246.9285 113.0715  1.00270000    03
USA 250
1 39652U 14020A   17015.02195921 0.00000000  00000-0  00000-0 0    08
2 39652   2.8469 319.5183 0003455 332.8264  27.1575  1.00270006    04
WGS 8
1 41879U 16075A   16358.21353247 0.00000000  00000-0  00000-0 0    01
2 41879   3.6003  66.5855 0199996 312.3102   7.7135  1.00270000    06
ISON 61100
1 90119U 16843A   16343.42987787 0.00000142  00000-0  27797-3 0    06
2 90119  28.7816 227.6741 7149883 333.5099   3.3944  2.37617559    03
DSCS 3-9
1 23628U 95038A   16329.64722082 0.00000000  00000-0  00000-0 0    01
2 23628  10.0654  40.6121 0003516 111.6319 248.4234  1.00270000    07
UFO F8
1 25258U 98016A   16329.45184925 0.00000000  00000-0  00000-0 0    08
2 25258   7.3145  39.0000 0004809 204.6795 155.3088  1.00270000    00
FleetSatCom 7
1 17181U 86096A   16266.74107602 0.00000000  00000-0  00000-0 0    08
2 17181  14.7111   9.1749 0023795 159.0970 201.0142  1.00270000    02
Ofeq 11
1 41759U 16056A   16262.10113449 0.00138035  00000-0  24500-2 0    00
2 41759 142.5282 325.3519 0184795  50.1757 311.5128 15.32477128    00
GSSAP 4
1 41745U 16052B   16239.71428764 0.00000000  00000-0  00000-0 0    08
2 41745   0.0190 120.2942 0010000 300.4515  59.5217  1.00104330    03
GSSAP 3
1 41744U 16052A   16239.71177259 0.00000000  00000-0  00000-0 0    07
2 41744   0.0040 120.2942 0008000 355.4515   4.5217  1.00274330    01
GSSAP 3 r
1 41746U 16052C   16233.50208616 0.00000000  00000-0  00000-0 0    02
2 41746   0.8621  50.2917 0005920 265.4971  95.1165  0.98987562    06
ISON 42000
1 90118U 16730A   16230.35935117 0.00011366  00000-0  14734-2 0    03
2 90118  26.0225 336.1134 6270391 200.1137 116.5868  3.66447608    00
WGS 7
1 40746U 15036A   16212.98877681 0.00000000  00000-0  00000-0 0    05
2 40746   0.0220  79.1171 0004580 133.4127 226.5873  1.00270000    04
USA 269
1 41724U 16047A   16211.22686712 0.00000000  00000-0  00000-0 0    04
2 41724  18.6851 325.1617 6992826 178.8357 185.2363  2.21876674    06
ISON 35200
1 90117U 16707A   16207.35955033 0.00000000  00000-0  00000-0 0    01
2 90117  63.4918 231.6878 5884284 265.7474  29.0451  4.09304115    08
Mentor 7 r
1 41585U 16036B   16206.24457998 0.00000000  00000-0  00000-0 0    05
2 41585   7.6093 354.1663 0215708 185.2147 174.5696  1.04075044    02
ISON 51100
1 90116U 16697A   16197.02271432 0.00000000  00000-0  00000-0 0    04
2 90116   3.9248 273.8998 6620303 223.5734 136.4263  2.80970031    02
MUOS 5
1 41622U 16041A   16191.51826304 0.00000000  00000-0  00000-0 0    07
2 41622   9.8109 324.2407 3211951 178.9804 181.9317  1.52735617    02
MUOS 5 r
1 41623U 16041B   16177.33159821 0.00000000  00000-0  00000-0 0    05
2 41623  19.1010 322.8427 6092785 178.1097 181.9138  2.09515519    06
Mentor 7
1 41584U 16036A   16167.96105997  .00000000  00000-0  00000-0 0    08
2 41584   7.5055 353.7008 0046333  41.2140 319.1375  1.00195548    05
ISON 63700
1 90115U 16612A   16112.02101776 0.00001839  00000-0  54920-1 0    02
2 90115   5.5953  41.9123 7102035   6.8645 358.9886  2.26165691    07
ISON 144402
1 90100U 14798A   16094.39398747 0.00000000  00000-0  00000-0 0    02
2 90100  10.4683  39.0470 0206359 312.6121  45.6776  0.99706215    02
ISON 49200
1 90114U 16591A   16091.06076050 0.00017500  00000-0  11494-2 0    05
2 90114  63.3298 353.0721 6721151 268.3028  19.9584  3.04943579    01
FIA Radar 4
1 41334U 16010A   16042.12521527 0.00000000  00000-0  00000-0 0    04
2 41334 122.9820 357.1748 0001000   0.6468 359.3531 13.46533695    05
ISON 32000
1 90113U 16535A   16035.80645369 0.00022000  00000-0  12036-2 0    01
2 90113  25.7492 289.9636 5615007  15.7724 356.3818  4.69385969    01
USA 250 r
1 39653U 14020B   15290.00159653 0.00000000  00000-0  00000-0 0    02
2 39653  10.9881 261.7799 4853383 283.0181  28.8166  1.86026107    05
NOSS 3-7 (R)
1 40981U 15058R   15286.05573889 0.00000000  00000-0  00000-0 0    01
2 40981  63.4353 281.3310 0124989 179.3855 180.6145 13.40311788    08
NOSS 3-7 (R)
1 40979U 15058R   15282.84751800 0.00000000  00000-0  00000-0 0    02
2 40979  63.4350 289.4959 0126213 179.4631 180.5064 13.40312760    05
NOSS 3-7 (A)
1 40964U 15058A   15282.84746112 0.00000000  00000-0  00000-0 0    06
2 40964  63.4349 289.4988 0126612 179.0834 180.9166 13.40379204    06
NOSS 3-7 r
1 40978U 15058Q   15282.12325980 0.00000000  00000-0  00000-0 0    08
2 40978  64.7704 289.8805 0219834 284.4137  73.2663 14.78941654    00
MUOS 1
1 38093U 12009A   15278.37810261 0.00000000  00000-0  00000-0 0    09
2 38093   3.8500 332.8334 0059750 180.1670 179.8329  1.00270000    05
MUOS 4
1 40887U 15044A   15259.40453690 0.00000000  00000-0  00000-0 0    07
2 40887   5.0430 328.7371 0001000 140.0000 220.0000  1.00270000    02
ISON 63200
1 90099U 14792C   15253.75900097 0.00000300  00000-0  56680-3 0    07
2 90099  28.8113 318.4133 7231764 181.9215 173.1245  2.27903210    01
MUOS 3 r
1 40375U 15002B   15253.71322792 0.00000000  00000-0  00000-0 0    09
2 40375  18.5498 286.0940 6083604 254.8778  33.8705  2.08929700    06
GSSAP 2
1 40100U 14043B   15253.07958315 0.00000000  00000-0  00000-0 0    04
2 40100   0.0581   5.0168 0002000 174.4752 185.4978  1.00270000    05
MUOS 4 r
1 40888U 15044B   15251.42355530 0.00000000  00000-0  00000-0 0    06
2 40888  19.0850 326.7373 6080000 179.7900 180.2000  2.08796000    04
MUOS 3
1 40374U 15002A   15250.99325315 0.00000000  00000-0  00000-0 0    09
2 40374   4.8951 328.7601 0058632 178.7298 181.2702  1.00270000    01
Elisa 99450
1 99450U 15720B   15224.89694404 0.00000500  00000-0  94309-4 0    07
2 99450  98.0802 297.9838 0005267 322.6356  37.3643 14.64577524    00
Essaim 99449
1 99449U 15720A   15220.86620070 0.00000000  00000-0  00000-0 0    02
2 99449  98.2702 294.2724 0001261 247.1290 112.8708 14.63067828    02
Sicral 2
1 40614U 15022B   15182.22211214 0.00000000  00000-0  00000-0 0    00
2 40614   0.0470  35.8635 0001000 157.7440 202.2560  1.00270000    04
LightSail-A
1 40661U 15025L   15159.06218063 0.02648498  00000-0  67226-1 0    05
2 40661  55.0136 260.3261 0243391 227.2228 135.1229 15.14087982    04
NOSS 6 P/S
1 14691U 84012B   15157.92364826 0.00030000  00000-0  49029-2 0    07
2 14691  63.2063 101.5270 0508509  92.9460 267.6227 14.10126907    09
OTV 4
1 40651U 15025A   15153.41113187 0.00000000  00000-0  00000-0 0    03
2 40651  38.0218 255.0262 0009791   9.5017 350.5955 15.85156401    08
CLIO ISON 143663
1 40208U 14055A   15133.18330974 0.00000000  00000-0  00000-0 0    00
2 40208   0.0440  44.7375 0011405 315.6929  44.2191  1.00270000    01
IGS 9
1 40381U 15004A   15116.92747674 0.00000000  00000-0  00000-0 0    09
2 40381  97.4995 188.9595 0006379  74.2520 285.7480 15.27764783    05
ISON 62200
1 90112U 15614A   15114.81795662 0.00000505  00000-0  12336-2 0    06
2 90112   5.6630 163.6807 7185228 168.6699 227.4237  2.32366316    03
IGS 9 r
1 40382U 15004B   15111.89449586 0.00015000  00000-0  56321-3 0    08
2 40382  97.4877 184.9834 0012862 106.5662 253.4337 15.27156191    08
ISON 60601
1 90111U 15607A   15107.89871643 0.00001000  00000-0  13050-1 0    05
2 90111  10.6896  53.7508 7057175 341.8331   1.9904  2.37655470    09
NOSS 1-7 PS
1 16592U 86014B   15105.10231904 0.00001500  00000-0  68791-3 0    07
2 16592  63.3160  10.7169 0540649  97.1787 262.8213 13.64013249    02
IGS Opt 5
1 40538U 15015A   15095.89867762 0.00000000  00000-0  00000-0 0    08
2 40538  97.5000 168.3467 0003000 146.0759 213.9239 15.17587539    03
IGS Opt 5 r
1 40539U 15015B   15091.90843653 0.00012500  00000-0  42829-3 0    06
2 40539  97.2694 164.0290 0054534 346.4875  12.9436 15.28766798    04
GSSAP 1
1 40099U 14043A   15075.15735905 0.00000000  00000-0  00000-0 0    00
2 40099   0.1049 100.4273 0004545 328.1692  31.8192  1.00139487    01
JAWSAT
1 26065U 00004E   15054.09556197 0.00000000  00000-0  00000-0 0    03
2 26065 100.2306 253.2202 0037976 171.2560 188.7439 14.36618221    07
WGS 4 r
1 38071U 12003B   15053.99435768 0.00000008  00000-0  19809-3 0    01
2 38071  22.0934 101.0464 8200411 170.2769 234.7800  1.15520163    03
ANGELS
1 40101U 14043C   15047.61959938 0.00000000  00000-0  00000-0 0    08
2 40101   0.2861   6.6268 0010708 280.8296  79.0674  0.98918407    03
ISON 20100
1 90110U 15545A   15045.04292572 0.00000901  00000-0  94884-3 0    06
2 90110  63.6259 336.8399 3953340 298.9469  27.1475  7.14307836    04
CLIO r
1 40209U 14055B   15044.70114305 0.00000000  00000-0  00000-0 0    08
2 40209  20.6201 168.7594 4753934 201.2359 129.5757  1.84619428    04
ISON 54102
1 90109U 15523A   15029.57905560 0.00005800  00000-0  46958-2 0    09
2 90109  10.4211 317.0590 6904054 338.7542   2.8690  2.72178709    03
USA 259
1 40344U 14081A   14350.26041667 0.00000000  00000-0  00000-0 0    07
2 40344  62.8515 212.5009 6775547 266.7169 108.1768  2.03519385    08
ISON 47601
1 90108U 14845A   14345.78155113 0.00130000  00000-0  18587-2 0    06
2 90108  26.1828  35.4683 6439223 226.4502  57.9456  3.48344430    05
ISON  59700
1 90106U 14844A   14344.93775833 0.00001037  00000-0  11372-2 0    08
2 90106   1.7288 107.8123 7133426  65.2861 350.7480  2.42060426    03
ISON 68600
1 90107U 14844B   14344.56595229 0.00000000  00000-0  00000-0 0    00
2 90107   5.9532  78.8720 6279691 158.2173 249.7319  2.09703600    04
ISON 64800
1 90103U 14820A   14329.50798226 0.00000000  00000-0  00000-0 0    09
2 90103  63.9343 196.8175 6524807 260.9662  25.3221  2.21892500    07
ISON 81600
1 90105U 14824A   14324.50091989 0.00000000  00000-0  00000-0 0    02
2 90105  20.9494 158.0091 5607648 162.1109 197.8891  1.76312000    08
ISON 37600
1 90097U 14792A   14324.22065240 0.00000000  00000-0  00000-0 0    06
2 90097   4.5567 104.4372 5658746  77.6790 337.3548  3.99368491    07
WGS 6
1 39222U 13041A   14320.90546396 0.00000000  00000-0  00000-0 0    02
2 39222   0.0150 270.3700 0001000 210.8973 125.3893  1.00270000    07
ISON 64800
1 70283U          14320.49456760 0.00000000  00000-0  00000-0 0    04
2 70283  63.9317 197.8354 6523714 261.0625  25.2811  2.21894000    03
ISON 59501
1 70184U          14317.09270388 0.00000000  00000-0  00000-0 0    06
2 70184  10.7796 334.9840 6996980 142.3878 218.4241  2.41793291    03
ISON 37600
1 70036U          14314.68605640 0.00000000  00000-0  00000-0 0    07
2 70036   4.5600 111.6760 5662209  63.5018 295.3748  3.99208818    04
ISON 144402
1 71171U          14313.95572657 0.00000000  00000-0  00000-0 0    08
2 71171   9.6970  44.0880 0220655 176.3869 183.8703  0.99723473    08
ISON 77400
1 90104U 14735A   14311.60381953 0.00000000  00000-0  00000-0 0    02
2 90104  11.4240 296.6895 4859083 216.4018  97.9237  1.86027107    01
Trumpet 2
1 23609U 95034A   14301.66813519 0.00000046  00000-0  00000-0 0    02
2 23609  63.4451 255.3436 6933054 268.9888  17.8027  2.00608837    01
Trumpet 1
1 23097U 94026A   14301.56449094 0.00000264  00000-0  00000-0 0    07
2 23097  64.0600 221.8444 6447805 273.5901  20.0715  2.00616570    07
Unknown 140823
1 99424U 14735B   14291.72435747 0.00000000  00000-0  00000-0 0    07
2 99424  11.4451 298.6308 4870003 212.6338 104.7926  1.86027107    00
USA 200 r
1 32707U 08010B   14290.43525739 0.00000400  00000-0  11525-2 0    05
2 32707  63.5611  67.2355 7356940 250.7816  21.9391  2.11366141    04
Unknown 141017
1 90096U 14790A   14290.32717842 0.00001216  00000-0  00000-0 0    08
2 90096  63.5519 329.1665 7278087 274.7780  13.2468  2.04981299    09
Unknown 141011
1 90095U 14784A   14284.61299940 0.00000000  00000-0  00000-0 0    09
2 90095  63.1946 229.8784 6997432 265.8347  18.5519  2.38687000    02
Unknown141003B
1 90094U 14776B   14283.36769152 0.00000000  00000-0  00000-0 0    07
2 90094  24.2135 306.5490 5129031 168.6285 210.0496  1.94990330    05
Unknown141003A
1 90093U 14576A   14276.74591757 0.00003373  00000-0  13244-0 0    02
2 90093   3.8791 318.8159 7248031 272.6482  14.1023  2.08151131    05
GPS 70 r
1 39742U 14026B   14262.60191257 0.00000000  00000-0  00000-0 0    07
2 39742  54.9489 140.2888 0043262 346.5976  13.4024  1.95489795    05
Unknown 140824
1 90092U 14735A   14242.95503590 0.00000000  00000-0  00000-0 0    02
2 90092  15.1286   9.3792 0089042  56.2201 304.3016  0.99531895    00

1 99999U 14736A   14236.81819308  .00000000  00000-0  00000-0 0    03
2 99999  15.2395   9.6197 1034942 127.6835 195.0717  1.21226772    09
USA 58
1 20562U 90031C   14217.03818759 0.00000000  00000-0  00000-0 0    07
2 20562  89.7939 335.9734 0001983 235.6846 124.3153 14.59434657    08
GSSAP r
1 40102U 14043D   14213.29410491 0.00000000  00000-0  00000-0 0    03
2 40102   0.4803 306.6432 0009502   3.3829 356.6355  0.98907512    03
Trumpet 3
1 25034U 97068A   14203.73894686 -.00001155  00000-0  00000-0 0    01
2 25034  63.2760 326.0072 6828663 284.1592  13.6226  2.00610838    08
Unknown 140607
1 99224U 14658A   14158.05870913 0.00000000  00000-0  00000-0 0    05
2 99224  63.2984  59.7602 0649136  78.7674 281.2326 13.86763379    04
USA 252
1 39751U 14027A   14144.03015972 0.00000000  00000-0  00000-0 0    03
2 39751  20.6956 263.7634 7074111 178.0121  96.0401  2.24037956    05
Unk
1 99406U 14602A   14109.95853628 0.00001600  00000-0  51820-3 0    01
2 99406  63.2995  78.8961 0737856  80.7875 279.2125 13.43060588    00
Ofeq 10
1 39650U 14019A   14106.07914909 0.00070000  00000-0  19916-2 0    07
2 39650 140.9470 242.8354 0162954 123.9544 237.6834 15.22939887    00
DMSP F19
1 39630U 14015A   14095.71497852 0.00000000  00000-0  00000-0 0    07
2 39630  98.8700 111.1816 0009822 285.0801  74.9198 14.13792356    08
DMSP F19
1 72910U          14093.66263531 0.00000000  00000-0  00000-0 0    01
2 72910  98.8700 109.1454 0009822 295.9013  64.2057 14.13825356    09
Unknown 140303
1 99099U 14562A   14064.88053226 0.00910809  00000-0  25276-3 0    08
2 99099  21.5237 107.5170 4930158 197.9328 135.9812  5.98574706    08
Unknown140221E
1 99096U 14552E   14061.90935522 0.00002026  00000-0  23663-2 0    02
2 99096  63.2369  22.5189 7322465 270.6871 330.9436  2.18857743    04
SBIRS GEO 2
1 39120U 13011A   14055.40411744 0.00000000  00000-0  00000-0 0    04
2 39120   5.2166 320.3571 0003941 228.4966 131.4792  1.00270000    09
WGS 3 r
1 36109U 09068B   14053.01007272 0.00000000  00000-0  00000-0 0    07
2 36109  24.6755   3.9597 8162708 292.0115 296.9198  1.18380000    00
WGS 6 r
1 39223U 13041B   14052.84022525 0.00000000  00000-0  00000-0 0    01
2 39223  23.8998 115.7659 8281093 230.7244  23.7049  1.09740000    03
Essaim 14547A
1 99091U 14547A   14052.77390121 0.00000000  00000-0  00000-0 0    04
2 99091  98.3277  94.6861 0003236  86.3983 273.6664 14.78500946    09
Essaim 14544A
1 99221U 14544A   14052.75428076 0.00000500  00000-0  71134-4 0    00
2 99221  98.3503  87.4467 0000628   9.4204 350.5794 14.76943147    03
MUOS 2
1 39206U 13036A   14019.85792968 0.00000000  00000-0  00000-0 0    05
2 39206   4.9431 328.0286 0057037 359.3804   0.6127  1.00270000    02
WGS 5 r
1 39169U 13024B   14005.12611120 0.00000000  00000-0  00000-0 0    05
2 39169  25.4033  39.8556 8235545 234.2618  26.0965  1.08104166    06
Unknown 140103
1 99086U 14503A   14003.81258995 0.00000000  00000-0  00000-0 0    03
2 99086  11.2184  44.0392 0005179 296.4846  63.4155  1.00270000    08
Unknown131229B
1 99085U 13863B   14003.80411560 0.00000000  00000-0  00000-0 0    08
2 99085   0.1713  81.5121 0003189 144.4001 215.5999  1.00376385    01
AEHF 3
1 39256U 13050A   13362.30780316 0.00000000  00000-0  00000-0 0    00
2 39256   4.8845 304.1814 0345112 179.9578 336.7311  0.99205949    00
Unknown 131224
1 99155U 13858A   13358.26109368 0.00000000  00000-0  00000-0 0    02
2 99155   4.9439 303.9995 0480203 182.4544 328.4754  0.99493725    04
FIA Radar 3 r
1 39475U 13072P   13345.20809444 0.00000000  00000-0  00000-0 0    01
2 39475 120.4582 244.1978 0286404 342.8858  17.1141 14.61081031    09
FIA Radar 3
1 39462U 13072A   13344.12994719 0.00000000  00000-0  00000-0 0    07
2 39462 123.0082 236.8229 0012759 307.2947  52.7053 13.47778591    04
Unknown 131121
1 90091U 13825A   13341.95489258 -.00001113  00000-0  00000-0 0    00
2 90091  62.6309  14.1059 7269922 270.7699  14.5171  2.00560139    09
FIA Radar 3
1 78817U 13072A   13341.53383309 0.00000000  00000-0  00000-0 0    03
2 78817 122.9957 228.6601 0014502 298.6008  61.3992 13.47753224    06
FIA Radar 3 r
1 78820U 13072P   13341.44424121 0.00000000  00000-0  00000-0 0    05
2 78820 120.4883 230.9287 0276875 339.4109  19.5967 14.61190032    02
Unknown 131120
1 99079U 13825A   13335.71953869 0.00002800  00000-0  12676-2 0    03
2 99079  28.4923   5.3250 7184644 218.6097  57.5864  2.38762084    01
WGS 5
1 39168U 13024A   13317.25465817 0.00000000  00000-0  00000-0 0    03
2 39168   0.0350  91.4850 0002000 180.0000 180.0000  1.00270000    04
Unknown 131021
1 99075U 13794A   13296.82824030 0.00000000  00000-0  00000-0 0    05
2 99075   2.9784 314.0976 0002683 308.1391  51.8406  1.00270000    00
Unknown 131012
1 99218U 13785A   13295.97738589 0.00001000  00000-0  13232-3 0    07
2 99218  98.3481 327.0658 0000500  25.7826  20.4778 14.80017172    09
MUOS 2 r
1 39207U 13036B   13282.13634292 0.00000000  00000-0  00000-0 0    03
2 39207  18.6538 310.2079 6155019 204.8400 104.9075  2.09952624    06
Unknown 131001
1 99070U 13774A   13278.79023945 0.00000000  00000-0  00000-0 0    00
2 99070   5.2985 319.5957 0005819 266.2397  93.7006  1.00270000    08
Unknown 130929
1 99069U 13772A   13273.75224919 0.00000138  00000-0  00000-0 0    03
2 99069  64.0272 258.5812 6654330 276.1244  16.1326  2.00614452    03
SAR Lupe3or5
1 99068U 13770A   13271.79560051 0.00000000  00000-0  00000-0 0    00
2 99068  98.1752 308.5386 0003602   0.3543 359.6456 15.27557102    08
Unknown 130725
1 99212U 13706A   13248.88429323 0.00000200  00000-0  51524-3 0    02
2 99212  27.9553 235.4646 7168230 359.9657 359.9774  2.34151114    03
USA 245
1 39232U 13043A   13241.13429432 0.00025000  00000-0  21639-3 0    03
2 39232  97.8732 304.6187 0528234 192.3915 167.7736 14.80683858    08
Sicral 1
1 26694U 01005A   13214.20728829 0.00000000  00000-0  00000-0 0    05
2 26694   4.8244  62.5072 0004226 116.2035 243.8645  1.00270000    07
SBIRS GEO 2 r
1 39121U 13011B   13206.14342780 0.00002225  00000-0  10769-2 0    02
2 39121  21.9142 267.5106 7256990 274.7545   7.9326  2.29613940    09
Unknown 130704
1 99210U 13685A   13199.96892181 0.00001150  00000-0  92963-3 0    03
2 99210  63.3059 191.0441 0405425 116.8184 243.1816 13.57884301    03
Unk 130404
1 99208U 13594A   13196.65856129 0.00430000  00000-0  27787-2 0    05
2 99208  20.2342 280.8648 5993339 159.4367 242.7508  4.16919351    02
Unknown 130608
1 99064U 13659A   13171.34611362 0.00000000  00000-0  00000-0 0    04
2 99064   4.7115  62.4659 0004148   8.0943 351.9292  1.00427101    08
Object 10062X
1 99207U 10062X   13155.25626156 0.00000000  00000-0  00000-0 0    07
2 99207  72.0259 255.5944 0020000 337.6259  66.2618 14.77170909    09
Sicral 1B
1 34810U 09020A   13141.79392576 0.00000000  00000-0  00000-0 0    08
2 34810   0.1028  82.0406 0005392  27.2992  68.0656  1.00270000    00
Unknown 130428
1 99143U 13618A   13129.37386472 0.00000000  00000-0  00000-0 0    04
2 99143  97.1534 250.2405 0005719 244.0786 172.8044 15.46470036    00
IGS 8 Db D
1 39064U 13002D   13124.04353781 0.00028336  00000-0  12595-2 0    09
2 39064  97.6067 245.9456 0025211 326.1169  33.2972 15.21264961    06
IGS 8 Db E
1 39065U 13002E   13122.03288079 0.00041000  00000-0  17432-2 0    02
2 39065  97.4942 243.7765 0002996 272.3416  87.6582 15.23070998    05
IGS 8 Db F
1 39066U 13002F   13122.01706688 0.00020500  00000-0  63916-3 0    03
2 39066  97.5213 244.8534 0048335 174.3422 185.6576 15.32084308    01
IGS 8B
1 39062U 13002B   13122.01510889 0.00049000  00000-0  20498-2 0    08
2 39062  97.4912 243.9044 0001752 178.8640 181.1358 15.23623977    01
IGS 8A
1 39061U 13002A   13121.97756745 0.00000000  00000-0  00000-0 0    06
2 39061  97.4279 242.7329 0003000 129.2047 230.7951 15.17643370    00
IGS 8 r
1 39063U 13002C   13120.00020091 0.00002800  00000-0  22745-3 0    02
2 39063  97.6606 239.5592 0016692 194.3256 165.6742 14.99562829    02
99048
1 99048U          13118.00841701 0.00036500  00000-0  15440-2 0    08
2 99048  97.4912 239.8975 0001752 142.9081 217.0918 15.23247676    08
99050
1 99050U          13117.99836650 0.00002000  00000-0  16259-3 0    03
2 99050  97.6576 237.5699 0015692 204.0608 155.9391 14.99547427    04
99049
1 99049U          13116.98765167 0.00012800  00000-0  39776-3 0    01
2 99049  97.5373 239.8673 0054335 195.1828 164.8171 15.31880471    05
99047
1 99047U 13595B   13115.98761716 0.00023000  00000-0  99272-3 0    08
2 99047  97.4882 237.6643 0002996 353.5123   6.4875 15.22560744    04
99046
1 99046U          13115.97760364 0.00000090  00000-0  44798-5 0    00
2 99046  97.4409 236.8971 0003000 170.0754 189.9244 15.17645170    00
Pleiades 1B
1 39019U 12068A   13089.90057915 0.00000000  00000-0  00000-0 0    09
2 39019  98.2085 166.2336 0001000   0.0000  57.5005 14.58553606    09
AEHF 2
1 38254U 12019A   13058.76513473 0.00000000  00000-0  00000-0 0    01
2 38254   3.1694 313.1993 0006856 338.0255  21.9467  1.00270000    06
OTV 3
1 39025U 12071A   12348.51262355 0.00015000  00000-0  10571-3 0    03
2 39025  43.4959 127.0411 0012422 332.5991  27.4004 15.73041223    09
Muos r
1 38094U 12009B   12319.41029435 0.00000000  00000-0  00000-0 0    03
2 38094  18.0821 266.9340 6213463 273.3248  22.1483  2.11710260    00
Unknown 120530
1 90090U 12651A   12310.78408745 0.00000452  00000-0  21111-3 0    06
2 90090  63.3240 192.1322 0669187  50.1557 309.7753 13.41089659    08
NOSS 3-6 (P)
1 38773U 12048P   12263.16874014 0.00000000  00000-0  00000-0 0    01
2 38773  63.4386  28.3553 0127283 180.8086 179.1914 13.40519112    09
NOSS 3-6 (P)
1 79603U 12048P   12261.45298345 0.00000000  00000-0  00000-0 0    05
2 79603  63.4386  32.7196 0127283 180.8197 179.1803 13.40494112    00
NOSS 3-6 r
1 38770U 12048N   12260.17511925 0.00068242  00000-0  54452-2 0    09
2 38770  64.6150  33.5493 0214551 293.7818  66.2662 14.83675255    06
NOSS 3-6 (P)
1 38771U 12048P   12260.11029461 0.00000000  00000-0  00000-0 0    09
2 38771  63.4386  36.1322 0127783 180.4284 179.5715 13.40441112    06
NOSS 3-6 (A)
1 38758U 12048A   12260.11019213 0.00000000  00000-0  00000-0 0    08
2 38758  63.4386  36.1321 0127783 180.8284 179.1715 13.40501612    02
DSP F15 Cover
1 96143U 90095E   12252.35954447 0.00000000  00000-0  00000-0 0    02
2 96143  14.1584  29.3941 0086528 131.4655 229.2929  0.99285540    07
STPSat 2
1 37222U 10062A   12232.94555056 0.00000320  00000-0  45657-4 0    03
2 37222  71.9651 172.3631 0018000 196.5016 163.4984 14.76589784    01
Unknown 120723
1 90089U 12705A   12220.02431339 0.00023389  00000-0  95520-3 0    05
2 90089  25.6421 131.8563 7019888 177.3023 191.5831  2.65684060    04
USA 237 r
1 38529U 12034B   12201.16401249 0.00000000  00000-0  00000-0 0    03
2 38529   3.5829 299.0775 0197347 196.4398 163.3022  1.03226679    09
USA 236
1 38466U 12033A   12201.02221518 0.00000000  00000-0  00000-0 0    06
2 38466   4.9082 274.5087 0005000 175.6170 184.6492  1.00273922    07
Elisa W23
1 38009U 11076C   12199.27393649 0.00000200  00000-0  39016-4 0    08
2 38009  98.1819 272.9488 0001486 102.4077 257.7291 14.63066078    02
Elisa W11
1 38007U 11076A   12199.27377032 0.00000200  00000-0  38982-4 0    05
2 38007  98.1589 272.9104 0010685 143.9017 216.2908 14.63069705    09
IGS 7A
1 37954U 11075A   12198.09926076 0.00000000  00000-0  00000-0 0    05
2 37954  97.5197 269.8670 0010529 310.4530  49.5784 15.17603387    07
USA 237
1 38528U 12034A   12197.78746808 0.00000000  00000-0  00000-0 0    07
2 38528   3.5184 299.5137 0050303 310.7722  48.7936  0.99909995    04
Elisa E12
1 38010U 11076D   12196.19638590 0.00000256  00000-0  49937-4 0    09
2 38010  98.1819 272.4855 0001493 112.0474 248.0886 14.63069469    03
Elisa E24
1 38008U 11076B   12196.19622887 0.00000257  00000-0  50093-4 0    04
2 38008  98.1589 272.4606 0010692 121.7407 238.4838 14.63068126    01
Unknown 120530
1 99015U 12651A   12169.31301658 0.00001300  00000-0  15136-3 0    01
2 99015  98.1973 111.5061 0010333 298.8158  61.1840 14.85307145    07
FIA Radar 2
1 38109U 12014A   12097.24217641 0.00000000  00000-0  00000-0 0    08
2 38109 122.9914 224.3990 0009283 284.9437  75.1044 13.45794928    02
FIA Radar 2
1 79701U 12014A   12095.23647071 0.00000000  00000-0  00000-0 0    02
2 79701 123.0192 218.2476 0016360 317.0451  42.9234 13.45650207    08
SAR Lupe 3or5
1 70002U 08036A   12090.39115859 0.00004000  00000-0  14855-3 0    02
2 70002  98.1320  66.2797 0014999 187.0872 172.9126 15.27484427    08
IGS 7A r
1 37955U 11075B   12082.87443186 0.00005600  00000-0  21802-3 0    07
2 37955  97.4180 155.2591 0027670  42.0496 317.9502 15.25664235    01
WGS 4
1 38070U 12003A   12063.65981561  .00000000  00000-0  00000-0 0    00
2 38070   0.0541 274.4832 0549995 184.8475 175.1525  1.00180033    00
GeoLite
1 26770U 01020A   11349.95867440 0.00000000  00000-0  00000-0 0    09
2 26770   2.7931  51.9289 0018954 357.4321   2.5909  0.98843605    00
RadioAstron
1 37755U 11037A   11343.96971181 0.00000000  00000-0  00000-0 0    06
2 37755  74.9673 308.4764 8612669 316.2510   3.7923  0.11953359    03
Unknown 111101
1 90088U 11805A   11309.06268930 0.00195000  00000-0  52546-3 0    01
2 90088  24.0237  18.9989 6960288 186.2817 155.5822  2.76778641    07
IGS 6A
1 37813U 11050A   11272.94111109 0.00000619  00000-0  60047-4 0    08
2 37813  97.6931  31.0490 0002497 291.0367  69.0585 14.92733754    04
IGS 6A r
1 37814U 11050B   11272.85741330 0.00000455  00000-0  39984-4 0    08
2 37814  97.6540  31.0070 0019112   2.8113 357.3213 14.96485088    03
Canyon 6
1 07963U 75055A   11221.82705374 0.00000000  00000-0  00000-0 0    03
2 07963  20.8266 336.9310 1291601 251.9194  93.6187  1.00161775    09
Mentor 5
1 37232U 10063A   11213.60548493 0.00000000  00000-0  00000-0 0    07
2 37232   6.4453 263.4062 0035159 336.2384  23.5997  1.00277406    08
Mentor 1
1 23567U 95022A   11212.97783719 0.00000000  00000-0  00000-0 0    02
2 23567  10.0373  68.5437 0121312  21.6476 338.8609  1.00273447    03
Canyon 7
1 10016U 77038A   11210.94542121 0.00000000  00000-0  00000-0 0    09
2 10016  11.2708   6.6753 1234411 353.9543   4.6847  1.00230764    06
SAR Lupe 3
1 32283U 07053A   11203.31709745 0.00001300  00000-0  48521-4 0    07
2 32283  98.1293 149.8191 0005557 188.9386 171.0613 15.27414496    02
ORS 1
1 37728U 11029A   11183.10603239 0.00006852  00000-0  10000-3 0    06
2 37728  40.0000 125.8626 0009897 284.9325  75.0391 15.54660733    04
Unknown 110623
1 90087U 11674A   11177.96275344 0.00000100  00000-0  00000-0 0    04
2 90087  26.7578 123.5582 7347027 137.0879 222.9119  2.00830285    06

1 99994U 11674A   11176.13115708 0.00000000  00000-0  00000-0 0    03
2 99994  26.2366 130.3455 6105404 148.2332 313.8428  4.01632994    07

1 99995U 11674A   11176.12751252 0.00000000  00000-0  00000-0 0    02
2 99995  26.4366 129.5536 5483915 149.7695 295.2928  5.02022994    05

1 99996U 11674A   11176.12140414 0.00000000  00000-0  00000-0 0    04
2 99996  26.5366 129.1682 4902726 151.7450 268.2928  6.02405994    07

1 99993U 11674A   11176.08369001 0.00000000  00000-0  00000-0 0    04
2 99993  26.1166 131.3682 6781610 145.7450 274.2928  3.01235994    02
FAST 2
1 37380U 10062M   11155.19780612 0.00000130  00000-0  18663-4 0    02
2 37380  71.9889  68.1025 0017205 296.9102  63.0897 14.76335623    04
DSP F13 r
1 18584U 87097B   11154.57379289 0.00000000  00000-0  00000-0 0    02
2 18584  12.4519  22.5409 0005636  88.0849 271.9918  1.01240645    09
SBIRS GEO 1
1 37481U 11019A   11154.45872124 0.00000000  00000-0  00000-0 0    03
2 37481   6.4830 319.9777 0001300 143.8525 216.1475  1.00270000    07
DSCS 3-6
1 22009U 92037A   11148.79132668 0.00000000  00000-0  00000-0 0    04
2 22009   8.2184  58.4688 0002761 263.7119  96.2686  1.00452281    02
2010-062 UNID
1 78701U 10062X   11120.10505598 0.00000400  00000-0  57405-4 0    02
2 78701  71.9574 145.3579 0017000 355.7358   4.2641 14.76352554    05
NOSS 3-5 (B)
1 37391U 11014B   11110.75281113 0.00000000  00000-0  00000-0 0    05
2 37391  63.4047 338.3792 0127413 180.4827 179.5173 13.39341423    08
NOSS 3-5 (B)
1 79937U 11014B   11110.75281113 0.00000000  00000-0  00000-0 0    07
2 79937  63.4047 338.3792 0127413 180.4827 179.5173 13.39341423    00
NOSS 3-5 (B)
1 37387U 11014B   11109.03548857 0.00000000  00000-0  00000-0 0    00
2 37387  63.4167 342.7331 0128413 180.9847 179.0943 13.39251023    08
NOSS 3-5 (A)
1 37386U 11014A   11107.10689160 0.00000000  00000-0  00000-0 0    08
2 37386  63.4238 346.0103 0128090 179.8530 180.1470 13.34368235    04
USA 227
1 37377U 11011A   11098.49400289 0.00000000  00000-0  00000-0 0    09
2 37377   4.9151 343.8190 0001043  15.4298 344.5885  1.00270000    01
SAR Lupe 5
1 33244U 08036A   11098.02690432 0.00001200  00000-0  44740-4 0    07
2 33244  98.1680  35.7157 0016319 346.4017  13.5981 15.27334359    02
Ekran 5
1 11890U 80060A   11087.45687140 0.00000000  00000-0  00000-0 0    08
2 11890  14.3967 346.5687 0018148  37.1907 322.9468  1.00283477    05
SAR Lupe 4
1 32750U 08014A   11077.19385881 0.00002300  00000-0  86015-4 0    01
2 32750  98.1839 246.5658 0017316  10.7656 349.2342 15.27216362    08
OTV 2
1 37375U 11010A   11073.71563114 0.00007980  00000-0  39958-4 0    03
2 37375  42.8585 237.5217 0018908 356.6571   3.2257 15.80528259    09
SAR Lupe 1
1 29658U 06060A   11070.12965775 0.00001600  00000-0  59766-4 0    00
2 29658  98.1769 237.9832 0015428 236.5024 123.4974 15.27285723    00
HAPS r
1 37229U 10062H   11062.78081731 0.00000150  00000-0  21631-4 0    03
2 37229  71.9874 271.7369 0017000 117.2072 242.7927 14.76146611    04
Ofeq 9
1 36608U 10031A   11062.70774936 0.00002800  00000-0  95322-4 0    09
2 36608 141.7685   4.6085 0165306 274.0977  85.9015 15.17341025    04
FAST 1
1 37227U 10062F   11057.21878648 0.00000076  00000-0  00000-0 0    04
2 37227  71.9724 283.9188 0016148 131.5768 228.6802 14.76395401    01
DSCS 3-7
1 22719U 93046A   11055.93398839 0.00000000  00000-0  00000-0 0    00
2 22719   6.8249  63.1383 0005558 302.6320  57.3264  0.99006663    01
DSP F15 r3
1 20932U 90095D   11055.88946838 0.00000000  00000-0  00000-0 0    08
2 20932  12.9195  36.6967 0072353 302.6888  56.6275  0.99915351    00
NanoSail-D
1 37361U 10062L   11053.18324610 0.00045000  00000-0  60443-2 0    05
2 37361  71.9732 292.6219 0023333  99.1733 261.2301 14.79073791    01
TecSAR
1 32476U 08002A   11049.05080476 0.00003000  00000-0  68921-4 0    03
2 32476  41.0264  26.3829 0077736 116.4231 243.5763 15.38583238    05
RAX
1 37223U 10062B   11047.27696737 0.00000210  00000-0  00000-0 0    02
2 37223  71.9744 305.5778 0020243 156.1195 204.0952 14.77236729    05
O/OREOS
1 37224U 10062C   11043.43618410 0.00000219  00000-0  00000-0 0    08
2 37224  71.9758 314.1598 0019424 162.0076 198.1778 14.76892599    01
Ofeq 7
1 31601U 07025A   11041.01942323 0.00001650  00000-0  74097-4 0    02
2 31601 141.7491 116.2780 0091897 282.8335  77.1657 15.16476805    06
SAR Lupe 2
1 31797U 07030A   11039.78731563 0.00001500  00000-0  56307-4 0    05
2 31797  98.1084 273.2461 0009814 290.2418  69.7581 15.27193401    01
Ofeq 5
1 27434U 02025A   11039.78070777 0.00001700  00000-0  11165-3 0    04
2 27434 143.4626 301.4704 0026074 352.9413   7.0579 15.06461984    05
USA 224
1 37348U 11002A   11023.83162841 0.00008800  00000-0  50440-4 0    05
2 37348  97.9000 139.0368 0563457 277.2512  82.7487 14.79617543    01
STPSAT 2 r
1 37228U 10062G   11022.74152336 0.00000000  00000-0  00000-0 0    01
2 37228  71.9734 359.9669 0010000 194.6902 165.3098 14.76000000    04
FASTSAT
1 37225U 10062D   11014.05373812 0.00000060  00000-0  85753-5 0    06
2 37225  71.9620  19.0237 0019965 207.0682 152.9317 14.76490180    01
Rhyolite 3
1 10508U 77114A   11008.74855715 0.00000000  00000-0  00000-0 0    09
2 10508  19.0226 351.8409 0020259 213.5990 146.2844  1.00289870    07
DSP F9 r2
1 12371U 81025C   11008.65766043 0.00000000  00000-0  00000-0 0    00
2 12371  14.0354 356.4170 0050104 158.5486 201.6742  1.01328057    05
DSP F7 Cover
1 09856U 77007D   11008.58424549 0.00000000  00000-0  00000-0 0    03
2 09856  13.5082 335.8751 0280774 338.3763  20.7070  1.00562393    07
Canyon 3
1 04510U 70069A   11008.55443638 0.00000000  00000-0  00000-0 0    03
2 04510  17.7662 292.6247 0869018 244.5444 106.2216  1.00243524    01
Canyon 5
1 06317U 72101A   11008.54416051 0.00000000  00000-0  00000-0 0    07
2 06317  20.0936 334.3235 1324186 283.8601  61.7469  1.00221794    04
Vortex 1 r
1 10942U 78058B   11005.78215515 0.00000000  00000-0  00000-0 0    08
2 10942   4.1414  29.4797 1477379  17.7038 346.9449  0.99630870    05
Mercury 1 r
1 23247U 94054B   11005.77075415 0.00000000  00000-0  00000-0 0    06
2 23247   9.6741  38.3676 0122820 209.8320 149.4835  0.99588186    07
Mentor 2 r
1 25337U 98029B   11005.72886267 0.00000000  00000-0  00000-0 0    04
2 25337   9.9060  10.2291 0050559  44.2198 316.2053  1.00269978    05
Mercury 2 r
1 25349U 96026B   11005.59407392 0.00000000  00000-0  00000-0 0    05
2 25349   8.9424   5.3872 0468483 275.3341  79.3626  0.99563671    04
Vortex 4 r2
1 14677U 84009C   11005.54089154 0.00000000  00000-0  00000-0 0    02
2 14677   7.9119 358.7188 0973592   1.3230 358.9621  0.99442161    08
DSP F2 r
1 05205U 71039B   11005.53095150 0.00000000  00000-0  00000-0 0    00
2 05205   9.7468 321.1078 0032465 323.0265  36.7621  1.00414555    01
DSP F3 r
1 05854U 72010B   11005.43225509 0.00000000  00000-0  00000-0 0    02
2 05854  10.3342 324.0683 0063364 357.7199   2.2635  1.00673084    03
Rhyolite 2
1 06380U 73013A   11005.41574207 0.00000000  00000-0  00000-0 0    01
2 06380  11.3440 327.9270 0021169 109.4382 250.8027  1.00264876    06
Rhyolite 1
1 04418U 70046A   11005.40772169 0.00000000  00000-0  00000-0 0    00
2 04418   9.3696 318.3178 0011896  57.3581 302.7686  1.00251116    06
SBSS 1
1 37168U 10048A   11005.27810923 0.00000150  00000-0  20380-4 0    03
2 37168  98.0154 231.9758 0002500  27.7937 332.2061 14.78900661    00
WGS F3
1 36108U 09068A   11005.02353592 0.00000000  00000-0  00000-0 0    00
2 36108   0.0026 100.5215 0004229  21.4235 338.6194  1.00270000    00
Canyon 1 r
1 27785U 68063B   11002.69552116 0.00000000  00000-0  00000-0 0    04
2 27785  14.4213 342.8047 1095502  87.5165 284.9585  1.01773464    02
AEHF 1 r
1 36869U 10039B   11002.48493822 0.00000200  00000-0  17139-3 0    08
2 36869  21.0322 277.4191 7885107 240.4423  21.6745  1.55587975    07
DSCS 3-5 r2
1 21877U 92006C   11002.20253967 0.00000000  00000-0  00000-0 0    03
2 21877  10.2452  22.1501 0648096 278.9656  73.7723  1.10779583    08
DSP F18 r3
1 24740U 97008D   11002.19332744 0.00000000  00000-0  00000-0 0    01
2 24740   9.1536  57.5687 0025271  30.7570 329.4030  0.99490376    08
Vortex 6 r2
1 19983U 89035C   11002.10744857 0.00000000  00000-0  00000-0 0    08
2 19983   6.8705  13.8944 1025712 297.2868  52.6590  0.99428067    09
DSP F20 r3
1 26359U 00024D   11002.08177633 0.00000000  00000-0  00000-0 0    03
2 26359   6.6356  59.5431 0009443  13.1812 346.8556  0.99699248    09
DSCS 3-13 r2
1 27693U 03008C   11002.07825266 0.00000000  00000-0  00000-0 0    01
2 27693   7.0061  62.1537 0004810  43.4018 316.6682  1.01116496    01
DSP F21 r3
1 26883U 01033D   11002.06214617 0.00000000  00000-0  00000-0 0    08
2 26883   5.5905  61.5661 0006246 248.1881 111.7576  0.99888268    04
DSCS 3-2
1 16116U 85092B   11002.02934994 0.00000000  00000-0  00000-0 0    06
2 16116  12.5337  40.0812 0005992 320.9918  38.9771  0.98986082    05
DSCS 3-3
1 16117U 85092C   11002.02521120 0.00000000  00000-0  00000-0 0    00
2 16117  12.3047  41.8378 0003933  42.3089 317.7264  0.99321201    07
DSP F16 r2
1 21807U 91080D   11002.01305000 0.00000000  00000-0  00000-0 0    02
2 21807  12.3044  39.1416 0019700 201.2681 158.6621  1.01277059    06
Vortex 3 r2
1 12932U 81107C   11002.00572033 0.00000000  00000-0  00000-0 0    01
2 12932   7.7252 351.7751 0964737  28.0144 336.8851  0.99598272    01
DSP F4 r
1 11940U 73040B   11001.96298108 0.00000000  00000-0  00000-0 0    08
2 11940  12.1271 327.7115 0028171 267.2785  92.4171  0.99556133    08
DSCS 2-15 r2
1 20205U 89069D   11001.90521396 0.00000000  00000-0  00000-0 0    02
2 20205  13.3566  21.9145 0065448 194.7902 165.0577  1.01242289    06
DSCS 3-2 r2
1 16119U 85092E   11001.86215215 0.00000000  00000-0  00000-0 0    08
2 16119  14.5985  12.3049 0060958  24.0546 336.2479  1.01082978    00
Magnum 1 r2
1 15545U 85010D   11001.85767895 0.00000000  00000-0  00000-0 0    05
2 15545  16.9666  17.2390 0024810 132.4417 227.7805  1.00811075    09
DSP F7 r2
1 09855U 77007C   11001.84593791 0.00000000  00000-0  00000-0 0    00
2 09855  13.6141 337.9179 0012657 249.6341 110.2420  1.00250495    00
Mentor 5 r
1 37233U 10063B   11001.68520661 0.00000000  00000-0  00000-0 0    08
2 37233   6.9953 266.8852 0220851 140.0576 221.6006  1.04031629    03
Milstar 4 r
1 26716U 01009B   11001.24367419 0.00000000  00000-0  00000-0 0    04
2 26716   6.2596  56.2099 0017452 348.0440  11.9266  1.00468874    08
AEHF 1
1 36868U 10039A   11001.20444344 0.00000000  00000-0  00000-0 0    05
2 36868  10.5699 284.5336 5611939 219.6849 343.0000  1.23768400    08
DSCS 3-5
1 21873U 92006A   11001.19697838 0.00000000  00000-0  00000-0 0    05
2 21873   9.5882  56.0610 0003064 235.6309 124.3521  0.99032102    08
FIA Radar 1
1 37162U 10046A   10365.68598779 0.00000000  00000-0  00000-0 0    07
2 37162 122.9944  52.8158 0005000 102.1579 257.8421 13.41452514    00
Unknown 101208
1 99991U 10742A   10345.69214651 0.00000000  00000-0  00000-0 0    01
2 99991   0.0668  12.3384 0002903 145.4049 214.6472  1.00404895    08
Unknown 101019
1 90086U 10792A   10293.40767197  .01192144  00000-0  74211-3 0    01
2 90086  26.3644  16.4586 2095633 273.6405  94.8735 11.57122578    00
SBSS 1 r
1 37169U 10048B   10273.80860640 0.00000000  00000-0  00000-0 0    07
2 37169  98.0000 135.5082 0008000  44.9343 315.0656 15.10164263    09
DSP F18 Cover
1 27680U 97008E   10273.49042398 0.00000000  00000-0  00000-0 0    02
2 27680   8.8526  57.3275 0148455  25.4214 335.3707  0.99519054    08
Canyon 5 r
1 06318U 72101B   10239.11847001 0.00000000  00000-0  00000-0 0    09
2 06318  19.3177 331.9150 1282609 333.9047  20.1530  1.02309316    03
Helios 2B
1 36124U 09073A   10239.07282622 0.00000000  00000-0  00000-0 0    02
2 36124  98.1220 173.9535 0003000  68.3825 291.7697 14.63824605    08
Helios 2B r
1 36125U 09073B   10237.02021578 0.00000102  00000-0  15029-4 0    01
2 36125  98.0401 175.1666 0040933   2.2543 357.8842 14.74859328    06
DSCS 3-14 r2
1 27877U 03040C   10224.65989715 0.00000000  00000-0  00000-0 0    00
2 27877   6.2418  64.9054 0017404 154.3367 205.7796  1.00749133    01
DSCS 2-15
1 20202U 89069A   10220.38055627 0.00000000  00000-0  00000-0 0    02
2 20202  13.2973  29.8468 0011478  95.6547 264.4849  0.98613270    00
DSP F20 Cover
1 28156U 00024E   10219.54841720 0.00000000  00000-0  00000-0 0    05
2 28156   6.5337  61.3504 0236099 220.3280 137.8983  0.99704389    01
DSP F17 r3
1 23438U 94084D   10214.62345466 0.00000000  00000-0  00000-0 0    02
2 23438  10.4068  51.4622 0004460 329.9707  30.0084  1.01180360    07
DSP F22 r3
1 28161U 04004D   10194.17389645 0.00000000  00000-0  00000-0 0    07
2 28161   2.9900  66.4668 0004829 255.6058 104.3420  0.99812515    04
Canyon 7 r2?
1 15422U 77038C   10191.67764865 0.00000000  00000-0  00000-0 0    03
2 15422  10.5096   7.4978 1472221  32.1671 336.0317  1.02333119    07
DSP F14 r3
1 20069U 89046D   10191.67588769 0.00000000  00000-0  00000-0 0    05
2 20069  11.9707  33.5320 0046338 215.8917 143.8083  1.01304169    09
DSP F12 r
1 15454U 84129B   10191.65064750 0.00000000  00000-0  00000-0 0    01
2 15454  14.4335  15.4732 0004626   5.5645 354.4527  1.01159923    07
DSCS 3-8 r
1 22916U 93074B   10186.49616209 0.00000000  00000-0  00000-0 0    09
2 22916  12.6587  38.0691 0008701 275.5345  84.3780  0.99249324    07
DSP F8 r2
1 11436U 79053C   10186.45711167 0.00000000  00000-0  00000-0 0    00
2 11436  14.9061 354.8558 0054070 136.1219 224.3289  0.99437731    08
Mentor 1 r
1 23568U 95022B   10170.81502268 0.00000000  00000-0  00000-0 0    06
2 23568  10.9214  79.3584 0011176 188.1995 171.8066  1.00559637    01
Canyon 3 r
1 27787U 70069B   10170.36389558 0.00000000  00000-0  00000-0 0    02
2 27787  16.6678 285.4757 1264801 311.7085  38.1336  1.01706096    06
DSCS 3-12 r2
1 26577U 00065C   10163.77567858 0.00000000  00000-0  00000-0 0    05
2 26577   8.5277  58.6293 0050772 116.0677 244.4680  1.01179455    01
DSCS 3-7 r2
1 22738U 93046C   10163.69616747 0.00000000  00000-0  00000-0 0    04
2 22738  12.1950  35.6416 0079059 336.3576  23.2839  1.02122163    05
DSCS 3-6 r2
1 22011U 92037C   10163.59337545 0.00000000  00000-0  00000-0 0    02
2 22011  12.5364  31.4773 0025384 280.7688  78.9577  1.01646308    07
Vortex 2 r2
1 11560U 79086C   10163.55770832 0.00000000  00000-0  00000-0 0    04
2 11560   6.9789 352.5593 1298164  38.3842 330.1857  0.99674722    08
Canyon 2 r
1 27786U 69036B   10163.00168806 0.00000000  00000-0  00000-0 0    07
2 27786   4.1309 116.8438 0969700  46.5985 321.0825  1.03853244    09
DSCS 3-9 r2
1 23648U 95038C   10155.58771574 0.00000000  00000-0  00000-0 0    07
2 23648  11.5522  44.2078 0015192 165.7499 194.3050  1.01266427    06
Magnum 2 r2
1 20357U 89090D   10154.45931574 0.00000000  00000-0  00000-0 0    05
2 20357  14.8484  49.1417 0320218 295.8635  60.8843  0.99522508    07
Rhyolite 4
1 10787U 78038A   10154.31636398 0.00000000  00000-0  00000-0 0    02
2 10787  10.9051 348.3458 0009044 140.3101 219.7682  1.00463900    01
OTV-1
1 36514U 10015A   10143.39927771 0.00001500  00000-0  23465-4 0    03
2 36514  39.9923 169.4404 0015696 208.7785 151.2208 15.52671083    05
Canyon 2
1 03889U 69036A   10123.85895608 0.00000000  00000-0  00000-0 0    01
2 03889   2.1240 154.2443 0941406 326.6324  27.8335  1.00368037    08
Canyon 1
1 03334U 68063A   10123.40009905 0.00000000  00000-0  00000-0 0    03
2 03334  15.3109 349.9077 0930186  62.8827 306.3130  0.99244310    01
Milstar 1 r
1 22989U 94009B   10122.91088427 0.00000000  00000-0  00000-0 0    00
2 22989   6.7942 104.0615 0009881  53.7279 306.3753  1.00595740    04
Milstar 2 r
1 23713U 95060B   10122.81724332 0.00000000  00000-0  00000-0 0    05
2 23713   9.3135  57.1125 0033938  48.2190 312.0826  1.00597069    09
DSP F5 r2
1 08516U 75118C   10122.76384947 0.00000000  00000-0  00000-0 0    09
2 08516  13.0312 335.7526 0014254  26.1951 333.8889  1.00537189    09
DSCS 3-11 r2
1 26054U 00001C   10122.76136962 0.00000000  00000-0  00000-0 0    07
2 26054   8.9107  57.9538 0015899 210.1349 149.7857  1.01179694    02
DSCS 3-4
1 20203U 89069B   10122.71740873 0.00000000  00000-0  00000-0 0    05
2 20203   8.6420  60.0767 0006037 253.8998 106.0458  0.99114991    02
DSP F10 r
1 13089U 82019B   10122.67457340 0.00000000  00000-0  00000-0 0    06
2 13089  14.2542   2.0245 0015158 336.6330  23.3102  1.01259794    07
DSP F11 r
1 14931U 84037B   10122.64908370 0.00000000  00000-0  00000-0 0    06
2 14931  14.0201   9.2730 0027160 163.5370 196.5700  1.01165890    09
Canyon 6 r
1 07964U 75055B   10122.60104465 0.00000000  00000-0  00000-0 0    03
2 07964  20.3166 338.6817 1312086 297.0392  50.1742  1.02091197    04
DSP F6 r2
1 08918U 76059C   10122.52944398 0.00000000  00000-0  00000-0 0    06
2 08918  13.3364 337.3635 0012322  64.7732 295.3666  1.00562065    09
Helios 1A
1 23605U 95033A   10097.11731295 0.00000000  00000-0 -14523-3 0    04
2 23605  98.1038  33.6397 0002499 104.4270 255.5729 14.63844028    05
Essaim 3
1 28496U 04049E   10091.34788348 0.00000020  00000-0  33248-5 0    02
2 28496  98.3032  64.3619 0009789  59.9821 300.0177 14.70164628    09
Essaim 4
1 28497U 04049F   10091.34742217 0.00000020  00000-0  33229-5 0    07
2 28497  98.3046  64.4188 0012914  55.6010 304.3989 14.70165884    07
Helios 2A
1 28492U 04049A   10087.08779818 0.00000000  00000-0  39215-3 0    02
2 28492  98.1112  24.1031 0001504 132.1829 227.8169 14.63842742    02
IGS 5A
1 36104U 09066A   10079.86836021 0.00000000  00000-0  00000-0 0    09
2 36104  97.8129 153.1807 0001000   4.2748 355.7250 14.93388774    04
Essaim 2
1 28495U 04049D   10078.14406910 0.00000010  00000-0  16636-5 0    07
2 28495  98.2815  46.0980 0004617  92.5141 267.4857 14.70158428    09
Essaim 1
1 28494U 04049C   10078.14361211 0.00000090  00000-0  14966-4 0    01
2 28494  98.3005  46.2035 0003783  98.9520 261.0479 14.70180409    01
IGS 5A r
1 36105U 09066B   10072.86172539 0.00000803  00000-0  65607-4 0    09
2 36105  97.6507 144.6866 0043019  43.1528 317.3053 14.98708889    00
Unknown 100202
1 96041U 96541A   10033.50617528 0.00000000  00000-0  00000-0 0    09
2 96041  14.1070 359.5358 0044918 231.0381 128.5729  1.00224248    04
STSS Demo r
1 35939U 09052C   09337.06590627 0.00243000  00000-0  24874-3 0    02
2 35939  59.6643 210.1386 0654620 289.3240  70.6760 14.79164575    01
DMSP F18
1 35951U 09057A   09292.07608029 0.00000000  00000-0  00000-0 0    01
2 35951  98.9336 326.0730 0010024 295.5843  64.4156 14.12545987    09
Unknown 091017
1 90085U 09790A   09292.01577191  .00000000  00000-0  00000+0 0    02
2 90085  25.3410  12.0524 6961417 187.5746 150.4904  2.73606553    05
STSS Demo 1
1 35937U 09052A   09271.78649380 0.00000000  00000-0  00000-0 0    00
2 35937  57.9904  82.1205 0013359 323.1724  36.8701 12.79625382    04
STSS Demo 2
1 35938U 09052B   09270.77181345 0.00000000  00000-0  00000-0 0    01
2 35938  57.9922  84.8776 0007193 297.9025  62.0975 12.79020022    02
PAN USA 207
1 35815U 09047A   09263.63810579 0.00000000  00000-0  00000-0 0    04
2 35815   0.0533 274.1181 0003730  63.1363 286.5617  1.00270000    09
Unknown 9O0DC57
1 90084U 09710A   09244.64721928 0.00000000  00000-0  00000-0 0    09
2 90084  41.8425 356.8152 7570669 190.1322 133.6279  0.44275082    08
Unknown 090720
1 96044U 96544A   09201.96545740 0.00000000  00000-0  00000-0 0    06
2 96044  14.3745   1.0263 0053649 298.1383  61.3327  1.00336036    06
WGS F2 USA 204
1 34713U 09017A   09141.35810465 0.00000000  00000-0  00000-0 0    05
2 34713   0.0915 245.2475 0004000  23.0065 336.9754  1.00317756    01
STSS-ATRR r
1 34904U 09023B   09130.12101793 0.00480000  00000-0  68103-2 0    06
2 34904 112.7678 228.4968 0309489 290.6359  68.9977 15.16282514    01
STSS-ATRR
1 34903U 09023A   09127.88488268 0.00000000  00000-0  00000-0 0    07
2 34903  98.9513 226.1446 0007714 220.9054 139.0944 14.06067719    03
Unknown 090420
1 96033U 96533A   09110.63239993 0.00000000  00000-0  00000-0 0    05
2 96033  13.9432  18.2202 0057566   3.7749 356.2802  1.01080704    06
DSCS 3-1
1 13637U 82106B   09086.57587271 0.00000000  00000-0  00000-0 0    05
2 13637  12.8363  29.5893 0014471  24.5147 335.5789  0.97822440    07
Unknown 090222
1 96151U 96651A   09061.26213363 0.00000000  00000-0  00000-0 0    03
2 96151   2.8722 110.6502 0007024 173.3904 186.6327  1.00271000    04
Unknown 090220
1 96067U 96567A   09061.15788108 0.00000000  00000-0  00000-0 0    08
2 96067   5.0689  67.0894 0005392 347.9646  12.0344  0.99703848    02
Unknown 090220
1 96135U 96635A   09061.02229998 0.00000000  00000-0  00000-0 0    03
2 96135  12.8109  29.8292 0032281  35.1712 324.9230  0.97828162    00
Unknown 090222
1 96153U 96653A   09052.88999143 0.00000000  00000-0  00000-0 0    03
2 96153   2.2340  34.5244 0255638 191.4014 168.0085  0.95121995    07
Unknown 090215
1 96002U 96502A   09046.73183017 0.00000000  00000-0  00000-0 0    01
2 96002   4.9583  72.2162 0020199 137.2073 222.9621  1.00738930    07
Unknown 090215
1 96127U 96627A   09046.66695530 0.00000000  00000-0  00000-0 0    07
2 96127   7.9678  64.6583 0006567 199.8241 160.1623  0.99036302    05
USA 202
1 33490U 09001A   09046.30328249 0.00000000  00000-0  00000-0 0    02
2 33490   2.8915 337.5826 0024996 190.8227 169.2084  1.00130520    01
Unknown 090214
1 96087U 96587A   09044.89525712 0.00000000  00000-0  00000-0 0    04
2 96087  12.3775  34.9456 0011397  90.8437 269.2989  0.98605782    00
Intelsat 3F7
1 04376U 70032A   09043.49870956 0.00000000  00000-0  00000-0 0    09
2 04376  10.3292 321.4666 0004451 284.3056  75.6570  1.00281526    04
Unknown 090123
1 29241U 06024B   09043.13578394 0.00000000  00000-0  00000-0 0    09
2 29241   0.0930 268.8956 0001722  79.0749 280.9526  1.00600180    02
Unknown 000405
1 90083U 09526A   09041.61082110 -.00000043  00000-0  00000-0 0    06
2 90083  63.9971 336.2962 7172924 278.6846  12.8961  2.00612597    00
MiTEx NRL U/S USA 189
1 29242U 06024C   09034.74688303 0.00000000  00000-0  00000-0 0    09
2 29242   2.0973  77.0138 0001706 153.1240 206.8902  1.04004000    04
Unknown 090128
1 96047U 96547A   09028.63032334 0.00000000  00000-0  00000-0 0    03
2 96047  16.0654  24.9673 0024383 122.3340 237.9143  1.00815221    05
USA 202 r
1 33491U 09001B   09023.53756835 0.00000000  00000-0  00000-0 0    09
2 33491   2.9844 334.0731 0246632  12.9987 347.6968  0.96057197    06
Unknown 090123
1 91141U 09523A   09023.27786493 0.00000000  00000-0  00000-0 0    08
2 91141   0.1465 277.1835 0001045 113.3174 246.6826  1.00566977    02
Unknown 090104
1 96104U 96604A   09004.46041200 0.00000000  00000-0  00000-0 0    08
2 96104   0.0050  84.9509 0001000 173.8940 186.1060  1.00270000    07
Milstar 4 USA 157
1 26715U 01009A   09004.42726648 0.00000000  00000-0  00000-0 0    06
2 26715   2.8864  50.0981 0001000 205.9101 154.0822  1.00270000    05
UFO F4 USA 108
1 23467U 95003A   09004.33456456 0.00000000  00000-0  00000-0 0    01
2 23467   4.7731  47.6367 0006000 221.7153 138.2785  1.00270000    00
Unknown 090103
1 96005U 96505A   09003.90602467 0.00000000  00000-0  00000-0 0    04
2 96005   5.1196  67.1652 0239868 214.2204 144.2231  0.99716871    07
Unknown 090103
1 96144U 96644A   09003.50600162 0.00000000  00000-0  00000-0 0    08
2 96144  11.6034 330.3545 0008228 236.2970 123.6365  0.99765774    03
DSP F18 USA 130
1 24737U 97008A   09002.49706237 0.00000000  00000-0  00000-0 0    09
2 24737   7.3728  66.6604 0000496 258.3498 101.6521  1.00270000    04
Unknown 081224
1 91132U 08859A   08363.85226720 0.00000000  00000-0  00000-0 0    01
2 91132   0.1956  67.6540 0002292 197.1192 162.8932  0.99949073    03
Unknown 081120
1 96077U 96577A   08325.85800704 0.00000000  00000-0  00000-0 0    06
2 96077  10.7161  50.2040 0004288 267.6007  92.3622  0.99322423    06
Unknown 081118
1 96020U 96520A   08323.70749973 0.00000000  00000-0  00000-0 0    04
2 96020   6.1839  11.7069 1043244 284.6255  64.0509  0.99426703    04
Unknown 050415
1 90075U 05605D   08320.72470970 0.00000000  00000-0  00000-0 0    09
2 90075   6.9467 351.1744 1279846  28.4373 338.0007  0.99676604    02
Unknown 081022
1 96084U 96584A   08302.94748073 0.00000000  00000-0  00000-0 0    07
2 96084  11.4187  44.2975 0009022 232.7367 127.1884  0.99248500    03
Unknown 081022
1 96137U 96637A   08301.95162800 0.00000000  00000-0  00000-0 0    03
2 96137  14.4606 353.6224 0013800 171.0170 189.0197  1.00329687    04
Unknown 081021
1 96076U 96576A   08301.85393732 0.00000000  00000-0  00000-0 0    06
2 96076   7.7179 351.1443 0960487  12.7427 349.4839  0.99600970    09
UFO F3 USA 104
1 23132U 94035A   08297.50944147 0.00000000  00000-0  00000-0 0    05
2 23132   5.7058  54.4158 0004958 209.2649 150.7194  1.00332118    09
Unknown 081022
1 96080U 96580A   08296.85496185 0.00000000  00000-0  00000-0 0    05
2 96080  10.8549  39.4838 0048453 198.5563 161.2785  1.01304710    05
Unknown 081022
1 96010U 96510A   08296.77355037 0.00000000  00000-0  00000-0 0    02
2 96010   2.9182  15.4739 1442354  15.8083 348.2633  0.99618090    08
Unknown 081021
1 96015U 96515A   08294.41062971 0.00000000  00000-0  00000-0 0    03
2 96015   7.5933  65.0334 0020417 222.4009 137.4533  1.01182968    06
Unknown 081021
1 96019U 96519A   08294.35649347 0.00000000  00000-0  00000-0 0    02
2 96019   8.9308  59.2425 0003407 253.9774 105.9972  1.01182092    00
Unknown 081021
1 96081U 96581A   08294.25232584 0.00000000  00000-0  00000-0 0    00
2 96081  11.2450  45.7120 0077703 275.0046  84.1210  0.99906934    01
Unknown 081021
1 96095U 96595A   08294.18251905 0.00000000  00000-0  00000-0 0    00
2 96095  13.5257  14.1909 0031472 154.1760 205.9936  1.01164980    03
Unknown 081019
1 96059U 96559A   08293.81340330 0.00000000  00000-0  00000-0 0    00
2 96059  19.8602 340.0457 1275710 313.4680  36.5967  1.02314755    02
Unknown 081019
1 96088U 96588A   08292.96283639 0.00000000  00000-0  00000-0 0    07
2 96088  12.1705  29.4325 0069691 174.4171 185.6732  1.01239903    00
DSP F22 USA 176
1 28158U 04004A   08292.82125469 0.00000000  00000-0  00000-0 0    03
2 28158   1.4073  67.1299 0010770  51.8717 308.2483  1.00270000    07
FleetSatCom 1
1 10669U 78016A   08291.77004869 0.00000000  00000-0  00000-0 0    08
2 10669  15.3166 359.1225 0003786 189.3854 170.6196  0.99001209    05
Unknown 080927
1 96098U 96598A   08277.88170435 0.00000000  00000-0  00000-0 0    02
2 96098  14.5448 354.0857 0008392  26.0996 333.9717  1.00198879    02
Unknown 080927
1 96071U 96571A   08277.13303548 0.00000000  00000-0  00000-0 0    05
2 96071   7.1630  67.9520 0024000  10.2236 349.8262  0.99498363    06
Unknown 080930
1 96145U 96645A   08277.05017666 0.00000000  00000-0  00000-0 0    03
2 96145  18.0058 294.7849 1246854 290.1798  56.8594  1.01708854    09
DSCS 3-11 USA 148
1 26052U 00001A   08274.63870388 0.00000000  00000-0  00000-0 0    03
2 26052   0.0382 104.3705 0019368 128.4344 231.7569  1.00270000    06
Unknown 060326
1 90074U 06585B   08271.90138811 0.00000000  00000-0  00000-0 0    06
2 90074  14.7436   0.1190 0055910 121.5737 238.9855  0.99437823    09
DSCS 3-10 USA 135
1 25019U 97065A   08271.55834468 0.00000000  00000-0  00000-0 0    08
2 25019   2.4599  77.9836 0006877 344.1851  15.7946  1.00270000    04
Unknown 080926
1 96025U 96525A   08270.96309031 0.00000000  00000-0  00000-0 0    00
2 96025   7.6389 358.4193 0975000 344.5655  12.6679  0.99444016    01
Unknown 080926
1 96061U 96561A   08270.24471407 0.00000000  00000-0  00000-0 0    08
2 96061   3.5773  70.0911 0009000 203.4988 156.4722  0.99905530    07
Unknown 080920
1 96103U 96603A   08264.92829330 0.00000000  00000-0  00000-0 0    02
2 96103  20.6123 345.7805 1312167 279.6206  65.8356  1.02087560    02
Unknown 080920
1 96132U 96632A   08264.17193122 0.00000000  00000-0  00000-0 0    06
2 96132   9.1149  30.8425 0655443 252.7264 100.0146  1.10773811    05
SDS 3F3 AQUILA USA 162
1 26948U 01046A   08263.73192277 0.00000000  00000-0  00000-0 0    00
2 26948   2.4912 118.5410 0007986 166.4257 193.6102  1.00270000    02
Vortex 3
1 12930U 81107A   08256.17620449 0.00000000  00000-0  00000-0 0    09
2 12930   7.2702 358.1588 0937156 264.7361  84.5292  1.00196143    08
Unknown 080911
1 96029U 96529A   08255.93880784 0.00000000  00000-0  00000-0 0    07
2 96029  10.9471  31.4307 0004599 107.2756 252.7868  1.01242586    00
Unknown 080911
1 96094U 96594A   08255.89252771 0.00000000  00000-0  00000-0 0    05
2 96094  12.9829   8.6765 0696377  99.3668 268.5795  0.93696548    04
Unknown 080911
1 96054U 96554A   08255.87927744 0.00000000  00000-0  00000-0 0    04
2 96054  13.6860 342.2216 0010151  46.8918 313.2051  1.00552224    00
DSP F17 USA 107
1 23435U 94084A   08255.32935064 0.00000000  00000-0  00000-0 0    07
2 23435   8.9380  59.9535 0027817  16.4882 343.6267  1.00270000    08
Unknown 080911
1 96050U 96550A   08255.02233796 0.00000000  00000-0  00000-0 0    00
2 96050  13.4137 340.5469 0012896   2.9643 357.0553  1.00524592    08
Vortex 6 USA 37
1 19976U 89035A   08254.92982997 0.00000000  00000-0  00000-0 0    04
2 19976   5.6687  10.8577 0957500 218.1037 134.7383  1.00270000    01
Vortex 4
1 14675U 84009A   08254.00611331 0.00000000  00000-0  00000-0 0    01
2 14675   7.6479 356.0872 1075535 282.8383  65.3832  1.00270000    06
Unknown 080818
1 90082U 08731A   08238.36640692 0.00000000  00000-0  00000-0 0    08
2 90082  64.1000  87.1676 6500000 260.3687  14.3594  2.00600500    09
Adv Orion 3 USA 171
1 27937U 03041A   08224.27606074 0.00000000  00000-0  00000-0 0    07
2 27937   3.1995 154.8696 0046919 127.2981 233.1479  1.00270000    04
Magnum 2 USA 48
1 20355U 89090B   08224.02190055 0.00000000  00000-0  00000-0 0    02
2 20355  13.2472  57.6713 0261787 276.6026  80.4301  1.00270000    01
UFO F6 USA 114
1 23696U 95057A   08217.55569624 0.00000000  00000-0  00000-0 0    05
2 23696   4.0529  48.3448 0005132 245.6947 114.2602  1.00270000    03
Unknown 080803
1 96093U 96593A   08215.28997837 0.00000000  00000-0  00000-0 0    01
2 96093  10.8328 326.6735 0038054 304.7776  54.8767  1.00434895    08
UFO F5 USA 111
1 23589U 95027A   08184.63450042 0.00000000  00000-0  00000-0 0    08
2 23589   4.7805  49.0518 0005954 237.0213 122.9306  1.00270000    04
Unknown 080507
1 90081U 08628A   08137.07694771 -.00000848  00000-0  00000-0 0    06
2 90081  62.8133 214.3140 6808239 276.9167  16.0088  2.00573006    08
Milstar 1 USA 99
1 22988U 94009A   08126.87731780 0.00000000  00000-0  00000-0 0    02
2 22988   5.6904 141.0599 0010295 273.5206  86.3680  1.00270000    07
Unknown 080501
1 96078U 96078A   08122.54349808 0.00000000  00000-0  00000-0 0    07
2 96078  10.3461  49.7125 0024235 179.3373 180.6780  1.01274257    03
Unknown 080309
1 96082U 96582A   08122.37762015 0.00000000  00000-0  00000-0 0    02
2 96082   9.8078  12.1480 1460039  12.0363 351.1134  1.02326597    06
Unknown 080331
1 90080U 08591A   08114.89787183 0.00000000  00000-0  00000-0 0    08
2 90080  63.3561 169.3958 4938027 292.2456  67.7544  5.52688554    08
DSP F7
1 09803U 77007A   08114.44862472 0.00000000  00000-0  00000-0 0    05
2 09803  14.7754 349.6778 0080086 225.1035 134.2558  0.97530801    05
USA 137
1 25148U 98005A   08105.89470532 0.00001391  00000-0  00000-0 0    01
2 25148  64.2508 175.7217 7145485 255.3197  21.8969  2.00594627    03
USA 179
1 28384U 04034A   08105.57031399 0.00001405  00000-0  00000-0 0    00
2 28384  63.1359  58.7451 7286209 271.8820  14.0454  2.00613917    03
Mercury 2
1 23855U 96026A   08105.54515348 0.00000000  00000-0  00000-0 0    08
2 23855   7.3324  15.8034 0501103 176.6202 183.7537  1.00270000    03
Unknown 080304
1 96070U 96570A   08101.00872691 0.00000000  00000-0  00000-0 0    05
2 96070   2.4964 215.8648 0985398 253.4186  95.5602  1.00368077    03
Unknown 080304
1 96062U 96562A   08100.71696554 0.00000000  00000-0  00000-0 0    06
2 96062   0.9611  64.2132 0006150 222.5308 137.4336  0.99820367    05
Unknown 080409
1 96085U 96585A   08100.69892177 0.00000000  00000-0  00000-0 0    02
2 96085  11.1264  39.3093 0026169 252.4349 107.2911  1.01639621    05
Unknown 050301
1 96028U 96528A   08100.58033098 0.00000000  00000-0  00000-0 0    03
2 96028  10.7066  43.8128 0082752 306.4114  52.8402  1.02110481    05
Unknown 050227
1 96055U 96555A   08100.44212720 0.00000000  00000-0  00000-0 0    09
2 96055  14.6318 351.7468 1080958  59.5789 310.6741  1.01770851    00
DSP F12 USA 7
1 15453U 84129A   08100.43318721 0.00000000  00000-0  00000-0 0    03
2 15453  13.8988  24.8677 0003138 220.2659 139.7229  0.98851744    01
Unknown 080408
1 96022U 96522A   08099.61641082 0.00000000  00000-0  00000-0 0    00
2 96022   9.8980  52.9806 0016445 145.2103 214.9094  1.01259033    04
Mercury 1 USA 105
1 23223U 94054A   08098.72636622 0.00000000  00000-0  00000-0 0    06
2 23223   4.5914  70.5938 0046177 192.8760 167.0182  1.00270000    02
Unknown 080229
1 96027U 96527A   08098.39106334 0.00000000  00000-0  00000-0 0    00
2 96027   9.0026  13.9951 0045502  22.0048 338.2019  1.00351012    02
DSP F4
1 06691U 73040A   08098.37693189 0.00000000  00000-0  00000-0 0    00
2 06691  12.9189 334.4397 0007787 208.6198 151.3495  0.99825195    06
UFO F10 USA 146
1 25967U 99063A   08098.31161688 0.00000000  00000-0  00000-0 0    08
2 25967   1.6695  21.0153 0016980 267.7109  92.1015  1.00270000    04
Unknown 050406
1 96012U 96512A   08096.86498368 0.00000000  00000-0  00000-0 0    09
2 96012   3.0349 157.4932 0998767 349.8187   8.2990  1.03851217    02
Unknown 080229
1 96009U 96509A   08096.51286366 0.00000000  00000-0  00000-0 0    06
2 96009   2.8307  21.8640 1452369 290.8193  54.2771  1.00124605    04
DSP F5
1 08482U 75118A   08096.39725032 0.00000000  00000-0  00000-0 0    01
2 08482  14.2089 345.0303 0004294 353.2314   6.7748  0.99469072    04
Mentor 5 USA 139
1 25336U 98029A   08094.37073255 0.00000000  00000-0  00000-0 0    03
2 25336   7.5221  10.0919 0052658 214.9992 144.6642  1.00270000    07
FleetSatCom 8 USA 46
1 20253U 89077A   08090.65047492 0.00000000  00000-0  00000-0 0    00
2 20253   8.2319  47.4526 0008934 267.8261  92.0783  1.00270000    00
DSP F11
1 14930U 84037A   08090.56650089 0.00000000  00000-0  00000-0 0    08
2 14930  14.0419  18.2076 0005398 121.6795 238.3852  0.98681548    08
DSP F8
1 11397U 79053A   08090.53814964 0.00000000  00000-0  00000-0 0    05
2 11397  14.8450   2.2863 0005860 133.4590 226.6018  0.98746460    09
Vortex 1
1 10941U 78058A   08090.45486010 0.00000000  00000-0  00000-0 0    01
2 10941   7.6350 355.8693 1079347 280.1798  67.8410  1.00276373    08
DSP F16 USA 75
1 21805U 91080B   08088.72882587 0.00000000  00000-0  00000-0 0    08
2 21805  10.3736  50.6365 0011224 177.2610 182.7582  1.00270000    00
Milstar 2 USA 115
1 23712U 95060A   08086.55593646 0.00000000  00000-0  00000-0 0    03
2 23712   7.1392  68.5502 0007556 190.5725 169.4235  0.99034856    01
DSCS III B10 USA 97
1 22915U 93074A   08086.54366224 0.00000000  00000-0  00000-0 0    09
2 22915   3.9939  77.0038 0011292 232.3070 127.6000  1.00270000    07
UFO F2 USA 95
1 22787U 93056A   08086.54301158 0.00000000  00000-0  00000-0 0    01
2 22787   5.5241  48.5394 0007510 232.6485 127.2925  1.00270000    09
Unknown 050403
1 96058U 96558A   08086.39376577 0.00000000  00000-0  00000-0 0    03
2 96058  16.8187   5.3065 0036070 257.7007 101.9200  0.94327282    05
Vortex B
1 11558U 79086A   08086.38392276 0.00000000  00000-0  00000-0 0    05
2 11558   5.5456   9.1846 0949142 216.9956 136.0829  1.00270000    01
Magnum 1 USA 8
1 15543U 85010B   08086.36389186 0.00000000  00000-0  00000-0 0    01
2 15543  15.5902  26.8044 0016419 255.3492 104.4758  1.00270000    06
UFO F11 USA 174
1 28117U 03057A   08086.20850047 0.00000000  00000-0  00000-0 0    05
2 28117   2.2933 330.1377 0005154 119.9365 240.1326  1.00270000    01
DSP F3
1 05851U 62010A   08086.20613198 0.00000000  00000-0  00000-0 0    03
2 05851  12.2906 334.7519 0018455  92.8538 267.3695  1.00270317    00
DSP F2
1 05204U 71039A   08086.15413223 0.00000000  00000-0  00000-0 0    07
2 05204  10.7656 324.2652 0007863  26.4922 333.5601  1.00266212    02
SDS 3F2 USA 155
1 26635U 00080A   08084.63045670 0.00000000  00000-0  00000-0 0    04
2 26635   2.1120  39.4865 0012830 188.2367 171.7550  1.00270000    00
USA 184 r
1 29250U 06027B   08082.02503547 0.00000000  00000-0  00000-0 0    00
2 29250  62.3743 309.7803 7050465 274.7610  14.8472  2.17595297    02
USA 200
1 32706U 08010A   08080.11461581 0.00000000  00000-0  00000-0 0    03
2 32706  63.5619  40.8769 7095838 271.6711  15.8320  2.10156510    09
Unknown 080309
1 96079U 96579A   08069.69673970 0.00000000  00000-0  00000-0 0    05
2 96079  10.3707  50.9256 0007270 261.4505  98.4791  0.98989015    04
DSP F20 USA 149
1 26356U 00024A   08066.83903380 -.00000166  00000-0  00000-0 0 00009
2 26356 004.0836 070.1118 0001346 296.7291 063.8756 00.99855931000007
Unknown 050627
1 96011U 96511A   08064.64212642 0.00000000  00000-0  00000-0 0    07
2 96011   6.5684  69.5637 0053365  96.6612 263.9586  1.01183929    09
Unknown 080304
1 96039U 96539A   08064.62138421 0.00000000  00000-0  00000-0 0    07
2 96039  13.8130   8.7463 0013569 304.8716  55.0129  1.01251536    02
Unknown 080304
1 96040U 96540A   08064.58411234 0.00000000  00000-0  00000-0 0    02
2 96040  13.6458   5.0879 0052131 138.0675 222.3450  1.01329548    00
Unknown 080304
1 96049U 96549A   08064.44685507 0.00000000  00000-0  00000-0 0    01
2 96049  13.1088 335.3875 0031824 238.9238 120.7755  0.99556421    06
Unknown 080304
1 96038U 96538A   08064.40626317 0.00000000  00000-0  00000-0 0    07
2 96038  11.4764 330.8618 0065894 331.1138  28.5350  1.00659910    06
Unknown 080304
1 96060U 96560A   08064.39018608 0.00000000  00000-0  00000-0 0    03
2 96060  21.2625 351.7156 1302320 215.7121 134.8443  1.00184598    02
DSP F10
1 13086U 82019A   08064.36790061 0.00000000  00000-0  00000-0 0    01
2 13086  14.6381  12.2070 0003547 192.0567 167.9468  0.98187064    08
Unknown 050612
1 96031U 96531A   08064.36769844 0.00000000  00000-0  00000-0 0    01
2 96031   8.7338 322.6710 0224048 198.1654 161.0338  1.01903049    04
Unknown 080302
1 96032U 96532A   08062.64872644 0.00000000  00000-0  00000-0 0    05
2 96032  13.4036  23.3941 0001000 125.9163 234.1039  1.01155123    00
Unknown 080229
1 96101U 96601A   08062.49629351 0.00000000  00000-0  00000-0 0    07
2 96101  15.2567   1.0345 0004633 173.2996 186.7187  0.99004765    09
Unknown 080302
1 96102U 96602A   08062.41228654 0.00000000  00000-0  00000-0 0    02
2 96102  15.2927 356.6593 0914988  41.9981 324.6887  0.99235365    04
Unknown 080229
1 96126U 96626A   08060.78546095 0.00000000  00000-0  00000-0 0    04
2 96126   6.7593  70.1253 0007953 192.3467 167.6458  0.99119499    08
Unknown 080229
1 96006U 96506A   08060.77423349 0.00000000  00000-0  00000-0 0    07
2 96006   4.5303  75.9027 0002291 319.4726  40.5224  1.01113961    04
Unknown 080229
1 96089U 96589A   08060.53498818 0.00000000  00000-0  00000-0 0    02
2 96089   9.6611 330.6652 0185997 220.1976 138.4244  1.00699880    05
Unknown 080229
1 96091U 96591A   08060.32446549 0.00000000  00000-0  00000-0 0    09
2 96091  10.9952 352.4674 0014798 154.6112 205.4736  1.00501009    06
DSP 15 (USA 65
1 20929U 90095A   08059.52443716 0.00000000  00000-0  00000-0 0    02
2 20929  10.7927  46.6862 0007936 247.2447 112.6835  0.98391988    08
SDS 2F4 USA 125
1 23945U 96038A   08057.84877624 0.00001355  00000-0  00000-0 0    02
2 23945  64.0583 290.0161 7425694 255.4767  18.8791  2.00624178    07
MiTEX1 USA 187
1 29240U 06024A   08048.86864532 0.00000000  00000-0  00000-0 0    04
2 29240   1.2647  81.3384 0003038 154.6375 205.3903  1.04000000    08
FleetSatCom 4
1 12046U 80087A   08048.55787839 0.00000000  00000-0  00000-0 0    01
2 12046  14.3411   7.6528 0000303 216.0758 143.9342  0.98954925    09
UFO F9 USA 140
1 25501U 98058A   08047.63563391 0.00000000  00000-0  00000-0 0    01
2 25501   2.4697  28.0195 0016339 255.5349 104.2965  0.98179571    07
DSP F21 USA 159
1 26880U 01033A   08043.61029153 0.00000000  00000-0  00000-0 0    06
2 26880   3.0088  71.2071 0014726 185.6100 174.3900  1.00270000    08
DSCS 3-13 USA 167
1 27691U 03008A   08042.98221351 0.00000000  00000-0  00000-0 0    04
2 27691   0.0165 194.9748 0000100 227.3477 132.6621  1.00270000    05
DSP F13 USA 28
1 18583U 87097A   08030.76666845 0.00000000  00000-0  00000-0 0    08
2 18583  11.0074  34.8814 0021881 107.0759 253.1760  0.98386091    05
Unknown 050227
1 90071U 05558B   08030.76647236 0.00000000  00000-0  00000-0 0    05
2 90071  10.9841  34.8099 0021503 106.0371 254.2119  0.98385359    08
DSCS 3-12 USA 153
1 26575U 00065A   08029.90854415 0.00000000  00000-0  00000-0 0    04
2 26575   0.0400  83.5695 0003000 191.3683 168.6317  1.00270000    03
Unknown 071225
1 90079U 07859A   08005.82782101 0.00000000  00000-0  00000-0 0    09
2 90079  62.4173 321.5587 7063071 273.7666  86.2334  2.17597297    07
USA 198
1 32378U 07060A   07346.89533062 0.00001757  00000-0  17534-3 0    08
2 32378  60.0106 317.1239 5543977 287.1515  72.8485  4.77580618    03
USA 198 Cn r
1 32379U 07060B   07346.84730914 0.00069200  00000-0  28374-2 0    09
2 32379  60.7629 318.0027 5493200 285.4805  74.5049  4.90067973    06
Unknown 071201
1 90078U 07835A   07337.91338451 0.00000000  00000-0  00000-0 0    04
2 90078   1.0439  81.5551 0002593 163.2956 196.7247  1.04000377    07
DSP F19 USA 142
1 25669U 99017A   07324.02276106 0.00000000  00000-0  00000-0 0    07
2 25669  29.0657 245.4422 7091527 341.3340  18.6658  2.32920751    06
USA 197
1 32287U 07054A   07317.90389715 0.00000000  00000-0  00000-0 0    01
2 32287   3.9960 273.0734 0003000  60.0268 299.9732  0.99731100    03
USA 197 Cn r
1 32288U 07054B   07315.89571404 0.00000000  00000-0  00000-0 0    06
2 32288   3.9650 272.1000 0001000 154.0000 206.0000  0.99676600    02
DSP F9
1 12339U 81025A   07313.15890331 0.00000000  00000-0  00000-0 0    01
2 12339  14.3160   8.7296 0016263 108.4172 251.7717  0.98821615    08
DSCS 3-14 USA 170
1 27875U 03040A   07274.36836055 0.00000000  00000-0  00000-0 0    05
2 27875   0.0200  90.0004 0001000 180.0001 179.9999  1.00270000    00
Unknown 070914
1 90077U 07757A   07272.02679788 0.00000700  00000-0  53965-3 0    05
2 90077  28.1149 223.4027 7211623  34.5532 325.4466  2.33718986    01
Unknown 070918
1 90076U 07761A   07261.14212025 0.00000000  00000-0  00000-0 0    09
2 90076  18.7352   4.4643 0024056 177.2573 182.7789  1.00217190    03
SDS2 F2 Magnum 3 USA 67
1 20963U 90097B   07232.00023005 0.00000000  00000-0  00000-0 0    02
2 20963  12.3782  43.6309 0129130  94.7845 265.2341  1.00270000    06
Unknown 070310
1 90073U 07569A   07218.27701724 0.00000000  00000-0  00000-0 0    07
2 90073  12.3375 333.6121 0016032 220.0822 139.8115  0.98152425    03
NOSS 3-4 r
1 31702U 07027B   07211.98602379 0.00000483  00000-0  20711-3 0    06
2 31702  63.3731 274.4572 0163620 189.3552 170.3056 14.17708429    05
NOSS 3-4 (C)
1 31708U 07027C   07193.35731252 0.00000000  00000-0  00000-0 0    06
2 31708  63.4300 335.2216 0234817 150.8127 209.1873 13.65500000    08
NOSS 3-4 (C)
1 71703U 07027C   07170.06971504 0.00000000  00000-0  00000-0 0    04
2 71703  63.4300  37.1342 0234817 144.7322 215.3563 13.65609061    06
NOSS 3-4 (A)
1 31701U 07027A   07170.06953822 0.00000000  00000-0  00000-0 0    01
2 31701  63.4491  37.1181 0234547 144.6382 215.4221 13.65677834    02
Milstar 5 Cn r
1 27169U 02001B   07164.98349897 0.00000000  00000-0  00000-0 0    06
2 27169   2.2751 323.3619 0049349  78.2542 287.0261  1.00137794    06
Unknown 070511
1 91117U 07631A   07139.26722877  .00000000  00000-0  00000+0 0    09
2 91117  50.7032 157.3669 4804844 248.9007 111.6171  5.07303637    09
IGS R2
1 30586U 07005A   07108.00162496 0.00001600  00000-0  62349-4 0    06
2 30586  97.3219 228.6634 0004789 117.0927 242.9071 15.25995200    04
IGS R2 r
1 30588U 07005C   07107.99867309 0.00004000  00000-0  78749-4 0    08
2 30588  97.2912 229.6846 0095798 294.2453  65.7546 15.42260292    06
IGS R2 shroud2
1 30591U 07005F   07107.99494023 0.00007000  00000-0  26144-3 0    05
2 30591  97.2300 228.3472 0007979 235.7727 124.2272 15.27384068    08
IGS R1 shroud1
1 30590U 07005E   07107.99315165 0.00007300  00000-0  27229-3 0    01
2 30590  97.2211 228.2657 0008108 233.2259 126.7740 15.27426208    00
IGS-R2 adapter
1 30589U 07005D   07107.98881854 0.00005000  00000-0  18693-3 0    01
2 30589  97.2372 228.3467 0007973 199.6670 160.3328 15.27351491    04
IGS OVS
1 30587U 07005B   07106.97556309 0.00000000  00000-0  19730-2 0    08
2 30587  97.2818 227.5525 0001804  89.7710 270.2288 15.26031287    07
DSP F6
1 08916U 76059A   07079.50377131 0.00000000  00000-0  00000-0 0    04
2 08916  13.8181 344.4747 0029627 177.9250 182.0994  1.00452685    02
NOSS 2-2 (A)
1 21775U 91076A   07074.65642862 0.00000000  00000-0  00000-0 0    05
2 21775  63.3589 225.0012 3325559 266.6830  93.3170  5.53394968    08
Unknown 050301
1 90072U 05560C   07063.31680326 0.00000000  00000-0  00000-0 0    02
2 90072  14.4214 348.0660 0002296  16.0318 343.9875  0.99461249    04
NOSS 2-3 (A)
1 23893U 96029A   07060.82206468 0.00000000  00000-0  00000-0 0    03
2 23893  63.4733 352.7942 3314138 264.6933  95.3067  5.52843875    08
NOSS 2-1 (A)
1 20641U 90050A   07060.70300488 0.00000000  00000-0  00000-0 0    03
2 20641  63.4172  96.2736 4033400 268.3644  91.6356  6.02572519    05
UFO 7
1 23967U 96042A   07053.75412736 0.00000000  00000-0  00000-0 0    01
2 23967   2.8276  41.8670 0008000 200.9769 159.0231  1.00270000    02
Delta4 Demo
1 28500U 04050A   07030.25879883 0.00000000  00000-0  00000-0 0    07
2 28500  11.9212 199.6328 2887341 244.8710 115.1442  1.41309200    08
Delta4 Demo r
1 28546U 04050B   07028.57971064 0.00000000  00000-0  00000-0 0    03
2 28546  12.2910 202.7945 2680736 239.2158 120.7992  1.37842000    08
USA 193
1 29651U 06057A   06351.27314032  .00012066  00000-0  10000-3 0    00
2 29651  58.5075 109.9880 0009237 103.8726 256.3387 15.69650945    02
Unknown 060326
1 90067U 06085A   06346.15791963 0.00000000  00000-0  00000-0 0    04
2 90067  14.9277 353.2022 0078968 211.7528 147.7807  0.97525542    08
Unknown 061210
1 91090U 06844A   06344.94929672 0.00000000  00000-0  00000-0 0    09
2 91090   2.7000  38.7258 0001000 341.1643  18.8357  1.00270000    08
Unknown 061125
1 90070U 06829A   06336.25247557 0.00013000  00000-0  57382-3 0    01
2 90070  27.4667  75.3817 4799897 331.0516  28.9480  6.04892999    00
Unknown 060503
1 90056U 06623A   06322.94510516 0.00000000  00000-0  00000-0 0    04
2 90056   7.2520 356.1980 0932075 255.9116 104.0884  1.00270000    00
Unknown 050301
1 90069U 05560A   06316.23065343 0.00000000  00000-0  00000-0 0    05
2 90069  14.6843   5.9956 0008122 115.5975 244.4985  0.98741716    01
Unknown 061108
1 90068U 06812A   06315.12171652 0.00000000  00000-0  00000-0 0    03
2 90068   9.2728  55.6347 0002000 340.3244  19.6756  1.00270000    09
DMSP F17
1 29522U 06050A   06313.22739550 0.00000062  00000-0  33121-4 0    02
2 29522  98.7877 311.9526 0009224 249.9390 110.0609 14.13250636    06
Unknown 040920
1 90022U 04764A   06269.06199207 0.00000000  00000-0  00000-0 0    04
2 90022  11.6732  66.9434 0316489 252.0766 104.4603  0.99514325    02
Unknown 050616
1 90066U 05667A   06264.54841245 0.00000000  00000-0  00000-0 0    09
2 90066   2.5399  65.1529 0013926 309.9507  49.9391  1.00475347    09
IGS 2A
1 29393U 06037A   06255.94050995 0.00000000  00000-0  00000-0 0    04
2 29393  97.3059  14.6731 0005460 350.5714   9.4284 15.25871519    04
Unknown 060320
1 90064U 06579A   06239.69337876 0.00000000  00000-0  00000-0 0    08
2 90064  63.4467  68.5584 3305539 264.7788  95.2212  5.52842574    00
Unknown 060509
1 90065U 06629B   06239.61902766 0.00004000  00000-0  30340+1 0    07
2 90065  63.3895 300.5325 3358959 269.6587  90.3414  5.54462256    09
Unknown 060802
1 90063U 06214A   06227.02166296 0.00000000  00000-0  00000-0 0    03
2 90063  11.6391  47.0304 0126000  81.1450 278.8550  1.00270000    02
Unknown 060718
1 90062U 06199A   06223.76547498 0.00000000  00000-0  00000-0 0    08
2 90062   7.2890 189.8930 6839993 283.3245  76.6751  2.77430457    08
Unknown 060616
1 90061U 06667A   06222.02218586 0.00003000  00000-0  37574-3 0    00
2 90061  27.3823 233.4744 6875518 226.8912 133.1086  2.82348878    02
Unknown 060617
1 90058U 06668A   06213.87615521 0.00110000  00000-0  70237-3 0    02
2 90058  26.4049 222.4175 5435308 258.1896 101.8100  5.06142444    00
Unknown 060520
1 90060U 06640A   06213.63054290 0.00000000  00000-0  00000-0 0    05
2 90060  29.2763  47.7373 7093583  80.6305 279.3694  2.32913910    04
Unknown 060624
1 90059U 06675A   06213.40370816 0.00000542  00000-0  14233-3 0    08
2 90059  28.7365 286.3203 7286371 158.7000 201.2761  2.27620548    00
Unknown 060625
1 90057U 06676A   06207.01005982 0.00000000  00000-0  00000-0 0    09
2 90057  26.9476  68.1456 7173774  54.7817 305.4409  2.34416859    02
USA 184
1 29249U 06027A   06200.42851878 0.00000700  00000-0  15249-0 0    03
2 29249  63.2108  44.0449 7162774 268.3637  91.6363  2.00508383    09
Unknown 960906
1 90055U 96750A   06199.08002185 0.00000000  00000-0  00000-0 0    08
2 90055   5.2943   3.1498 0925710 210.8082 149.1923  1.00270000    03
Unknown 950327
1 90054U 95586A   06198.46725162 0.00000000  00000-0  00000-0 0    01
2 90054   3.0358  76.0091 0039416 175.6179 184.2812  1.00270000    07
Unknown 030923
1 90016U 03766A   06198.19827141 0.00000000  00000-0  00000-0 0    08
2 90016   6.8666  13.8494 0583335 183.1413 176.5626  1.00270000    00
Unknown 041026
1 90025U 04800A   06183.53789828 0.00001050  00000-0  14709-0 0    06
2 90025  64.1225 256.4894 7210093 262.9974  99.0174  2.00587000    09
Unknown 041211
1 90028U 04846A   06159.43062649 0.00000000  00000-0  00000-0 0    09
2 90028  64.0772  29.4966 7382273 261.9243  98.0757  2.00625000    03
Unknown 000405
1 90006U 00596A   06145.29819421 0.00000095  00000-0  23938-0 0    09
2 90006  63.3529 199.9244 6752207 283.4119  76.5881  2.00555791    09
Unknown 050220
1 90053U 05551A   06143.34198075 0.00000000  00000-0  00000-0 0    07
2 90053   7.8144 353.9381 1073396 272.0437  87.9563  1.00270000    07
Unknown 010313
1 90009U 01572A   06140.74274119 0.00000000  00000-0  00000-0 0    02
2 90009   2.9314  45.9265 0015000 339.4929  20.5071  1.00270000    00
Unknown 060419
1 90052U 04109A   06109.85366700 0.00000000  00000-0  00000-0 0    04
2 90052   9.3679  53.1385 0012000 315.6230  44.3770  1.00270000    05
USA 116
1 23728U 95066A   06108.05776286 0.00001000  00000-0  51035-4 0    06
2 23728  97.8800 241.3477 0282154  48.8003 311.1996 14.88264379    01
Unknown 000601
1 90007U 00653A   06098.95306970 0.00000000  00000-0  00000-0 0    05
2 90007   9.8323  48.0204 0047144  54.8546 305.5982  1.00239154    00
Unknown 990907
1 90004U 99750A   06097.80600307 -.00000505  00000-0 -18863-0 0    00
2 90004  64.5291 350.4796 7084586 279.3597  80.6391  2.01495310    08
Unknown 050518
1 90037U 05638A   06079.40180517 0.00000000  00000-0  00000-0 0    02
2 90037  14.2982  33.7953 0021888 235.5780 124.4306  1.00271000    05
Unknown 041206
1 90027U 04841A   06071.55035598 0.00001113  00000-0  11045+1 0    09
2 90027  62.3773 158.6750 6940454 268.4454  91.5512  2.00728666    05
Unknown 050227
1 90050U 05558C   06059.93910082 0.00000000  00000-0  00000-0 0    02
2 90050  13.9238  13.1234 0018764  91.5995 268.6274  0.98818813    01
Milstar 6 Cr
1 27712U 03012B   06059.79819916 0.00000000  00000-0  00000-0 0    08
2 27712   1.5656 328.5041 0038437 140.3392 219.9544  1.00554043    00
KH 9-16 Elint
1 11852U 80052C   06039.21206398 0.00000017  00000-0  71475-4 0    00
2 11852  96.6040  17.8887 0001500  51.8884 308.1115 12.83309062    06
Unknown 050415
1 90048U 05605B   06038.05573991 0.00000000  00000-0  00000-0 0    06
2 90048   5.5634  76.0751 0032072  14.1134 345.9977  1.00594285    08
Unknown 050415
1 90049U 05605C   06037.27383977 0.00000000  00000-0  00000-0 0    03
2 90049   4.1640 161.3551 0011879 324.0805  35.8513  1.00595721    04
STEX
1 25489U 98055A   06030.73270506 0.00000110  00000-0  30596-4 0    06
2 25489  84.9825  81.8375 0008000 315.1152  44.8847 14.46509155    09
Unknown 060121
1 90047U 06521A   06024.72702083 0.00000000  00000-0  00000-0 0    08
2 90047  25.7535 308.6171 7207107 335.9939  24.0059  2.28274700    02
Unknown 051002
1 90041U 05775A   06024.52102519 0.00000000  00000-0  00000-0 0    08
2 90041  14.1180 347.6590 0030902 162.3863 197.7332  1.00479337    04
KH 9-17 Elint
1 13172U 82041C   06021.77836867 0.00000380  00000-0  48262-4 0    00
2 13172  95.9810  59.5302 0003003 148.0009 211.9990 14.81752848    09
NOSS 0 (D)
1 05681U 71110D   06021.76087966 0.00000030  00000-0  31852-4 0    07
2 05681  69.9900 253.0594 0004000 210.9628 149.0372 13.74150281    03
NOSS 0 (A)
1 05678U 71110A   06021.74281767 0.00000020  00000-0  21364-4 0    02
2 05678  69.9820 260.2836 0006000 164.1547 195.8453 13.73783199    09
NOSS 2 (F)
1 10594U 77112F   06021.23098060 0.00000180  00000-0  36089-4 0    06
2 10594  63.3373  73.9008 0818000  28.9052 331.0948 13.44595788    08
NOSS 0 (C)
1 05680U 71110C   06020.75411501 0.00000030  00000-0  31803-4 0    06
2 05680  69.9810 254.0019 0008000 161.0640 198.9360 13.74231084    00
Unknown 050227
1 90033U 05558A   06018.85731161 0.00000000  00000-0  00000-0 0    08
2 90033   2.0160  74.6800 0030000  33.1612 326.8388  1.00270000    08
Unknown 991031
1 90005U 99804A   06018.73290965 0.00000000  00000-0  00000-0 0    03
2 90005   7.9806   6.3675 0472424 243.4249 111.6810  0.99563483    09
Unknown 050402
1 90034U 05592A   06018.71910417 0.00000000  00000-0  00000-0 0    05
2 90034   3.8000  45.6702 0007491 106.8854 253.1146  1.00270000    08
Unknown 050215
1 90031U 05546A   06018.65572539 0.00000000  00000-0  00000-0 0    03
2 90031   1.1000  63.5709 0010222 179.2424 180.7576  1.00270000    07
Unknown 050112
1 90029U 05512A   06018.63718640 0.00000000  00000-0  00000-0 0    06
2 90029  13.8738  13.1142 0003995  71.2329 288.8224  0.98951704    01
Milstar 3 Cn r
1 25725U 99023B   06018.02416152 0.00000130  00000-0  29077-3 0    05
2 25725  28.3070 308.1593 2388000  91.5240 268.4755  9.67067529    02
Unknown 990103
1 90003U 99503A   06018.00710268 0.00000000  00000-0  00000-0 0    00
2 90003  13.1475  24.2150 0009180 116.4066 243.6997  0.98677698    01
KH 9-18 Elint
1 14139U 83060C   06017.76197650 -.00000010  00000-0 -36357-4 0    04
2 14139  96.6545 212.5709 0001500 215.9289 144.0710 12.93723529    03
USA 186
1 28888U 05042A   06012.74211712 0.00010500  00000-0  10732-3 0    04
2 28888  97.8724  77.6223 0550578 269.8685  90.1314 14.72977790    05
NOSS 3-2 (C)
1 28097U 03054C   06012.28086606 0.00000030  00000-0  53974-4 0    01
2 28097  63.4380 140.5002 0063000 175.7481 184.2519 13.40484583    06
NOSS 3-2 (A)
1 28095U 03054A   06012.28078454 0.00000030  00000-0  54013-4 0    06
2 28095  63.4350 140.3003 0061000 175.2463 184.7537 13.40484330    08
NOSS 2-1 (E)
1 20642U 90050E   06012.26882069 0.00000010  00000-0  10763-4 0    03
2 20642  63.4060 119.1582 0423000 358.1103   1.8897 13.40460764    00
NOSS 5 (D)
1 14144U 83056D   06012.26535057 0.00000030  00000-0  14479-4 0    03
2 14144  63.3700 156.2478 0660000  16.5321 343.4679 13.41342763    08
NOSS 3 (A)
1 11720U 80019A   06012.26008070 0.00000100  00000-0  41590-4 0    08
2 11720  63.4061  63.2060 0689094 339.9632  20.0368 13.42277773    03
NOSS 5 (G)
1 14180U 83056G   06012.25830263 0.00000030  00000-0  14961-4 0    05
2 14180  63.3700 157.2054 0652500  11.3842 348.6158 13.41275153    03
NOSS 5 (C)
1 14143U 83056C   06012.25073528 0.00000060  00000-0  29173-4 0    01
2 14143  63.3670 155.4097 0658000  16.3428 343.6572 13.41381711    04
NOSS 2 (E)
1 10544U 77112E   06012.24981873 0.00000240  00000-0  48080-4 0    06
2 10544  63.3280  91.6270 0816500  34.9837 325.0163 13.44913427    05
NOSS 8 (F)
1 18010U 87043F   06012.23104210 0.00000030  00000-0  23342-4 0    08
2 18010  63.3950 102.2883 0534000   6.2713 353.7287 13.40809255    05
NOSS 2 (D)
1 10529U 77112D   06012.22156335 0.00000250  00000-0  49488-4 0    08
2 10529  63.3330  91.3147 0818500  35.0169 324.9831 13.44914612    03
NOSS 5 (A)
1 14112U 83056A   06012.20716683 0.00000100  00000-0  50482-4 0    00
2 14112  63.3690 152.9751 0648000  11.5924 348.4076 13.41544224    00
NOSS 3 (G)
1 11745U 80019G   06012.20310123 0.00000100  00000-0  42507-4 0    03
2 11745  63.4122  71.4502 0686500 339.2665  20.7335 13.41864885    04
DMSP F16
1 28054U 03048A   06011.79395072 -.00000020  00000-0 -10654-4 0    01
2 28054  98.8208  54.4827 0010000 116.4122 243.5877 14.13401246    06
Lacrosse 3
1 25017U 97064A   06011.27682724 0.00000140  00000-0  22468-4 0    01
2 25017  57.0100 167.8106 0005000 108.4515 251.5485 14.71324217    00
NOSS 8 (E)
1 18009U 87043E   06011.25757371 0.00000050  00000-0  39153-4 0    08
2 18009  63.3960 104.7865 0532000   5.9063 354.0938 13.40811205    08
NOSS 0 (E)
1 05682U 71110E   06010.89007426 0.00000020  00000-0  21229-4 0    09
2 05682  69.9803 275.1969 0010000 175.2520 184.7480 13.74147571    02
USA 32
1 19460U 88078A   06010.87279986 0.00000050  00000-0  18408-4 0    07
2 19460  84.9840 123.8525 0004000 235.1365 124.8634 14.32693695    06
MSX
1 23851U 96024A   06010.81985590 0.00000060  00000-0  42438-4 0    06
2 23851  99.1184  89.5662 0007000 352.2393   7.7606 13.97829114    04
DMSP F15
1 25991U 99067A   06010.71545390 0.00000100  00000-0  50644-4 0    05
2 25991  98.5989  58.3927 0013001 112.0755 247.9244 14.16086491    08
Milstar 5
1 27168U 02001A   06010.59487748 0.00000000  00000-0  00000-0 0    09
2 27168   1.6801 327.9695 0006833  20.2919 339.7081  1.00270000    07
Unknown 050702
1 90040U 05683A   06010.57318895 0.00000407  00000-0  31110-3 0    01
2 90040  27.5239 114.8635 7016479 266.8135  93.2557  2.58073078    07
Unknown 050509
1 90036U 05629A   06010.40206371 0.00000000  00000-0  00000-0 0    03
2 90036   1.8500 326.9206 0020000 308.9433  51.0567  1.00270000    08
Unknown 050518
1 90038U 05638B   06010.36547102 0.00000000  00000-0  00000-0 0    00
2 90038   3.6133 312.7763 0010000 263.6647  96.3353  1.00270400    05
NOSS 2 (A)
1 10502U 77112A   06009.76375048 0.00000250  00000-0  50559-4 0    09
2 10502  63.3360  98.9638 0815500  28.7167 331.2833 13.44798729    01
Unknown 051230
1 90046U 05864A   06009.57536690 0.00000112  00000-0  10215-0 0    04
2 90046  63.4777 260.4332 6956666 276.0373  83.9628  2.00613732    07
NOSS 1 (C)
1 08835U 76038C   06009.27537296 0.00000900  00000-0  94452-4 0    04
2 08835  63.3040  85.2586 0871500  58.5500 301.4500 13.53464917    06
NOSS 1 (A)
1 08818U 76038A   06009.27071717 0.00000910  00000-0  93106-4 0    02
2 08818  63.3050  84.6572 0875000  53.9584 306.0416 13.53455271    06
Alexis r
1 22639U 93026B   06009.24935143 0.00000070  00000-0  26102-4 0    03
2 22639  69.9190  48.0928 0064000 302.0895  57.9105 14.30763043    04
NOSS 8 (A)
1 17997U 87043A   06009.24674221 0.00000050  00000-0  36703-4 0    09
2 17997  63.3950  96.3688 0548500   2.8452 357.1548 13.41315349    01
AMS 2(DMSP F2)
1 10033U 77044A   06009.20947247 0.00000055  00000-0  22039-4 0    02
2 10033  99.1150 341.8062 0041000 195.1400 164.8599 14.27901766    08
USA 39 (DSP)
1 20066U 89046A   06008.23830112 0.00000000  00000-0  00000-0 0    08
2 20066   8.9654  47.9789 0012000 312.8426  47.1608  1.00270000    07
Alexis
1 22638U 93026A   06008.04402818 0.00000100  00000-0  36599-4 0    02
2 22638  69.9176  29.4719 0061000 285.0361  74.9639 14.31805374    09
Unknown 050213
1 90030U 05544A   06007.24787862 0.00000000  00000-0  00000-0 0    00
2 90030   6.0118  48.8949 0114617 166.7998 193.5150  0.99578393    05
Unknown 981016
1 90002U 98789A   06006.92648003 0.00000000  00000-0  00000-0 0    09
2 90002  13.7831 340.5774 0016555 305.1111  54.7458  0.99808667    06
Unknown 041002
1 90023U 04776A   06006.38858888 0.00000000  00000-0  00000-0 0    09
2 90023   5.0100 177.7034 0004000 205.7851 154.2263  1.00270000    06
Milstar 3
1 25724U 99023A   06005.78692418 0.00000080  00000-0  10081-2 0    02
2 25724  28.2355 206.3189 2132000 174.9652 185.0343  9.37434718    08
Milstar 6
1 27711U 03012A   06005.70465450 0.00000000  00000-0  00000-0 0    09
2 27711   1.9200 268.8640 0003000 300.5910  59.4134  1.00270200    05
NOSS 3-2 r
1 28096U 03054B   06004.26667110 0.00000020  00000-0  35653-4 0    07
2 28096  63.6760 176.3028 0082000 131.1629 228.8371 13.40560965    05
DMSP 7
1 07816U 75043A   06004.26317354 0.00000070  00000-0  31254-4 0    01
2 07816  98.5820 203.1249 0053000 225.1915 134.8084 14.22025303    00
USA 3
1 15071U 84065C   06004.24535974 0.00000500  00000-0  60160-4 0    01
2 15071  95.8872 199.5948 0003000 160.1409 199.8589 14.84003314    01
NOSS 1 (J)
1 08884U 76038J   06004.24488934 0.00000900  00000-0  94391-4 0    06
2 08884  63.3070  98.1516 0871500  58.2759 301.7241 13.53482768    01
NOSS 4 (H)
1 13874U 83008H   06003.75362458 0.00000160  00000-0  74156-4 0    08
2 13874  63.3690 324.6016 0669000  18.2405 341.7596 13.41442010    00
AMS 4(DMSP F4)
1 11389U 79050A   06003.72990493 0.00000060  00000-0  24677-4 0    04
2 11389  98.8730  44.0192 0014000 100.7336 259.2663 14.26974127    00
DMSP F14
1 24753U 97012A   06003.72450074 0.00000080  00000-0  41276-4 0    03
2 24753  98.5480  19.8760 0009000 139.4492 220.5507 14.15118092    02
IGS 1A
1 27698U 03009A   06002.84702713 0.00000000  00000-0  00000-0 0    07
2 27698  97.4061  78.8833 0001000 346.0767  13.9232 15.25957369    04
USA 141 (ATEX)
1 25615U 98055C   06002.84052518 0.00000150  00000-0  44352-4 0    08
2 25615  84.9820 104.9407 0007000  46.9351 313.0648 14.43555225    03
Unknown 051225
1 90044U 05859A   06002.82944993 0.00020000  00000-0  96959-3 0    06
2 90044  63.2528 236.8413 4261404 294.7048  65.2952  6.98670114    08
IGS 1B
1 27699U 03009B   06002.82136744 0.00000000  00000-0  00000-0 0    01
2 27699  97.4011  78.8328 0001500 337.8526  22.1473 15.25959078    03
USA 125 r
1 23947U 96038C   06002.80292820 0.00000070  00000-0  17014-3 0    06
2 23947  55.3758 221.6783 4893500 174.2271 185.7729  5.48310268    08
Unknown 051228
1 90045U 05862B   06002.66182344 0.00000000  00000-0  00000-0 0    04
2 90045   8.5203 186.2035 5754874  27.5269 332.4727  4.22727690    01
NOSS 3 (C)
1 11731U 80019C   06002.19803734 0.00000100  00000-0  31733-4 0    09
2 11731  63.3990  75.3164 0744500 347.7610  12.2390 13.42586373    08
NOSS 2-1 (D)
1 20692U 90050D   06002.19775123 0.00000010  00000-0  10628-4 0    01
2 20692  63.4060 145.1925 0428000   2.4392 357.5608 13.40462948    06
NOSS 2-1 (C)
1 20691U 90050C   06002.19768306 0.00000010  00000-0  10628-4 0    05
2 20691  63.4080 145.4648 0428000   2.3923 357.6077 13.40463970    08
NOSS 3-3 r
1 28538U 05004B   06002.19553970 0.00000010  00000-0  16881-4 0    04
2 28538  63.8281  43.9989 0114000 147.8157 212.1843 13.42859142    07
NOSS 3 (D)
1 11732U 80019D   06002.19206682 0.00000110  00000-0  35134-4 0    09
2 11732  63.3970  75.5233 0743500 347.9431  12.0569 13.42531475    07
NOSS 8 (H)
1 18025U 87043H   06002.17263149 0.00000040  00000-0  32346-4 0    08
2 18025  63.3940 128.2963 0522000 359.7676   0.2324 13.40795143    04
Lacrosse 2
1 21147U 91017A   06002.17048373 0.00000160  00000-0  23506-4 0    04
2 21147  67.9940 150.6437 0005000 254.4290 105.5710 14.75374457    05
USA 89 r
1 22519U 92086C   06002.16731662 0.00001900  00000-0  32267-3 0    00
2 22519  56.9280  45.0522 3218246 309.2593  50.7407  8.76398053    08
USA 171 r
1 27938U 03041B   06002.16161718 0.00000000  00000-0  00000-0 0    09
2 27938   4.8448 219.9329 0036325 166.7110 193.3965  1.00857694    01
NOSS 3-3 (C)
1 28541U 05004C   06002.15450342 0.00000020  00000-0  35290-4 0    09
2 28541  63.4340  35.9774 0103000 177.6416 182.3585 13.40481471    08
NOSS 3-3 (A)
1 28537U 05004A   06002.15441714 0.00000010  00000-0  17645-4 0    00
2 28537  63.4340  35.7759 0103000 177.7610 182.2391 13.40481310    07
NOSS 2-2 (D)
1 21808U 91076D   06002.15211711 0.00000020  00000-0  23697-4 0    05
2 21808  63.4130  34.0652 0382500   1.3918 358.6082 13.40475952    00
NOSS 2-2 (E)
1 21809U 91076E   06002.15200984 0.00000020  00000-0  23938-4 0    04
2 21809  63.4140  33.6286 0378000 356.1064   3.8936 13.40476059    09
NOSS 2-2 (C)
1 21799U 91076C   06002.15198731 0.00000020  00000-0  23751-4 0    01
2 21799  63.4120  33.7995 0381500   1.6448 358.3552 13.40476112    02
USA 144 Deb
1 25746U 99028C   06002.14793056 0.00000060  00000-0  92484-2 0    03
2 25746  63.4412  85.4913 0242000 294.0968  65.9032  9.69821966    03
Lacrosse 5 r
1 28647U 05016B   06001.68331250 0.00000600  00000-0  44507-4 0    07
2 28647  56.9980 231.2148 0164000  89.6177 270.3822 14.92462870    03
AMS 1(DMSP F1)
1 09415U 76091A   06001.25011777 0.00000070  00000-0  29618-4 0    09
2 09415  98.9850 210.8688 0012000 137.6036 222.3963 14.25525199    02
XSS-11 r
1 28637U 05011B   06001.24515133 0.00000060  00000-0  33380-4 0    04
2 28637  98.8516 356.0730 0010997 169.6387 190.3612 14.11054175    06
XSS-11
1 28636U 05011A   06001.24510227 0.00000070  00000-0  38934-4 0    03
2 28636  98.8526 356.0685 0013000 178.6393 181.3606 14.11055223    08
DMSP B5D2-7
1 23233U 94057A   06001.23996751 0.00000090  00000-0  46824-4 0    07
2 23233  98.5560 347.5658 0012000 299.9347  60.0652 14.14656230    03
NOSS 1 (D)
1 08836U 76038D   06001.23692537 0.00000900  00000-0  92190-4 0    00
2 08836  63.3045 116.3278 0878000  53.6809 306.3191 13.52814296    04
USA 102
1 23031U 94017B   06001.05606452 0.00002450  00000-0  10644-3 0    07
2 23031 105.0348 197.9572 0016000 126.6818 233.3181 15.22131729    05
Geosat FO
1 25157U 98007A   06001.01381868 0.00000050  00000-0  18797-4 0    00
2 25157 108.0561 183.2132 0001965 319.6116  40.3884 14.31515516    00
NOSS 3-1 (A)
1 26905U 01040A   05365.82917860 0.00000020  00000-0  36402-4 0    01
2 26905  63.4370 252.6798 0005000  66.7155 293.2845 13.40482888    00
NOSS 3-1 (C)
1 26907U 01040C   05365.82908481 0.00000020  00000-0  36402-4 0    02
2 26907  63.4290 252.4506 0005000  90.4103 269.5897 13.40483196    01
NOSS 6 (C)
1 14728U 84012C   05365.82802004 0.00000140  00000-0  76072-4 0    04
2 14728  63.3730 255.3263 0634500  15.1951 344.8049 13.40721876    03
NOSS 6 (D)
1 14729U 84012D   05365.82148756 0.00000140  00000-0  76387-4 0    01
2 14729  63.3730 254.7782 0633000  15.3266 344.6734 13.40800738    02
TiPS
1 23937U 96029F   05365.81682843 0.00001000  00000-0  73955-3 0    05
2 23937  63.4005 236.3733 0323997   4.2196 355.7804 13.73082070    09
NOSS 3-1 r
1 26906U 01040B   05365.81442981 0.00000010  00000-0  17328-4 0    03
2 26906  63.4746 235.6115 0010500 169.7159 190.2841 13.43638197    02
DMSP B5D2-6
1 21798U 91082A   05365.79588958 0.00000090  00000-0  45971-4 0    07
2 21798  98.6393  16.1728 0013000  20.6178 339.3821 14.15631006    06
NOSS 6 (A)
1 14690U 84012A   05365.79376013 0.00000150  00000-0  83314-4 0    02
2 14690  63.3780 249.4662 0625000   7.9287 352.0713 13.41396801    05
NOSS 4 (F)
1 13845U 83008F   05365.78563490 0.00000180  00000-0  85077-4 0    04
2 13845  63.3660 332.2210 0664500  18.6956 341.3044 13.41422712    02
USA 179 Cn r
1 28385U 04034B   05365.77545288 0.00002300  00000-0  69736-3 0    04
2 28385  57.3912 281.7272 5245781  61.4870 298.5130  5.17267731    09
NOSS 2-3 (E)
1 23936U 96029E   05365.77526370 0.00000030  00000-0  46450-4 0    04
2 23936  63.4210 313.6991 0235000   0.3324 359.6676 13.40477576    01
NOSS 2-3 (C)
1 23908U 96029C   05365.77520912 0.00000030  00000-0  46482-4 0    04
2 23908  63.4190 313.4749 0234500 357.6241   2.3759 13.40477541    02
NOSS 2-3 (D)
1 23862U 96029D   05365.77515009 0.00000030  00000-0  46515-4 0    01
2 23862  63.4170 313.5618 0234000   0.8115 359.1885 13.40476571    02
NOSS 6 (F)
1 14795U 84012F   05365.76390722 0.00000110  00000-0  61830-4 0    03
2 14795  63.3770 258.4890 0626000   7.7191 352.2809 13.40703219    08
Lacrosse 5
1 28646U 05016A   05365.76346897 0.00000040  00000-0  95517-5 0    06
2 28646  57.0110 293.2429 0007000 187.6750 172.3250 14.53349022    07
NOSS 0 r
1 05679U 71110B   05365.76203398 0.00000030  00000-0  26500-4 0    07
2 05679  70.0000 210.4505 0015000 293.5570  66.4430 13.84958551    02
NOSS 4 (A)
1 13791U 83008A   05365.75640978 0.00000240  00000-0  11426-3 0    01
2 13791  63.3680 326.6365 0661000  13.3522 346.6478 13.41737496    02
USA 40 r
1 20344U 89061D   05365.75227907 0.00000080  00000-0  74094-4 0    04
2 20344  57.0097 333.9693 3552000  50.5787 309.4213  7.85782853    01
NOSS 4 (E)
1 13844U 83008E   05365.75151752 0.00000200  00000-0  96629-4 0    02
2 13844  63.3690 333.2877 0659500  13.2795 346.7205 13.41384743    09
DMSP B5D2-8
1 23533U 95015A   05365.74221147 0.00000080  00000-0  41460-4 0    03
2 23533  98.8056  18.3941 0007000 250.8729 109.1270 14.14886173    03
NOSS 7 (H)
1 16631U 86014H   05365.73927053 0.00000070  00000-0  51003-4 0    04
2 16631  63.3890 217.8019 0556000   2.1894 357.8106 13.40471184    09
NOSS 7 (E)
1 16624U 86014E   05365.73905480 0.00000080  00000-0  55849-4 0    09
2 16624  63.3830 214.1538 0568500  11.2175 348.7825 13.40470702    04
NOSS 7 (D)
1 16623U 86014D   05365.73886567 0.00000080  00000-0  56334-4 0    02
2 16623  63.3842 214.0383 0566000  11.2966 348.7034 13.40471088    04
NOSS 7 (A)
1 16591U 86014A   05365.73722074 0.00000070  00000-0  49561-4 0    01
2 16591  63.3900 210.5319 0560502   2.3116 357.6884 13.41103355    04
Lacrosse 4
1 26473U 00047A   05365.73533576 0.00000100  00000-0  18922-4 0    01
2 26473  67.9950 310.5724 0006000 273.8098  86.1902 14.64250326    04
Unknown 030305
1 90013U 03564A   05365.62255760 0.00000000  00000-0  00000-0 0    06
2 90013   7.1137   8.3672 0042091 213.9246 146.0754  1.00270000    00
USA 161
1 26934U 01044A   05364.93732890 0.00000900  00000-0  51180-4 0    03
2 26934  97.9180 109.5229 0343693 129.9356 230.0642 14.74398653    08
USA 129
1 24680U 96072A   05364.85222684 0.00011000  00000-0  15375-3 0    08
2 24680  97.9382  65.5364 0514056 244.8119 115.1880 14.74984649    09
Unknown 051124
1 90042U 05828A   05364.80475198 0.00000000  00000-0  00000-0 0    01
2 90042   1.8300  85.8634 0002000 213.9437 146.0563  1.00270000    09
USA 81
1 21949U 92023A   05364.75195687 0.00000040  00000-0  15305-4 0    02
2 21949  85.0070  58.6990 0002000 125.3078 234.6920 14.30742967    01
Unknown 051201
1 90043U 05835A   05364.71370386 0.00000000  00000-0  00000-0 0    03
2 90043   1.5656 346.0967 0007000 148.2516 211.7484  1.00270000    07
Unknown 001203
1 90008U 00838A   05362.95530853 0.00000000  00000-0  00000-0 0    03
2 90008   6.9461 114.1948 0019914 174.6606 185.3725  1.00547382    08
Unknown 050505
1 90035U 05625A   05362.54974897 0.00000000  00000-0  00000-0 0    07
2 90035   0.0200 354.9914 0003000  95.6060 264.3940  1.00270000    03
Unknown 050708
1 90039U 05689A   05346.40921668 0.00001052  00000-0  00000-0 0    04
2 90039  63.8308  12.1969 7098024 260.2953  99.7042  2.00744639    02
Unknown 041011
1 90024U 04785A   05274.35638107 0.00000000  00000-0  00000-0 0    03
2 90024   0.0500  85.8960 0001000   9.5595 350.4405  1.00270000    03
Unknown 040208
1 90020U 04539A   05257.20527666 -.00000371  00000-0 -79704-0 0    08
2 90020  64.7204 285.9802 6783484 266.9398  93.0589  2.00951372    06
Unknown 050415
1 90051U 05605A   05241.35118712 0.00000000  00000-0  00000-0 0    04
2 90051   7.2179 348.6914 1295010 314.1949  35.8646  1.00150951    01
Unknown 050318
1 90032U 05577A   05116.46023920 0.00000411  00000-0  00000-0 0    06
2 90032  63.5256 327.4948 7380134 263.0325  96.9675  2.00614585    00
'''

snapshots['test_object_influence 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'application/json', 'Access-Control-Allow-Origin': '*'}

CONTENT:[
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 28, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 25, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 21, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 20, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 18, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 17, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 15, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 13, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 07, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 02, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "July 23, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "July 20, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "June 06, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 22, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 21, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 15, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 14, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 01, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 29, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 23, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 22, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 21, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 17, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 17, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 13, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 12, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 09, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 25, 2019",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 12, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 08, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 07, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 04, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 01, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 29, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 24, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 23, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 07, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "July 24, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "July 19, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "July 17, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "June 06, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 23, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 18, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 14, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 13, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 08, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 06, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 04, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 02, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 30, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 24, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 21, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 20, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 19, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 17, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 14, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 09, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 08, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 04, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 28, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 28, 2018",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 07, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 05, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 30, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 26, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 20, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 20, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 19, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 15, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 13, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 11, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 05, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "August 03, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "July 24, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "June 02, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 22, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "May 07, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 27, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 25, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 23, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 23, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 17, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 17, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 14, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 12, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 09, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 08, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 06, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 05, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "April 05, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 31, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 25, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 21, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 20, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 20, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 16, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "March 16, 2017",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 22, 2016",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 17, 2016",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    },
    {
        "object_origin": "JP",
        "observation_quality": "99",
        "observation_time": "September 16, 2016",
        "observation_time_difference": "3",
        "observation_weight": "0.123456",
        "user_address": "0x7C21fa08867F3bF07E8ECd793CA4719f431e1edd",
        "user_location": null,
        "username": "Russell Eberst"
    }
]'''

snapshots['test_object_info 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'application/json', 'Access-Control-Allow-Origin': '*'}

CONTENT:{
    "address_last_tracked": "0x730A8Ce1ad08d9FcCb162eD94416Ab5135823742",
    "heavens_above_url": "https://www.heavens-above.com/SatInfo.aspx?satid=40538",
    "number_users_tracked": "5",
    "object_background": "",
    "object_name": "IGS O-5",
    "object_origin": "JP",
    "object_purpose": "Optical Imaging",
    "object_secondary_purpose": "Optical reconnaissance.",
    "object_type": "Earth Observation",
    "observation_quality": "99",
    "time_last_tracked": "July 22, 2019",
    "username_last_tracked": "Pierros Papadeas",
    "year_launched": 2015
}'''

snapshots['test_tle_object 1'] = '''STATUS: 200

HEADERS:{'Server': 'BaseHTTP/0.6 Python/3.7.1', 'Date': 'XXX', 'Content-type': 'text/plain', 'Access-Control-Allow-Origin': '*'}

CONTENT:IGS Opt 5r
1 40538U 15015A   19235.85317892 0.00000000  00000-0  00000-0 0    08
2 40538  97.4630 309.8098 0001995 290.6915  69.3083 15.17628735    08
'''
