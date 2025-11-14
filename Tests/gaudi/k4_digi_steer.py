#!/usr/bin/python3

from Gaudi.Configuration import *
from GaudiKernel.Constants import INFO, WARNING

DD4hepXMLFile = "/usr/share/muonc-detector-geometry/MuSIC_v2/MuSIC_v2.xml"
simInputFile = "sim_output.edm4hep.root"
digiOutputFile = "digi_output.edm4hep.root"

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
    Input = [ simInputFile ],
    Output = digiOutputFile
)

###############################################################################
# Digitization
###############################################################################
from Configurables import DDPlanarDigi

algList.append(DDPlanarDigi(
    "VXDBarrelDigitiser",
    CorrectTimesForPropagation = True,
    IsStrip = False,
    ResolutionT = [0.03],
    ResolutionU = [0.005],
    ResolutionV = [0.005],
    SubDetectorName = "Vertex",
    TimeWindowMax = [0.15],
    TimeWindowMin = [-0.09],
    UseTimeWindow = True,
    SimTrackHitCollectionName = ["VertexBarrelCollection"],
    SimTrkHitRelCollection = ["VXDBarrelHitsRelations"],
    TrackerHitCollectionName = ["VXDBarrelHits"],
    OutputLevel = INFO
))

algList.append(DDPlanarDigi(
    "VXDEndcapDigitiser",
    CorrectTimesForPropagation = True,
    IsStrip = False,
    ResolutionT = [0.03],
    ResolutionU = [0.005],
    ResolutionV = [0.005],
    SubDetectorName = "Vertex",
    TimeWindowMax = [0.15],
    TimeWindowMin = [-0.09],
    UseTimeWindow = True,
    SimTrackHitCollectionName = ["VertexEndcapCollection"],
    SimTrkHitRelCollection = ["VXDEndcapHitsRelations"],
    TrackerHitCollectionName = ["VXDEndcapHits"],
    OutputLevel = INFO
))

algList.append(DDPlanarDigi(
    "InnerBarrelDigitiser",
    CorrectTimesForPropagation = True,
    IsStrip = True,
    ResolutionT = [0.06],
    ResolutionU = [0.007],
    ResolutionV = [0.09],
    SubDetectorName = "InnerTrackers",
    TimeWindowMax = [0.3],
    TimeWindowMin = [-0.18],
    UseTimeWindow = True,
    SimTrackHitCollectionName = ["InnerTrackerBarrelCollection"],
    SimTrkHitRelCollection = ["ITBarrelHitsRelations"],
    TrackerHitCollectionName = ["ITBarrelHits"],
    OutputLevel = INFO
))

algList.append(DDPlanarDigi(
    "InnerEndcapDigitiser",
    CorrectTimesForPropagation = True,
    IsStrip = False,
    ResolutionT = [0.06],
    ResolutionU = [0.007],
    ResolutionV = [0.09],
    SubDetectorName = "InnerTrackers",
    TimeWindowMax = [0.3],
    TimeWindowMin = [-0.18],
    UseTimeWindow = True,
    SimTrackHitCollectionName = ["InnerTrackerEndcapCollection"],
    SimTrkHitRelCollection = ["ITEndcapHitsRelations"],
    TrackerHitCollectionName = ["ITEndcapHits"],
    OutputLevel = INFO
))

algList.append(DDPlanarDigi(
    "OTBarrelDigitiser",
    CorrectTimesForPropagation = True,
    IsStrip = False,
    ResolutionT = [0.06],
    ResolutionU = [0.007],
    ResolutionV = [0.09],
    SubDetectorName = "OuterTrackers",
    TimeWindowMax = [0.3],
    TimeWindowMin = [-0.18],
    UseTimeWindow = True,
    SimTrackHitCollectionName = ["OuterTrackerBarrelCollection"],
    SimTrkHitRelCollection = ["OTBarrelHitsRelations"],
    TrackerHitCollectionName = ["OTBarrelHits"],
    OutputLevel = INFO
))

algList.append(DDPlanarDigi(
    "OTEndcapDigitiser",
    CorrectTimesForPropagation = True,
    IsStrip = True,
    ResolutionT = [0.06],
    ResolutionU = [0.007],
    ResolutionV = [0.09],
    SubDetectorName = "OuterTrackers",
    TimeWindowMax = [0.3],
    TimeWindowMin = [-0.18],
    UseTimeWindow = True,
    SimTrackHitCollectionName = ["OuterTrackerEndcapCollection"],
    SimTrkHitRelCollection = ["OTEndcapHitsRelations"],
    TrackerHitCollectionName = ["OTEndcapHits"],
    OutputLevel = INFO
))

###############################################################################
# Digi filters
###############################################################################
from Configurables import FilterDoubleLayerHits

#algList.append(FilterDoubleLayerHits(
#    "FilterDL_VXDB",
#    DoubleLayerCuts = ["0", "1", "2.0", "35.0", "2", "3", "1.7", "18.0", "4", "5", "1.5", "10.0", "6", "7", "1.4", "6.5"],
#    FillHistograms = False,
#    SubDetectorName = "Vertex",
#    InputCollection = ["VXDBarrelHits"],
#    OutputCollection = ["VXDBarrelHits_DLFiltered"],
#    OutputLevel = INFO
#))

#algList.append(FilterDoubleLayerHits(
#    "FilterDL_VXDE",
#    DoubleLayerCuts = ["0", "1", "2.2", "8.0", "2", "3", "1.4", "2.8", "4", "5", "0.86", "0.7", "6", "7", "0.7", "0.3"],
#    FillHistograms = False,
#    SubDetectorName = "Vertex",
#    InputCollection = ["VXDEndcapHits"],
#    OutputCollection = ["VXDEndcapHits_DLFiltered"],
#    OutputLevel = INFO
#))

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


