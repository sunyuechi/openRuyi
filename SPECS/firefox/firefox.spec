# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: Maybe we need to remove this for licensing reasons
%bcond fdk_aac 0

# TODO: Official branding is tricky
# https://www.mozilla.org/en-US/foundation/trademarks/policy/
%bcond official_branding 0

Name:           firefox
Version:        154.0
Release:        %autorelease
Summary:        Free web browser backed by Mozilla
License:        MPL-2.0
URL:            https://www.firefox.com
# https://bugzilla.mozilla.org/show_bug.cgi?id=1863519
VCS:            git:https://github.com/mozilla-firefox/firefox
#!RemoteAsset:  sha256:36cec5b3688a60f78a6d20dcaee15b598f84e03c66f6587056aead6cb498b99a
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/source/%{name}-%{version}.source.tar.xz
# We need the language packs
#!RemoteAsset:  sha256:cac1095e82bd25746b1ec9415d1d21e3f3c632dd3c056bf59e508e5ab8e7e8f3
Source1:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ach.xpi
#!RemoteAsset:  sha256:96a8c6d851c797bf2e4428643470bb1a6c3ac727f334d0d7f4a11fae3a4f96f2
Source2:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/af.xpi
#!RemoteAsset:  sha256:da88b6f4a641cbdb83be3d265c38173bf76e49adff1d84dc183f60ce025ef746
Source3:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/an.xpi
#!RemoteAsset:  sha256:31e2cbe67123a3cb514fd5bbfc6ea94f15103dde8e382de9f23b9f4fb1f2cd4f
Source4:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ar.xpi
#!RemoteAsset:  sha256:bf0f0931c86460bc2728edcac0b18c29841838367af6e6225a0d849cc4858d16
Source5:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ast.xpi
#!RemoteAsset:  sha256:18818ded623dc0b0c63af0a70bb22d4de3803bcdbf1812db47502c725a22ae8c
Source6:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/az.xpi
#!RemoteAsset:  sha256:dbad2dd2d0c6f59912cdd02424b694444296bd0e969ce4c398f3c22a7532b0ca
Source7:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/be.xpi
#!RemoteAsset:  sha256:37d2e755ff0dfc7a62e623badf6f2c27e03ecec055f169ec4796c2b361a391ed
Source8:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bg.xpi
#!RemoteAsset:  sha256:35c059aaffadbd4a7d1823392f0deef94d0ebeeb943446215b80887d7886ee51
Source9:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bn.xpi
#!RemoteAsset:  sha256:25949fac86780c856018e9fafbefa16af27b7c1dc7dccf13abf47ccc7d63d1c6
Source10:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/br.xpi
#!RemoteAsset:  sha256:b62f9871c6531da3fec847335a31b40bef52f6268d692e001291daf76a095964
Source11:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bs.xpi
#!RemoteAsset:  sha256:de669503670af8dbe8dfe31dd87b41a03f7ffe41f4b6cfcaa83c37b78922f81b
Source12:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca-valencia.xpi
#!RemoteAsset:  sha256:a360f442864bfd6a79466e01db0efaf034b18346fefc37d86da9935e9f98c746
Source13:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca.xpi
#!RemoteAsset:  sha256:94d6b0c2a84ab120eb949ada17222fa794b94f9350b684c27bf65896b5df6e7b
Source14:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cak.xpi
#!RemoteAsset:  sha256:6a94ac89163e88e5c653173e5f83aed25b2eebdb5c8ed8435c40a782d25e94a7
Source15:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cs.xpi
#!RemoteAsset:  sha256:69893dca1666987b11bb14ca6690415628e4b917a0cae1a35007140e32ae636c
Source16:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cy.xpi
#!RemoteAsset:  sha256:9b57b8e0a1abaa3b8a873e7a377fa7310aa0195980810ccbe53be17a3cc47f9a
Source17:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/da.xpi
#!RemoteAsset:  sha256:9e192a4f283fdae1871a910f1289f868ac92a40f25be33e8251d661339f444e7
Source18:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/de.xpi
#!RemoteAsset:  sha256:9ccdef7cea6212efc2f98c46c7360d16b203ac1f933a94f33fcde99e2510bf48
Source19:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/dsb.xpi
#!RemoteAsset:  sha256:f5e116c803b118d4de8f398b4cd52916fd98f3e9ff2951f6b3ac232efdd94591
Source20:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/el.xpi
#!RemoteAsset:  sha256:78d5b8fdb2c9813397fe9a7edadf7f22e9dd6961fa593088583f691ed2326d98
Source21:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-CA.xpi
#!RemoteAsset:  sha256:5bdb43a86d8f6bdbb91905d228595511b542cf5851697b6200455e883c9f1ff0
Source22:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-GB.xpi
#!RemoteAsset:  sha256:1ac85a7a0d7f9608e7819efe735dcbcd560746da6751632863e2c5eb67873a37
Source23:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-US.xpi
#!RemoteAsset:  sha256:0d945b5d8b4444567d989e17c066b959d12371f5235561da7928654e79ba9751
Source24:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eo.xpi
#!RemoteAsset:  sha256:3aa87f96d9e52e03d1185edb1f2edc9b5b93e2a797627ae0d150cf051d026a9a
Source25:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-AR.xpi
#!RemoteAsset:  sha256:6551228ad60db5ebadb71ba726a6c082030262b055eb4bdb26f45ed4921786a8
Source26:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-CL.xpi
#!RemoteAsset:  sha256:6e7a6932cc87701e871443ea4f10b0ccf4c4e0de9cf65ab48292767d7dcb4f4e
Source27:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-ES.xpi
#!RemoteAsset:  sha256:2655d4e0b680b3f994d9087f4bdfae6ba21fb5d7f0a8bc3ba17bc2315e203ccd
Source28:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-MX.xpi
#!RemoteAsset:  sha256:c48718a5dc3eb213f4c2e45857934a25d3830188b55b5d363acaeef042db7806
Source29:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/et.xpi
#!RemoteAsset:  sha256:dae462f0aee5d8470b78eb1e6bf28a0d1a763dbc53a8c43b11b83e6efff061ab
Source30:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eu.xpi
#!RemoteAsset:  sha256:cc81edd70be35ee9fcabc890b99b1bfe0a66b5da60fd51bebe47008452846815
Source31:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fa.xpi
#!RemoteAsset:  sha256:6782565463ceb07389099d0ebc8342f5aa9d8a856e5d7d8945608b28cc2efa6c
Source32:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ff.xpi
#!RemoteAsset:  sha256:d124f6ecb31bc8a16926744991fd8d7e7fbbbd96d8d9921442c5d3a5bf3189b0
Source33:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fi.xpi
#!RemoteAsset:  sha256:074f1f442fa0ef4b091e3b1adbeb7b32e4a2062b6638698f1f060bbf6384ba4c
Source34:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fr.xpi
#!RemoteAsset:  sha256:994680b58c22a624536d44c6bc0e13db99b28f366dbdf0b0270cb7a736782671
Source35:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fur.xpi
#!RemoteAsset:  sha256:407f0b9f2696d7173e5d23a420c0b88c48c3ae7aedfa99db04558f70b86f5970
Source36:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fy-NL.xpi
#!RemoteAsset:  sha256:64c043269906d0505a62e7e440d066c42191f92de14936958af8922f4e0f80b2
Source37:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ga-IE.xpi
#!RemoteAsset:  sha256:b1a0e07b909f5a2bc2ec368f18e5b71e32a5c102a6da81b2d22e64bb85b28505
Source38:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gd.xpi
#!RemoteAsset:  sha256:d27b5b4a7392030c2acc2eee6a6962d9f6a469e0393e256ed7e38ec5f7ca9209
Source39:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gl.xpi
#!RemoteAsset:  sha256:86a05f0caf32203e81b589d814c1bdadc33d1079b45847a90b0b3cd23409d1fb
Source40:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gn.xpi
#!RemoteAsset:  sha256:e08a35b52c6e52569d59483935bfa31d808cb7463b021fec57f9f0a5101cf48f
Source41:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gu-IN.xpi
#!RemoteAsset:  sha256:256917afeb68ec6ea43e0135792f5c67d34aa6c2bbf0fda7de04a77c3c634fb5
Source42:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/he.xpi
#!RemoteAsset:  sha256:4a85c214c14d5dc25c07caa8d07b1de1f5050578113fe991c4ce0ea46b3422ea
Source43:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hi-IN.xpi
#!RemoteAsset:  sha256:8b5e19ebeafa0e0b4ca400b0ed1626098041d3721f9422c0a69f91b5f9305b80
Source44:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hr.xpi
#!RemoteAsset:  sha256:6b5231405e42a9a334dd50a5cca52faa30f6671b474a0db139ac49c63b7576cb
Source45:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hsb.xpi
#!RemoteAsset:  sha256:a6a3333b985c62aa1bb13529daf6771089834947c77c673439addd3316a63ede
Source46:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hu.xpi
#!RemoteAsset:  sha256:b6eddb8dcdaca9b7deb79d561dfce169e39bcdd7adf500626f0b5988aa84d6b1
Source47:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hy-AM.xpi
#!RemoteAsset:  sha256:29f22ef0d0dbb3dbb26dcaeb3809498521211b0b22bf600e52d5cd580d0253a3
Source48:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ia.xpi
#!RemoteAsset:  sha256:7df0b8db5eb1f31ff22eb8f5b9080c071e0ba7adf2890ab135ae8c2b31ee9906
Source49:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/id.xpi
#!RemoteAsset:  sha256:16ffa6b730c8c1ffaabce97ed461c8f5c38215ff4d317ad880a721dd139b5c12
Source50:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/is.xpi
#!RemoteAsset:  sha256:e31ed2a0727a8479fc29a326766c9e6ab74311096ef8c0ffac7778ec6a88af32
Source51:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/it.xpi
#!RemoteAsset:  sha256:4dd5d1bce48d0e74f4787c769f746803ce85e0338af4f90f8ae2cc94f58db399
Source52:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ja.xpi
#!RemoteAsset:  sha256:5debef65380e24e9049ea46cfb7da6db4db692069a49b1a1ec86fb52cbd9227b
Source53:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ka.xpi
#!RemoteAsset:  sha256:2c4667277924143421da95a8744101892829a119ccfa47810e5482fc8a606ac9
Source54:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kab.xpi
#!RemoteAsset:  sha256:7580af78314c4fb23b922deeb16ce6ba468343fed970378b4e011b7d5b85899b
Source55:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kk.xpi
#!RemoteAsset:  sha256:b04bfde57627f7c7b1ba3d96e751ba093634e229803b43b2f717acb1a4e8bdd6
Source56:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/km.xpi
#!RemoteAsset:  sha256:793348b117a6831c2c1ad5ab07a359bbc3f4aee18cb60e0da40889f3ad765903
Source57:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kn.xpi
#!RemoteAsset:  sha256:7bd0af9ca0f1dcf54602417ae0370cf2a669e2957521fadcdde51c7cc14aa0a2
Source58:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ko.xpi
#!RemoteAsset:  sha256:20b0c623c6683f68b28d9d704c8b190d2b1953ee62f726ebc89e3b92c054d539
Source59:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lij.xpi
#!RemoteAsset:  sha256:c4a2cc2c56f4ba63c7d001f6d8a7778cc7f1bd244b52ae85151cdcdd50fed0fc
Source60:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lt.xpi
#!RemoteAsset:  sha256:72d089f8fa2c6a4ca714670c3405d9ea4bdaab9479fe139c8a52e8dc6b923ec3
Source61:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lv.xpi
#!RemoteAsset:  sha256:a76da1c6c58f74189632ee8e86e795575a333ea38efd2ad04c4974abfa82adf1
Source62:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mk.xpi
#!RemoteAsset:  sha256:063355a484a95f426c67826c4382d8fc1c2f8949cff8ad05872f525a455897c5
Source63:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mr.xpi
#!RemoteAsset:  sha256:95a26680c063917b335dfa7a836bd737e7cc39f3f0cbcd73756dfdd42391114d
Source64:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ms.xpi
#!RemoteAsset:  sha256:a7f62893e3394568e191740c6cf5306c810c85bcb0ebf52bc293126e80828761
Source65:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/my.xpi
#!RemoteAsset:  sha256:1cc1efe3e7cd561a90934fe4c5079cfe6823f5dc11eacbb11a4178d9dd4da2a1
Source66:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nb-NO.xpi
#!RemoteAsset:  sha256:40dc72e803139ecc155c08f3c66c53f04e2e74841076b5595411a60b854e2d5e
Source67:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ne-NP.xpi
#!RemoteAsset:  sha256:f4735c76dcb82e4e05cc2430b5d6ac0a4ff5501f9a0a42aa4f1b9cfdaba7e28a
Source68:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nl.xpi
#!RemoteAsset:  sha256:34354c6368bb53295dedec1a9452a52a79dff9b38fbf11a9428d0fac6a902761
Source69:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nn-NO.xpi
#!RemoteAsset:  sha256:6ac5d97860316da543c2867b2b3ce0d534ea4ad42fb4ed83d3c93936886bba42
Source70:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/oc.xpi
#!RemoteAsset:  sha256:b654facb5d286b2e5133601e4aef0b56a15e18cdfff3e36f2ef439dade02c399
Source71:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pa-IN.xpi
#!RemoteAsset:  sha256:aff1dd11c20b17e6dc4280d65d1de7c285c92e445d5af85def67b3f4210aedba
Source72:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pl.xpi
#!RemoteAsset:  sha256:93008726e131124e04e77e97f913fde6fd8ff3e9f0ba1c83892a60880fa2f5f8
Source73:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-BR.xpi
#!RemoteAsset:  sha256:930003d0639472583d70ad3748c24a9517ba36810c255ea8a1b34679bd10b51c
Source74:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-PT.xpi
#!RemoteAsset:  sha256:23f1910f505c8a6562b0c829386db5d5f42ea67d2d58a1a1cbc06c33e3cdf6f3
Source75:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/rm.xpi
#!RemoteAsset:  sha256:ea92db183a507045a5cca3111f862c6c2e60dbf36527b8401dd4fc4d7e1e6c3c
Source76:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ro.xpi
#!RemoteAsset:  sha256:b3b9e7d91dcf2f09a59b98cd50956cc0c17e5577a580f6d318ba1970fa265822
Source77:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ru.xpi
#!RemoteAsset:  sha256:2239d0e19550a72703ff61a48b9cda093c21d5b9d5e58023b61857b6c9cb24f7
Source78:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sat.xpi
#!RemoteAsset:  sha256:8bd59c2d8e2974add2e1728433a1793c2d44811a673bdc39ef526a849fc33599
Source79:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sc.xpi
#!RemoteAsset:  sha256:cfe71438f3db2fdee3cb0ce058132cd0de641b10b82902ca3e6dfcbf521c4d2f
Source80:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sco.xpi
#!RemoteAsset:  sha256:406332f2355da95b53a34abf87e4dd4be94cfee37a3f926324dff4f35f486501
Source81:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/si.xpi
#!RemoteAsset:  sha256:0c9564d8b2ad9f91796af1f765fc382dc6ac5c5a8cb801ad1b3de35d653ae7e3
Source82:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sk.xpi
#!RemoteAsset:  sha256:e3ff61febcf091b7eaad0147d6c52cad8af3756e7762140294c35c1e5c4a9107
Source83:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/skr.xpi
#!RemoteAsset:  sha256:b2b43636d06f3b4285f1feb6e818d219a98de83c53f4893d4c986bc89b9cab10
Source84:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sl.xpi
#!RemoteAsset:  sha256:bf83f535681c230e793b8a29f02acde2ce8735940224de19485b041cae3c434b
Source85:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/son.xpi
#!RemoteAsset:  sha256:b7ec080667e9d07e25c7d02cae6a6e497771d8b9a4c6c75cea91d841b32fef8a
Source86:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sq.xpi
#!RemoteAsset:  sha256:780f4845a0dc0f95a54733a6ea55369d8c872ac00b4143a590b98ad7d9bee6fe
Source87:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sr.xpi
#!RemoteAsset:  sha256:3e286e8ef301979b3d16976f9a14976d60e492d22163ef6e6cdad82034aff675
Source88:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sv-SE.xpi
#!RemoteAsset:  sha256:be0869824a456d082e391cc3cd3e9446583f642d91d83bbec5ce9644f5574ce9
Source89:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/szl.xpi
#!RemoteAsset:  sha256:7361a388a503d32267e4ead9da588d90d5c7a595d1d99dfc96a7202f1d3e6bb6
Source90:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ta.xpi
#!RemoteAsset:  sha256:9319d9905f0310b4057295d90de7a13c99b4821c3acf14dceac787e24c04c9e6
Source91:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/te.xpi
#!RemoteAsset:  sha256:e8bdf0ff109d3f99d5680026586148e66e5bb5b1b072feb1722ba8655a1d0c15
Source92:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tg.xpi
#!RemoteAsset:  sha256:47586ada275c1c0c36f080ba6c1feafc6333c608ade4ee60f63bc14f08d5889f
Source93:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/th.xpi
#!RemoteAsset:  sha256:a1bd3364476b7e7819395cf9f6268bdfbacf3a45ef91c67b53299a461199d067
Source94:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tl.xpi
#!RemoteAsset:  sha256:bc70799e6416d1b9c52de1c3d32b82ea404a1b85d0031c074f1a7c4e8579d0f5
Source95:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tr.xpi
#!RemoteAsset:  sha256:a79a8ed4bf00791af11835b792ebd40a7fcc297f414a304326ce6c94edcdf950
Source96:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/trs.xpi
#!RemoteAsset:  sha256:e70d35541740ff769d14259dd52148082f02e032d463463a3f73377059981f30
Source97:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uk.xpi
#!RemoteAsset:  sha256:4b6148583ced890adbb17942d21f9b233a51ac869315b6173067d91d14fe38c0
Source98:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ur.xpi
#!RemoteAsset:  sha256:5cf851a27d4cb31c1dcb7a60056a7f20707534b079a44af42c26f4c6797e0445
Source99:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uz.xpi
#!RemoteAsset:  sha256:6d48b9d2435fc3969bb6935d4faf05e286800ca0d77ab56daa91d9d9b352dedc
Source100:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/vi.xpi
#!RemoteAsset:  sha256:b60525b647b3f504d1b00f1e5bd2f6e7106e3d7cc2579e33f5683070b90f61f5
Source101:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/xh.xpi
#!RemoteAsset:  sha256:eb960dd09911ce43f9008c7a07eed13583f6362deca82c3aa66cd221d2469222
Source102:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/zh-CN.xpi
#!RemoteAsset:  sha256:c37778863d18d2a6ef314afda61a06f68dc2f4f1bdeacb87bd37eb288026ebef
Source103:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/zh-TW.xpi
# What if firefox add another language? We should start at 200 - 251
# https://www.chromium.org/developers/how-tos/api-keys/
# Note: This key is for openRuyi use ONLY.
# For your own distribution, please get your own set of keys.
Source200:      google-api-key
Source201:      firefox.desktop
Source202:      firefox.js
Source203:      distribution.ini.in
Source204:      firefox.xml
Source205:      run-wayland-compositor.sh

