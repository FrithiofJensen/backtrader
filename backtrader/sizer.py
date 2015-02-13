#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
################################################################################
#
# Copyright (C) 2015 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
import metabase


class SizerBase(object):
    __metaclass__ = metabase.MetaParams

    params = (('broker', None,),)

    def getsizing(self, data, broker=None):
        broker = broker or self.params.broker
        return self._getsizing(broker.getcommissioninfo(data), broker.getcash())

    def _getsizing(self, comminfo, cash):
        raise NotImplementedError

    def setbroker(self, broker):
        self.params.broker = broker

    def getbroker(self):
        return self.params.broker


class SizerFix(SizerBase):
    params = (('stake', 1),)

    def _getsizing(self, comminfo, cash):
        return self.params.stake