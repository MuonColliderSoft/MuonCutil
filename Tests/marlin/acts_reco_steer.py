#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper, ApplicationMgr
from k4MarlinWrapper.parseConstants import *
from Gaudi.Main import gaudimain
import os

os.environ['LD_LIBRARY_PATH'] = '/usr/lib64'

algList = []
evtsvc = EventDataSvc()

CONSTANTS = {}

parseConstants(CONSTANTS)


# In[ ]:


read = LcioEvent()
read.OutputLevel = INFO
read.Files = ["muonGun_sim.slcio"]
algList.append(read)


# In[ ]:


Config = MarlinProcessorWrapper("Config")
Config.OutputLevel = INFO
Config.ProcessorType = "CLICRecoConfig"
Config.Parameters = {
                     "Overlay": ["False"],
                     "OverlayChoices": ["False", "Test", "BIB", "Trimmed"],
                     "Tracking": ["ACTs"],
                     "TrackingChoices": ["Truth", "Conformal", "ACTs"],
                     "VertexUnconstrained": ["OFF"],
                     "VertexUnconstrainedChoices": ["ON", "OFF"]
                     }
algList.append(Config)


# In[ ]:


EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = INFO
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
                          "HowOften": ["1"]
                          }
algList.append(EventNumber)


# In[ ]:


MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = INFO
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["lctuple"],
                              "FileType": ["root"]
                              }
algList.append(MyAIDAProcessor)


# In[ ]:


InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = INFO
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
                         "DD4hepXMLFile": ["/usr/share/muonc-detector-geometry/MuSIC_v2/MuSIC_v2.xml"],
                         "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
                         }
algList.append(InitDD4hep)


# In[ ]:


OverlayFalse = MarlinProcessorWrapper("OverlayFalse")
OverlayFalse.OutputLevel = INFO
OverlayFalse.ProcessorType = "OverlayTimingGeneric"
OverlayFalse.Parameters = {
                           "BackgroundFileNames": ["/dev/null"],
                           "Collection_IntegrationTimes": ["VertexBarrelCollection", "-0.18", "0.24", "VertexEndcapCollection", "-0.18", "0.24", "InnerTrackerBarrelCollection", "-0.36", "0.48", "InnerTrackerEndcapCollection", "-0.36", "0.48", "OuterTrackerBarrelCollection", "-0.36", "0.48", "OuterTrackerEndcapCollection", "-0.36", "0.48", "ECalBarrelCollection", "0.25", "ECalEndcapCollection", "0.25", "ECalPlugCollection", "0.25", "HCalBarrelCollection", "0.25", "HCalEndcapCollection", "0.25", "HCalRingCollection", "0.25", "YokeBarrelCollection", "0.25", "YokeEndcapCollection", "0.25"],
                           "Delta_t": ["1"],
                           "MCParticleCollectionName": ["MCParticle"],
                           "MCPhysicsParticleCollectionName": ["MCPhysicsParticles"],
                           "MergeMCParticles": ["false"],
                           "NBunchtrain": ["0"],
                           "NumberBackground": ["0."],
                           "PhysicsBX": ["1"],
                           "Poisson_random_NOverlay": ["false"],
                           "RandomBx": ["false"],
                           "TPCDriftvelocity": ["0.05"]
                           }
algList.append(OverlayFalse)


# In[ ]:


VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = INFO
VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDBarrelDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexBarrelCollection"],
                                 "SimTrkHitRelCollection": ["VXDTrackerHitRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.15"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VXDTrackerHits"],
                                 "UseTimeWindow": ["true"]
                                 }
algList.append(VXDBarrelDigitiser)


# In[ ]:


VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = INFO
VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDEndcapDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexEndcapCollection"],
                                 "SimTrkHitRelCollection": ["VXDEndcapTrackerHitRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.15"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VXDEndcapTrackerHits"],
                                 "UseTimeWindow": ["true"]
                                 }
algList.append(VXDEndcapDigitiser)


# In[ ]:


InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.OutputLevel = INFO
InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerPlanarDigiProcessor.Parameters = {
                                       "CorrectTimesForPropagation": ["true"],
                                       "IsStrip": ["false"],
                                       "ResolutionT": ["0.06"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.090"],
                                       "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection"],
                                       "SimTrkHitRelCollection": ["ITBarrelHitsRelations"],
                                       "SubDetectorName": ["InnerTrackers"],
                                       "TimeWindowMax": ["0.3"],
                                       "TimeWindowMin": ["-0.18"],
                                       "TrackerHitCollectionName": ["ITrackerHits"],
                                       "UseTimeWindow": ["true"]
                                       }
algList.append(InnerPlanarDigiProcessor)


# In[ ]:


InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper("InnerEndcapPlanarDigiProcessor")
InnerEndcapPlanarDigiProcessor.OutputLevel = INFO
InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerEndcapPlanarDigiProcessor.Parameters = {
                                             "CorrectTimesForPropagation": ["true"],
                                             "IsStrip": ["false"],
                                             "ResolutionT": ["0.06"],
                                             "ResolutionU": ["0.007"],
                                             "ResolutionV": ["0.090"],
                                             "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection"],
                                             "SimTrkHitRelCollection": ["ITEndcapHitsRelations"],
                                             "SubDetectorName": ["InnerTrackers"],
                                             "TimeWindowMax": ["0.3"],
                                             "TimeWindowMin": ["-0.18"],
                                             "TrackerHitCollectionName": ["ITrackerEndcapHits"],
                                             "UseTimeWindow": ["true"]
                                             }
algList.append(InnerEndcapPlanarDigiProcessor)


# In[ ]:


OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = INFO
OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterPlanarDigiProcessor.Parameters = {
                                       "CorrectTimesForPropagation": ["true"],
                                       "IsStrip": ["false"],
                                       "ResolutionT": ["0.06"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.090"],
                                       "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection"],
                                       "SimTrkHitRelCollection": ["OTBarrelHitsRelations"],
                                       "SubDetectorName": ["OuterTrackers"],
                                       "TimeWindowMax": ["0.3"],
                                       "TimeWindowMin": ["-0.18"],
                                       "TrackerHitCollectionName": ["OTrackerHits"],
                                       "UseTimeWindow": ["true"]
                                       }
