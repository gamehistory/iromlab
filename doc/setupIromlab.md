# Iromlab setup and configuration

## Installation

The recommended way to install Iromlab is to use *pip*. Installing with *pip* will also automatically install any Python packages that are used by Iromlab. On Windows systems the *pip* executable is located in the *Scripts* directory which is located under Python's top-level installation folder (e.g. *C:\Python36\Scripts*). To install Iromlab, follow the steps below:

1. Launch a Command Prompt window. Depending on your system settings you may need to do this with Administrator privilege (right-click on the *Command Prompt* icon and the choose *Run as Administrator*).
2. Type:

      `%path-to-pip%\pip install iromlab`
   
    Here, replace %path-to-pip% with the actual file bpath on your system. For example:

     `C:\Python36\Scripts\pip install iromlab`
    
The above steps will install Iromlab and all required libraries. It also installs Windows binaries of the following tools:

* [cd-info](https://linux.die.net/man/1/cd-info) - this tool is part of [libcdio](https://www.gnu.org/software/libcdio/),  the "GNU Compact Disc Input and Control Library".
* [shntool](http://www.etree.org/shnutils/shntool/) - used to verify the integrity of created WAVE files.
* [flac](https://xiph.org/flac/) - used to verify the integrity of created WAVE files.

Finally it also creates a shortcut to the main Iromlab application on the Windows Desktop.
        
## Configuration

Before Iromlab is ready to use it is necessary to apply some configuration settings. You can do this by editing a configuration file. To find it you first need to locate the Windows User Profile directory[^1]. Open a Command Prompt window and type:

    set USERPROFILE

The output will be something like this:

    USERPROFILE=C:\Users\jkn010

If you open this location on your machine with Window Explorer you will find that it contains a folder named *iromlab*:   

![](./img/userDir.png)

Open the folder, and you will see this:

![](./img/userDir2.png)

Now open *config.xml* in a text editor (e.g. Notepad), or alternatively use a dedicated XML editor. Carefully go through all the variables (which are defined as XML elements), and modify them if necessary. Here is an explanation of all variables.

### cdDriveLetter

This is the drive letter that is assigned to the Nimbie discrobot's built-in optical drive. If you don't know what value to use, just switch on the Nimbie. Then open a Windows Explorer window, click on *Computer* and then look under *Devices with Removable Storage*. You will see something like this: 

![](./img/cddrives.png)

In this case we have 2 CD drives, where *D* is the internal drive, and *I* is the Nimbie. So we enter this in the configuration file like this:

    <cdDriveLetter>I</cdDriveLetter>

(Note: do *not* add a colon to the drive letter).

### rootDir

This defines the root directory where Iromlab will write its data. Iromlab output is organised into *batches*, and each batch is written to *rootDir*. Make sure to pick an existing directory with plenty of space. Example:

    <rootDir>E:\nimbieTest</rootDir>


### tempDir

This is the directory that is used for writing temporary files. It must be an existing directory; in most cases you can use the default value (*C:\Temp*). Example:

    <tempDir>C:\Temp</tempDir>

### prefixBatch

This is a text prefix that is added to the automatically-generated batch names:

    <prefixBatch>kb</prefixBatch>

### audioFormat

This defines the audio ripping format. Permitted values are  *wav* or *flac*. This setting is *only* used for the audio verification component, the ripping format must be set from dBpoweramp's CD Ripper tool, which is explained in the [dBpoweramp setup and configuration](./setupDbpoweramp.md) instructions. You have to make sure that both settings are consistent, as unexpected behaviour may occur otherwise. Example: 

    <audioFormat>flac</audioFormat>

### secondsToTimeout

Defines the maximum number of seconds that Iromlab will wait while trying to load a new disc. This will prevent iromlab from entering an infinite loop if e.g. a disc cannot be loaded properly because its is badly damaged.

    <secondsToTimeout>20</secondsToTimeout>

### Location of disc robot drivers

The following four settings define the full file paths to the driver programs for the disc robot. These are all located in dBpoweramp's BatchRipper folder (installation instructions for dBpoweramp and the drivers can be found [here](./setupDbpoweramp.md)). Example:

    <prebatchExe>C:\Program Files\dBpoweramp\BatchRipper\Loaders\Nimbie\Pre-Batch\Pre-Batch.exe</prebatchExe>
    <loadExe>C:\Program Files\dBpoweramp\BatchRipper\Loaders\Nimbie\Load\Load.exe</loadExe>
    <unloadExe>C:\Program Files\dBpoweramp\BatchRipper\Loaders\Nimbie\Unload\Unload.exe</unloadExe>
    <rejectExe>C:\Program Files\dBpoweramp\BatchRipper\Loaders\Nimbie\Reject\Reject.exe</rejectExe>

### isoBusterExe

Location of isoBuster (installation instructions for Isobuster can be found [here](./setupIsobuster.md)). Example:

    <isoBusterExe>C:\Program Files (x86)\Smart Projects\IsoBuster\IsoBuster.exe</isoBusterExe>

### dBpowerampConsoleRipExe

Location of the dBpoweramp console ripper tool (note: not included with dBpoweramp!): 

    <dBpowerampConsoleRipExe>C:\Program Files\dBpoweramp\kb-nl-consolerip.exe</dBpowerampConsoleRipExe>

If all went well, Iromlab will now be ready to use!

| |
|:--|
|[Back to Setup Guide](./setupGuide.md)|

[^1]: To be more precise: the profile of the user that installed Iromlab (in case of multiple user profiles)