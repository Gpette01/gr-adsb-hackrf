#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ADS-B Receiver
# Author: Matt Hostetter
# GNU Radio version: v3.11.0.0git-791-gb404dd7e

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import correctiq
import gnuradio.adsb as adsb
import osmosdr
import time
import threading




class adsb_rx(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "ADS-B Receiver", catch_exceptions=True)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.threshold = threshold = 0.05
        self.gain = gain = 125
        self.fs = fs = 2e6
        self.fc = fc = 1090e6

        ##################################################
        # Blocks
        ##################################################

        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_source_0.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
        self.osmosdr_source_0.set_sample_rate(2e6)
        self.osmosdr_source_0.set_center_freq(1090e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(True, 0)
        self.osmosdr_source_0.set_gain(60, 0)
        self.osmosdr_source_0.set_if_gain(40, 0)
        self.osmosdr_source_0.set_bb_gain(40, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.correctiq_correctiq_0 = correctiq.correctiq()
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.adsb_framer_1 = adsb.framer(fs, threshold)
        self.adsb_demod_0 = adsb.demod(fs)
        self.adsb_decoder_0 = adsb.decoder("Extended Squitter Only", "None", "Error")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.adsb_demod_0, 'demodulated'), (self.adsb_decoder_0, 'demodulated'))
        self.connect((self.adsb_demod_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.adsb_framer_1, 0), (self.adsb_demod_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.adsb_framer_1, 0))
        self.connect((self.correctiq_correctiq_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.correctiq_correctiq_0, 0))


    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.adsb_framer_1.set_threshold(self.threshold)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc




def main(top_block_cls=adsb_rx, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    tb.flowgraph_started.set()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
