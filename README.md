# Vulcan 3D Engine from scratch
This Repo is my attempt to build a 3D game engine written in C++, using Vulkan as a Low Level graphics card API and GLFW as a window manager.

# Reminders and things to look out for
* Apparently Metal has some kind of internal setup which causes Vulkan with MoltenVK to not be able to render more than the display refresh rate, that means that I am capped to 60fps rendering.
    * This seems to be a well known issue, Path of Exile seems to have the same issue from what I saw.
* I use a studio display, which has a "retina" display. What it does concretely it renders things at 5k and then downscales it to (in my case 2880x1620, i.e. with a 2x downscaling factor for width and height). Default scale is 2560x1440.
* (Currently not implemented) Be careful whether you are compiling with DEBUG flag set or not
* (Currently always on) The runtime sanitizers in compilation settings are VERY slow, active during debug, if things are slow should try to disable those first.
* Regarding MacOS Specific Workarounds
    * https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_KHR_portability_enumeration.html
    * https://github.com/ocornut/imgui/issues/6101#issuecomment-1398223233
    * https://stackoverflow.com/questions/72374316/validation-error-on-device-extension-on-m1-mac
    * https://stackoverflow.com/questions/66659907/vulkan-validation-warning-catch-22-about-vk-khr-portability-subset-on-moltenvk/66660106#66660106
    * https://www.youtube.com/watch?v=7Sp7waWUXOc

# Setup
I'm using AppleClang 15.0.0.15000309 as my compiler and CMake to generate my make files. The project can be rebuild by using the `clean_and_recompile.sh` script (Warning: This wipes all build information and so can be quite slow. Although I don't build my dependencies from scratch so it shouldn't be too bad. Might build vulcan from source later on, but currently I just use the SDK directly.)

