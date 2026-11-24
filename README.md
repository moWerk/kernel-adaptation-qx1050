# kernel-adaptation-qx1050

Kernel, modules and device tree for the F(x)tec Pro1-X (qx1050) on a mainline kernel, packaged
for Sailfish OS after the mainline HADK (kernel-adaptation-simplified, chapter 5).

- `linux`: Linux 7.3 with the Pro1-X series (branch `sfos-7.3`), one commit per feature.
- `sfos-qx1050_defconfig`: the full configuration the phone runs (`CONFIG_LOCALVERSION="-qx1050"`),
  except `CONFIG_CRC_OPTIMIZATIONS` (needs `CONFIG_EXPERT` to be switched off) and `CONFIG_BTRFS_FS`: their NEON code does not build under the
  SDK's scratchbox2 (lib/crc/crc64-neon.c: conflicting int64_t), and Sailfish uses neither;
  and `CONFIG_GCC_PLUGINS`, which the SDK's gcc offers but cannot load.
- `rpm/kernel-adaptation-qx1050.spec`: boot image values as the Pro1-X's Android bootloader (ABL)
  wants them: Image.gz with the DTB appended, header version 0, 4 KiB pages.

Build in the Platform SDK: `kernel-adaptation-qx1050/kernel-adaptation-simplified/helpers/build_packages.sh -k`.