algList.append(OuterPlanarDigiProcessor)


# In[ ]:


OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper("OuterEndcapPlanarDigiProcessor")
OuterEndcapPlanarDigiProcessor.OutputLevel = INFO
OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterEndcapPlanarDigiProcessor.Parameters = {
                                             "CorrectTimesForPropagation": ["true"],
                                             "IsStrip": ["false"],
                                             "ResolutionT": ["0.06"],
                                             "ResolutionU": ["0.007"],
                                             "ResolutionV": ["0.090"],
                                             "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection"],
                                             "SimTrkHitRelCollection": ["OTEndcapHitsRelations"],
                                             "SubDetectorName": ["OuterTrackers"],
                                             "TimeWindowMax": ["0.3"],
                                             "TimeWindowMin": ["-0.18"],
                                             "TrackerHitCollectionName": ["OTrackerEndcapHits"],
                                             "UseTimeWindow": ["true"]
                                             }
algList.append(OuterEndcapPlanarDigiProcessor)


# In[ ]:


MyCKFTracking = MarlinProcessorWrapper("MyCKFTracking")
MyCKFTracking.OutputLevel = INFO 
MyCKFTracking.ProcessorType = "ACTSCKFSeededTracker" 
MyCKFTracking.Parameters = {
                            "MatFile": ["/usr/share/MarlinACTS/data/material-maps.json"],
                            "TGeoFile": ["/usr/share/MarlinACTS/data/MuSIC_v2.root"],
                            "TGeoDescFile": ["/usr/share/MarlinACTS/data/MuSIC_v2.json"],
                            "DetectorSchema": ["MuSIC_v2"],
                            "SeedingLayers": ["13", "2", "13", "6", "13", "10", "13", "14", "14", "2", "14", "6", "14", "10", "14", "14", "15", "2", "15", "6", "15", "10", "15", "14"],
                            "SeedFinding_RMax": ["150"],
                            "SeedFinding_DeltaRMin": ["5"],
                            "SeedFinding_DeltaRMax": ["80"],
                            "SeedFinding_CollisionRegion": ["1"],
                            "SeedFinding_RadLengthPerSeed": ["0.1"],
                            "SeedFinding_SigmaScattering": ["50"],
                            "SeedFinding_MinPt": ["500"],
                            "SeedFinding_zBinSchema": ["-600,1,1,1,1", "-300,1,1,1,1", "0,1,1,1,1", "300,1,1,1,1"],
                            "CKF_Chi2CutOff": ["10"],
                            "CKF_NumMeasurementsCutOff": ["1"],
                            "TrackerHitCollectionNames": ["VXDTrackerHits", "VXDEndcapTrackerHits", "ITrackerHits", "ITrackerEndcapHits", "OTrackerHits", "OTrackerEndcapHits"],
                            "RunCKF": ["True"],
                            "MTCKFMode": ["True"],
                            "TrackCollectionName": ["SiTracks"]
                            }
algList.append(MyCKFTracking)


# In[ ]:


#MyTrackDeduper = MarlinProcessorWrapper("MyTrackDeduper")
#MyTrackDeduper.OutputLevel = INFO 
#MyTrackDeduper.ProcessorType = "ACTSDuplicateRemoval" 
#MyTrackDeduper.Parameters = {
#                             "InputTrackCollectionName": ["SiTracksACTs"],
#                             "OutputTrackCollectionName": ["SiTracks"]
#                             }
#algList.append(MyTrackDeduper)


# In[ ]:


Refit = MarlinProcessorWrapper("Refit")
Refit.OutputLevel = INFO
Refit.ProcessorType = "RefitFinal"
Refit.Parameters = {
                    "EnergyLossOn": ["true"],
                    "InputRelationCollectionName": ["MCParticle_Tracks"],
                    "InputTrackCollectionName": ["SiTracks"],
                    "Max_Chi2_Incr": ["1.79769e+30"],
                    "MinClustersOnTrackAfterFit": ["3"],
                    "MultipleScatteringOn": ["true"],
                    "NHitsCuts": ["1,2", "4", "3,4", "3"],
                    "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
                    "OutputTrackCollectionName": ["SiTracks_Refitted"],
                    "ReducedChi2Cut": ["-1"],
                    "ReferencePoint": ["-1"],
                    "SmoothOn": ["false"],
                    "extrapolateForward": ["true"]
                    }
algList.append(Refit)

MyFilterTracks = MarlinProcessorWrapper("MyFilterTracks")
MyFilterTracks.OutputLevel = INFO
MyFilterTracks.ProcessorType = "FilterTracks"
MyFilterTracks.Parameters = {
                            "BarrelOnly": ["false"],
                            "Chi2Spatial": ["0.0"],
                            "InputTrackCollectionName": ["SiTracks"],
                            "MinPt": ["1.0"],
                            "NHitsInner": ["3"],
                            "NHitsOuter": ["0"],
                            "NHitsTotal": ["7"],
                            "NHitsVertex": ["4"],
                            "OutputTrackCollectionName": ["FilteredTracks"]
                            }
algList.append(MyFilterTracks)

# In[ ]:


