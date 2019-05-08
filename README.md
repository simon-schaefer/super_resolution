# TAR

Task-Aware image and video super resolution using unsupervised learning (autoencoders)

## Literature
- [Paper: Task-Aware Image Downscaling (Kyoung Mu Lee)](http://openaccess.thecvf.com/content_ECCV_2018/papers/Heewon_Kim_Task-Aware_Image_Downscaling_ECCV_2018_paper.pdf)

- [Paper: Multi-bin Trainable Linear Unit for Fast Image Restoration Networks](https://arxiv.org/pdf/1807.11389.pdf)
- [Paper: Frame-Recurrent Video Super Resolution (Google)](https://arxiv.org/pdf/1801.04590.pdf)
- [Paper: Photorealistic Video Super Resolution (Amazon)](https://arxiv.org/pdf/1807.07930.pdf)
- [Paper: Seven Ways to improve example-based single image super resolution (ETH)](http://www.vision.ee.ethz.ch/~timofter/publications/Timofte-CVPR-2016.pdf)
- [Paper: Photo-Realistic Single Image Super Resolution Using a GAN (Twitter)](https://arxiv.org/pdf/1609.04802.pdf)
- [Paper: A Fully Progressive Approach to Single-Image Super Resolution (ETH)](http://igl.ethz.ch/projects/prosr/prosr-cvprw-2018-wang-et-al.pdf)
- [Paper: Generative Adversarial Networks (Montereal)](https://arxiv.org/pdf/1406.2661.pdf)

## References
Implementation inspired by EDSR code (https://github.com/thstkdgus35/EDSR-PyTorch).

## Meeting Notes
### 11.02.2019
- "Auto-Encoder with visual encoding"
- starting with image domain (kyoung mu lee)
--> reimplementation
--> intermediate scales
- previous CVL project: Dario Fuerli
- extension to video domain by RNN

## To-Do Lists
### Biwi Clusters
- [x] Access Biwi clusters and do simple calculation (prime numbers)
- [x] Install CUDA (https://git.ee.ethz.ch/baumgach/biwi_tensorflow_setup_instructions/tree/master)
- [x] Install and execute torch training on cluster (https://git.ee.ethz.ch/baumgach/biwi_tensorflow_setup_instructions/tree/master)
- [x] Install specific torch version as specified in BIWI wiki (Biwi wiki)
### Knowledgebase
- [x] Read papers about image super resolution in general
- [x] Read papers about video super resolution in general
- [x] RNN and GAN training in pytorch tutorials
- [x] Read papers about task aware image superresolution
### Implementation of task-aware image downscaling
- [x] Build image processing, training pipeline and network architecture (downscaling for
I_guidance bicubic with anti-alising, cropping to factor of 2, normalization, 6 patches of
96 × 96 HR sub images each coming from different HR image --> mini-batch, Adam Optimizer,
guidance and SR L1 losses, inverse pixel shuffeling module incl. testing, resblock module,
general network architecture)
- [x] Restructuring project to be general use (yaml -> input arguments, "intelligent" checkpoints,
automated saving and easy loading of previous training iterations, block-loss-function, etc.)
- [x] Test implementation using MNIST dataset (errors: no denormalization for saving,
downscaling did not preserve input pixel intensity range, GPU training --> custom dataloader,
num_workers=0 for test))
- [x] Training of TAD network on DIV2K dataset for scale=2 on small set (overfitting)
--> fix wrongly colored SR images bug (renormalization to [0,1], image saving integer division)
--> fix dark, one-channel-only SR images bug (discretization in fine-tuning only)
- [x] Loss graph in logarithmic and linear scale
- [x] Training of TAD network on whole DIV2K dataset
- [x] Trainer generalizen (HR, LR print dependent on self.ckp.log.shape[-1] and descriptions,
which depends on self.args.model_type argument)
- [x] Testing framwork for multiple datasets at the end of training with several dataset
(input argument, Set5, Set14, B100, Urban100, DIV2K) and listing several information
(for several scales: PSNR -> best, second best; runtime)
- [x] Extreme image downscaling (save SHR images next to bicubic downsampled image)
