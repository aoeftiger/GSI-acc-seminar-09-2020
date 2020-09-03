# Simulation of Intense Beams in Synchrotrons

## ... a story of resonances and instabilities.

### a notebook talk by [Adrian Oeftiger](http://oeftiger.net/)

Find here the announcement of the [GSI Accelerator Seminar on 3 September 2020](https://indico.gsi.de/event/10059/).
See also [rendered talk slides on github](https://aoeftiger.github.io/GSI-acc-seminar-09-2020/).

## Abstract

This introduction on collective beam dynamics focuses on high-intensity effects in synchrotrons like SIS18 or SIS100. The charged particles in the beam interact (a.) with the beam self-fields they produce and (b.) with the induced currents in the vacuum pipe. This interaction leads to corresponding collective effects, such as "space charge" (self-field interaction) or "beam coupling impedance" (interaction with the surroundings). The beam can become resonantly excited or is even driven into exponential instabilities over many revolutions in the circular accelerator. These effects potentially limit the performance, they scale with the number of particles in the beam: their understanding (and mitigation) is crucial to safely operate synchrotrons like SIS100 at highest beam intensities.

We dive into the world of these collective effects in beam physics, exploring their mechanisms and how they can lead to beam loss. During the talk, we also look behind the scenes on how to numerically model such long-term effects, in particular employing high-performance techniques such as GPU computing.

## How to run this notebook at GSI:

Connect to the GSI high-performance computing cluster `virgo.hpc` (with port forwarding), load the accelerator physics environment and run the jupyter notebook server:

```
$ ssh virgo.hpc -L 8888:localhost:8888
$ singularity exec --bind /cvmfs \
    /cvmfs/vae.gsi.de/centos7/containers/user_container-develop.sif \
    bash -l
Singularity> cd /cvmfs/aph.gsi.de/
Singularity> source modules.sh
Singularity> module load aph_all
Singularity> cd
Singularity> git clone https://github.com/aoeftiger/GSI-acc-seminar-09-2020
Singularity> cd GSI-acc-seminar-09-2020
Singularity> jupyter notebook --no-browser --port=8888
```

... and you're ready to open your local browser and type in `localhost:8888`, where you open this notebook.

## How to run this notebook on your individual workstation:

Install [`PyHEADTAIL`](https://pypi.org/project/PyHEADTAIL/), [`cpymad`](https://pypi.org/project/cpymad/), [`PySixTrack`](https://github.com/SixTrack/pysixtrack/) and [`SixTrackLib`](https://github.com/SixTrack/sixtracklib) in your `python3` environment and run this `jupyter notebook`.
