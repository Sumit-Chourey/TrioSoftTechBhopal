package com.triosoft.service.impl;

import java.util.Date;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import com.triosoft.entities.SuryaDev;
import com.web_tomorrow.utils.suntimes.SunTimes;
import com.web_tomorrow.utils.suntimes.SunTimesException;
import com.web_tomorrow.utils.suntimes.Time;

@Service
@Component
public class SunTimesService {

	public Time calculateSunTimes(SuryaDev suryaDev) {
		// SunTimes st1 = new SunTimes();

		int year = suryaDev.getYear();
		int month = suryaDev.getMonth();
		int date = suryaDev.getDate();
		double latitude = suryaDev.getLatitude();
		double longitude = suryaDev.getLongitude();
		double zenith = suryaDev.getZenith();

		//Time sunrise=null;
		try {
			Time sunrise =SunTimes.getSunriseTimeUTC(year, month, date, longitude, latitude, SunTimes.ZENITH);
			
			return sunrise;
		} catch (SunTimesException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
		
		// Time sunset = st1.getSunsetTimeUTC(year, month, day, latitude, longitude,
		// suryaDev.getZenith());

		// LocalDateTime sunriseTime = convertToLocalDateTime(sunrise);
		// LocalDateTime sunsetTime = convertToLocalDateTime(sunset);

		// Log or use sunriseTime and sunsetTime as needed
		// System.out.println("Sunrise: " + sunrise);
		// System.out.println("Sunset: " + sunset);

		// Returning sunrise time for simplicity, you may choose to return both times
		// return sunrise;
	}

}