BuildRequires:  appstream-glib
BuildRequires:  autoconf
BuildRequires:  cargo
BuildRequires:  cbindgen
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  cmake(LLVM)
BuildRequires:  compiler-rt
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  nodejs
BuildRequires:  pciutils
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vpx)
# We can't remove this because of desktop_capture_gn:
#    modules/desktop_capture/linux/x11/screen_capturer_x11.h
# This header will include <X11/extensions/Xdamage.h>
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rust
BuildRequires:  unzip
BuildRequires:  zip
# For PGO desktop
#BuildRequires:  kscreenlocker
BuildRequires:  kf6-kconfig
BuildRequires:  kf6-kwallet
BuildRequires:  kwin
BuildRequires:  desktop-file-utils

Requires:       ffmpeg

%patchlist
2000-riscv64-Use-long-tail-jump-for-xptcall-stubs.patch
# https://bugzilla.mozilla.org/show_bug.cgi?id=1865601
2001-riscv64-enable-gles-rendering.patch
2003-blindly-set-rust-rva23-target-when-needed.patch
2005-add-riscv64-support-for-crash-context.patch
2006-enable-crashreporter-for-riscv64.patch

%description
Mozilla Firefox is a free, open-source web browser developed by
the Mozilla Foundation, focused on user privacy, speed, and
customization.

