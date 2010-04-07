Name: task-sound-studio
Version: 0.3
Release: %mkrel 1
Summary: Metapackage for Computer-Aided Music 
Group: Sound
License: GPLv2+

## By group organization, each have suggests and requires
#########################################################

# Jack Family
Suggests: ac3jack
Suggests: ffado
Suggests: jackeq
Requires: jackasyn
Suggests: jackbeat
Requires: jackit
Requires: jackit-example-clients
Suggests: jack-rack
Suggests: ladish
Requires: laditools
Suggests: qjacktl

# Midibase, soundfonts and tablatures
Requires: fluid-soundfont-common
Requires: fluid-soundfont-gm
Requires: fluid-soundfont-gs
Suggests: ktabedit
Requires: lilypond
Suggests: mscore
Requires: soundfont-utils
Requires: timidity-patch-gravis
Requires: timidity-patch-freepat
Requires: TiMidity++
Suggests: TiMidity++-interfaces-extra
Suggests: qsynth

# Ladspa, dssi, LV2 and plugins
Suggests: a2jmidid
Requires: blop
Requires: bse-alsa
Requires: calf
Requires: caps
Requires: cmt
Requires: dssi
Suggests: EXEf
Requires: fluidsynth-dssi
Requires: fluidsynth
Requires: hexter
Suggests: jconv
Requires: ladspa
Requires: ladspa-quitte-dsp
Requires: ll-plugins
Suggests: ll-plugins-gui
Requires: lv2core
Requires: mcp-plugins
Requires: nekobee
Requires: pvc
Requires: pvoc
Requires: rev-plugins
Requires: slv2
Requires: swh-lv2
Requires: swh-plugins
Requires: tap-plugins
Requires: tritonus-fluidsynth
Requires: whysynth
Requires: wsynth-dssi
Requires: xsynth-dssi

# Synthes
Suggests: ams
Suggests: bristol
Suggests: bristol-aks
Suggests: bristol-arp2600
Suggests: bristol-axxe
Suggests: bristol-b3
Suggests: bristol-dx
Suggests: bristol-explorer
Suggests: bristol-hammond
Suggests: bristol-juno
Suggests: bristol-memory
Suggests: bristol-mini
Suggests: bristol-mixer
Suggests: bristol-mono
Suggests: bristol-obx
Suggests: bristol-obxa
Suggests: bristol-odyssey
Suggests: bristol-poly
Suggests: bristol-prophet
Suggests: bristol-rhodes
Suggests: bristol-rhodesbass
Suggests: bristol-roadrunner
Suggests: bristol-solina
Suggests: bristol-vox
Suggests: kmid2
Suggests: qsampler
Suggests: qmidiroute
Suggests: swami
Suggests: vmpk
Requires: yoshimi
Suggests: zynaddsubfx

# Players, and simple recorders
Requires: jack_capture
Suggests: timemachine
Requires: uade
Requires: upse
Requires: xmp

# DAW - SAW and Sequencers
Suggests: ardour
Suggests: audacity
Suggests: dino
Suggests: jokosher
Suggests: lmms
Suggests: qtractor
Suggests: rezound
Suggests: rosegarden
Suggests: seq24

# Guitars
Suggests: ecamegapedal
Suggests: gnuitar
Suggests: guitarix
Suggests: jc_gui
Suggests: rakarrack
Suggests: tuxguitar

# RythmBox, mix and scratch
Suggests: hydrogen
Suggests: mixxx
Suggests: terminatorx
	    
# Audio Developpers
Suggests: faust
Suggests: pd
		
# KernelRT
Suggests: kernel-rt-latest
Suggests: kernel-rt-devel-latest
Suggests: rtirq

# Media players
Suggest: xine-jack
Requires: mplayer
Suggests: vlc-plugin-jack

# Desktop-specific configuration files
Suggests: lilypond-kde4

#########################################################

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package which install everything
needed to have a complete sound processing studio.
- Mandriva for Digital Audio Workstation -


%files
