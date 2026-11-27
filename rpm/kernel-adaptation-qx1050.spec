%define device qx1050
%define kernel_arch arm64
%define device_target_cpu aarch64

# The full resolved configuration of the running kernel (arm64 defconfig + the Pro1-X and
# SailfishOS fragments, olddefconfig on the patched tree, every fragment line verified).
%define extra_config sfos-qx1050_defconfig
%define defconfig %{extra_config}
%define source_directory linux

%define build_modules 1
%define build_Image 1
%define kernel_image Image.gz

%define ramdisk_directory ramdisk

# The Pro1-X's ABL wants the DTB appended to Image.gz, header version 0, 4 KiB pages.
%define deviceinfo_dtb qcom/sm6115-fxtec-pro1x.dtb
%define deviceinfo_append_dtb true
%define deviceinfo_kernel_cmdline console=ttyMSM0,115200n8 loglevel=3 log_buf_len=1M lsm=landlock,yama,bpf logo.nologo vt.global_cursor_default=0 audit=0
%define deviceinfo_flash_pagesize 4096
%define deviceinfo_flash_offset_base 0x00000000
%define deviceinfo_flash_offset_kernel 0x00008000
%define deviceinfo_flash_offset_ramdisk 0x01000000
%define deviceinfo_flash_offset_second 0x00f00000
%define deviceinfo_flash_offset_tags 0x00000100
%define deviceinfo_bootimg_header_version 0
%define deviceinfo_bootimg_os_version 0
%define deviceinfo_bootimg_os_patch_level 0

Version:        7.3.0
Release:        2

Provides:       droid-hal-qx1050-kernel
Provides:       droid-hal-qx1050-kernel-modules

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc
