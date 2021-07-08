#!/bin/bash

SYMBOLSDIR='../eSim-Cloud/esim-cloud-backend/kicad-symbols'

./pinscript.awk \
    $SYMBOLSDIR/additional/4xxx.lib \
    $SYMBOLSDIR/additional/Analog.lib \
    $SYMBOLSDIR/additional/Device.lib \
    $SYMBOLSDIR/additional/Diode.lib \
    $SYMBOLSDIR/additional/LED.lib \
    $SYMBOLSDIR/additional/Motor.lib \
    $SYMBOLSDIR/additional/Oscillator.lib \
    $SYMBOLSDIR/default/Transistor_BJT.lib \
    $SYMBOLSDIR/additional/Transistor_FET.lib \
    $SYMBOLSDIR/additional/Transistor_IGBT.lib \
    $SYMBOLSDIR/additional/Triac_Thyristor.lib \
    $SYMBOLSDIR/additional/eSim_Hybrid.lib \
    $SYMBOLSDIR/default/eSim_Sources.lib \
    $SYMBOLSDIR/default/power.lib \
    $SYMBOLSDIR/default/pspice.lib
