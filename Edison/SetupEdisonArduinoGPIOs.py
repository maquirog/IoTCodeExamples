rulesMatrix = [] 
#OE stands for Output Enable, and it should be provided by the user....high=output
#PUD stands for Pull UP pull down resistor mode, and should be provided by user...
#* stands for values that are ignored...
		 #             GPIO    PWM      UART   I2S     I2C    SPI
rulesMatrix.append(["IO0",130,"mode0","*"    ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO0",248,"OE"   ,"*"    ,"OE"   ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO0",216,"PUD"  ,"*"    ,"PUD"  ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO1",131,"mode0","*"    ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO1",249,"OE"   ,"*"    ,"OE"   ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO1",217,"PUD"  ,"*"    ,"PUD"  ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO2",128,"mode0","*"    ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO2",250,"OE"   ,"*"    ,"OE"   ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO2",218,"PUD"  ,"*"    ,"PUD"  ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO3",12 ,"mode0","mode1","*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO3",251,"OE"   ,"OE"   ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO3",219,"PUD"  ,"PUD"  ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO4",129,"mode0","*"    ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO4",252,"OE"   ,"*"    ,"OE"   ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO4",220,"PUD"  ,"*"    ,"PUD"  ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO5",13 ,"mode0","mode1","*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO5",253,"OE"   ,"OE"   ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO5",221,"PUD"  ,"PUD"  ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO6",182,"mode0","mode1","*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO6",254,"OE"   ,"OE"   ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO6",222,"PUD"  ,"PUD"  ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO7",48 ,"mode0","*"    ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO7",255,"OE"   ,"*"    ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO7",223,"PUD"  ,"*"    ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO8",49 ,"mode0","*"    ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO8",256,"OE"   ,"*"    ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO8",224,"PUD"  ,"*"    ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO9",183,"mode0","mode1","*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO9",257,"OE"   ,"OE"   ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO9",225,"PUD"  ,"PUD"  ,"*"    ,"*"    ,"*"    ,"*"])
rulesMatrix.append(["IO10",263,"high" ,"*"   ,"*"    ,"high" ,"*"    ,"high"])
rulesMatrix.append(["IO10",240,"low"  ,"*"   ,"*"    ,"low"  ,"*"    ,"high"])
rulesMatrix.append(["IO10",41 ,"mode0","*"   ,"*"    ,"mode1","*"    ,"*"])
rulesMatrix.append(["IO10",111,"*"    ,"*"   ,"*"    ,"*"    ,"*"    ,"mode1"])
rulesMatrix.append(["IO10",258,"OE"   ,"*"   ,"*"    ,"OE"   ,"*"    ,"OE"])
rulesMatrix.append(["IO10",226,"PUD"  ,"*"   ,"*"    ,"PUD"  ,"*"    ,"PUD"])
rulesMatrix.append(["IO11",262,"high" ,"*"   ,"*"    ,"high" ,"*"    ,"high"])
rulesMatrix.append(["IO11",241,"low"  ,"*"   ,"*"    ,"low"  ,"*"    ,"high"])
rulesMatrix.append(["IO11",43 ,"mode0","*"   ,"*"    ,"mode1","*"    ,"*"])
rulesMatrix.append(["IO11",115,"*"    ,"*"   ,"*"    ,"*"    ,"*"    ,"mode1"])
rulesMatrix.append(["IO11",259,"OE"   ,"*"   ,"*"    ,"OE"   ,"*"    ,"OE"])
rulesMatrix.append(["IO11",227,"PUD"  ,"*"   ,"*"    ,"PUD"  ,"*"    ,"PUD"])
rulesMatrix.append(["IO12",242,"low"  ,"*"   ,"*"    ,"low"  ,"*"    ,"low"])
rulesMatrix.append(["IO12",42 ,"mode0","*"   ,"*"    ,"mode1","*"    ,"*"])
rulesMatrix.append(["IO12",114,"*"    ,"*"   ,"*"    ,"*"    ,"*"    ,"mode1"])
rulesMatrix.append(["IO12",260,"OE"   ,"*"   ,"*"    ,"OE"   ,"*"    ,"OE"])
rulesMatrix.append(["IO12",228,"PUD"  ,"*"   ,"*"    ,"PUD"  ,"*"    ,"PUD"])
rulesMatrix.append(["IO13",243,"low"  ,"*"   ,"*"    ,"low"  ,"*"    ,"low"])
rulesMatrix.append(["IO13",40 ,"mode0","*"   ,"*"    ,"mode1","*"    ,"*"])
rulesMatrix.append(["IO13",109,"*"    ,"*"   ,"*"    ,"*"    ,"*"    ,"mode1"])
rulesMatrix.append(["IO13",261,"OE"   ,"*"   ,"*"    ,"OE"   ,"*"    ,"OE"])
rulesMatrix.append(["IO13",229,"PUD"  ,"*"   ,"*"    ,"PUD"  ,"*"    ,"PUD"])
rulesMatrix.append(["IO14",200,"low"  ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO14",44 ,"mode0","*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO14",232,"OE"   ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO14",228,"PUD"  ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO15",201,"low"  ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO15",45 ,"mode0","*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO15",233,"OE"   ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO15",209,"PUD"  ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO16",202,"low"  ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO16",46 ,"mode0","*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO16",234,"OE"   ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO16",210,"PUD"  ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO17",203,"low"  ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO17",47 ,"mode0","*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO17",235,"OE"   ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO17",211,"PUD"  ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO18",204,"low"  ,"*"   ,"mode1","*"    ,"low"  ,"*"])
rulesMatrix.append(["IO18",14 ,"mode0","*"   ,"mode1","*"    ,"mode1","*"])
rulesMatrix.append(["IO18",28 ,"*"    ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO18",236,"OE"   ,"*"   ,"mode1","*"    ,"OE"   ,"*"])
rulesMatrix.append(["IO18",212,"PUD"  ,"*"   ,"mode1","*"    ,"PUD"  ,"*"])
rulesMatrix.append(["IO19",205,"low"  ,"*"   ,"mode1","*"    ,"low"  ,"*"])
rulesMatrix.append(["IO19",165,"mode0","*"   ,"mode1","*"    ,"mode1","*"])
rulesMatrix.append(["IO19",27 ,"*"    ,"*"   ,"mode1","*"    ,"*"    ,"*"])
rulesMatrix.append(["IO19",237,"OE"   ,"*"   ,"mode1","*"    ,"OE"   ,"*"])
rulesMatrix.append(["IO19",213,"PUD"  ,"*"   ,"mode1","*"    ,"PUD"  ,"*"])

EXPORT_TRI_STATE_ALL="echo 214 /sys/class/gpio/export"
ENABLE_TRI_STATE_ALL="echo low > /sys/class/gpio/gpio214/direction"
DISABLE_TRI_STATE_ALL="echo high > /sys/class/gpio/gpio214/direction"
def exportGPIO(GPIO):
	return "echo " + str(GPIO) +" /sys/class/gpio/export";
def setGPIOValue(GPIO, VALUE):
	if "mode" in VALUE:
		return "echo "+VALUE+" > /sys/kernel/debug/gpio_debug/gpio"+str(GPIO)+"/current_pinmux";
	elif "OE" in VALUE:
		return "echo "+OE+" > /sys/class/gpio/gpio"+str(GPIO)+"/direction"
	elif "PUD" in VALUE:
		return "echo "+PUD+" > /sys/class/gpio/gpio"+str(GPIO)+"/direction"
	else:
		return "echo "+VALUE+" > /sys/class/gpio/gpio"+str(GPIO)+"/direction"; 
def generateInstructions(TYPE,PIN,OE,PUD,DIRECTION):
	print EXPORT_TRI_STATE_ALL
	for i in range(0, 78):
	    if rulesMatrix[i][0] == PIN:	
		print exportGPIO(rulesMatrix[i][1])
	print ENABLE_TRI_STATE_ALL
	for i in range(0, 78):
	    if rulesMatrix[i][0] == PIN:	
		print setGPIOValue(rulesMatrix[i][1],rulesMatrix[i][3])      
	print DISABLE_TRI_STATE_ALL


TYPE="GPIO"
PIN="IO5" # pin we want to generate the instructions
OE="high" # high=output; low=input
PUD="in" #in = pullup disabled; out= pullup enabled
DIRECTION="in" #for GPIO, to tell the direction of the GPIO
generateInstructions(TYPE,PIN,OE,PUD,DIRECTION)






 