MyDDCaloDigi = MarlinProcessorWrapper("MyDDCaloDigi")
MyDDCaloDigi.OutputLevel = INFO
MyDDCaloDigi.ProcessorType = "DDCaloDigi"
MyDDCaloDigi.Parameters = {
                           "CalibECALMIP": ["0.0001"],
                           "CalibHCALMIP": ["0.0001"],
                           "CalibrECAL": ["35.8411424188", "35.8411424188"],
                           "CalibrHCALBarrel": ["49.2031079063"],
                           "CalibrHCALEndcap": ["53.6263377733"],
                           "CalibrHCALOther": ["62.2125698179"],
                           "ECALBarrelTimeWindowMax": ["10"],
                           "ECALCollections": ["ECalBarrelCollection", "ECalEndcapCollection", "ECalPlugCollection"],
                           "ECALCorrectTimesForPropagation": ["1"],
                           "ECALDeltaTimeHitResolution": ["10"],
                           "ECALEndcapCorrectionFactor": ["1.0672142727"],
                           "ECALEndcapTimeWindowMax": ["10"],
                           "ECALGapCorrection": ["1"],
                           "ECALGapCorrectionFactor": ["1"],
                           "ECALLayers": ["41", "100"],
                           "ECALModuleGapCorrectionFactor": ["0.0"],
                           "ECALOutputCollection0": ["ECALBarrel"],
                           "ECALOutputCollection1": ["ECALEndcap"],
                           "ECALOutputCollection2": ["ECALOther"],
                           "ECALSimpleTimingCut": ["true"],
                           "ECALThreshold": ["0.002"],
                           "ECALThresholdUnit": ["GeV"],
                           "ECALTimeResolution": ["10"],
                           "ECALTimeWindowMin": ["-1"],
                           "ECAL_PPD_N_Pixels": ["10000"],
                           "ECAL_PPD_N_Pixels_uncertainty": ["0.05"],
                           "ECAL_PPD_PE_per_MIP": ["7"],
                           "ECAL_apply_realistic_digi": ["0"],
                           "ECAL_deadCellRate": ["0"],
                           "ECAL_deadCell_memorise": ["false"],
                           "ECAL_default_layerConfig": ["000000000000000"],
                           "ECAL_elec_noise_mips": ["0"],
                           "ECAL_maxDynamicRange_MIP": ["2500"],
                           "ECAL_miscalibration_correl": ["0"],
                           "ECAL_miscalibration_uncorrel": ["0"],
                           "ECAL_miscalibration_uncorrel_memorise": ["false"],
                           "ECAL_pixel_spread": ["0.05"],
                           "ECAL_strip_absorbtionLength": ["1e+06"],
                           "HCALBarrelTimeWindowMax": ["10"],
                           "HCALCollections": ["HCalBarrelCollection", "HCalEndcapCollection", "HCalRingCollection"],
                           "HCALCorrectTimesForPropagation": ["1"],
                           "HCALDeltaTimeHitResolution": ["10"],
                           "HCALEndcapCorrectionFactor": ["1.000"],
                           "HCALEndcapTimeWindowMax": ["10"],
                           "HCALGapCorrection": ["1"],
                           "HCALLayers": ["100"],
                           "HCALModuleGapCorrectionFactor": ["0.5"],
                           "HCALOutputCollection0": ["HCALBarrel"],
                           "HCALOutputCollection1": ["HCALEndcap"],
                           "HCALOutputCollection2": ["HCALOther"],
                           "HCALSimpleTimingCut": ["true"],
                           "HCALThreshold": ["0.002"],
                           "HCALThresholdUnit": ["GeV"],
                           "HCALTimeResolution": ["10"],
                           "HCALTimeWindowMin": ["-1"],
                           "HCAL_PPD_N_Pixels": ["400"],
                           "HCAL_PPD_N_Pixels_uncertainty": ["0.05"],
                           "HCAL_PPD_PE_per_MIP": ["10"],
                           "HCAL_apply_realistic_digi": ["0"],
                           "HCAL_deadCellRate": ["0"],
                           "HCAL_deadCell_memorise": ["false"],
                           "HCAL_elec_noise_mips": ["0"],
                           "HCAL_maxDynamicRange_MIP": ["200"],
                           "HCAL_miscalibration_correl": ["0"],
                           "HCAL_miscalibration_uncorrel": ["0"],
                           "HCAL_miscalibration_uncorrel_memorise": ["false"],
                           "HCAL_pixel_spread": ["0"],
                           "Histograms": ["0"],
                           "IfDigitalEcal": ["0"],
                           "IfDigitalHcal": ["0"],
                           "MapsEcalCorrection": ["0"],
                           "RelationOutputCollection": ["RelationCaloHit"],
                           "RootFile": ["Digi_SiW.root"],
                           "StripEcal_default_nVirtualCells": ["9"],
                           "UseEcalTiming": ["1"],
                           "UseHcalTiming": ["1"],
                           "energyPerEHpair": ["3.6"]
                           }
algList.append(MyDDCaloDigi)


# In[ ]:


MyDDSimpleMuonDigi = MarlinProcessorWrapper("MyDDSimpleMuonDigi")
MyDDSimpleMuonDigi.OutputLevel = INFO
MyDDSimpleMuonDigi.ProcessorType = "DDSimpleMuonDigi"
MyDDSimpleMuonDigi.Parameters = {
                                 "CalibrMUON": ["70.1"],
                                 "MUONCollections": ["YokeBarrelCollection", "YokeEndcapCollection"],
                                 "MUONOutputCollection": ["MUON"],
                                 "MaxHitEnergyMUON": ["2.0"],
                                 "MuonThreshold": ["1e-06"],
                                 "RelationOutputCollection": ["RelationMuonHit"]
                                 }
algList.append(MyDDSimpleMuonDigi)


# In[ ]:


