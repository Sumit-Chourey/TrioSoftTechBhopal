package com.suntime.service;

import com.suntime.entities.Watch;
import com.web_tomorrow.utils.suntimes.SunTimes;
import java.lang.reflect.Field;

import org.springframework.stereotype.Component;

@Component
public class Watchprivateserivce {

	//Method for Sun Degree per hour
	public static String degreePerHour(Watch watch) {
		try {
			Field degPerHourField = SunTimes.class.getDeclaredField("DEG_PER_HOUR");
			degPerHourField.setAccessible(true);
			double degreeValue = degPerHourField.getDouble(watch);
			String result = "The value of Degree per hour: " + degreeValue;
			return result;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}

	
	
	//Method for Type SunRise and SunSet
	public static String UseReflect(Watch watch) {
		try {
			// Get the Field object for TYPE_SUNRISE
			Field sunriseField = SunTimes.class.getDeclaredField("TYPE_SUNRISE");

			// Make the field accessible
			sunriseField.setAccessible(true);

			// Get the value of TYPE_SUNRISE
			int sunriseValue = (int) sunriseField.get(null);
			// System.out.println("Value of TYPE_SUNRISE: " + sunriseValue);

			// Get the Field object for TYPE_SUNSET
			Field sunsetField = SunTimes.class.getDeclaredField("TYPE_SUNSET");

			// Make the field accessible
			sunsetField.setAccessible(true);

			// Get the value of TYPE_SUNSET
			int sunsetValue = (int) sunsetField.get(null);
			// System.out.println("Value of TYPE_SUNSET: " + sunsetValue);

			String result = "Value of TYPE_SUNRISE: " + sunriseValue + ", Value of TYPE_SUNSET: " + sunsetValue;

			return result;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}
}
