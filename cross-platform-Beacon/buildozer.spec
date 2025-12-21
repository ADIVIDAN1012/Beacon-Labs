[app]

# (str) Title of your application
title = Beacon Code Engine

# (str) Package name
package.name = beacon_engine

# (str) Package domain (needed for android/ios packaging)
# (str) Package domain (needed for android/ios packaging)
package.domain = org.beacon

# (str) Source code where the main.py live
source.dir = .

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py
# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,bpl

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (str) python-for-android branch to use
p4a.branch = master

# (str) Custom source folders to add to the python path
# source.paths = .

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 20

# (str) Android NDK version to use
# android.ndk = 19b

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (str) Android additional libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_arm64_v8a = libs/android-v8/*.so
# android.add_libs_x86 = libs/android-x86/*.so
# android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Dont forget to add the WAKE_LOCK permission if you set this to True
# android.wakelock = False

# (list) Android application meta-data to set (key=value format)
# android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
# android.library_references =

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.renpy.android.PythonActivity

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# android.add_jars = foo.jar,bar.jar,path/to/more/*.jar
# android.add_jars =

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# bootstrap)
# android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# android.add_assets =

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# bootstrap)
# android.gradle_dependencies =

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for more information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes 
# e.g. android.gradle_repositories = "maven { url 'https://jitpack.io' }"
# android.gradle_repositories =

# (list) Packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes 
# e.g. android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"
# android.add_packaging_options =

# (list) Java classes to add as activities to the manifest 
# android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# The default is APP
# android.ouya.category = GAME

# (str) Filename associated with the presplash, where the sub-keys are the
# screen density names or scale.
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
# android.presplash_color = #FFFFFF

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
# icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
# icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Adaptive icon of the application (used if Android API level is 26+ at runtime)
# icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
# icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (str) Filename associated with the icon, where the sub-keys are the
# screen density names or scale.
# icon.filename = %(source.dir)s/data/icon.png

# (str) Android-specific build dependencies
# android.build_deps =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / requirements. Instead of doing:
#
#    [app]
#    requirements = sqlite3,kivy
#
#    You can do:
#
#    [app:requirements]
#    sqlite3
#    kivy
#
#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a debug version of your application
#    and a release version of your application
#
#    [app:debug]
#    title = My Application Debug
#
#    [app:release]
#    title = My Application
#
#    Then, to run the build, you just need to:
#
#    buildozer --profile debug android debug
#