MyDDMarlinPandora = MarlinProcessorWrapper("MyDDMarlinPandora")
MyDDMarlinPandora.OutputLevel = INFO
MyDDMarlinPandora.ProcessorType = "DDPandoraPFANewProcessor"
MyDDMarlinPandora.Parameters = {
                                "ClusterCollectionName": ["PandoraClusters"],
                                "CreateGaps": ["false"],
                                "CurvatureToMomentumFactor": ["0.00015"],
                                "D0TrackCut": ["200"],
                                "D0UnmatchedVertexTrackCut": ["5"],
                                "DigitalMuonHits": ["0"],
                                "ECalBarrelNormalVector": ["0", "0", "1"],
                                "ECalCaloHitCollections": ["ECALBarrel", "ECALEndcap", "ECALOther"],
                                "ECalMipThreshold": ["0.5"],
                                "ECalScMipThreshold": ["0"],
                                "ECalScToEMGeVCalibration": ["1"],
                                "ECalScToHadGeVCalibrationBarrel": ["1"],
                                "ECalScToHadGeVCalibrationEndCap": ["1"],
                                "ECalScToMipCalibration": ["1"],
                                "ECalSiMipThreshold": ["0"],
                                "ECalSiToEMGeVCalibration": ["1"],
                                "ECalSiToHadGeVCalibrationBarrel": ["1"],
                                "ECalSiToHadGeVCalibrationEndCap": ["1"],
                                "ECalSiToMipCalibration": ["1"],
                                "ECalToEMGeVCalibration": ["1.02373335516"],
                                "ECalToHadGeVCalibrationBarrel": ["1.24223718397"],
                                "ECalToHadGeVCalibrationEndCap": ["1.24223718397"],
                                "ECalToMipCalibration": ["181.818"],
                                "EMConstantTerm": ["0.01"],
                                "EMStochasticTerm": ["0.17"],
                                "FinalEnergyDensityBin": ["110."],
                                "HCalBarrelNormalVector": ["0", "0", "1"],
                                "HCalCaloHitCollections": ["HCALBarrel", "HCALEndcap", "HCALOther"],
                                "HCalMipThreshold": ["0.3"],
                                "HCalToEMGeVCalibration": ["1.02373335516"],
                                "HCalToHadGeVCalibration": ["1.01799349172"],
                                "HCalToMipCalibration": ["40.8163"],
                                "HadConstantTerm": ["0.03"],
                                "HadStochasticTerm": ["0.6"],
                                "InputEnergyCorrectionPoints": [],
                                "KinkVertexCollections": ["KinkVertices"],
                                "LayersFromEdgeMaxRearDistance": ["250"],
                                "MCParticleCollections": ["MCParticle"],
                                "MaxBarrelTrackerInnerRDistance": ["200"],
                                "MaxClusterEnergyToApplySoftComp": ["2000."],
                                "MaxHCalHitHadronicEnergy": ["1000000"],
                                "MaxTrackHits": ["5000"],
                                "MaxTrackSigmaPOverP": ["0.15"],
                                "MinBarrelTrackerHitFractionOfExpected": ["0"],
                                "MinCleanCorrectedHitEnergy": ["0.1"],
                                "MinCleanHitEnergy": ["0.5"],
                                "MinCleanHitEnergyFraction": ["0.01"],
                                "MinFtdHitsForBarrelTrackerHitFraction": ["0"],
                                "MinFtdTrackHits": ["0"],
                                "MinMomentumForTrackHitChecks": ["0"],
                                "MinTpcHitFractionOfExpected": ["0"],
                                "MinTrackECalDistanceFromIp": ["0"],
                                "MinTrackHits": ["0"],
                                "MuonBarrelBField": ["-1.34"],
                                "MuonCaloHitCollections": ["MUON"],
                                "MuonEndCapBField": ["0.01"],
                                "MuonHitEnergy": ["0.5"],
                                "MuonToMipCalibration": ["19607.8"],
                                "NEventsToSkip": ["0"],
                                "NOuterSamplingLayers": ["3"],
                                "OutputEnergyCorrectionPoints": [],
                                "PFOCollectionName": ["PandoraPFOs"],
                                "PandoraSettingsXmlFile": ["config-files/PandoraSettings/PandoraSettingsDefault.xml"],
                                "ProngVertexCollections": ["ProngVertices"],
                                "ReachesECalBarrelTrackerOuterDistance": ["-100"],
                                "ReachesECalBarrelTrackerZMaxDistance": ["-50"],
                                "ReachesECalFtdZMaxDistance": ["1"],
                                "ReachesECalMinFtdLayer": ["0"],
                                "ReachesECalNBarrelTrackerHits": ["0"],
                                "ReachesECalNFtdHits": ["0"],
                                "RelCaloHitCollections": ["RelationCaloHit", "RelationMuonHit"],
                                "RelTrackCollections": ["SiTracks_Refitted_Relation"],
                                "ShouldFormTrackRelationships": ["1"],
                                "SoftwareCompensationEnergyDensityBins": ["0", "2.", "5.", "7.5", "9.5", "13.", "16.", "20.", "23.5", "28.", "33.", "40.", "50.", "75.", "100."],
                                "SoftwareCompensationWeights": ["1.61741", "-0.00444385", "2.29683e-05", "-0.0731236", "-0.00157099", "-7.09546e-07", "0.868443", "1.0561", "-0.0238574"],
                                "SplitVertexCollections": ["SplitVertices"],
                                "StartVertexAlgorithmName": ["PandoraPFANew"],
                                "StartVertexCollectionName": ["PandoraStartVertices"],
                                "StripSplittingOn": ["0"],
                                "TrackCollections": ["SiTracks_Refitted"],
                                "TrackCreatorName": ["DDTrackCreatorCLIC"],
                                "TrackStateTolerance": ["0"],
                                "TrackSystemName": ["DDKalTest"],
                                "UnmatchedVertexTrackMaxEnergy": ["5"],
                                "UseEcalScLayers": ["0"],
                                "UseNonVertexTracks": ["1"],
                                "UseOldTrackStateCalculation": ["0"],
                                "UseUnmatchedNonVertexTracks": ["0"],
                                "UseUnmatchedVertexTracks": ["1"],
                                "V0VertexCollections": ["V0Vertices"],
                                "YokeBarrelNormalVector": ["0", "0", "1"],
                                "Z0TrackCut": ["200"],
                                "Z0UnmatchedVertexTrackCut": ["5"],
                                "ZCutForNonVertexTracks": ["250"]
                                }
algList.append(MyDDMarlinPandora)


# In[ ]:


