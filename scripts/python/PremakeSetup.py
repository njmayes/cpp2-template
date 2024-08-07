import sys
import os
import platform
import requests
import shutil
import subprocess
from pathlib import Path
    
class PremakeConfiguration:

    workingDir = os.getcwd()
    premakeCoreRoot = f"{workingDir}/../dependencies/premake-core"

    if platform.system() == "Windows":
        premakeBootstrap = os.path.abspath(f"{premakeCoreRoot}/Bootstrap.bat")
        premakeExtension = ".exe"
    elif platform.system() == "Linux":
        premakeBootstrap = f"make -C {os.path.abspath(premakeCoreRoot)} -f Bootstrap.mak"
        premakeExtension = ""
    else:
        premakeSuffix = ""
        premakeExtension = ""
        
    premakeSrcDirectory  = f"{premakeCoreRoot}/bin/release"
    premakeSrcBinary  = f"{premakeSrcDirectory}/premake5{premakeExtension}"
    
    premakeDestDirectory = f"{workingDir}/../dependencies/premake/bin"
    premakeDestBinary = f"{premakeDestDirectory}/premake5{premakeExtension}"

    @classmethod
    def Validate(cls):
        if (not cls.CheckIfPremakeInstalled()):
            print("Premake is not built.")
            return False

        print(f"Correct Premake located at {os.path.abspath(cls.premakeDestDirectory)}")
        return True

    @classmethod
    def CheckIfPremakeInstalled(cls):
        

        premakeBinary = Path(cls.premakeSrcBinary);
        built = premakeBinary.exists()
        if ( not built ):
            built = cls.BuildPremake()

        if ( not built ): 
            return False

        premakeBinary = Path(cls.premakeDestBinary);
        if (not premakeBinary.exists()):
            return cls.CopyPremake()

        return True

    @classmethod
    def BuildPremake(cls):
        permissionGranted = False
        while not permissionGranted:
            reply = str(input("Premake not found. Would you like to build Premake? [Y/N]: ")).lower().strip()[:1]
            if reply == 'n':
                return False
            permissionGranted = (reply == 'y')

        print( "Building premake binary from source..." )
        os.chdir( cls.premakeCoreRoot ) # Change working dir to repo root
        subprocess.call( [ cls.premakeBootstrap ] )
        shutil.copy2( cls.premakeSrcBinary, cls.premakeDestBinary )

        return True

    @classmethod
    def CopyPremake(cls):
        print( "Copying premake binary to target directory..." )
        os.makedirs(os.path.abspath(cls.premakeDestDirectory), exist_ok=True)
        shutil.copy2( os.path.abspath(cls.premakeSrcBinary), os.path.abspath(cls.premakeDestDirectory) )

        return True