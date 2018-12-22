#!/usr/bin/env python3

__author__ = "Siraj Saleheen"

class FontHelper:

    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

    def set_pass_color_block(self, starter_color):
        color_block_start = starter_color
        color_block_end = self.ENDC
        return color_block_start+"PASS: "+color_block_end