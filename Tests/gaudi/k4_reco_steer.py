#!/usr/bin/python3

from Gaudi.Configuration import *
from GaudiKernel.Constants import INFO, WARNING

DD4hepXMLFile = "/usr/share/muonc-detector-geometry/MuSIC_v2/MuSIC_v2.xml"
matMapFile = "/usr/share/MarlinACTS/data/material-maps.json"
TGeoFile = "/usr/share/MarlinACTS/data/MuSIC_v2.root"
TGeoDescFile = "/usr/share/MarlinACTS/data/MuSIC_v2.json"
GeoSchema = "MuSIC_v2"

digiInputFile = "digi_output.edm4hep.root"
recoOutputFile = "reco_output.edm4hep.root"

rSeed = 42

algList = []

###############################################################################
# Services
###############################################################################
from Configurables import GeoSvc, UniqueIDGenSvc, EventDataSvc, THistSvc
from k4FWCore import IOSvc

geoservice = GeoSvc(
    "GeoSvc",
    detectors = [ DD4hepXMLFile ],
    OutputLevel = INFO,
    EnableGeant4Geo = False
)

evtsvc = EventDataSvc("EventDataSvc")

id_service = UniqueIDGenSvc(
    "UniqueIDGenSvc", 
    Seed = rSeed
)
    
THistSvc().Output = ["histos DATAFILE='digi_histograms.root' TYP='ROOT' OPT='RECREATE'"]
THistSvc().PrintAll = True
THistSvc().AutoSave = True
THistSvc().AutoFlush = True
THistSvc().OutputLevel = WARNING

svc = IOSvc(
    "IOSvc",
    Input = [ digiInputFile ],
    Output = recoOutputFile
)

###############################################################################
# Reconstruction
###############################################################################
from Configurables import ACTSSeededCKFTrackingAlg, ACTSDuplicateRemoval

algList.append(ACTSSeededCKFTrackingAlg(
    "Reconstructor",
    MatFile = matMapFile,
    TGeoFile = TGeoFile,
    TGeoDescFile = TGeoDescFile,
    DetectorSchema = GeoSchema,
    RunCKF = "True",
    CKF_Chi2CutOff = 10,
    SeedFinding_RMax = 150,
    SeedFinding_MinPt = 500,
    SeedFinding_DeltaRMin = 2,
    SeedFinding_DeltaRMax = 60,
    CKF_NumMeasurementsCutOff = 1,
    SeedFinding_SigmaScattering = 3,
    SeedFinding_CollisionRegion = 3.5,
    SeedFinding_RadLengthPerSeed = 0.1,
    SeedingLayers = ["13", "2", "13", "6", "13", "10", "13", "14", "14", "2", "14", "6", "14", "10", "14", "14", "15", "2", "15", "6", "15", "10", "15", "14"],
    OutputTrackCollectionName = ["AllTracks"],
    OutputSeedCollectionName = ["SeedTracks"],
    InputTrackerHitCollectionName = [
        "VXDBarrelHits",
        "VXDEndcapHits",
        "ITBarrelHits",
        "ITEndcapHits",
        "OTBarrelHits",
        "OTEndcapHits"
    ],
    OutputLevel = INFO
))

algList.append(ACTSDuplicateRemoval(
    "Deduper",
    InputTrackCollectionName = ["AllTracks"],
    OutputTrackCollectionName = ["DedupedTracks"],
    OutputLevel = INFO
))

###############################################################################
# Execution
###############################################################################
from Configurables import EventLoopMgr
from k4FWCore import ApplicationMgr

ApplicationMgr(
    TopAlg = algList,
    EvtSel = 'NONE',
    EvtMax   = 10,
    ExtSvc = [evtsvc, geoservice],
    EventLoop = EventLoopMgr(),
    OutputLevel=INFO
)



