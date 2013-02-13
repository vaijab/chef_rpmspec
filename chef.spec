%global gem_name chef
%global rubyabi 1.9.1

%global chef_confdir %{_sysconfdir}/chef
%global chef_home %{_sharedstatedir}/chef
%global chef_logdir %{_localstatedir}/log/chef
%global chef_rundir /run/chef

Summary: A systems integration framework 
Name: %{gem_name}
Version: 11.2.0
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://wiki.opscode.com/display/chef

Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: client.rb
Source2: chef-client.service
Source3: chef-client.logrotate

Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: rubygem(mixlib-config) >= 1.1.2
Requires: rubygem(mixlib-cli) => 1.3.0
Requires: rubygem(mixlib-cli) < 1.4
Requires: rubygem(mixlib-log) >= 1.3.0
Requires: rubygem(mixlib-authentication) >= 1.3.0
Requires: rubygem(mixlib-shellout) 
Requires: rubygem(ohai) >= 0.6.0
Requires: rubygem(rest-client) >= 1.0.4
Requires: rubygem(rest-client) < 1.7.0
Requires: rubygem(json) >= 1.4.4
Requires: rubygem(json) => 1.7.6
Requires: rubygem(json) < 1.8
Requires: rubygem(yajl-ruby) => 1.1
Requires: rubygem(yajl-ruby) < 2
Requires: rubygem(net-ssh) => 2.6
Requires: rubygem(net-ssh) < 3
Requires: rubygem(net-ssh-multi) => 1.1
Requires: rubygem(net-ssh-multi) < 1.2
Requires: rubygem(highline) >= 1.6.9
Requires: rubygem(erubis) 

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildArch: noarch
Provides: %{gem_name} = %{version}


%description
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --rdoc --ri --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}


%build


%install
install -p -d %{buildroot}%{gem_dir}
install -p -d %{buildroot}%{_bindir}
install -p -d %{buildroot}%{_mandir}
install -p -d %{buildroot}%{gem_docdir}/html
install -p -d %{buildroot}%{_unitdir}

install -p -d -m 0755 %{buildroot}%{chef_confdir}
install -p -d -m 0750 %{buildroot}%{chef_home}
install -p -d -m 0750 %{buildroot}%{chef_logdir}
install -p -d -m 0755 %{buildroot}%{chef_rundir}

install -p -m 0644 %{SOURCE1} %{buildroot}%{chef_confdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
install -p -D -m 0644 %{SOURCE3} \
                      %{buildroot}%{_sysconfdir}/logrotate.d/chef-client

cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}
cp -a .%{_bindir}/*  %{buildroot}%{_bindir}
cp -a %{buildroot}%{gem_instdir}/distro/common/man/* \
      %{buildroot}%{_mandir}
cp -a %{buildroot}%{gem_instdir}/distro/common/html/* \
      %{buildroot}%{gem_docdir}/html


#%%check
# TODO


%files
%dir %{chef_confdir}
%dir %{chef_home}
%dir %{chef_logdir}
%dir %{chef_rundir}

%config(noreplace) %{chef_confdir}/client.rb
%config(noreplace) %{_sysconfdir}/logrotate.d/chef-client
%{_unitdir}/chef-client.service

%dir %{gem_instdir}
%{_bindir}/chef-client
%{_bindir}/chef-solo
%{_bindir}/knife
%{_bindir}/chef-shell
%{_bindir}/shef
%{_bindir}/chef-apply
%{gem_instdir}/bin
%{gem_libdir}
%{gem_spec}
%{_mandir}/man1/knife*.1.gz
%{_mandir}/man1/chef-*
%{_mandir}/man8/chef-*
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/distro


%files doc
%{gem_docdir}
%{gem_instdir}/spec
%{gem_instdir}/tasks
%{gem_instdir}/Rakefile
%{gem_instdir}/CONTRIBUTING.md


%post
%systemd_post chef-client.service


%preun
%systemd_preun chef-client.service


%postun
%systemd_postun_with_restart chef-client.service


%changelog
* Wed Feb 13 2013 Vaidas Jablonskis <jablonskis@gmail.com> - 11.2.0-1
- Initial package
