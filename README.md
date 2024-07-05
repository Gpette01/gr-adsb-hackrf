# README

## Overview

This reposiroty is an ADS-B reader using GnuRadio and hackrf device

## Features

- **HackRF Support**: Replaced USRP device with HackRF for receiving ADS-B signals.
- **Osmocom Module**: Utilizes the Osmocom module in GNU Radio for interfacing with HackRF.
- **Customized Decoder**: Modified `decoder.py` script to customize the printing of decoded ADS-B messages.

## Requirements

- [GNU Radio]([InstallingGR - GNU Radio](https://wiki.gnuradio.org/index.php/InstallingGR))
- HackRF
- [Osmocom Module]([GrOsmoSDR - gr-osmosdr - Open Source Mobile Communications](https://osmocom.org/projects/gr-osmosdr/wiki))

## Installation

1. **Install Gnu Radio from the link provided above.**

2. **Module install:**
   
   Install the [gr-adsb]([GitHub - mhostetter/gr-adsb: GNU Radio OOT module for demodulating and decoding ADS-B packets](https://github.com/mhostetter/gr-adsb)) and [gr-osmosdr]([GrOsmoSDR - gr-osmosdr - Open Source Mobile Communications](https://osmocom.org/projects/gr-osmosdr/wiki)) using the 2 linked repositories, and they should be placed as directed: If gnuradio is installed in `~/Directory1/gnuradio` then the modules should be `~/Directory1/gnuradio/gr-adsb`, `~/Directory1/gnuradio/gr-osmosdr`. In the gnuradio-companion you should see ADSB and Osmocom modules.

## Usage

1. ## **Modify the GNU Radio flowgraph:**

Using the flowgraph located in `/gnuradio/gr-adsb/examples/adsb_rx.grc` remove the ursp module and add the osmocom modules so it should look like something like this:

<img title="" src="https://github.com/Gpette01/gr-adsb-hackrf/blob/main/images/Flowchart" alt="">

if you try to start the flowchart now everything should open up correctly but the hackrf might not be reading any data. This issue should be fixed if you change the `IF` and `BB` gain to `40dB` in the `osmocom Source` block. Also a good idea is to set the `gain` which for now is located in the `QT GUI Entry` to `100dB`or `125dB`. If you see overflow(The letter o spammed in the terminal) you can try changing the osmocom `Source sync to PC Clock` **if your hackrf has a clock**, and most importantly raise the `Detection Threshold` in the `QT GUI Entry`, i found `0.05` a good value just bear in mind that overflow will not dissapear.



2. **Remove GUI(If needed)**
   
   If you want to remove the GUI and directly access the decoded data for some other use you can edit your flowchart to be like this:
   
   <img title="" src="https://github.com/Gpette01/gr-adsb-hackrf/blob/main/images/Flowchart2" alt="">

    When you run the flowchart now once, in the examples directory a python file named `adsb_rx.py` will be generated that will allow you to run the flowchart without the gnuradio-companion you still need the dependecies though.

In the `ADS-B decoder module` you can change the `Print Level` to verbose so you can manage the data printed. To actually access the data, you have to open the `decoder.py` file which is essentially the source code of the `ADS-B decoder module`. The file is located `~/usr/local/lib/python3.12/dist-packages/gnuradio/adsb/decoder.py`

The logging happens in the `self.log()` statements. Eg. `self.log("info", "Datetime", self.datetime)` which would print `[INFO] Datetime: TimeHere`. You can then find the `self.log()` statements in the multiple `if's (self.msg_filter == "All Messages" or self.msg_filter == "Extended Squitter Only")` since the `Message Filter` in the `ADS-B Decoder` is set to `Extended Squiiter Only` there you can do whatever you like with the data.