#MyRecoMCTruthLinker = MarlinProcessorWrapper("MyRecoMCTruthLinker")
#MyRecoMCTruthLinker.OutputLevel = INFO
#MyRecoMCTruthLinker.ProcessorType = "RecoMCTruthLinker"
#MyRecoMCTruthLinker.Parameters = {
#                                  "BremsstrahlungEnergyCut": ["1"],
#                                  "CalohitMCTruthLinkName": ["CalohitMCTruthLink"],
#                                  "ClusterCollection": ["PandoraClusters"],
#                                  "ClusterMCTruthLinkName": ["ClusterMCTruthLink"],
#                                  "FullRecoRelation": ["false"],
#                                  "InvertedNonDestructiveInteractionLogic": ["false"],
#                                  "KeepDaughtersPDG": ["22", "111", "310", "13", "211", "321", "3120"],
#                                  "MCParticleCollection": ["MCParticle"],
#                                  "MCParticlesSkimmedName": ["MCParticlesSkimmed"],
#                                  "MCTruthClusterLinkName": [],
#                                  "MCTruthRecoLinkName": [],
#                                  "MCTruthTrackLinkName": [],
#                                  "RecoMCTruthLinkName": ["RecoMCTruthLink"],
#                                  "RecoParticleCollection": ["PandoraPFOs"],
#                                  "SaveBremsstrahlungPhotons": ["false"],
#                                  "SimCaloHitCollections": ["ECalBarrelCollection", "ECalEndcapCollection", "HCalBarrelCollection", "HCalEndcapCollection", "HCalRingCollection", "YokeBarrelCollection", "YokeEndcapCollection"],
#                                  "SimCalorimeterHitRelationNames": ["RelationCaloHit", "RelationMuonHit"],
#                                  "SimTrackerHitCollections": ["VertexBarrelCollection", "VertexEndcapCollection", "InnerTrackerBarrelCollection", "InnerTrackerEndcapCollection", "OuterTrackerBarrelCollection", "OuterTrackerEndcapCollection"],
#                                  "TrackCollection": ["SiTracks_Refitted"],
#                                  "TrackMCTruthLinkName": ["SiTracksMCTruthLink"],
#                                  "TrackerHitsRelInputCollections": ["VXDTrackerHitRelations", "VXDEndcapTrackerHitRelations", "ITBarrelHitsRelations", "ITEndcapHitsRelations", "OTBarrelHitsRelations", "OTEndcapHitsRelations"],
#                                  "UseTrackerHitRelations": ["true"],
#                                  "UsingParticleGun": ["false"],
#                                  "daughtersECutMeV": ["10"]
#                                  }
#algList.append(MyRecoMCTruthLinker)


# In[ ]:


#MyTrackChecker = MarlinProcessorWrapper("MyTrackChecker")
#MyTrackChecker.OutputLevel = INFO
#MyTrackChecker.ProcessorType = "TrackChecker"
#MyTrackChecker.Parameters = {
#                             "MCParticleCollectionName": ["MCParticle"],
#                             "TrackCollectionName": ["SiTracks_Refitted"],
#                             "TrackRelationCollectionName": ["SiTracksMCTruthLink"],
#                             "TreeName": ["checktree"],
#                             "UseOnlyTree": ["true"]
#                             }
#algList.append(MyTrackChecker)


# In[ ]:


CLICPfoSelectorDefault_HE = MarlinProcessorWrapper("CLICPfoSelectorDefault_HE")
CLICPfoSelectorDefault_HE.OutputLevel = INFO
CLICPfoSelectorDefault_HE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorDefault_HE.Parameters = {
                                        "ChargedPfoLooseTimingCut": ["3"],
                                        "ChargedPfoNegativeLooseTimingCut": ["-1"],
                                        "ChargedPfoNegativeTightTimingCut": ["-0.5"],
                                        "ChargedPfoPtCut": ["0"],
                                        "ChargedPfoPtCutForLooseTiming": ["4"],
                                        "ChargedPfoTightTimingCut": ["1.5"],
                                        "CheckKaonCorrection": ["0"],
                                        "CheckProtonCorrection": ["0"],
                                        "ClusterLessPfoTrackTimeCut": ["10"],
                                        "CorrectHitTimesForTimeOfFlight": ["0"],
                                        "DisplayRejectedPfos": ["1"],
                                        "DisplaySelectedPfos": ["1"],
                                        "FarForwardCosTheta": ["0.975"],
                                        "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                        "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                        "HCalBarrelLooseTimingCut": ["20"],
                                        "HCalBarrelTightTimingCut": ["10"],
                                        "HCalEndCapTimingFactor": ["1"],
                                        "InputPfoCollection": ["PandoraPFOs"],
                                        "KeepKShorts": ["1"],
                                        "MaxMomentumForClusterLessPfos": ["2"],
                                        "MinECalHitsForTiming": ["5"],
                                        "MinHCalEndCapHitsForTiming": ["5"],
                                        "MinMomentumForClusterLessPfos": ["0.5"],
                                        "MinPtForClusterLessPfos": ["0.5"],
                                        "MinimumEnergyForNeutronTiming": ["1"],
                                        "Monitoring": ["0"],
                                        "MonitoringPfoEnergyToDisplay": ["1"],
                                        "NeutralFarForwardLooseTimingCut": ["2"],
                                        "NeutralFarForwardTightTimingCut": ["1"],
                                        "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                        "NeutralHadronLooseTimingCut": ["2.5"],
                                        "NeutralHadronPtCut": ["0"],
                                        "NeutralHadronPtCutForLooseTiming": ["8"],
                                        "NeutralHadronTightTimingCut": ["1.5"],
                                        "PhotonFarForwardLooseTimingCut": ["2"],
                                        "PhotonFarForwardTightTimingCut": ["1"],
                                        "PhotonLooseTimingCut": ["2"],
                                        "PhotonPtCut": ["0"],
                                        "PhotonPtCutForLooseTiming": ["4"],
                                        "PhotonTightTimingCut": ["1"],
                                        "PtCutForTightTiming": ["0.75"],
                                        "SelectedPfoCollection": ["SelectedPandoraPFOs"],
                                        "UseClusterLessPfos": ["1"],
                                        "UseNeutronTiming": ["0"]
                                        }
algList.append(CLICPfoSelectorDefault_HE)


# In[ ]:


