# -*- coding: utf-8 -*-

from ctypes.util import find_library
from ctypes import CDLL
from ctypes import CFUNCTYPE
from functools import partial

from os import path
from os import pathsep
from os import environ
from sys import maxsize

from ctypes import Structure
from ctypes import POINTER
from ctypes import c_void_p
from ctypes import c_float
from ctypes import c_double
from ctypes import c_char
from ctypes import c_uint32
from ctypes import c_int32

def __GetOdeLib():
    odeLibName = find_library('ode')
    if odeLibName is not None:
        odeLib = CDLL(odeLibName, use_errno=True)
    else:
        ldLibraryPath = environ.get('LD_LIBRARY_PATH')
        if ldLibraryPath is None:
            ldLibraryPath = []
        else:
            ldLibraryPath = ldLibraryPath.split(pathsep)
        localOdeInstallLibDir = path.join(environ.get('HOME'), '.pyode', 'lib')
        ldLibraryPath.append(localOdeInstallLibDir)
        environ['LD_LIBRARY_PATH'] = pathsep.join(ldLibraryPath)
        odeLib = CDLL(path.join(localOdeInstallLibDir, find_library('ode')), use_errno=True)
    return odeLib

def __load(lib, name, restype, *args):
    return (CFUNCTYPE(restype, *args))((name, lib))

loadOde = partial(__load, __GetOdeLib())

if maxsize > 2**32:
    dReal = c_double
else:
    dReal = c_float

dTriIndex = c_uint32

dDA__A_MAX = 6
dDA__A_MIN = 3
dDA_AX = 3
dDA_AY = 4
dDA_AZ = 5
dDA__L_MAX = 3
dDA__L_MIN = 0
dDA_LX = 0
dDA_LY = 1
dDA_LZ = 2
dDA__MAX = 6
dDA__MIN = 0
dM3E__MAX = 12
dM3E__MIN = 0
dM3E__X_AXES_MAX = 3
dM3E__X_AXES_MIN = 0
dM3E__X_MAX = 4
dM3E__X_MIN = 0
dM3E_XPAD = 3
dM3E_XX = 0
dM3E_XY = 1
dM3E_XZ = 2
dM3E__Y_AXES_MAX = 7
dM3E__Y_AXES_MIN = 4
dM3E__Y_MAX = 8
dM3E__Y_MIN = 4
dM3E_YPAD = 7
dM3E_YX = 4
dM3E_YY = 5
dM3E_YZ = 6
dM3E__Z_AXES_MAX = 11
dM3E__Z_AXES_MIN = 8
dM3E__Z_MAX = 12
dM3E__Z_MIN = 8
dM3E_ZPAD = 11
dM3E_ZX = 8
dM3E_ZY = 9
dM3E_ZZ = 10
dM4E__MAX = 16
dM4E__MIN = 0
dM4E__O_MAX = 16
dM4E__O_MIN = 12
dM4E_OO = 15
dM4E_OX = 12
dM4E_OY = 13
dM4E_OZ = 14
dM4E__X_MAX = 4
dM4E__X_MIN = 0
dM4E_XO = 3
dM4E_XX = 0
dM4E_XY = 1
dM4E_XZ = 2
dM4E__Y_MAX = 8
dM4E__Y_MIN = 4
dM4E_YO = 7
dM4E_YX = 4
dM4E_YY = 5
dM4E_YZ = 6
dM4E__Z_MAX = 12
dM4E__Z_MIN = 8
dM4E_ZO = 11
dM4E_ZX = 8
dM4E_ZY = 9
dM4E_ZZ = 10
dMD_ANGULAR = 1
dMD_LINEAR = 0
dMD__MAX = 2
dMD__MIN = 0
dQUE__AXIS_MAX = 4
dQUE__AXIS_MIN = 1
dQUE_I = 1
dQUE_J = 2
dQUE_K = 3
dQUE__MAX = 4
dQUE__MIN = 0
dQUE_R = 0
dSA__MAX = 3
dSA__MIN = 0
dSA_X = 0
dSA_Y = 1
dSA_Z = 2
dV3E__AXES_COUNT = 3
dV3E__AXES_MAX = 3
dV3E__AXES_MIN = 0
dV3E__MAX = 4
dV3E__MIN = 0
dV3E_PAD = 3
dV3E_X = 0
dV3E_Y = 1
dV3E_Z = 2
dV4E__MAX = 4
dV4E__MIN = 0
dV4E_O = 3
dV4E_X = 0
dV4E_Y = 1
dV4E_Z = 2

dVector3 = dReal * dV3E__MAX;
dVector4 = dReal * dV4E__MAX;
dMatrix3 = dReal * dM3E__MAX;
dMatrix4 = dReal * dM4E__MAX;
dMatrix6 = dReal * (dMD__MAX * dV3E__MAX) * (dMD__MAX * dSA__MAX);
dQuaternion = dReal * dQUE__MAX;

class dxWorld(Structure):
    pass

class dxSpace(Structure):
    pass

class dxBody(Structure):
    pass

class dxGeom(Structure):
    pass

class dxJoint(Structure):
    pass

class dxJointGroup(Structure):
    pass

dWorldID = POINTER(dxWorld)
dSpaceID = POINTER(dxSpace)
dBodyID = POINTER(dxBody)
dGeomID = POINTER(dxGeom)
dJointID = POINTER(dxJoint)
dJointGroupID = POINTER(dxJointGroup)

d_ERR_UNKNOWN = 0  
d_ERR_IASSERT = 1  
d_ERR_UASSERT = 2  
d_ERR_LCP = 3  
dJointTypeNone = 0  
dJointTypeBall = 1  
dJointTypeHinge = 2  
dJointTypeSlider = 3  
dJointTypeContact = 4  
dJointTypeUniversal = 5  
dJointTypeHinge2 = 6  
dJointTypeFixed = 7  
dJointTypeNull = 8  
dJointTypeAMotor = 9  
dJointTypeLMotor = 10 
dJointTypePlane2D = 11 
dJointTypePR = 12 
dJointTypePU = 13 
dJointTypePiston = 14 
dJointTypeDBall = 15 
dJointTypeDHinge = 16 
dJointTypeTransmission = 17 
dAMotorUser = 0  
dAMotorEuler = 1  
dTransmissionParallelAxes = 0  
dTransmissionIntersectingAxes = 1  
dTransmissionChainDrive = 2  

class dJointFeedback(Structure):
    _fields_ = [('f1', dVector3),
                ('t1', dVector3),
                ('f2', dVector3),
                ('t2', dVector3)]
    def _init_(self, f1, t1, f2, t2):
        self.f1 = f1
        self.t1 = t1
        self.f2 = f2
        self.t2 = t2

dGeomMoved = loadOde('dGeomMoved', c_void_p, dGeomID)
dGeomGetBodyNext = loadOde('dGeomGetBodyNext', dGeomID, dGeomID)
dGetConfiguration = loadOde('dGetConfiguration', POINTER(c_char))
dCheckConfiguration = loadOde('dCheckConfiguration', c_int32, POINTER(c_char))
