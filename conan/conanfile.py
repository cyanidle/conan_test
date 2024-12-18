import os, shutil
from conan import ConanFile
from conan.tools.files import save, load, copy
from conan.tools.cmake import cmake_layout, CMake

class Damn(ConanFile):
    name = "damn"
    version = "1.0"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain", "CMakeDeps"

    def export_sources(self):
        # The path of the CMakeLists.txt and sources we want to export are one level above
        folder = os.path.join(self.recipe_folder, "..")
        copy(self, "CMakeLists.txt", folder, self.export_sources_folder)
        copy(self, "src/*.cpp", folder, self.export_sources_folder)
        copy(self, "include/*.hpp", folder, self.export_sources_folder)

    def requirements(self):
        self.requires("fmt/11.0.2")
        self.requires("libdatachannel/0.22.2")

    def layout(self):
        self.folders.root = ".." 
        cmake_layout(self, "Ninja")
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()