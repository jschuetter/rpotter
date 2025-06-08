#!/usr/bin/python
import pigpio
import time

pi = pigpio.pi()

#pin for Powerswitch (Lumos,Nox)
switch_pin = 23
pi.set_mode(switch_pin,pigpio.OUTPUT)

#pin for Particle (Nox)
nox_pin = 24
pi.set_mode(nox_pin,pigpio.OUTPUT)

#pin for Particle (Incendio)
incendio_pin = 22
pi.set_mode(incendio_pin,pigpio.OUTPUT)

#pin for Trinket (Colovario)
trinket_pin = 12
pi.set_mode(trinket_pin,pigpio.OUTPUT)

pi.write(nox_pin,1)
pi.write(incendio_pin,0)
pi.write(switch_pin,0)
time.sleep(2)