%prep
%autosetup -p1 -n %{name}-%{version}

%conf
# Configure build file for openRuyi (Globally)
cat > .mozconfig <<EOF
# Release & Branding
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1
ac_add_options --enable-update-channel=release

# Install directories
mk_add_options MOZ_OBJDIR=${PWD@Q}/obj
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --includedir=%{_includedir}

# Updater
ac_add_options --disable-updater
# Addon sideload
ac_add_options --allow-addon-sideload
ac_add_options --with-unsigned-addon-scopes=app,system

# Debug Symbols
# Normally we disable debug build because of the build time... - 251
ac_add_options --disable-debug
# But we need debug symbols
ac_add_options --enable-debug-symbols
# Let rpm do it's job - 251
ac_add_options --disable-strip
ac_add_options --disable-install-strip

# Optimization related
ac_add_options --enable-optimize
ac_add_options --enable-hardening
ac_add_options --enable-rust-simd
# Build
ac_add_options --enable-linker=lld

# Use system libraries
ac_add_options --with-system-gbm
ac_add_options --with-system-jpeg
ac_add_options --with-system-libdrm
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-pipewire
ac_add_options --with-system-webp
ac_add_options --with-system-zlib
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

# Multimedia & network related
ac_add_options --enable-pulseaudio
ac_add_options --enable-libproxy

