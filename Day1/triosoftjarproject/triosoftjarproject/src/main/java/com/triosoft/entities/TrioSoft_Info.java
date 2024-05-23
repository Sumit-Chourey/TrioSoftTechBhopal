package com.triosoft.entities;


import org.springframework.lang.NonNull;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
@Getter@Setter@AllArgsConstructor@NoArgsConstructor
@Entity
@Table(name="triosoft_emp_information")
public class TrioSoft_Info{

	
	//All Properties of Table
	//@Id,@NonNull all are Validations for each properties.
	
	@Id  @GeneratedValue(strategy = GenerationType.AUTO)
	private int emp_Id ;
	@NonNull
	private String emp_position;
	
 	private String emp_Tech;
	@NonNull
	private int emp_Mob;
	
	
	
	/*
	
	//Getter and Setter for 
	public int getEmp_Id() {
		return emp_Id;
	}



	public void setEmp_Id(int emp_Id) {
		this.emp_Id = emp_Id;
	}



	public String getEmp_position() {
		return emp_position;
	}



	public void setEmp_position(String emp_position) {
		this.emp_position = emp_position;
	}



	public String getEmp_Tech() {
		return emp_Tech;
	}



	public void setEmp_Tech(String emp_Tech) {
		this.emp_Tech = emp_Tech;
	}



	public int getEmp_Mob() {
		return emp_Mob;
	}



	public void setEmp_Mob(int emp_Mob) {
		this.emp_Mob = emp_Mob;
	}
	*/

	/*
	public TrioSoft_Info(int emp_Id, String emp_position, String emp_Tech, int emp_Mob) {
		super();
		this.emp_Id = emp_Id;
		this.emp_position = emp_position;
		this.emp_Tech = emp_Tech;
		this.emp_Mob = emp_Mob;
	}
	*/

	/*
	public TrioSoft_Info() {
		super();
		
	}
	*/
	@Override
	public String toString() {
		return "TrioSoft_Info [emp_Id=" + emp_Id + ", emp_position=" + emp_position + ", emp_Tech=" + emp_Tech
				+ ", emp_Mob=" + emp_Mob + "]";
	}

	
}
