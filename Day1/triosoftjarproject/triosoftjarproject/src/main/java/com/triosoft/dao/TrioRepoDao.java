package com.triosoft.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.triosoft.entities.TrioSoft_Info;


@Repository
public interface TrioRepoDao extends JpaRepository<TrioSoft_Info, Integer> {

	//This interface extends Jpa Repo for performing CRUD Operation into contacted Database.
	//Due to this Database Migration is easy.
	
}
