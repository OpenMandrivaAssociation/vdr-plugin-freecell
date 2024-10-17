%define plugin	freecell

Summary:	VDR plugin: The well-known card game
Name:		vdr-plugin-%plugin
Version:	0.0.2
Release:	22
Group:		Video
License:	GPL+
URL:		https://www.magoa.net/linux/index.php?view=freecell
Source:		http://www.magoa.net/linux/files/vdr-%plugin-%{version}.tar.bz2
Patch0:		vdr-cardgames-0.0.2-to-gcc3.4.diff
Patch1:		vdr-freecell-0.0.2-time.patch
Patch2:		93_freecell-0.0.2-1.5.4.dpatch
Patch3:		freecell-0.0.2-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This Freecell plugin is an implementation of the (well-known) card game
"Freecell" played on the On Screen Display of your Video Disk Recorder.

%prep
%setup -q -n %plugin-%{version}
%patch0 -p1 -b .gcc34
%patch1 -p1 -b .time
%patch2 -p1
%patch3 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_datadir}/%{plugin}
install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}
install -m644 freecell/* %{buildroot}%{vdr_plugin_datadir}/%{plugin}
ln -s %{vdr_plugin_datadir}/%{plugin} 	%{buildroot}%{vdr_plugin_cfgdir}/freecell


%files -f %plugin.vdr
%doc README COPYING HISTORY CONTRIBUTORS
%{vdr_plugin_cfgdir}/freecell
%{vdr_plugin_datadir}/%{plugin}




