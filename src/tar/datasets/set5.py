#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Simon Schaefer
# Description : SET5 validation dataset extension. 
# =============================================================================
import os

from tar.dataloader import _Dataset_

class SET5(_Dataset_):
    def __init__(self, args, name='SET5', train=True):
        super(SET5, self).__init__(args, name=name, train=train)

    def _scan(self):
        names_hr, names_lr = super(SET5, self)._scan()
        names_hr = names_hr[self.begin:self.end]
        names_lr = names_lr[self.begin:self.end]
        return names_hr, names_lr

    def _set_filesystem(self, dir_data):
        super(SET5, self)._set_filesystem(dir_data)
        self.dir_hr = os.path.join(self.directory, 'HR')
        self.dir_lr = os.path.join(self.directory, 'LR_bicubic')
