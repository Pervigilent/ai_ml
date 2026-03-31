# AI-ML

This is an educational repository that teaches artificial intelligence and machine learning through several examples:

1. Introduction
2. AI acceleration
3. Protein folding
4. Gene splicing
5. Mixed signal design and VLSI
6. Computational lithography

## Introduction

This module introduces artificial intelligence and machine learning.

## AI Acceleration

CUDA has emerged as the preeminent platform for AI acceleration. In this module we will focus on alternatives to CUDA, but also look briefly at CUDA itself. We will focus heavily on both hardware and software. Our primary interest is in SYCL and Intel oneAPI for Intel GPUs. Secondarily, we will look at AMDs ROCm and HIP. We will look at the graphics pipeline and ask how both OpenGL and Vulkan might be leveraged as an alternative to these acceleration libraries. Finally, we will briefly touch on ZLUDA as an open-source drop-in replacement for CUDA.

## Protein Folding

There are two goals in this project. The first is to generate a neural network that can predict protein folding given a sequence of amino acids similar to AlphaFold. The second task is to generate a neural network which can create de novo proteins such as RFdiffusion. The goal in this case would be to create a protein with a specified binding site.

## Gene Splicing

Splicing is the transformation of pre-mRNA into mRNA by the removal of introns. A deep-learning model similar to SpliceAI will be constructed to predict introns. This will be part of a larger suite of tools which identify numerous genetic sequences. Ideally the library will identify all known regulatory elements of transcription in both human and mice. This will be a complete computer of genetic expression in a library that can recreate the transcriptome.

## Mixed Signal Design and VLSI

In this case, the goal is to improve open source tools for generating mixed signal circuits and VLSI design.

## Computational Lithography

The goal in this instance is to create an inverse lithography model and implement a neural network capable of generating output of part of the model in order to reduce computation time.

