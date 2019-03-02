#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Simon Schaefer
# Description : Test cases for image domain. 
# =============================================================================
import numpy as np
import os
import unittest

import super_resolution.inputs as argus
import super_resolution.dataloader as dataloader
import super_resolution.optimization as optimization
import super_resolution.miscellaneous as miscellaneous

class DataLoaderTest(unittest.TestCase): 
    
    def test_initialization(self): 
        args = argus.args
        loader = dataloader._Data_(args)
        assert loader
        # Testing data loader. 
        loader_test = loader.loader_test
        assert loader_test
        # Training data loader. 
        if not args.test_only: 
            loader_train = loader.loader_train
            assert loader_train
    
    def test_batching(self): 
        args = argus.args
        args.test_only = False
        loader = dataloader._Data_(args)
        loader_train = loader.loader_train
        for batch, (lr, hr, files) in enumerate(loader_train): 
            assert lr.shape[0] == args.batch_size and hr.shape[0] == args.batch_size
            assert lr.shape[1] == args.n_colors and hr.shape[1] == args.n_colors
            s, ls = args.patch_size, int(args.patch_size/args.scale)
            assert lr.shape[2] == ls and hr.shape[2] == s
            assert lr.shape[3] == ls and hr.shape[3] == s
            break

    def test_div2k(self):
        args = argus.args
        args.test_only = False
        args.data_train = "DIV2K"
        args.data_test = "DIV2K"
        loader = dataloader._Data_(args)
        loader_train = loader.loader_train
        for batch, (lr, hr, files) in enumerate(loader_train): 
            assert lr.shape[0] == args.batch_size and hr.shape[0] == args.batch_size
            assert lr.shape[1] == args.n_colors and hr.shape[1] == args.n_colors
            s, ls = args.patch_size, int(args.patch_size/args.scale)
            assert lr.shape[2] == ls and hr.shape[2] == s
            assert lr.shape[3] == ls and hr.shape[3] == s
            break   

    def test_mnist(self):
        args = argus.args
        args.test_only = False
        args.data_train = "MNIST"
        args.data_test = "MNIST"
        args.patch_size = 10
        loader = dataloader._Data_(args)
        loader_train = loader.loader_train
        for batch, (lr, hr, files) in enumerate(loader_train): 
            assert lr.shape[0] == args.batch_size and hr.shape[0] == args.batch_size
            assert lr.shape[1] == args.n_colors and hr.shape[1] == args.n_colors
            s, ls = args.patch_size, int(args.patch_size/args.scale)
            assert lr.shape[2] == ls and hr.shape[2] == s
            assert lr.shape[3] == ls and hr.shape[3] == s
            if batch == 3: 
                break        

class MiscellaneousTest(unittest.TestCase): 

    def test_timer(self): 
        timer = miscellaneous._Timer_()
        timer.hold()
        dt = timer.toc()
        assert dt > 0 and dt < 1.0

    def test_checkpoint(self): 
        args = argus.args
        ckp = miscellaneous._Checkpoint_(args)
        ckp.write_log("test")
        ckp.done()

class OptimizationTest(unittest.TestCase):

    def test_loss_init(self): 
        # Intialize loss module input arguments. 
        args = argus.args
        args.load = ""
        ckp = miscellaneous._Checkpoint_(args)
        # Initialize loss module. 
        loss = optimization._Loss_(args, ckp)  
        assert loss
        ckp.done()

    def test_loss_forward(self): 
        # Intialize loss module input arguments. 
        args = argus.args
        args.test_only = False
        args.loss = "HR*1*L1"
        args.load = ""
        ckp = miscellaneous._Checkpoint_(args)
        loader = dataloader._Data_(args)
        loader_train = loader.loader_train   
        # Test forward. 
        loss = optimization._Loss_(args, ckp)  
        loss.start_log()   
        for batch, (lr, hr, files) in enumerate(loader_train): 
            loss_kwargs = {'HR_GT': hr, 'HR_OUT': hr}
            loss_sum = loss.forward(loss_kwargs)
            assert loss_sum == 0
            break 
        ckp.done()

    def test_loss_display(self): 
        # Intialize loss module input arguments. 
        args = argus.args
        args.loss = "HR*1*L1"
        args.load = ""
        ckp = miscellaneous._Checkpoint_(args)
        # Test loss description. 
        loss = optimization._Loss_(args, ckp)  
        loss.start_log()      
        log = loss.display_loss(0)
        log = str(log)
        assert log.find("TOTAL") > 0 and log.find("HR") > 0
        ckp.done()

    def test_loss_modules(self): 
        # Intialize loss module input arguments. 
        args = argus.args
        args.loss = "HR*1*L1"
        args.load = ""
        ckp = miscellaneous._Checkpoint_(args)
        # Test loss description. 
        loss = optimization._Loss_(args, ckp)        
        modules = loss.get_loss_module()  
        assert modules     
        ckp.done()

if __name__ == '__main__':
    unittest.main()