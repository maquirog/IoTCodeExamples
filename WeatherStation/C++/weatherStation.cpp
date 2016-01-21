#include "mraa.hpp"

#include <iostream>
#include <unistd.h>
#include "SparkFunADS1015.h"
#include "tsl2561.h"
#include <cmath>
#include <string.h>
#include "Freeboard.h"

using namespace std;
#define DWEET_URL "https://dweet.io/dweet/for/WZPN1"
#define V_SUPPLY 3.3;
#define WIND_SPEED_MPH 1.492  
#define WIND_SPEED_KM_H 2.4 
#define TIME_LIMIT_SECS 10 
#define ANEMOMETER_GPIO 48
#define RAINGAUGE_GPIO 36
#define RH_POWER_GPIO 47
#define RAIN_MM 0.2794
#define RAIN_INCHES 0.011
#define DLS_BUS 1
#define DLS_ADDRESS 0x29
map<string,string> dweet_data;
int anemometerTotal= 0;
int Time = 0;
float raingaugeTotal= 0.0;
float adc_float = 0;
float zeroOffset = 0.0;
float slope = 0.0;
Freeboard * freeBoard;
mraa::I2c* adc_i2c;
ads1015 *adc;
mraa::Gpio* gpioAnemometer;
mraa::Gpio* gpioRainGauge;
mraa::Gpio* gpioPowerRH;
upm::TSL2561* digLight;

//---------------------------------------------------------------------------------

void setupFreeboard()
{
	freeBoard = new Freeboard();
}
void setupDigitalLight()                                           
{                                                                         
	digLight= new upm::TSL2561(DLS_BUS,DLS_ADDRESS,0x00,0x00);
}     
int getLuxDigitalLight()
{
	int lux =0;
	lux = digLight->getLux();
	return lux;
}
int setupHumiditySensor()
{
   slope = 0.0062 * V_SUPPLY;                           
   zeroOffset = 0.16 * V_SUPPLY;
/*	
   gpioPowerRH = new mraa::Gpio(RH_POWER_GPIO);
   if (gpioPowerRH == NULL)
   {
      return mraa::ERROR_UNSPECIFIED;
   }
   mraa::Result response = gpioPowerRH->dir(mraa::DIR_OUT);
   if (response != mraa::SUCCESS) {
       mraa::printError(response);
       return 1;
   }

   gpioPowerRH->write(1);
*/

}
float getRawHumidity()
{
        return adc->getResult(1);
}
float getSensorRH()                             
{                                     
  return ((getRawHumidity() - zeroOffset) / slope);
}                                        
float getTrueRH(float temperature)
{     
  return getSensorRH() / (1.0546 - (0.00216 * temperature));
}
void anemometerEvent(void * args)
{
    anemometerTotal++;
	//printf("testing wind %d \n", Total);
}
void raingaugeEvent(void * args)
{
    raingaugeTotal++;
}
int setupRainGauge()
{
    gpioRainGauge = new mraa::Gpio(RAINGAUGE_GPIO);
    if (gpioRainGauge == NULL) {
        return mraa::ERROR_UNSPECIFIED;
    }
    mraa::Result response = gpioRainGauge->dir(mraa::DIR_IN);
    if (response != mraa::SUCCESS) {
        mraa::printError(response);
        return 1;
    }
    response = gpioRainGauge->mode(mraa::MODE_PULLDOWN);
    if (response != mraa::SUCCESS) {                      
        mraa::printError(response);                       
        return 1;                                         
    } 
    response = gpioRainGauge->isr(mraa::EDGE_RISING,&raingaugeEvent,NULL);
    if (response != mraa::SUCCESS) {
        mraa::printError(response);
        return 1;
    }
    return mraa::SUCCESS;
}
int setupAnemometer()
{
    gpioAnemometer = new mraa::Gpio(ANEMOMETER_GPIO);
    if (gpioAnemometer == NULL) {
        return mraa::ERROR_UNSPECIFIED;
    }
    mraa::Result response = gpioAnemometer->dir(mraa::DIR_IN);
    if (response != mraa::SUCCESS) {
        mraa::printError(response);
        return 1;
    }
    response = gpioAnemometer->mode(mraa::MODE_PULLDOWN);
    if (response != mraa::SUCCESS) {                      
        mraa::printError(response);                       
        return 1;                                         
    } 
    response = gpioAnemometer->isr(mraa::EDGE_BOTH,&anemometerEvent,NULL);
    if (response != mraa::SUCCESS) {
        mraa::printError(response);
        return 1;
    }
    return mraa::SUCCESS;
}
int setupADC()
{
    adc_i2c = new mraa::I2c(1);
    adc = new ads1015(adc_i2c, 0x48);
    adc->setRange(_6_144V);
    return MRAA_SUCCESS;	
}

