Name: task-sound-studio
Version: 0.3
Release: %mkrel 3
Summary: Meta package for Sound Studio and Music Production
Group: Sound
License: GPLv2+

## Packages organized by groups and divided in Suggests and Requires
####################################################################

# Jack engine-related
Requires: jackit
Requires: jackit-example-clients
Requires: laditools
Requires: qjackctl
Suggests: ladish
Suggests: ac3jack
Suggests: ffado

# Bridges to other sound systems
Requires: tritonus-fluidsynth
Requires: jackasyn
Suggests: bse-alsa

# Basic MIDI utilities
Suggests: a2jmidid
Suggests: vmpk
Suggests: qmidiroute
Suggests: qmidiarp

# Soundfont-related
Requires: fluid-soundfont-common
Requires: fluid-soundfont-gm
Requires: fluid-soundfont-gs
Requires: soundfont-utils
Suggests: swami
Requires: timidity-patch-gravis
Requires: timidity-patch-freepats
Requires: TiMidity++
Suggests: TiMidity++-interfaces-extra

# Score and tablature editors
Requires: lilypond
Suggests: nted
Suggests: ktabedit
Suggests: mscore

# Ladspa system and effect plugins
Requires: ladspa
Requires: ladspa-quitte-dsp
Requires: mcp-plugins
Requires: pvc
Requires: pvoc
Requires: rev-plugins
Requires: swh-plugins
Requires: tap-plugins
Requires: cmt
Requires: blop
Requires: caps

# LV2 system and plugins
Requires: lv2core
Requires: slv2
Requires: swh-lv2
Requires: ll-plugins
Requires: calf
Requires: ll-plugins-gui
Requires: invada-studio-plugins-lv2

# DSSI system and synth plugins
Requires: dssi
Requires: fluidsynth-dssi
Requires: hexter
Requires: nekobee
Requires: whysynth
Requires: wsynth-dssi
Requires: xsynth-dssi

# Standalone Synths
Requires: fluidsynth
Suggests: yoshimi
Suggests: qsynth
Suggests: ams
Suggests: phasex
Suggests: bristol
Suggests: bristol-arp2600
Suggests: bristol-axxe
Suggests: bristol-b3
Suggests: bristol-dx
Suggests: bristol-explorer
Suggests: bristol-juno
Suggests: bristol-memory
Suggests: bristol-mini
Suggests: bristol-mono
Suggests: bristol-obx
Suggests: bristol-obxa
Suggests: bristol-odyssey
Suggests: bristol-poly800
Suggests: bristol-prophet
Suggests: bristol-rhodes
Suggests: bristol-rhodesbass
Suggests: bristol-roadrunner
Suggests: bristol-solina
Suggests: bristol-vox
Suggests: qsampler
Suggests: zynaddsubfx

# Simple audio recorders and players
Suggests: jack_capture
Suggests: timemachine
Suggests: qarecord
Suggests: uade
Suggests: upse
Suggests: xmp

# DAW - SAW and sequencers
Suggests: ardour
Suggests: audacity
Suggests: dino
Suggests: jokosher
Suggests: lmms
Suggests: qtractor
Suggests: rezound
Suggests: rosegarden
Suggests: seq24
Suggests: jackbeat
Suggests: beast
Suggests: kmid2

# Effect racks
Suggests: jack-rack
Suggests: zynjacku
Suggests: ecamegapedal
Suggests: gnuitar
Suggests: guitarix
Suggests: jc_gui
Suggests: jconvolver
Suggests: rakarrack
Suggests: tuxguitar
Suggests: jackeq

# Drum machines, live audio tools
Suggests: hydrogen
Suggests: mixxx
Suggests: terminatorx
Suggests: sooperlooper
        
# Audio developpers
Suggests: faust
Suggests: pd
Suggests: drumstick
        
# KernelRT
Suggests: kernel-rt-latest
Suggests: kernel-rt-devel-latest
Suggests: rtirq

# Media players
Suggests: xine-jack
Suggests: mplayer
Suggests: vlc-plugin-jack

# Desktop-specific configuration files
Suggests: lilypond-kde4

#########################################################

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package which installs everything
needed to have a complete sound creation and processing studio.
- Mandriva for Digital Audio Workstations -


%files