# We use wayland
ac_add_options --enable-default-toolkit=cairo-gtk3-wayland

# sandbox libraries
ac_add_options --without-wasm-sandboxed-libraries

# Google Services
# Not free anymore... - 251
#ac_add_options --with-google-location-service-api-keyfile=%{SOURCE200}
ac_add_options --with-google-safebrowsing-api-keyfile=%{SOURCE200}

# Firefox crash reporter
ac_add_options --enable-crashreporter
# Misc
ac_add_options --disable-bootstrap
ac_add_options --disable-tests
# Enable SpiderMonkey JS shell
ac_add_options --enable-js-shell
EOF

# Some optimization related - 251
echo "ac_add_options --enable-lto" >> .mozconfig

%if %{with official_branding}
echo "ac_add_options --enable-official-branding" >> .mozconfig
%endif

# Some libraries we don't have but i think we should? - 251
%if %{with fdk_aac}
echo "ac_add_options --with-system-fdk-aac" >> .mozconfig
%endif

%build
#ifarch riscv64
#FF_OPTFLAGS="%{optflags}"
# Otherwise will segmentation fault w/ V extension
# https://github.com/llvm/llvm-project/issues/198699
#FF_OPTFLAGS="${FF_OPTFLAGS//-fstack-clash-protection/}"
#echo "export CFLAGS=\"$FF_OPTFLAGS\""  >> .mozconfig
#echo "export CXXFLAGS=\"$FF_OPTFLAGS\"" >> .mozconfig
#else
echo "export CFLAGS=\"%{optflags}\""   >> .mozconfig
echo "export CXXFLAGS=\"%{optflags}\"" >> .mozconfig
#endif
echo "export LDFLAGS=\"%{build_ldflags}\"" >> .mozconfig
echo "export LLVM_PROFDATA=\"llvm-profdata\"" >> .mozconfig
echo "export AR=\"llvm-ar\"" >> .mozconfig
echo "export NM=\"llvm-nm\"" >> .mozconfig
echo "export RANLIB=\"llvm-ranlib\"" >> .mozconfig
# Fix: Could not find libclang to generate rust bindings for C/C++
echo "ac_add_options --with-libclang-path=`llvm-config --libdir`" >> .mozconfig

