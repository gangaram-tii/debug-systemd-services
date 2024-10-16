# Audit report: network hardening using sysctl
| index | sysctl configs | retrieved value | expected value | status | references
|---|---|---|---|---|---|
| 1 | net.ipv6.conf.all.disable_ipv6  | 0 |  1  | NOK |  [cis_suse_linux](https://www.tenable.com/audits/items/CIS_SUSE_Linux_Enterprise_Server_12_v3.0.0_L2.audit:37d7eb8b0f8888f9a8d9c7db32a975a7) |
| 2 | net.ipv6.conf.default.disable_ipv6  | 0 |  1  | NOK |  [cis_suse_linux](https://www.tenable.com/audits/items/CIS_SUSE_Linux_Enterprise_Server_12_v3.0.0_L2.audit:37d7eb8b0f8888f9a8d9c7db32a975a7) |
| 3 | net.ipv6.conf.lo.disable_ipv6  | 0 |  1  | NOK |  [cis_suse_linux](https://www.tenable.com/audits/items/CIS_SUSE_Linux_Enterprise_Server_12_v3.0.0_L2.audit:37d7eb8b0f8888f9a8d9c7db32a975a7) |
| 4 | net.ipv4.tcp_syncookies  | 1 |  1  | OK |  [cis_rocky_linux_8](https://www.tenable.com/audits/items/CIS_Rocky_Linux_8_v1.0.0_L1_Server.audit:95e3320517071e79c94501bed716202c) |
| 5 | net.ipv4.tcp_syn_retries  | 6 |  2  | NOK |  [harden-network](https://www.linuxwolfpack.com/linux-harden-network.php) |
| 6 | net.ipv4.tcp_synack_retries  | 5 |  2  | NOK |  [ibm](https://www.ibm.com/docs/en/cic/1.2.2?topic=configuration-enhancing-tcp-syn-flood-attack) |
| 7 | net.ipv4.tcp_max_syn_backlog  | 4096 |  1280  | NOK |  [vmware](https://docs.vmware.com/en/vRealize-Operations/8.10/com.vmware.vcom.scg.doc/GUID-50057346-AEC5-4597-9BB7-72028DAF627C.html) |
| 8 | net.ipv4.tcp_rfc1337  | 0 |  1  | NOK |  [ietf](https://datatracker.ietf.org/doc/html/rfc1337) |
| 9 | net.ipv4.conf.all.rp_filter  | 0 |  1  | NOK |  [cis_ubuntu_linux](https://www.tenable.com/audits/items/CIS_Ubuntu_Linux_18.04_LTS_v2.2.0_L1_Server.audit:2294214a0f263f5104f684818e9e3828?x-clickref=1101lzLFvPhz&x-promotion-id=afffiliate) |
| 10 | net.ipv4.conf.default.rp_filter  | 2 |  1  | NOK |  [cis_ubuntu_linux](https://www.tenable.com/audits/items/CIS_Ubuntu_Linux_18.04_LTS_v2.2.0_L1_Server.audit:2294214a0f263f5104f684818e9e3828?x-clickref=1101lzLFvPhz&x-promotion-id=afffiliate) |
| 11 | net.ipv4.conf.all.accept_redirects  | 1 |  0  | NOK |  [cis_red_hat_linux](https://www.tenable.com/audits/items/CIS_Red_Hat_EL7_STIG_v2.0.0_L1_Server.audit:4d9e23e2c48338239a2c2fc709a2a472) |
| 12 | net.ipv4.conf.default.accept_redirects  | 1 |  0  | NOK |  [cis_red_hat_linux](https://www.tenable.com/audits/items/CIS_Red_Hat_EL7_STIG_v2.0.0_L1_Server.audit:4d9e23e2c48338239a2c2fc709a2a472) |
| 13 | net.ipv4.conf.all.secure_redirects  | 1 |  0  | NOK |  [cis_debian_linux](https://www.tenable.com/audits/items/CIS_Debian_Linux_7_v1.0.0_L1.audit:746cc306d6e4153d4cb5bddcabb5df48) |
| 14 | net.ipv4.conf.default.secure_redirects  | 1 |  0  | NOK |  [cis_debian_linux](https://www.tenable.com/audits/items/CIS_Debian_Linux_7_v1.0.0_L1.audit:746cc306d6e4153d4cb5bddcabb5df48) |
| 15 | net.ipv4.conf.all.send_redirects  | 1 |  0  | NOK |  [cis_ubuntu_linux](https://www.tenable.com/audits/items/CIS_Ubuntu_12.04_LTS_Server_v1.1.0_L1.audit:37542e36de5b697c5f63481f2e657d42) |
| 16 | net.ipv4.conf.default.send_redirects  | 1 |  0  | NOK |  [cis_ubuntu_linux](https://www.tenable.com/audits/items/CIS_Ubuntu_12.04_LTS_Server_v1.1.0_L1.audit:37542e36de5b697c5f63481f2e657d42) |
| 17 | net.ipv4.conf.all.accept_source_route  | 0 |  0  | OK |  [cis_amazon_linux](https://www.tenable.com/audits/items/CIS_Amazon_Linux_2_STIG_v1.0.0_L1.audit:c5a0b89f950db0e87902138400ad127b) |
| 18 | net.ipv4.conf.default.accept_source_route  | 0 |  0  | OK |  [cis_amazon_linux](https://www.tenable.com/audits/items/CIS_Amazon_Linux_2_STIG_v1.0.0_L1.audit:c5a0b89f950db0e87902138400ad127b) |
| 19 | net.ipv4.icmp_echo_ignore_all  | 0 |  1  | NOK |  [cis_rocky_linux](https://www.tenable.com/audits/items/CIS_Rocky_Linux_8_v1.0.0_L1_Server.audit:a82dbeb614529af0ccae791e4e56cf89) |
| 20 | net.ipv4.conf.all.log_martians  | 0 |  1  | NOK |  [cis_ubuntu_linux](https://www.tenable.com/audits/items/CIS_Ubuntu_12.04_LTS_Server_v1.1.0_L1.audit:a9bad78b00fddec116bfe989cc36180b) |
| 21 | net.ipv4.conf.default.log_martians  | 0 |  1  | NOK |  [cis_ubuntu_linux](https://www.tenable.com/audits/items/CIS_Ubuntu_12.04_LTS_Server_v1.1.0_L1.audit:a9bad78b00fddec116bfe989cc36180b) |
| 22 | net.ipv4.icmp_ignore_bogus_error_responses  | 1 |  1  | OK |  [cis_rocky_linux](https://www.tenable.com/audits/items/CIS_Rocky_Linux_8_v1.0.0_L1_Server.audit:b41b63bbd97956320d9d10a9781b8cdb) |
| 23 | kernel.unprivileged_bpf_disabled  | 2 |  1  | NOK |  [cis_bottlerocket](https://www.tenable.com/audits/items/CIS_Bottlerocket_v1.0.0_L1.audit:0b66066e10907c3a7136e75917351508) |
| 24 | net.core.bpf_jit_harden  | 0 |  2  | NOK |  [disa_stig_red_hat_linux](https://www.tenable.com/audits/items/DISA_STIG_Red_Hat_Enterprise_Linux_9_v2r1.audit:a7366b2924f4fad4cc7a247a4f72fe9b) |
| 25 | net.ipv6.conf.all.accept_redirects  | 1 |  0  | NOK |  [cis_red_hat_linux](https://www.tenable.com/audits/items/CIS_Red_Hat_EL7_STIG_v2.0.0_L1_Server.audit:4d9e23e2c48338239a2c2fc709a2a472) |
| 26 | net.ipv6.conf.default.accept_redirects  | 1 |  0  | NOK |  [cis_red_hat_linux](https://www.tenable.com/audits/items/CIS_Red_Hat_EL7_STIG_v2.0.0_L1_Server.audit:4d9e23e2c48338239a2c2fc709a2a472) |
| 27 | net.ipv6.conf.all.accept_source_route  | 0 |  0  | OK |  [cis_amazon_linux](https://www.tenable.com/audits/items/CIS_Amazon_Linux_2_STIG_v1.0.0_L1.audit:c5a0b89f950db0e87902138400ad127b) |
| 28 | net.ipv6.conf.default.accept_source_route  | 0 |  0  | OK |  [cis_amazon_linux](https://www.tenable.com/audits/items/CIS_Amazon_Linux_2_STIG_v1.0.0_L1.audit:c5a0b89f950db0e87902138400ad127b) |
| 29 | net.ipv6.conf.default.router_solicitations  | -1 |  0  | NOK |  [vmware](https://docs.vmware.com/en/vRealize-Operations/8.10/com.vmware.vcom.scg.doc/GUID-16BDA67D-914A-484C-97CA-8624F4881605.html) |
| 30 | net.ipv6.conf.default.autoconf  | 1 |  0  | NOK |  [vmware](https://docs.vmware.com/en/vRealize-Operations/8.10/com.vmware.vcom.scg.doc/GUID-37B91C4A-5E1E-4F8E-BC59-B3552BA7CDFA.html) |
| 31 | net.ipv6.conf.all.autoconf  | 1 |  0  | NOK |  [vmware](https://docs.vmware.com/en/vRealize-Operations/8.10/com.vmware.vcom.scg.doc/GUID-37B91C4A-5E1E-4F8E-BC59-B3552BA7CDFA.html) |
| 32 | net.ipv6.conf.all.accept_ra  | 1 |  0  | NOK |  [vmware](https://docs.vmware.com/en/vRealize-Operations/8.10/com.vmware.vcom.scg.doc/GUID-A0017F16-AC96-490B-B213-BAB91B5AC0DB.html) |
| 33 | net.ipv6.conf.default.accept_ra  | 1 |  0  | NOK |  [vmware](https://docs.vmware.com/en/vRealize-Operations/8.10/com.vmware.vcom.scg.doc/GUID-A0017F16-AC96-490B-B213-BAB91B5AC0DB.html) |
| 34 | net.ipv6.conf.all.max_addresses  | 16 |  1  | NOK |  [vmware](https://docs.vmware.com/en/vRealize-Operations/8.10/com.vmware.vcom.scg.doc/GUID-1CC9DE00-5282-4F0C-BFAE-238849C6F8F4.html) |
| 35 | net.ipv6.conf.default.max_addresses  | 16 |  1  | NOK |  [vmware](https://docs.vmware.com/en/vRealize-Operations/8.10/com.vmware.vcom.scg.doc/GUID-1CC9DE00-5282-4F0C-BFAE-238849C6F8F4.html) |
