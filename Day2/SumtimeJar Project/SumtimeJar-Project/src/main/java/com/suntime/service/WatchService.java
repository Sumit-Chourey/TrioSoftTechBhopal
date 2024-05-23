package com.suntime.service;

import org.springframework.stereotype.Service;

import com.suntime.entities.Watch;
import com.web_tomorrow.utils.suntimes.SunTimes;
import com.web_tomorrow.utils.suntimes.SunTimesException;
import com.web_tomorrow.utils.suntimes.Time;

@Service
public class WatchService {

	// Business Logic of SunRise Calculation
	public Time SunRiseTime(Watch watch) {

		int year = watch.getYear();
		int month = watch.getMonth();
		int date = watch.getDate();
		double latitude = watch.getLatitude();
		double longitude = watch.getLongitude();
		double Zenith = watch.getZenith();

		try {
			Time sunrise = SunTimes.getSunriseTimeUTC(year, month, date, longitude, latitude, SunTimes.ZENITH);

			System.out.println("----------------------------------------------------------------------------------");
			System.out.println("Sunset Of Day : " + sunrise);
			System.out.println("----------------------------------------------------------------------------------");
			return sunrise;

		} catch (SunTimesException e) {

			e.printStackTrace();
		}

		return null;
	}

	// Business Logic of SunSet Calculation

	public Time SunSetTime(Watch watch) {

		int year = watch.getYear();
		int month = watch.getMonth();
		int date = watch.getDate();
		double latitude = watch.getLatitude();
		double longitude = watch.getLongitude();
		double Zenith = watch.getZenith();

		try {
			Time sunset = SunTimes.getSunsetTimeUTC(year, month, date, longitude, latitude, SunTimes.ZENITH);
			System.out.println("----------------------------------------------------------------------------------");
			System.out.println("Sunrise Of Day :  " + sunset);
			System.out.println("----------------------------------------------------------------------------------");

			return sunset;

		} catch (SunTimesException e) {

			e.printStackTrace();
		}

		return null;

	}

	// Business Logic of Sun NauticalZenith Calculation
	public double NauticalZenith(Watch watch) {

		double nauticalZenith = SunTimes.NAUTICAL_ZENITH;
		System.out.println("----------------------------------------------------------------------------------");
		System.out.println(" Sun Nautical Zenith : " + nauticalZenith);
		System.out.println("----------------------------------------------------------------------------------");
		return nauticalZenith;

	}

	// Business Logic of Sun CivilZenith Calculation
	public double CivilZenith(Watch watch) {

		double civilZenith = SunTimes.CIVIL_ZENITH;
		System.out.println("----------------------------------------------------------------------------------");
		System.out.println("Sun Civil Zenith : " + civilZenith);
		System.out.println("----------------------------------------------------------------------------------");
		return civilZenith;

	}

	// Business Logic of Sun AstronomicalZenith Calculation
	public double AstroZenith(Watch watch) {

		double astronomicalzenith = SunTimes.ASTRONOMICAL_ZENITH;
		System.out.println("----------------------------------------------------------------------------------");
		System.out.println("Sun Astronomial Zenith : " + astronomicalzenith);
		System.out.println("----------------------------------------------------------------------------------");
		return astronomicalzenith;

	}

}