CLICPfoSelectorLoose_HE = MarlinProcessorWrapper("CLICPfoSelectorLoose_HE")
CLICPfoSelectorLoose_HE.OutputLevel = INFO
CLICPfoSelectorLoose_HE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorLoose_HE.Parameters = {
                                      "ChargedPfoLooseTimingCut": ["3"],
                                      "ChargedPfoNegativeLooseTimingCut": ["-2.0"],
                                      "ChargedPfoNegativeTightTimingCut": ["-2.0"],
                                      "ChargedPfoPtCut": ["0"],
                                      "ChargedPfoPtCutForLooseTiming": ["4"],
                                      "ChargedPfoTightTimingCut": ["1.5"],
                                      "CheckKaonCorrection": ["0"],
                                      "CheckProtonCorrection": ["0"],
                                      "ClusterLessPfoTrackTimeCut": ["1000."],
                                      "CorrectHitTimesForTimeOfFlight": ["0"],
                                      "DisplayRejectedPfos": ["1"],
                                      "DisplaySelectedPfos": ["1"],
                                      "FarForwardCosTheta": ["0.975"],
                                      "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                      "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                      "HCalBarrelLooseTimingCut": ["20"],
                                      "HCalBarrelTightTimingCut": ["10"],
                                      "HCalEndCapTimingFactor": ["1"],
                                      "InputPfoCollection": ["PandoraPFOs"],
                                      "KeepKShorts": ["1"],
                                      "MaxMomentumForClusterLessPfos": ["2"],
                                      "MinECalHitsForTiming": ["5"],
                                      "MinHCalEndCapHitsForTiming": ["5"],
                                      "MinMomentumForClusterLessPfos": ["0.0"],
                                      "MinPtForClusterLessPfos": ["0.25"],
                                      "MinimumEnergyForNeutronTiming": ["1"],
                                      "Monitoring": ["0"],
                                      "MonitoringPfoEnergyToDisplay": ["1"],
                                      "NeutralFarForwardLooseTimingCut": ["2.5"],
                                      "NeutralFarForwardTightTimingCut": ["1.5"],
                                      "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                      "NeutralHadronLooseTimingCut": ["2.5"],
                                      "NeutralHadronPtCut": ["0"],
                                      "NeutralHadronPtCutForLooseTiming": ["8"],
                                      "NeutralHadronTightTimingCut": ["1.5"],
                                      "PhotonFarForwardLooseTimingCut": ["2"],
                                      "PhotonFarForwardTightTimingCut": ["1"],
                                      "PhotonLooseTimingCut": ["2."],
                                      "PhotonPtCut": ["0"],
                                      "PhotonPtCutForLooseTiming": ["4"],
                                      "PhotonTightTimingCut": ["2."],
                                      "PtCutForTightTiming": ["0.75"],
                                      "SelectedPfoCollection": ["LooseSelectedPandoraPFOs"],
                                      "UseClusterLessPfos": ["1"],
                                      "UseNeutronTiming": ["0"]
                                      }
algList.append(CLICPfoSelectorLoose_HE)


# In[ ]:


CLICPfoSelectorTight_HE = MarlinProcessorWrapper("CLICPfoSelectorTight_HE")
CLICPfoSelectorTight_HE.OutputLevel = INFO
CLICPfoSelectorTight_HE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorTight_HE.Parameters = {
                                      "ChargedPfoLooseTimingCut": ["2.0"],
                                      "ChargedPfoNegativeLooseTimingCut": ["-0.5"],
                                      "ChargedPfoNegativeTightTimingCut": ["-0.25"],
                                      "ChargedPfoPtCut": ["0"],
                                      "ChargedPfoPtCutForLooseTiming": ["4"],
                                      "ChargedPfoTightTimingCut": ["1.0"],
                                      "CheckKaonCorrection": ["0"],
                                      "CheckProtonCorrection": ["0"],
                                      "ClusterLessPfoTrackTimeCut": ["10"],
                                      "CorrectHitTimesForTimeOfFlight": ["0"],
                                      "DisplayRejectedPfos": ["1"],
                                      "DisplaySelectedPfos": ["1"],
                                      "FarForwardCosTheta": ["0.95"],
                                      "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                      "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                      "HCalBarrelLooseTimingCut": ["20"],
                                      "HCalBarrelTightTimingCut": ["10"],
                                      "HCalEndCapTimingFactor": ["1"],
                                      "InputPfoCollection": ["PandoraPFOs"],
                                      "KeepKShorts": ["1"],
                                      "MaxMomentumForClusterLessPfos": ["1.5"],
                                      "MinECalHitsForTiming": ["5"],
                                      "MinHCalEndCapHitsForTiming": ["5"],
                                      "MinMomentumForClusterLessPfos": ["0.5"],
                                      "MinPtForClusterLessPfos": ["1.0"],
                                      "MinimumEnergyForNeutronTiming": ["1"],
                                      "Monitoring": ["0"],
                                      "MonitoringPfoEnergyToDisplay": ["1"],
                                      "NeutralFarForwardLooseTimingCut": ["1.5"],
                                      "NeutralFarForwardTightTimingCut": ["1"],
                                      "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                      "NeutralHadronLooseTimingCut": ["2.5"],
                                      "NeutralHadronPtCut": ["0.5"],
                                      "NeutralHadronPtCutForLooseTiming": ["8"],
                                      "NeutralHadronTightTimingCut": ["1.5"],
                                      "PhotonFarForwardLooseTimingCut": ["2"],
                                      "PhotonFarForwardTightTimingCut": ["1"],
                                      "PhotonLooseTimingCut": ["2"],
                                      "PhotonPtCut": ["0.2"],
                                      "PhotonPtCutForLooseTiming": ["4"],
                                      "PhotonTightTimingCut": ["1"],
                                      "PtCutForTightTiming": ["1.0"],
                                      "SelectedPfoCollection": ["TightSelectedPandoraPFOs"],
                                      "UseClusterLessPfos": ["0"],
                                      "UseNeutronTiming": ["0"]
                                      }
algList.append(CLICPfoSelectorTight_HE)


# In[ ]:


