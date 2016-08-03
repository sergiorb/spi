#!/usr/bin/python3
# -*- coding: utf-8 -*-

from spi import info

class Spi():

	def info(self):

		return info.get_system_info()

	def memory(self):

		return info.get_system_memory()