obj-m += MPL3115A2.o
obj-m += JHD1313M2.o

all:i2ctest lcdtest modules 

i2ctest:i2c.c
		gcc -O i2c.c -o i2ctest
lcdtest:lcd.c
		gcc -O lcd.c -o lcdtest
example:example.c
		gcc -O example.c -o example
modules:MPL3115A2.c JHD1313M2.c
		#----------------------------------------------
		#started compiling MPL3115A2 and JHD1313M2 OK
		#----------------------------------------------
		make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
		#----------------------------------------------
		#finished compiling MPL3115A2 and JHD1313M2 
		#----------------------------------------------
clean:
		#----------------------------------------------
		#cleansing our mess....
		#----------------------------------------------
		-rm i2ctest lcdtest example *.*~ .*~
		make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
		#----------------------------------------------
		#done!
		#----------------------------------------------
