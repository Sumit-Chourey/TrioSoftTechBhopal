package com.suntime.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.suntime.entities.Watch;
import com.suntime.service.WatchService;
import com.suntime.service.Watchprivateserivce;
import com.web_tomorrow.utils.suntimes.Time;

@RestController
public class SunTimeController {

	// Spring Object bring here through Autowired.
	@Autowired
	private WatchService watchService;
	
	@Autowired
	private Watchprivateserivce watchprivateservice; 
	

	// All Method API's

	@PostMapping("/sunrisetimes")
	public Time getSunRiseTimes(@RequestBody Watch watch) {
		return watchService.SunRiseTime(watch);
	}

	@PostMapping("/sunsettime")
	public Time getSunSetTimes(@RequestBody Watch watch) {
		return watchService.SunSetTime(watch);
	}

	@PostMapping("/sunnauticalzenith")
	public double getSunZenith(@RequestBody Watch watch) {
		return watchService.NauticalZenith(watch);
	}

	@PostMapping("/suncivilzenith")
	public double getSunSetTime3(@RequestBody Watch watch) {
		return watchService.CivilZenith(watch);
	}

	@PostMapping("/sunastrozenith")
	public double getAstroenith(@RequestBody Watch watch) {
		return watchService.AstroZenith(watch);
	}
	
	
	//All Private variable Access API's
	

	@PostMapping("/sunref")
	public  String getSunRiseTimes1(@RequestBody Watch watch) {
		return Watchprivateserivce.UseReflect(watch);
	
	}
	
	@PostMapping("/sundegreeperhour")
	public  String getdegreeperhour(@RequestBody Watch watch) {
		return Watchprivateserivce.degreePerHour(watch);
	
	}

}
