import visa


# Modul zur Steuerung eines Siglent SPD3303X
class PowerSupply:
    def __init__(self,instrument):
        self.psu = instrument
        self.psu.write_termination='' #Ohne das geht es nicht!

    def getIdentity(self):
        return self.psu.query("*IDN?")

    def enableChannel(self,ch):
        self.psu.write("OUTP CH"+str(ch)+",ON")

    def disableChannel(self, ch):
        self.psu.write("OUTP CH" + str(ch) + ",OFF")

    def setCurrent(self,ch,current):
        self.psu.write("CH"+str(ch)+":CURR "+str(current))

    def setVoltage(self,ch,voltage):
        self.psu.write("CH"+str(ch)+":VOLT "+str(voltage))

    def measureCurrent(self,ch):
        return self.psu.query("MEAS:CURR? CH"+str(ch))

    def measureVoltage(self,ch):
        return self.psu.query("MEAS:VOLT? CH"+str(ch))

    def measurePower(self,ch):
        return self.psu.query("MEAS:POWE? CH"+str(ch))


#MAIN
_rm = visa.ResourceManager()
sds = _rm.open_resource("TCPIP::192.168.178.67::INSTR")


ps = PowerSupply(sds)
#sds.query("*IDN?")
print(ps.measurePower(2))
ps.setVoltage(2,0.23)

sds.close()

