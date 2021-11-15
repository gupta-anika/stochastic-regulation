# stochastic-regulation
Code for the manuscript "Inferring gene regulation from stochastic transcriptional variation across single cells at steady-state".

There are several parts:
1) Code related to the transcriptional bursting and gene regulation simulations (the simulator itself and code for running the simulator).
2) Code related to analyzing the simulated data generated from variations of (1) (depending on the parameter values and number of iteratins run. This notebook produces all output related to the manuscript's figures 1-3 and associated supplementary figures.
3) Code related to processing the time-resolved scRNA-seq data from raw sequencing reads to genes X cells matrices.
4) Code related to processing the genes X cells count matrices to get Spearman rho estimates of gene:gene covariation.
5) Code related to the two orthogonal checks: ChIP-seq and Perturb-seq.

With the exception of the K562 time-resolved scRNA-seq data that we introduce in figure 4 (GEO accession number: XX), all data used in the paper are either publicly available (references cited in the text) or can be generated with the simulator.
