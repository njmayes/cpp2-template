project "TemplateProject"
    language "C++"
    cppdialect "C++latest"
		
    targetdir 	("%{wks.location}/bin/%{prj.name}/" .. outputDir)
    objdir 		("%{wks.location}/obj/%{prj.name}/" .. outputDir)

    files 
    { 
        "src/**.h2",
        "src/**.cpp2",
    }
	
	defines
	{
		"_CRT_SECURE_NO_WARNINGS"
	}

    includedirs
    {
        "%{IncludeDir.cppfront}",
        "%{IncludeDir.TemplateProject}",
    }

	links
	{
	}

    buildstlmodules "On"
	
    filter "system:windows"
        kind "ProjectTypeWin"
        staticruntime "off"
        systemversion "latest"
		
	filter "system:linux"
        kind "ProjectTypeLinux"
        staticruntime "off"
        pic "On"
        systemversion "latest"

    filter "configurations:Debug"
		runtime "Debug"
        symbols "on"
    filter "configurations:Release"
		runtime "Release"
        optimize "on"
		
	filter "files:**.h2"
        buildmessage 'Compiling %{file.relpath}'
		
		buildcommands {
			'%{cppfrontBinary} "%{file.abspath}" -p -cwd "%{prj.location}src_cpp2"'
		}
		
		buildoutputs { "%{file.reldirectory}/../src_cpp2/%{file.basename}.h" }
		
		compilebuildoutputs 'on'
		
	filter "files:**.cpp2"
        buildmessage 'Compiling %[%{file.relpath}]'
		
		buildcommands {
			'%{cppfrontBinary} "%{file.abspath}" -p -cwd "%{prj.location}src_cpp2"'
		}
		
		buildoutputs { "%{file.reldirectory}/../src_cpp2/%{file.basename}.cpp" }
		
		compilebuildoutputs 'on'