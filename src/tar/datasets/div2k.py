#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Simon Schaefer
# Description : DIV2K dataset extension.
# =============================================================================
import os

from tar.dataloader import _IDataset_

class DIV2K(_IDataset_):
    def __init__(self, args, train, scale, name="DIV2K"):
        # Determining training/testing data range.
        self.begin, self.end = 1, 800
        # Initialization of dataset class.
        super(DIV2K, self).__init__(args, name=name, train=train, scale=scale)

    def _scan(self):
        names_hr, names_lr = super(DIV2K, self)._scan()
        names_hr = names_hr[self.begin:self.end]
        names_lr = names_lr[self.begin:self.end]
        return names_hr, names_lr

    def _set_filesystem(self, dir_data):
        super(DIV2K, self)._set_filesystem(dir_data)
        self.dir_hr = os.path.join(self.directory, "DIV2K_train_HR")
        self.dir_lr = os.path.join(self.directory, "DIV2K_train_LR_bicubic")
        self.dir_lr = os.path.join(self.dir_lr, "X{}".format(self.scale))