CLICPfoSelectorDefault_LE = MarlinProcessorWrapper("CLICPfoSelectorDefault_LE")
CLICPfoSelectorDefault_LE.OutputLevel = INFO
CLICPfoSelectorDefault_LE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorDefault_LE.Parameters = {
                                        "ChargedPfoLooseTimingCut": ["10.0"],
                                        "ChargedPfoNegativeLooseTimingCut": ["-5.0"],
                                        "ChargedPfoNegativeTightTimingCut": ["-2.0"],
                                        "ChargedPfoPtCut": ["0.0"],
                                        "ChargedPfoPtCutForLooseTiming": ["4.0"],
                                        "ChargedPfoTightTimingCut": ["3.0"],
                                        "CheckKaonCorrection": ["0"],
                                        "CheckProtonCorrection": ["0"],
                                        "ClusterLessPfoTrackTimeCut": ["10."],
                                        "CorrectHitTimesForTimeOfFlight": ["0"],
                                        "DisplayRejectedPfos": ["1"],
                                        "DisplaySelectedPfos": ["1"],
                                        "FarForwardCosTheta": ["0.975"],
                                        "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                        "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                        "HCalBarrelLooseTimingCut": ["5"],
                                        "HCalBarrelTightTimingCut": ["2.5"],
                                        "HCalEndCapTimingFactor": ["1"],
                                        "InputPfoCollection": ["PandoraPFOs"],
                                        "KeepKShorts": ["1"],
                                        "MaxMomentumForClusterLessPfos": ["5.0"],
                                        "MinECalHitsForTiming": ["5"],
                                        "MinHCalEndCapHitsForTiming": ["5"],
                                        "MinMomentumForClusterLessPfos": ["0.0"],
                                        "MinPtForClusterLessPfos": ["0.0"],
                                        "MinimumEnergyForNeutronTiming": ["1"],
                                        "Monitoring": ["0"],
                                        "MonitoringPfoEnergyToDisplay": ["1"],
                                        "NeutralFarForwardLooseTimingCut": ["4.0"],
                                        "NeutralFarForwardTightTimingCut": ["2.0"],
                                        "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                        "NeutralHadronLooseTimingCut": ["5.0"],
                                        "NeutralHadronPtCut": ["0.0"],
                                        "NeutralHadronPtCutForLooseTiming": ["2.0"],
                                        "NeutralHadronTightTimingCut": ["2.5"],
                                        "PhotonFarForwardLooseTimingCut": ["2"],
                                        "PhotonFarForwardTightTimingCut": ["1"],
                                        "PhotonLooseTimingCut": ["5.0"],
                                        "PhotonPtCut": ["0.0"],
                                        "PhotonPtCutForLooseTiming": ["2.0"],
                                        "PhotonTightTimingCut": ["1.0"],
                                        "PtCutForTightTiming": ["0.75"],
                                        "SelectedPfoCollection": ["LE_SelectedPandoraPFOs"],
                                        "UseClusterLessPfos": ["1"],
                                        "UseNeutronTiming": ["0"]
                                        }
algList.append(CLICPfoSelectorDefault_LE)


# In[ ]:


CLICPfoSelectorLoose_LE = MarlinProcessorWrapper("CLICPfoSelectorLoose_LE")
CLICPfoSelectorLoose_LE.OutputLevel = INFO
CLICPfoSelectorLoose_LE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorLoose_LE.Parameters = {
                                      "ChargedPfoLooseTimingCut": ["10.0"],
                                      "ChargedPfoNegativeLooseTimingCut": ["-20.0"],
                                      "ChargedPfoNegativeTightTimingCut": ["-20.0"],
                                      "ChargedPfoPtCut": ["0.0"],
                                      "ChargedPfoPtCutForLooseTiming": ["4.0"],
                                      "ChargedPfoTightTimingCut": ["5.0"],
                                      "CheckKaonCorrection": ["0"],
                                      "CheckProtonCorrection": ["0"],
                                      "ClusterLessPfoTrackTimeCut": ["50."],
                                      "CorrectHitTimesForTimeOfFlight": ["0"],
                                      "DisplayRejectedPfos": ["1"],
                                      "DisplaySelectedPfos": ["1"],
                                      "FarForwardCosTheta": ["0.975"],
                                      "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                      "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                      "HCalBarrelLooseTimingCut": ["10"],
                                      "HCalBarrelTightTimingCut": ["5"],
                                      "HCalEndCapTimingFactor": ["1"],
                                      "InputPfoCollection": ["PandoraPFOs"],
                                      "KeepKShorts": ["1"],
                                      "MaxMomentumForClusterLessPfos": ["5.0"],
                                      "MinECalHitsForTiming": ["5"],
                                      "MinHCalEndCapHitsForTiming": ["5"],
                                      "MinMomentumForClusterLessPfos": ["0.0"],
                                      "MinPtForClusterLessPfos": ["0.0"],
                                      "MinimumEnergyForNeutronTiming": ["1"],
                                      "Monitoring": ["0"],
                                      "MonitoringPfoEnergyToDisplay": ["1"],
                                      "NeutralFarForwardLooseTimingCut": ["10.0"],
                                      "NeutralFarForwardTightTimingCut": ["5.0"],
                                      "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                      "NeutralHadronLooseTimingCut": ["10.0"],
                                      "NeutralHadronPtCut": ["0.0"],
                                      "NeutralHadronPtCutForLooseTiming": ["2.0"],
                                      "NeutralHadronTightTimingCut": ["5.0"],
                                      "PhotonFarForwardLooseTimingCut": ["2"],
                                      "PhotonFarForwardTightTimingCut": ["1"],
                                      "PhotonLooseTimingCut": ["10.0"],
                                      "PhotonPtCut": ["0.0"],
                                      "PhotonPtCutForLooseTiming": ["2.0"],
                                      "PhotonTightTimingCut": ["2.5"],
                                      "PtCutForTightTiming": ["0.75"],
                                      "SelectedPfoCollection": ["LE_LooseSelectedPandoraPFOs"],
                                      "UseClusterLessPfos": ["1"],
                                      "UseNeutronTiming": ["0"]
                                      }
algList.append(CLICPfoSelectorLoose_LE)


# In[ ]:


