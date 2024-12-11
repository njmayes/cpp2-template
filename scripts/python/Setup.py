import sys
import os
import subprocess
import platform

from PremakeSetup import PremakeConfiguration as PremakeRequirements
from ProjectSetup import ProjectConfiguration as ProjectConfig

workingRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
print(workingRoot)

projectConfigured = ProjectConfig.CheckProjectConfig()
premakeInstalled = PremakeRequirements.Validate()

print("\n---------------------------------------------------------------------------------")

print(os.getcwd())

if (not projectConfigured):
    namespace = str(input("Enter the top level name for the repo...\n")).strip()
    ProjectConfig.SetupNamespace(namespace)

if (not projectConfigured):
    projectName = str(input("Enter the name for the template project...\n")).strip()
    ProjectConfig.SetupProject(projectName)

if (premakeInstalled):
    print("\nRunning premake...")
    genPath = os.path.join(workingRoot, "scripts", "gen-projects")
    
    if platform.system() == "Windows":
        genFile = "msvc.bat"
    elif platform.system() == "Linux":
        genFile = "gcc.sh"
        
    subprocess.run(os.path.join(genPath, genFile))

    print("\nSetup completed!")
else:
    print("Labyrinth requires Premake to generate project files.")