float getHumidity()
{
	float humidity = adc->getResult(1);
}
string getWindDirection(map<string,string> &dweet_data) 
{
	adc_float = adc->getResult(0);
	if(abs(adc_float-2.64)<0.1 ||  abs(adc_float-1.36)<0.1)
	{
		dweet_data["WDIRECTION_NAME"]="NORTH";dweet_data["WDIRECTION"]="0";
		return "NORTH\n";//cout<<"NORTH\n";
	}
	else if(abs(adc_float-1.55)<0.1 || abs(adc_float-1.282)<0.1)
	{
		dweet_data["WDIRECTION_NAME"]="NORTH_EAST";dweet_data["WDIRECTION"]="45";
		return "NORTH EAST\n";//cout<<"NORTH EAST\n";
	}
    else if(abs(adc_float-0.315)<0.1 || abs(adc_float-0.220)<0.1)       
    {
    	dweet_data["WDIRECTION_NAME"]="EAST";dweet_data["WDIRECTION"]="90";
    	return "EAST\n";//cout<<"EAST\n";
	}  
    else if(abs(adc_float-0.62)<0.1 || abs(adc_float-0.426)<0.1)
	{
    	dweet_data["WDIRECTION_NAME"]="SOUTH_EAST";dweet_data["WDIRECTION"]="135";
    	return "SOUTH EAST\n";//cout<<"SOUTH EAST\n";
	}  
    else if(abs(adc_float-0.965)<0.1 || abs(adc_float-0.82)<0.1)       
    {
    	dweet_data["WDIRECTION_NAME"]="SOUTH";dweet_data["WDIRECTION"]="180";
    	return"SOUTH\n";//cout<<"SOUTH\n";
	}  
	else if(abs(adc_float-2.12)<0.1 || abs(adc_float-2.018)<0.1)      
	{
		dweet_data["WDIRECTION_NAME"]="SOUTH_WEST";dweet_data["WDIRECTION"]="225";
		return "SOUTH WEST\n";//cout<<"SOUTH WEST\n";
	}  
	else if(abs(adc_float-3.177)<0.1 || abs(adc_float-2.8)<0.1)       
	{
		dweet_data["WDIRECTION_NAME"]="WEST";dweet_data["WDIRECTION"]="270";
		return"WEST\n";//cout<<"WEST\n";
	}  
	else if(abs(adc_float-2.9)<0.1 || abs(adc_float-2.36)<0.1)       
	{
		dweet_data["WDIRECTION_NAME"]="NORTH_WEST";dweet_data["WDIRECTION"]="315";
		return "NORTH WEST\n";//cout<<"NORTH WEST\n";
	}
	//else
	//{  
		//cout<<"Ch 0: "<<adc_float<<endl;
		//usleep(500);
	//}


}



int main()
{

	setupFreeboard();
	setupADC();
	setupHumiditySensor();
        setupDigitalLight();
	setupAnemometer();
	setupRainGauge();
	for(;;)
	{		
        
		getWindDirection(dweet_data);
                //cout<<"Wind direction: "<< dweet_data["WDIRECTION_NAME"]<<endl;
		if(Time > TIME_LIMIT_SECS)
		{
			//getWindDirection(dweet_data);
			dweet_data["WINDSPEED_MPH"] = to_string((anemometerTotal/Time)*WIND_SPEED_MPH);
			dweet_data["WINDSPEED_KM"] = to_string((anemometerTotal/Time)*WIND_SPEED_KM_H);
			dweet_data["RAIN_LVL_MM"] = to_string((raingaugeTotal/Time)*RAIN_MM);
			dweet_data["RAIN_LVL_INCH"] = to_string((raingaugeTotal/Time)*RAIN_INCHES);
			dweet_data["RH"] = to_string(getSensorRH());
			dweet_data["LUX"] = to_string(getLuxDigitalLight());
			
		    cout<<"Wind direction: "<< dweet_data["WDIRECTION_NAME"]<<endl;
		    cout<<"Wind speed: "<< dweet_data["WINDSPEED_MPH"]<<" Mph"<<endl;
		    cout<<"Wind speed: "<< dweet_data["WINDSPEED_KM"]<<" Kmh"<<endl;
		    cout<<"Rainfall mm/min: "<< dweet_data["RAIN_LVL_MM"]<<endl;
		    cout<<"Rainfall mm/inch: "<< dweet_data["RAIN_LVL_INCH"]<<endl;
		    cout<<"Relative Humidity: "<< dweet_data["RH"]<<" %"<<endl;
			cout<<"LUX: "<< dweet_data["LUX"]<<endl;
			
			//printf("Wind speed %f MPH \n", dweet_data["WINDSPEED_KM"].c_str());
		    //printf("Wind speed %f KM/H \n", dweet_data["WINDSPEED_KM"].c_str());
            //printf("rainfall per Min %fmm\n", (raingaugeTotal/Time)*RAIN_MM);
            //printf("rainfall per Min %fin\n", (raingaugeTotal/Time)*RAIN_INCHES);
		    //printf("RH: %.2f\n", getSensorRH());
		    //printf("Lux %d \n", getLuxDigitalLight());
		    anemometerTotal = 0;
		    raingaugeTotal = 0.0;
		    Time = 0;
                    freeBoard->sendValues(DWEET_URL,dweet_data);
		}
		sleep(1);
		Time++;	
	}
        //delete gpioPowerRH;
	delete gpioAnemometer;
	delete gpioRainGauge;
	delete digLight;
	delete freeBoard;
	delete adc_i2c;
	delete adc;
	return 0;
}