CLICPfoSelectorTight_LE = MarlinProcessorWrapper("CLICPfoSelectorTight_LE")
CLICPfoSelectorTight_LE.OutputLevel = INFO
CLICPfoSelectorTight_LE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorTight_LE.Parameters = {
                                      "ChargedPfoLooseTimingCut": ["4.0"],
                                      "ChargedPfoNegativeLooseTimingCut": ["-2.0"],
                                      "ChargedPfoNegativeTightTimingCut": ["-1.0"],
                                      "ChargedPfoPtCut": ["0.0"],
                                      "ChargedPfoPtCutForLooseTiming": ["3.0"],
                                      "ChargedPfoTightTimingCut": ["2.0"],
                                      "CheckKaonCorrection": ["0"],
                                      "CheckProtonCorrection": ["0"],
                                      "ClusterLessPfoTrackTimeCut": ["10."],
                                      "CorrectHitTimesForTimeOfFlight": ["0"],
                                      "DisplayRejectedPfos": ["1"],
                                      "DisplaySelectedPfos": ["1"],
                                      "FarForwardCosTheta": ["0.975"],
                                      "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                      "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                      "HCalBarrelLooseTimingCut": ["4"],
                                      "HCalBarrelTightTimingCut": ["2"],
                                      "HCalEndCapTimingFactor": ["1"],
                                      "InputPfoCollection": ["PandoraPFOs"],
                                      "KeepKShorts": ["1"],
                                      "MaxMomentumForClusterLessPfos": ["5.0"],
                                      "MinECalHitsForTiming": ["5"],
                                      "MinHCalEndCapHitsForTiming": ["5"],
                                      "MinMomentumForClusterLessPfos": ["0.0"],
                                      "MinPtForClusterLessPfos": ["0.75"],
                                      "MinimumEnergyForNeutronTiming": ["1"],
                                      "Monitoring": ["0"],
                                      "MonitoringPfoEnergyToDisplay": ["1"],
                                      "NeutralFarForwardLooseTimingCut": ["2.0"],
                                      "NeutralFarForwardTightTimingCut": ["2.0"],
                                      "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                      "NeutralHadronLooseTimingCut": ["4.0"],
                                      "NeutralHadronPtCut": ["0.0"],
                                      "NeutralHadronPtCutForLooseTiming": ["3.0"],
                                      "NeutralHadronTightTimingCut": ["2.0"],
                                      "PhotonFarForwardLooseTimingCut": ["2"],
                                      "PhotonFarForwardTightTimingCut": ["1"],
                                      "PhotonLooseTimingCut": ["1.0"],
                                      "PhotonPtCut": ["0.0"],
                                      "PhotonPtCutForLooseTiming": ["2.0"],
                                      "PhotonTightTimingCut": ["1.0"],
                                      "PtCutForTightTiming": ["0.75"],
                                      "SelectedPfoCollection": ["LE_TightSelectedPandoraPFOs"],
                                      "UseClusterLessPfos": ["1"],
                                      "UseNeutronTiming": ["0"]
                                      }
algList.append(CLICPfoSelectorTight_LE)


# In[ ]:


MyFastJetProcessor = MarlinProcessorWrapper("MyFastJetProcessor")
MyFastJetProcessor.OutputLevel = INFO
MyFastJetProcessor.ProcessorType = "FastJetProcessor"
MyFastJetProcessor.Parameters = {
                                 "algorithm": ["kt_algorithm", "0.5"],
                                 "clusteringMode": ["Inclusive", "5"],
                                 "jetOut": ["JetCaloOut"],
                                 "recParticleIn": ["SelectedPandoraPFOs"],
                                 "recombinationScheme": ["E_scheme"]
                                 }
algList.append(MyFastJetProcessor)


# In[ ]:


MyLCTuple = MarlinProcessorWrapper("MyLCTuple")
MyLCTuple.OutputLevel = INFO
MyLCTuple.ProcessorType = "LCTuple"
MyLCTuple.Parameters = {
                        "CalorimeterHitCollection": [],
                        "ClusterCollection": ["PandoraClusters"],
                        "FullSubsetCollections": [],
                        "IsoLepCollection": [],
                        "JetCollection": ["JetCaloOut"],
                        "JetCollectionDaughtersParameters": ["true"],
                        "JetCollectionExtraParameters": ["false"],
                        "JetCollectionTaggingParameters": ["false"],
                        "LCRelationCollections": [],
                        "LCRelationPrefixes": [],
                        "LCRelationwithPFOCollections": [],
                        "MCParticleCollection": ["MCPhysicsParticles"],
                        "MCParticleNotReco": [],
                        "RecoParticleCollection": ["PandoraPFOs"],
                        "SimCalorimeterHitCollection": [],
                        "SimTrackerHitCollection": [],
                        "TrackCollection": ["SiTracks_Refitted"],
                        "TrackerHitCollection": [],
                        "VertexCollection": [],
                        "WriteCalorimeterHitCollectionParameters": ["false"],
                        "WriteClusterCollectionParameters": ["false"],
                        "WriteIsoLepCollectionParameters": ["false"],
                        "WriteJetCollectionParameters": ["true"],
                        "WriteMCParticleCollectionParameters": ["false"],
                        "WriteRecoParticleCollectionParameters": ["false"],
                        "WriteSimCalorimeterHitCollectionParameters": ["false"],
                        "WriteSimTrackerHitCollectionParameters": ["false"],
                        "WriteTrackCollectionParameters": ["false"],
                        "WriteTrackerHitCollectionParameters": ["false"],
                        "WriteVertexCollectionParameters": ["false"]
                        }
algList.append(MyLCTuple)


# In[ ]:


Output_REC = MarlinProcessorWrapper("Output_REC")
Output_REC.OutputLevel = INFO
Output_REC.ProcessorType = "LCIOOutputProcessor"
Output_REC.Parameters = {
                         "DropCollectionNames": ["SeedTracks"],
                         "DropCollectionTypes": [],
                         "FullSubsetCollections": ["EfficientMCParticles", "InefficientMCParticles"],
                         "KeepCollectionNames": [],
                         "LCIOOutputFile": ["Output_ACTS_REC.slcio"],
                         "LCIOWriteMode": ["WRITE_NEW"]
                         }
algList.append(Output_REC)


# In[ ]:


ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=INFO
              )

gmain = gaudimain()
gmain.run(False)

