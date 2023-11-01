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

* Tue Nov 02 2021 Josh Stone <jistone@redhat.com> - 1.56.1-1
- Update to Rust and Cargo 1.56.1.

* Fri Oct 29 2021 Josh Stone <jistone@redhat.com> - 1.55.0-1
- Update to Rust and Cargo 1.55.0.

* Mon Aug 02 2021 Josh Stone <jistone@redhat.com> - 1.54.0-1
- Update to Rust and Cargo 1.54.0.

* Mon Jun 21 2021 Josh Stone <jistone@redhat.com> - 1.53.0-1
- Update to Rust and Cargo 1.53.0.

* Tue May 25 2021 Josh Stone <jistone@redhat.com> - 1.52.1-1
- Update to Rust and Cargo 1.52.1.

* Mon May 24 2021 Josh Stone <jistone@redhat.com> - 1.51.0-1
- Update to Rust and Cargo 1.51.0.

* Mon May 24 2021 Josh Stone <jistone@redhat.com> - 1.50.0-1
- Update to Rust and Cargo 1.50.0.

* Wed Jan 13 2021 Josh Stone <jistone@redhat.com> - 1.49.0-1
- Update to Rust and Cargo 1.49.0.

* Tue Jan 12 2021 Josh Stone <jistone@redhat.com> - 1.48.0-1
- Update to Rust and Cargo 1.48.0.

* Thu Oct 22 2020 Josh Stone <jistone@redhat.com> - 1.47.0-1
- Update to Rust and Cargo 1.47.0.

* Wed Oct 14 2020 Josh Stone <jistone@redhat.com> - 1.46.0-1
- Update to Rust and Cargo 1.46.0.

* Tue Aug 04 2020 Josh Stone <jistone@redhat.com> - 1.45.2-1
- Update to Rust and Cargo 1.45.2.

* Thu Jul 16 2020 Josh Stone <jistone@redhat.com> - 1.45.0-1
- Update to Rust and Cargo 1.45.0.

* Tue Jul 14 2020 Josh Stone <jistone@redhat.com> - 1.44.1-1
- Update to Rust and Cargo 1.44.1.

* Tue May 26 2020 Josh Stone <jistone@redhat.com> - 1.43.1-1
- Update to Rust and Cargo 1.43.1.

* Thu Apr 23 2020 Josh Stone <jistone@redhat.com> - 1.43.0-1
- Update to Rust and Cargo 1.43.0.

* Thu Apr 02 2020 Josh Stone <jistone@redhat.com> - 1.42.0-1
- Update to Rust and Cargo 1.42.0.

* Fri Feb 28 2020 Josh Stone <jistone@redhat.com> - 1.41.1-1
- Update to Rust and Cargo 1.41.1.

* Thu Jan 30 2020 Josh Stone <jistone@redhat.com> - 1.41.0-2
- Use --no-track in cargo_install

* Thu Jan 30 2020 Josh Stone <jistone@redhat.com> - 1.41.0-1
- Update to Rust and Cargo 1.41.0.

* Thu Jan 16 2020 Josh Stone <jistone@redhat.com> - 1.40.0-1
- Update to Rust and Cargo 1.40.0.

* Thu Nov 07 2019 Josh Stone <jistone@redhat.com> - 1.39.0-1
- Update to Rust and Cargo 1.39.0.

* Thu Sep 26 2019 Josh Stone <jistone@redhat.com> - 1.38.0-1
- Update to Rust and Cargo 1.38.0.

* Thu Aug 15 2019 Josh Stone <jistone@redhat.com> - 1.37.0-1
- Update to Rust and Cargo 1.37.0.

* Mon Jul 15 2019 Josh Stone <jistone@redhat.com> - 1.36.0-1
- Update to Rust and Cargo 1.36.0.

* Fri May 24 2019 Josh Stone <jistone@redhat.com> - 1.35.0-1
- Update to Rust and Cargo 1.35.0.

* Tue May 14 2019 Josh Stone <jistone@redhat.com> - 1.34.2-1
- Update to 1.34.2 -- fixes CVE-2019-12083.

* Thu May 09 2019 Josh Stone <jistone@redhat.com> - 1.34.1-1
- Update to Rust and Cargo 1.34.1.

* Thu Apr 11 2019 Josh Stone <jistone@redhat.com> - 1.34.0-1
- Update to Rust and Cargo 1.34.0.

* Wed Apr 10 2019 Josh Stone <jistone@redhat.com> - 1.33.0-1
- Update to Rust and Cargo 1.33.0.

* Tue Apr 09 2019 Josh Stone <jistone@redhat.com> - 1.32.0-1
- Update to Rust and Cargo 1.32.0.

* Thu Dec 13 2018 Josh Stone <jistone@redhat.com> - 1.31.0-1
- Update to Rust and Cargo 1.31.0.

* Wed Dec 12 2018 Josh Stone <jistone@redhat.com> - 1.30.1-1
- Update to Rust 1.30.1 and Cargo 1.30.0.

* Tue Nov 06 2018 Josh Stone <jistone@redhat.com> - 1.29.2-1
- Update to Rust 1.29.2 and Cargo 1.29.0.

* Thu Nov 01 2018 Josh Stone <jistone@redhat.com> - 1.28.0-1
- Update to Rust and Cargo 1.28.0.

* Thu Nov 01 2018 Josh Stone <jistone@redhat.com> - 1.27.2-1
- Update to Rust 1.27.2 and Cargo 1.27.0.

* Thu Oct 04 2018 Josh Stone <jistone@redhat.com> - 1.26.2-4
- Drop SCL macros. (rhbz1635067)

* Fri Aug 03 2018 Vít Ondruch <vondruch@redhat.com> - 1.26.2-3
- scl_files hack is not needed anymore.

* Tue Jul 31 2018 Josh Stone <jistone@redhat.com> - 1.26.2-2
- Rename to rust-toolset-1.26 for modules.

* Mon Jun 04 2018 Josh Stone <jistone@redhat.com> - 1.26.2-1
- Update to Rust 1.26.2

* Thu May 31 2018 Josh Stone <jistone@redhat.com> - 1.26.1-1
- Update to Rust 1.26.1

* Tue May 22 2018 Josh Stone <jistone@redhat.com> - 1.26.0-1
- Update to Rust and Cargo 1.26.0

* Tue May 08 2018 Josh Stone <jistone@redhat.com> - 1.25.0-2
- Add more macros to the runtime subpackage

* Tue Apr 03 2018 Josh Stone <jistone@redhat.com> - 1.25.0-1
- Update to rust-1.25.0 and cargo-0.26.0

* Thu Feb 22 2018 Josh Stone <jistone@redhat.com> - 1.24.0-1
- Update to rust-1.24.0 and cargo-0.25.0

* Tue Feb 20 2018 Josh Stone <jistone@redhat.com> - 1.23.0-2
- Add the %%enable_rusttoolset7 macro to the runtime subpackage.

* Tue Jan 16 2018 Josh Stone <jistone@redhat.com> - 1.23.0-1
- Initial rust-toolset on el8
