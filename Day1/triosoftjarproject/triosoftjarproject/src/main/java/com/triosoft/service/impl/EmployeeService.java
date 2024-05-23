package com.triosoft.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.triosoft.dao.EmployeeDao;
import com.triosoft.entities.Employee;

@Service
public class EmployeeService {

	@Autowired
	private EmployeeDao employeedao;
	
	public int addEmployee(Employee employee)
	{
		return employeedao.addEmployee(employee);
	}
	
}
