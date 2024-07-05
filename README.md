# README

## Overview

This repository is a modified version of [mhostetter/gr-adsb](https://github.com/mhostetter/gr-adsb). The original project uses a USRP device for ADS-B signal reception and decoding. This modified version uses a HackRF device with the Osmocom module in GNU Radio and includes a customized `decoder.py` script to meet specific printing needs.

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

1. **Modify the GNU Radio flowgraph:**
   
   Using the flowgraph located in `/gnuradio/gr-adsb/examples/adsb_rx.grc` remove the ursp module and add the osmocom modules so it should look like something like this:
   
   <img title="" src="https://github.com/Gpette01/gr-adsb-hackrf/tree/main/images/Flowchart.png" alt="">

## Customization

- **Decoder Script (`decoder.py`):**
  
  The `decoder.py` script has been modified to customize the output format of the decoded ADS-B messages. You can further modify this script to suit your specific needs.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
