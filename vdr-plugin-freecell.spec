
%define plugin	freecell
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define rel	14

Summary:	VDR plugin: The well-known card game
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.magoa.net/linux/index.php?view=freecell
Source:		http://www.magoa.net/linux/files/vdr-%plugin-%version.tar.bz2
Patch0:		vdr-cardgames-0.0.2-to-gcc3.4.diff
Patch1:		vdr-freecell-0.0.2-time.patch
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This Freecell plugin is an implementation of the (well-known) card game
"Freecell" played on the On Screen Display of your Video Disk Recorder.

%prep
%setup -q -n %plugin-%version
%patch0 -p1 -b .gcc34
%patch1 -p1 -b .time

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}

%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
install -m644 freecell/* %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
ln -s %{_vdr_plugin_datadir}/%{plugin} 	%{buildroot}%{_vdr_plugin_cfgdir}/freecell

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README COPYING HISTORY CONTRIBUTORS
%{_vdr_plugin_cfgdir}/freecell
%{_vdr_plugin_datadir}/%{plugin}


