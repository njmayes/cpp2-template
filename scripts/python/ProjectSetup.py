import sys
import os
import platform
from unicodedata import name
from pathlib import Path

def ReplaceNamespace(root, namespace):
    solutionFilepath = os.path.join(root, "premake5.lua")
    
    with open(solutionFilepath, 'r') as premakeRoot:
        filedata = premakeRoot.read()
        
    filedata = filedata.replace('cpp2-template', namespace)
    
    with open(solutionFilepath, 'w') as premakeRoot:
        premakeRoot.write(filedata)

def ReplaceProjectName(root, projectName):
    solutionFilepath = os.path.join(root, "premake5.lua")
    projectFilepath = os.path.join(root, projectName, "premake5.lua")
    
    with open(solutionFilepath, 'r') as premakeRoot:
        filedata = premakeRoot.read()
        
    filedata = filedata.replace('TemplateProject', projectName)
    
    with open(solutionFilepath, 'w') as premakeRoot:
        premakeRoot.write(filedata)
        
        
    with open(projectFilepath, 'r') as premakeProj:
        filedata = premakeProj.read()
        
    filedata = filedata.replace('TemplateProject', projectName)
    
    with open(projectFilepath, 'w') as premakeProj:
        premakeProj.write(filedata)
        
def ReplaceProjectType(root, projectType):
    match projectType:
        case 'l':
            winProjType = 'StaticLib'
            linuxProjType = 'SharedLib'
        case 'e':
            winProjType = 'ConsoleApp'
            linuxProjType = 'ConsoleApp'
        case _:
            return

    projectFilepath = os.path.join(root, 'TemplateProject/premake5.lua')
    with open(projectFilepath, 'r') as premakeProj:
        projectFiledata = premakeProj.readlines()
        
    newProjectFiledata = [line.replace('ProjectTypeLinux', linuxProjType).replace('ProjectTypeWin', winProjType) for line in projectFiledata]
    
    with open(projectFilepath, 'w') as premakeProj:
        premakeProj.writelines(newProjectFiledata)
        
    
    if projectType == 'l':
        solutionFilepath = os.path.join(root, 'premake5.lua')
        with open(solutionFilepath, 'r') as premakeSol:
            solutionFiledata = premakeSol.readlines()

        solutionFiledata.pop(1)

        with open(solutionFilepath, 'w') as premakeSol:
            premakeSol.writelines(solutionFiledata)
    
class ProjectConfiguration:

    workingRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    @classmethod
    def CheckProjectConfig(cls):
        return not os.path.isdir(os.path.join(cls.workingRoot, 'TemplateProject'))

    @classmethod
    def SetupNamespace(cls, namespace):
        ReplaceNamespace(cls.workingRoot, namespace)
        
    @classmethod
    def SetupProject(cls, projectName):
        projectTypeSetup = False
        projectType = ''
        while not projectTypeSetup:
            reply = str(input("Please choose binary type of project, executable or library? [E/L]: ")).lower().strip()[:1]
            projectTypeSetup = (reply == 'e' or reply == 'l')
            projectType = reply
            
        ReplaceProjectType(cls.workingRoot, projectType)
        
        os.rename(os.path.join(cls.workingRoot, "TemplateProject"), os.path.join(cls.workingRoot, projectName))
        
        ReplaceProjectName(cls.workingRoot, projectName)