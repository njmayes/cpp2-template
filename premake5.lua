workspace "cpp2-template"

    configurations 
    { 
        "Debug",
        "Release"
    }
    
    platforms
    {
        "x64",
        "ARM32",
        "ARM64"
    }

	filter "platforms:x64"
		architecture "x86_64"

	filter "platforms:ARM32"
		architecture "ARM"

 	filter "configurations:ARM64"
		architecture "ARM64"
		
	
cppfrontBinary = "%{wks.location}bin/cppfront/cppfront"

outputDir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

IncludeDir = {}
IncludeDir["cppfront"] 	= "%{wks.location}/dependencies/cppfront/include"
IncludeDir["TemplateProject"] 	= "%{wks.location}/TemplateProject/src"

group "cppfront"

include "dependencies/cppfront"

group ""

include "TemplateProject"