package com.triosoft.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Statement;

import org.junit.runner.Result;
import org.springframework.stereotype.Repository;

import com.triosoft.entities.Employee;

@Repository
public class EmployeeDao {

	public int addEmployee(Employee employee) {

		try {
			//All Print statement is for debugging purpose.
			
			System.out.println("1");
			//for Loading the Driver and Class is a class
			Class.forName("com.mysql.cj.jdbc.Driver");
			System.out.println("2");
			//Connection is for creating connection is a interface ,Driver manager is a class
			Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/triosoftdb", "root",
					"8446103055");
			System.out.println("3");

			//Write a query
			String qu = ("insert into empdetail values(?,?,?)");
			System.out.println("4");
			
			//For preparing statement is to use insert values using methods
			PreparedStatement pt = con.prepareStatement(qu);
			System.out.println("5");

			pt.setInt(1, employee.getId());
			System.out.println("6");
			pt.setString(2, employee.getName());
			System.out.println("7");
			pt.setString(3, employee.getCity());
			System.out.println("8");
			//For execute Query
			return pt.executeUpdate();

		} catch (Exception e) {
			System.out.println("Exception is here..." + e);
			
			
		}

		return 0;
	}

}