If you want to compile the project you can either use the `compile_and_run.sh` (just comment out the last line if you don't want to run after building)
```
You can download the newest Vulkan SDK [here](https://vulkan.lunarg.com/sdk/home) 

I'm using version 1.3.290.0 (23-Jul-2024) which has the following SHA256 checksum:

a14f3026290c2ef0a9fc96af3f6b75135018d145748543a644107a36f1d65a71

Add the following to your RC file (I'm using the ZSH shell so it's at `~/.zshrc` for me).
# Vulkan
export VULKAN_SDK=/Users/danielsinkin/VulkanSDK/1.3.290.0/macOS
export GLSC=$VULKAN_SDK/bin/glsc
export PATH=$VULKAN_SDK/bin:$PATH
export DYLD_LIBRARY_PATH=$VULKAN_SDK/lib:/usr/local/lib:$DYLD_LIBRARY_PATH
export VK_LAYER_PATH=$VULKAN_SDK/share/vulkan/explicit_layer.d
# export VK_INSTANCE_LAYERS="VK_LAYER_LUNARG_api_dump:VK_LAYER_KHRONOS_validation"
export VK_INSTANCE_LAYERS="VK_LAYER_KHRONOS_validation"
export VK_ICD_FILENAMES=/Users/danielsinkin/VulkanSDK/1.3.290.0/macOS/share/vulkan/icd.d/MoltenVK_icd.json
```

# My Dev Specs
```bash
system_profiler
    Software
        System Version: macOS 14.6.1 (23G93)
        Kernel Version: Darwin 23.6.0
    Hardware
        Model Name: MacBook Air
        Model Identifier: Mac14,2
        Model Number: MN703D/A
        Chip: Apple M2
        Total Number of Cores: 8 (4 performance and 4 efficiency)
        Memory: 16 GB
        System Firmware Version: 10151.140.19
        OS Loader Version: 10151.140.19
        Serial Number (system): *
        Hardware UUID: *
        Provisioning UDID: *
        Activation Lock Status: *
    Graphics/Displays:
        Chipset Model: Apple M2
        Type: GPU
        Bus: Built-In
        Total Number of Cores: 10
        Vendor: Apple (0x106b)
        Metal Support: Metal 3
        Displays:
            Studio Display:
                Display Type: Retina LCD
                Resolution: 5120 x 2880 Retina
                Display Serial Number: *
                Display Firmware Version: Version 17.0 (Build 21A329)
                Main Display: Yes
                Mirror: Off
                Online: Yes
                Automatically Adjust Brightness: No
```

# Credits and Attributions
* Models used
    * "Viking Room" (https://sketchfab.com/3d-models/viking-room-a49f1b8e4f5c4ecf9e1fe7d81915ad38) by nigelgoh
        * I'm using the clean up version made by Vulkan-Tutorial.com, found [here](https://vulkan-tutorial.com/Loading_models)..
    * "Nicole" (https://skfb.ly/pqvTX) by Voon Hong Liang is licensed under Creative Commons Attribution (http://creativecommons.org/licenses/by/4.0/).
    * "Suzanne" the famous monkey, from [here](https://github.com/OpenGLInsights/OpenGLInsightsCode/tree/master)
* Textures used
    * https://polyhaven.com/a/painted_plaster_wall
    * Metal texture from this group https://www.textures.com/category/metal/169
* Fonts
    * [Merriweather](https://fonts.google.com/specimen/Merriweather)
    * https://github.com/githubnext/monaspace/

# References
* Dependencies
    * [VulkanSDK](https://www.lunarg.com/vulkan-sdk/)
        * MacOS on the new Apple Silicon chips does not support Vulkan natively for that we use [MoltenVK](https://github.com/KhronosGroup/MoltenVK) which is included in the SDK
            * For more detaisl see this the following:
                * https://developer.apple.com/documentation/apple-silicon/porting-your-macos-apps-to-apple-silicon
                * https://support.apple.com/en-ca/101525
    * [GLFW](https://www.glfw.org)
    * [STB](https://github.com/nothings/stb)
       * Image, Image Write and Truetype
    * [tinyobjloader](https://github.com/tinyobjloader/tinyobjloader)
* Documentation
    * [CPPReference](https://en.cppreference.com/w/)
        * [Hash](https://en.cppreference.com/w/cpp/utility/hash)
    * [Vulkan](https://docs.vulkan.org/spec/latest/index.html)
    * [GLFW](https://www.glfw.org/docs/latest/vulkan_guide.html)
        * [Vulkan Integration](https://www.glfw.org/docs/latest/vulkan_guide.html)
* Educational Resources
    * Books
        * [Physically Based Rendering: From Theory to Implementation](https://www.pbr-book.org)
        * [Data-Oriented Design](https://www.dataorienteddesign.com/dodbook/)
        * [Ray Tracing in one Weekend](https://raytracing.github.io)
        * [Computer Graphics from Scratch](https://gabrielgambetta.com/computer-graphics-from-scratch/)
        * [The Art of writing Efficient Programs](https://github.com/ssloy/tinyraytracer/wiki)
    * Repositories
        * [tinyraytracer](https://github.com/ssloy/tinyraytracer/wiki)
        * https://github.com/SaschaWillems/Vulkan
        * [Unity Engine Bloom Implementation](https://github.com/Unity-Technologies/Graphics/blob/master/com.unity.postprocessing/PostProcessing/Shaders/Builtins/Bloom.shader)
    * Blogs
        * [The Essential Resources for Vulkan development](https://www.vulkan.org/learn)
        * [Nvidia's GPU Gems series](https://developer.nvidia.com/gpugems/gpugems/contributors)
        * [A trip through the Graphics Pipeline 2011: Index](https://fgiesen.wordpress.com/2011/07/09/a-trip-through-the-graphics-pipeline-2011-index/)
        * [Learning Modern 3D Graphics Programming](https://paroj.github.io/gltut/)
        * [Intel: API without secrets: Introduction to Vulkan](https://www.intel.com/content/www/us/en/developer/articles/training/api-without-secrets-introduction-to-vulkan-part-1.html)
        * [Writing an efficient Vulkan renderer](https://zeux.io/2020/02/27/writing-an-efficient-vulkan-renderer/)
        * [https://edw.is/learning-vulkan/](https://edw.is/learning-vulkan/)
    * Tutorials
        * [Vulkan Tutorial](https://vulkan-tutorial.com)
        * [Learn OpenGL](https://learnopengl.com)
            * [Advanced Lighting](https://learnopengl.com/Advanced-Lighting/Advanced-Lighting)
                * Noteably introduces the (Blinn-)Phong reflection model we use.
        * [VulkanGuide](https://vkguide.dev)
    * YouTube
        * MollyRocket
            * Handmade Hero Series
                * [Rendering Playlist](https://www.youtube.com/watch?v=ofMJUSchXwo&list=PLEMXAbCVnmY40lfaaowTqIs_dKNgOXR5Q)
                * [Lighting Playlist](https://www.youtube.com/watch?v=owpVP0IQWXk&list=PLEMXAbCVnmY4ASbr-fMBSroE2JF-u20du)
                * [Optimization Playlist](https://www.youtube.com/watch?v=qin-Eps3U_E&list=PLEMXAbCVnmY5qGQB96s7Vysr1nJcX_BW_)
                * [Multithreading Playlist](https://www.youtube.com/watch?v=qkugPXGeX58&list=PLEMXAbCVnmY7me6j4VtpCYMuZX3QpcBBH)
            * [Performanc-Aware Programming Playlist](https://www.youtube.com/watch?v=pZ0MF1q_LUE&list=PLEMXAbCVnmY7t29i_rd3mnALWu-aZr_42)
        * [Acerola](https://www.youtube.com/@Acerola_t)
            * Post-Processing with Shaders
        * [GetIntoGameDev's Vulkan 2024 Series](https://www.youtube.com/watch?v=Est5AvResbE&list=PLn3eTxaOtL2Nr89hYzKPib7tvce-ZO4yB)
](https://www.youtube.com/watch?v=wGSSUSeaLgA)
        * [Interactive Computer Graphics](https://www.youtube.com/watch?v=UVCuWQV_-Es&list=PLplnkTzzqsZS3R5DjmCQsqupu43oS9CFN&index=1)
        * GSN Compose
            * [Shaders Monthly Series](https://www.youtube.com/watch?v=mJOqVeiLOf0&list=PL8vNj3osX2PzZ-cNSqhA8G6C1-Li5-Ck8&index=1])
        * [Game Engine Series](https://www.youtube.com/@GameEngineSeries) (that's the name of the channel)
            * [Game Engine Programming Series](https://www.youtube.com/watch?v=hRL56gXqj-4&list=PLU2nPsAdxKWQYxkmQ3TdbLsyc1l2j25XM)
   * Conferences
      * SIGGRAPH
         * [2014](https://advances.realtimerendering.com/s2014/index.html)
      * Vulkanised
         * 2024
            * [Common Mistakes When Learning Vulkan - Charles Giessen](https://www.youtube.com/watch?v=0OqJtPnkfC8)
     * CppCon
        * 2021
            * [Back to Basics Series](https://www.youtube.com/watch?v=Bt3zcJZIalk&list=PLHTh1InhhwT4TJaHBVWzvBOYhp27UO7mI)
     * C++Now
         * 2024
             * [Unlocking Modern CPU Power - Next-Gen C++ Optimization Techniques - Fedor G Pikus - C++Now 2024
# Appendix A: YouTube Links to the recorded videos
TODO: Put them all in a single playlist and link that one
* https://youtu.be/afF579Obqlw (Not in the screencaps folder)
* https://youtu.be/JDX6OLH_uUA (Not in the screencaps folder)
* https://youtu.be/Sk9cLoi_Vtk
* https://youtu.be/5Q_WZqeqGG0
* https://youtu.be/tLEBiCrzxFk
