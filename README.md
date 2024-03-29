# AutoISCE
Stack processor for ISCE2
## Current version: 0.6
### Changelogs
- version 0.6 (2024.02.12): Added a mask feature during ionosphere correction. An external mask file can be used.
- version 0.5 (2023.02.02): Added support for giving external dem. Paths must be defined in parfile
- version 0.4 (2023.02.01): Stable version. Added instructions for the parfile. Added outputs to console about the status of the process
                           Process workflow has changed. Now, baselines will be calculated first to get both pbaseall.list and boundingbox
                           If boundingbox is given in parfile, those values will be used instead. download dem script is also changed. Now
                           it can download the dem file automaticaly with the boundingbox. Additionally, console outputs from ISCE will be
                           saved to AutoISCE.log file, they won't apper on the console.
- version 0.3 (2023.01.28): Added getboundingbox.py script. It can find the common geoboundingbox for all process pairs. This information
                          is later used in geocoding so that all the geocoded outputs will have the same coordinates / dimensions.
                          This informaton can also be used for automatic dem download.
- version 0.2 (2023.01.22): Baseline and main process are separated. Now the script generates pbaseall.list, baselines list, for each pair
                          Added downloaddem script to the workflow. Later it can be used for automatic dem download.
- version 0.1 (2023.01.17): Initial creation


This is an automatic processing workflow to produce series of interferograms from available SLC data.
### Outputs
* The outputs are stored in the main project folder (where you run the program) in separate folders named as yyyymmdd_yyyymmdd format. Here the first
date is the reference image, second date is the secondary image.
* Perpendicular baselines for each interferogram is saved in *pbaseall.list* in the main project folder.

### Available workflows:
* ALOS2 data (using alos2App.py)

At the moment, only the ALOS2 data can be processed with this script.



# Requirements
* ISCE > https://github.com/isce-framework/isce2

# Installation
* Download the scripts, AutoISCE, convert2int.py, downloadem, getboundingbox.py, prep_alos2xml, applyMask and add them to your PATH. Make sure that they have execution permissions.

# How to use the script

Here are the quick instructions to process your first stack:

* You need to place your SLC files in some folder. Each date must be in a folder with yyyymmdd format.
An example folder structure for **SLCDIR**:
```
(base) Yagizalps-MacBook-Pro:SLCDIR yagizalp$ pwd
/Volumes/SSD_TOHOKU_OKUR/alos2/path24frame3400f2_6/SLCDIR
(base) Yagizalps-MacBook-Pro:SLCDIR yagizalp$ ls
20160326        20170325        20170715        20190810        20191214        20200808        20210612
20160604        20170603        20180616        20190921        20200613        20201212        20211211
```
Inside each folder you should have the SLC and LED files:
```
(base) Yagizalps-MacBook-Pro:20160326 yagizalp$ pwd
/Volumes/SSD_TOHOKU_OKUR/alos2/path24frame3400f2_6/SLCDIR/20160326
(base) Yagizalps-MacBook-Pro:20160326 yagizalp$ ls
BRS-HH-ALOS2099363400-160326-FBDR1.1__D.jpg     IMG-HV-ALOS2099363400-160326-FBDR1.1__D         VOL-ALOS2099363400-160326-FBDR1.1__D
BRS-HV-ALOS2099363400-160326-FBDR1.1__D.jpg     LED-ALOS2099363400-160326-FBDR1.1__D            summary.txt
IMG-HH-ALOS2099363400-160326-FBDR1.1__D         TRL-ALOS2099363400-160326-FBDR1.1__D
```

* Then you need to create **pairs.list**. This file must contain the dates you want to process in *yyyymmdd yyyymmdd* format. Here, the first date is the reference, second date is the secondary image:

An example file:
```
20170603 20190810
20170603 20200613
20170603 20200808
20170603 20210612
20190810 20200613
20190810 20200808
20190810 20210612
20200613 20200808
20200613 20210612
20200808 20210612
20200808 20211211
20190810 20211211
20200613 20211211
20210612 20211211

```
**Important**: You must leave one empty space at the end of the file.

* You must prepare a parameter file. You can use the example for reference (AutoISCE_example.par).

* You need to give paths to your slc directory > **SLCDIR**, pairs.list > **flist**. Don't change the **script** variable.
Because only alos2App.py is available right now. Later, other scripts might be available.

* You can change **pol** if you have the data with different polarization.

* You can give **geocode_bounding_box** in the parameter file. However, this does not reduce the process area
This value is used in the geocoding step only. Whatever value you give, ISCE will process the full interferogram. 
But if you give a smaller bounding_box than your interferogram, your geocoded files will have a smaller extent. 
You can leave it empty. Because the script will automatically calculate the largest possible window using getboundingbox.py script.

* There are a bunch of different looks used in ISCE. You need to set your first look depending on the data that you are processing. 
I added the table from ISCE documentation for reference. 

* There are some parameters for filtering. The ones in the parameter file are the defaults. You can experiment with different values.

* At the end, you can define paths to the dem files manually. If you already have dem files maybe you can use them. 
If you comment these three lines, the script will automatically download the dem files. 

But you need an account from "urs.earthdata.nasa.gov". Here are the instructions on how to set up your account:
> https://github.com/isce-framework/isce2#notes-on-digital-elevation-models
> https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+cURL+And+Wget

* Create a main process folder and place your parameter file inside this folder.

Then run the script in the main process folder:
```
AutoISCE PARFILE
```

The script will run *alos2App.py* until the baseline step to obtain perpendicular baselines for each image pair. Since we want to use the outputs in a time-series, geocoded outputs have to be in the same reference frame. If **geocode_bounding_box** is not given in the parameter file, the script will run *getboundingbox.py* to determine the largest possible **geocode_bounding_box** for all image pairs. This value will be used for both geocoding and automatic dem download.

After the baseline step is over, *alos2App.py* will run until the last step to process all image pairs one by one.

