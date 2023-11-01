Summary:        Package that installs rust-toolset
Name:           rust-toolset
Version:        1.58.1
Release:        1%{?dist}
License:        ASL 2.0 or MIT

Source0:        macros.%{name}

Requires:       rust = %{version}
Requires:       cargo = %{version}

%description
This is the main package for rust-toolset.

%install

# This allows users to build packages using Rust Toolset.
%{__install} -D -m 644 %{S:0} %{buildroot}%{rpmmacrodir}/macros.%{name}

%files
%{rpmmacrodir}/macros.%{name}

%changelog
* Thu Jan 20 2022 Josh Stone <jistone@redhat.com> - 1.58.1-1
- Update to Rust and Cargo 1.58.1.

* Thu Jan 13 2022 Josh Stone <jistone@redhat.com> - 1.58.0-1
- Update to Rust and Cargo 1.58.0.

* Wed Dec 15 2021 Josh Stone <jistone@redhat.com> - 1.57.0-1
- Update to Rust and Cargo 1.57.0.

* Thu Nov 04 2021 Josh Stone <jistone@redhat.com> - 1.56.1-1
- Update to Rust and Cargo 1.56.1.

* Fri Oct 29 2021 Josh Stone <jistone@redhat.com> - 1.55.0-1
- Update to Rust and Cargo 1.55.0.

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.54.0-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Aug 04 2021 Josh Stone <jistone@redhat.com> - 1.54.0-1
- Update to Rust and Cargo 1.54.0.

* Tue Jun 22 2021 Josh Stone <jistone@redhat.com> - 1.53.0-1
- Update to Rust and Cargo 1.53.0.

* Thu May 13 2021 Josh Stone <jistone@redhat.com> - 1.52.1-1
- Update to Rust and Cargo 1.52.1.

* Wed Apr 28 2021 Josh Stone <jistone@redhat.com> - 1.51.0-1
- Update to Rust and Cargo 1.51.0.

* Tue Apr 27 2021 Josh Stone <jistone@redhat.com> - 1.50.0-1
- Update to Rust and Cargo 1.50.0.

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.49.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 06 2021 Josh Stone <jistone@redhat.com> - 1.49.0-1
- Update to Rust and Cargo 1.49.0.

* Thu Dec 10 2020 Josh Stone <jistone@redhat.com> - 1.48.0-1
- Update to Rust and Cargo 1.48.0.

* Tue Nov 10 2020 Josh Stone <jistone@redhat.com> - 1.47.0-1
- Initial rust-toolset on el9
