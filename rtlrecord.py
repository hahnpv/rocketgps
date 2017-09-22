#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Sep 18 17:45:05 2017
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2048000
        self.freq = freq = 1545420000
        fname = "/home/sdrgps/" + time.strftime("%Y%m%d%H%M%S") + ".s8"

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "rtl_tcp=127.0.0.1:1234" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(40, 0)
        self.rtlsdr_source_0.set_if_gain(30, 0)
        self.rtlsdr_source_0.set_bb_gain(30, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, fname, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_interleaved_char_0 = blocks.complex_to_interleaved_char(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_interleaved_char_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_complex_to_interleaved_char_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    time.sleep(1200)
#    try:
#        raw_input('Press Enter to quit: ')
#    except EOFError:
#        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
