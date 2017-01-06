# rpm_device is in 99% cases $DEVICE
%define rpm_device r7plus
# rpm_vendor is in 99% cases $VENDOR
%define rpm_vendor oppo

# Manufacturer and device name to be shown in UI
%define vendor_pretty Oppo
%define device_pretty R7 Plus

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1
%define have_led 1

%include droid-hal-version/droid-hal-version.inc