# https://firefox-source-docs.mozilla.org/build/buildsystem/pgo.html
%ifarch x86_64
echo "ac_add_options MOZ_PGO=1" >> .mozconfig

cp %{SOURCE205} .
. ./run-wayland-compositor.sh
%endif

./mach build -v

%install
DESTDIR=%{buildroot} make -C obj install

install -Dm0644 %{SOURCE201} %{buildroot}%{_datadir}/applications/firefox.desktop

# Install icons
%if %{with official_branding}
for s in 16 22 24 32 48 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    cp -p browser/branding/official/default${s}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/firefox.png
done
%else
for s in 16 22 24 32 48 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    cp -p browser/branding/unofficial/default${s}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/firefox.png
done
%endif

# We use %lang() for langpacks
echo > %{name}.lang
mkdir -p %{buildroot}%{_libdir}/firefox/langpacks
for langpack in %{_sourcedir}/*.xpi; do
    language="$(basename "$langpack" .xpi)"
    extensionID="langpack-$language@firefox.mozilla.org"

    rm -rf "$extensionID" "${extensionID}.xpi"
    mkdir -p "$extensionID"
    unzip -qq "$langpack" -d "$extensionID"
    find "$extensionID" -type f | xargs chmod 644

    cd "$extensionID"
    zip -qq -r9mX "../${extensionID}.xpi" .
    cd -

    install -m 644 "${extensionID}.xpi" %{buildroot}%{_libdir}/firefox/langpacks
    language="$(echo "$language" | sed -e 's/-/_/g')"
    echo "%%lang($language) %{_libdir}/firefox/langpacks/${extensionID}.xpi" >> %{name}.lang
done

# Install langpack workaround
function create_default_langpack() {
    language_long=$1
    language_short=$2
    cd %{buildroot}%{_libdir}/firefox/langpacks
    ln -s langpack-$language_long@firefox.mozilla.org.xpi langpack-$language_short@firefox.mozilla.org.xpi
    cd -
    echo "%%lang($language_short) %{_libdir}/firefox/langpacks/langpack-$language_short@firefox.mozilla.org.xpi" >> %{name}.lang
}

# Table of fallbacks for each language
create_default_langpack "es-AR" "es"
create_default_langpack "fy-NL" "fy"
create_default_langpack "ga-IE" "ga"
create_default_langpack "gu-IN" "gu"
create_default_langpack "hi-IN" "hi"
create_default_langpack "hy-AM" "hy"
create_default_langpack "nb-NO" "nb"
create_default_langpack "nn-NO" "nn"
create_default_langpack "pa-IN" "pa"
create_default_langpack "pt-PT" "pt"
create_default_langpack "sv-SE" "sv"
create_default_langpack "zh-TW" "zh"

# Default config
mkdir -p %{buildroot}%{_libdir}/firefox/browser/defaults/preferences
cp %{SOURCE202} %{buildroot}%{_libdir}/firefox/browser/defaults/preferences

# Add distribution.ini
mkdir -p %{buildroot}%{_libdir}/firefox/distribution
sed -e "s/__NAME__/%(source /etc/os-release; echo ${NAME})/" \
    -e "s/__ID__/%(source /etc/os-release; echo ${ID})/" \
    %{SOURCE203} > %{buildroot}%{_libdir}/firefox/distribution/distribution.ini

# Install appdata
# https://bugzilla.mozilla.org/show_bug.cgi?id=1071061
# We modify the upstream one here
mkdir -p %{buildroot}%{_datadir}/metainfo
sed -e "s/__VERSION__/%{version}/" \
    -e "s/__DATE__/$(date '+%F')/" \
    %{SOURCE204} > %{buildroot}%{_datadir}/metainfo/firefox.appdata.xml

# Install license file
install -Dpm0644 LICENSE %{buildroot}%{_libdir}/firefox

# Directory for system extensions
mkdir -p %{buildroot}%{_datadir}/mozilla/extensions/\{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
mkdir -p %{buildroot}%{_libdir}/mozilla/extensions/\{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}

# Use the system hunspell dictionaries
rm -rf %{buildroot}%{_libdir}/firefox/dictionaries
ln -s %{_datadir}/hunspell %{buildroot}%{_libdir}/firefox/dictionaries

# Delete unwanted files
rm -f %{buildroot}%{_libdir}/firefox/update-settings.ini
rm -f %{buildroot}%{_libdir}/firefox/removed-files

# There's no reason for any check, we already using PGO.
%check

%preun
# is it a final removal?
if [ $1 -eq 0 ]; then
    rm -rf %{_libdir}/firefox/components
    rm -rf %{_libdir}/firefox/extensions
    rm -rf %{_libdir}/firefox/plugins
    rm -rf %{_libdir}/firefox/langpacks
fi

%files -f %{name}.lang
%license %{_libdir}/firefox/LICENSE
%dir %{_datadir}/mozilla/extensions/*
%dir %{_libdir}/mozilla/extensions/*
%dir %{_libdir}/firefox/langpacks
%{_bindir}/firefox
%{_libdir}/firefox/application.ini
%{_libdir}/firefox/browser
%{_libdir}/firefox/crashreporter
%{_libdir}/firefox/crashhelper
%{_libdir}/firefox/defaults/pref/channel-prefs.js
%{_libdir}/firefox/dependentlibs.list
%{_libdir}/firefox/dictionaries
%{_libdir}/firefox/distribution
%{_libdir}/firefox/firefox
%{_libdir}/firefox/firefox-bin
%{_libdir}/firefox/fonts/TwemojiMozilla.ttf
%{_libdir}/firefox/glxtest
%{_libdir}/firefox/gmp-clearkey
%{_libdir}/firefox/omni.ja
%{_libdir}/firefox/pingsender
%{_libdir}/firefox/platform.ini
%ifarch riscv64
%{_libdir}/firefox/v4l2test
%endif
%{_libdir}/firefox/vaapitest
%{_libdir}/firefox/vulkantest
%{_libdir}/firefox/*.so
%{_datadir}/applications/firefox.desktop
%{_datadir}/icons/hicolor/16x16/apps/firefox.png
%{_datadir}/icons/hicolor/22x22/apps/firefox.png
%{_datadir}/icons/hicolor/24x24/apps/firefox.png
%{_datadir}/icons/hicolor/256x256/apps/firefox.png
%{_datadir}/icons/hicolor/32x32/apps/firefox.png
%{_datadir}/icons/hicolor/48x48/apps/firefox.png
%{_datadir}/metainfo/firefox.appdata.xml

%changelog
%autochangelog
