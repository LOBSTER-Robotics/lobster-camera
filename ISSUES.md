# Issues

Currently there are a few issues with this software


## Frame size is incorrect

You will see an output like this
```
< 47.77 fps
4096 != 549486
<4096 != 547428
<4096 != 547428
<4096 != 547428
<4096 != 547428
...
<4096 != 545370
<4096 != 545370
<4096 != 545370
<4096 != 545370
<4096 != 545370
<4096 != 545370
```

This happens after one incorrect frame is received. Sometimes you can recover
with restarting the process, but sometimes it stays even after restarting. That
might have something to do with the v4l2 linux driver. Unplugging and replugging
the camera might help.



`dmesg`

```
[  +0.019089] vc_sm_cma: module is from the staging directory, the quality is unknown, you have been warned.
[  +0.001756] vc_sm_cma: module is from the staging directory, the quality is unknown, you have been warned.
[  +0.000007] vc_sm_cma: module is from the staging directory, the quality is unknown, you have been warned.
[  +0.000563] bcm2835_vc_sm_cma_probe: Videocore shared memory driver
[  +0.000024] [vc_sm_connected_init]: start
[  +0.004841] [vc_sm_connected_init]: installed successfully
[  +0.015351] bcm2835_mmal_vchiq: module is from the staging directory, the quality is unknown, you have been warn
[  +0.002028] bcm2835_mmal_vchiq: module is from the staging directory, the quality is unknown, you have been warn
[  +0.000895] bcm2835_mmal_vchiq: module is from the staging directory, the quality is unknown, you have been warn
[  +0.012535] bcm2835_isp: module is from the staging directory, the quality is unknown, you have been warned.
[  +0.001333] bcm2835_v4l2: module is from the staging directory, the quality is unknown, you have been warned.
[  +0.001324] bcm2835_codec: module is from the staging directory, the quality is unknown, you have been warned.
...
[Mar19 16:16] uvcvideo: Non-zero status (-71) in video completion handler.
[Mar19 16:17] uvcvideo: Non-zero status (-71) in video completion handler.
[Mar19 16:18] uvcvideo: Non-zero status (-71) in video completion handler.
[Mar19 16:20] uvcvideo: Non-zero status (-71) in video completion handler.
[Mar19 16:21] uvcvideo: Non-zero status (-71) in video completion handler.
[Mar19 16:22] uvcvideo: Non-zero status (-71) in video completion handler.
[Mar19 16:23] uvcvideo: Non-zero status (-71) in video completion handler.
[Mar19 16:30] uvcvideo: Non-zero status (-71) in video completion handler.
```
