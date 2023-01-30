###########################################
#
# MuonCollider versioning file for release V02-08-MC
# The external base tools need to be installed
#
# MuonC Software team
###########################################
import datetime
import platform

# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='muonc'
# ----------------------------------------------------------------------------

# which cxx standard to use
cxx_standard = 17

afsPath = None

# --------- install dir ------------------------------------------------------
# ===========================================================
# Modify this path to where you want to install the software
# ===========================================================
#
if installPrefix is None:
    ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
else:
    ilcsoft_install_prefix = installPrefix

# --------- ilcsoft home -----------------------------------------------------
# ===========================================================
# Modify this path to where you want ilcinstall to look
# for pre-installed (base) packages
# typically this would be left to ilcsoft_install_prefix
# or set to an /afs or /cvmfs base installation that you
# want to use
# ===========================================================

ilcPath = ilcsoft_install_prefix

# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# detect the default software installation path
# when using package manager like apt-get, yum or brew
platfDefault = None

if platform.system().lower().find('linux') >= 0:
   platfDefault = '/usr'
elif platform.system().lower().find('darwin') >= 0:
   platfDefault = '/usr/local'

# ----- mysql --------------------------------------------------------
MySQL_version = "8.0.30"
MySQL_path = platfDefault

# overwrite with a patch set in the environment
my_mysql_path = os.getenv("MYSQL_DIR", default=None)
if( my_mysql_path !=  None ):
    MySQL_path = my_mysql_path

##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################


# ======================= PACKAGE VERSIONS ===================================

## System software

Geant4_version = "10.6.3-1"

CLHEP_version =  "2.4.1.3"

ROOT_version = "6.26.10-1"

GSL_version = "2.6.7"

Qt5_version = "v5.15.3-1"

CMake_version = "3.20.2.7"

Boost_version = "1.75.0-8"

Eigen_version = "3.4.0-1"

XercesC_version = "v3.2.3-5"
# xerces-c (needed by geant4 for building gdml support - required by mokka)
#XERCESC_ROOT_DIR = ilcPath + "/xercesc/" + XercesC_version

## Compiled software
CMake_version = "3.15.5"

FastJet_version = "3.4.0"
FastJetcontrib_version = "1.050"

CED_version = "v01-09-04"

SIO_version = "v00-01"

ILCUTIL_version = "v01-07"

# -------------------------------------------
# Marlin framework

Marlin_version = "v01-19"

MarlinReco_version = "v01-33-01"

MarlinUtil_version = "v01-17"

DetectorSimulation_version = "v01-03-MC"

# ---

DD4hep_version = "v01-23"
DD4hepExamples_version = "v01-23"
MarlinDD4hep_version = "v00-06-02"

PandoraAnalysis_version = "v02-00-01"
PandoraPFANew_version   = "v04-02-00"
DDMarlinPandora_version = "HEAD"

LCFIVertex_version = "v00-08"
LCFIPlus_version = "v00-10-01"

# ---

MarlinTrk_version = "v02-09-01"

#MarlinTrkProcessors_version = "v02-03-MC"
MarlinTrkProcessors_version = "HEAD"

ForwardTracking_version = "v01-14-MC"

ConformalTracking_version = "v01-12-MC"

ACTS_version = "v13.0.0"
ACTSTracking_version = "v1.1.0"

KiTrack_version = "v01-10"
KiTrackMarlin_version = "v01-13-02"

DDKalTest_version = "v01-07"
KalTest_version = "v02-05-01"
KalDet_version = "v01-14-01"

MarlinKinfit_version = "v00-06-01"
MarlinKinfitProcessors_version = "v00-05"

# ---

MarlinFastJet_version = "v00-05-03"

LCTuple_version = "v01-14-MC"

ClicPerformance_version = "v02-04-01"

MuonCVXDDigitiser_version = "HEAD"

# ---

CEDViewer_version = "v01-19-01"

Overlay_version = "HEAD"

lcgeo_version = "HEAD"

#LCIO_version = "v02-16-01-MC"
LCIO_version = "HEAD"

GEAR_version = "v01-09-01"

Garlic_version = "v03-01"

aidaTT_version = "v00-10"

RAIDA_version = "v01-09"

GBL_version = "V02-02-01" 

# ------------------------------------------------


