package com.triosoft.entities;


import org.springframework.stereotype.Component;

@Component
public class SuryaDev {

	private int year;
	private int month;
	private int date;

	private double latitude;
	private double longitude;
	private double zenith;

	
	
	public SuryaDev(int year, int month, int date, double latitude, double longitude, double zenith) {
		super();
		this.year = year;
		this.month = month;
		this.date = date;
		this.latitude = latitude;
		this.longitude = longitude;
		this.zenith = zenith;
	}



	public int getYear() {
		return year;
	}



	public void setYear(int year) {
		this.year = year;
	}



	public int getMonth() {
		return month;
	}



	public void setMonth(int month) {
		this.month = month;
	}



	public int getDate() {
		return date;
	}



	public void setDate(int date) {
		this.date = date;
	}



	public double getLatitude() {
		return latitude;
	}



	public void setLatitude(double latitude) {
		this.latitude = latitude;
	}



	public double getLongitude() {
		return longitude;
	}



	public void setLongitude(double longitude) {
		this.longitude = longitude;
	}



	public double getZenith() {
		return zenith;
	}



	public void setZenith(double zenith) {
		this.zenith = zenith;
	}



	//No0 argu constructor
	public SuryaDev() {
		super();
		// TODO Auto-generated constructor stub
	}



}
