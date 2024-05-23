package com.triosoft.service;

import java.util.List;

import org.springframework.stereotype.Component;


import com.triosoft.entities.TrioSoft_Info;


@Component
public interface TrioServices {
	

	//Different Methods for All Operation
	
	public List<TrioSoft_Info> getinfo();
	
	
	public TrioSoft_Info addemp(TrioSoft_Info triosoft_info);
	

	public void deleteemp(Integer emp_Id);


}
