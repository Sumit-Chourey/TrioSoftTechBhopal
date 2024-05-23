package com.triosoft.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


import com.triosoft.dao.TrioRepoDao;
import com.triosoft.entities.TrioSoft_Info;
import com.triosoft.service.TrioServices;


@Service
public class TrioServiceImpl implements TrioServices{

	@Autowired
	private TrioRepoDao triorepodao;
	
	//Implementation all Abstract Methods.
	
	
	//Method for Adding
	@Override
	public TrioSoft_Info addemp(TrioSoft_Info triosoft_info) {
		
		return triorepodao.save(triosoft_info);
	}
	
	
	//Method for Getting
	@Override
	public List<TrioSoft_Info> getinfo() {
		
		return triorepodao.findAll();
	}
	
	
	//Method for Removing
	@Override
	public void deleteemp(Integer emp_Id) {
		
		 triorepodao.deleteById(emp_Id);;
	}
	
	
	
	
	
}
