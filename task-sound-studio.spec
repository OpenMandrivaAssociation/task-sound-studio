Name:		task-sound-studio
Version:	0.1
Release:	%mkrel 1
Summary:	Metapackage for sound processing
Group:		Sound
License:	GPLv2+
Suggests:	kernel-rt-latest
Suggests:	qjackctl 
Suggests:	muse
Suggests:	rosegarden
Suggests:	timidity++
Suggests:	xmp
Suggests:	lilypond
Suggests:	ardour
Suggests:	audacity
Suggests:	jokosher
Suggests:	gnuitar
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package which install everything
needed to have a complete sound processing studio.

%files
