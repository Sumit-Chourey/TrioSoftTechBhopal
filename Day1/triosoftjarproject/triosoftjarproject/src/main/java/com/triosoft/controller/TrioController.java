package com.triosoft.controller;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDateTime;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.triosoft.entities.Employee;
import com.triosoft.entities.SuryaDev;
import com.triosoft.entities.TrioSoft_Info;
import com.triosoft.service.TrioServices;
import com.triosoft.service.impl.EmployeeService;
import com.triosoft.service.impl.SunTimesService;
import com.web_tomorrow.utils.suntimes.Time;

//Controller Class TO Handle the Incoming Request

@RestController
public class TrioController {

	@Autowired
	private TrioServices trioservices;

	@Autowired
	private EmployeeService employeeservice;

	@Autowired
	private SunTimesService suntimesservice;

	// API for adding information of Employee
	@PostMapping("/empaddinfo")
	public TrioSoft_Info addCourse(@RequestBody TrioSoft_Info triosoft_info) {
		return this.trioservices.addemp(triosoft_info);

	}

	// API for Show the list of all employee Information
	@GetMapping("/emplist")
	public List<TrioSoft_Info> getinfo() {
		return this.trioservices.getinfo();
	}

	// API for Deleting the employee Information one by one
	@DeleteMapping("/emplist/{emp_Id}")
	public void deleteemp(@PathVariable int emp_Id) {
		this.trioservices.deleteemp(emp_Id);

	}
	//for external Mysql jar file 
	@PostMapping("/empdetailadd")
	public int addEmployee(@RequestBody Employee employee) {
		return employeeservice.addEmployee(employee);

	}
		
	//For Suntime jar file
	@GetMapping("/suntimes")
	public Time getSunTimes(@RequestBody SuryaDev suryaDev) {
		return suntimesservice.calculateSunTimes(suryaDev);
	}

	/*
	 * @GetMapping("/suntime") public int gettime(@RequestBody SuryaDev suryadev) {
	 * return employeeservice.addEmployee(suryadev);
	 * 
	 * }
	 */

}
