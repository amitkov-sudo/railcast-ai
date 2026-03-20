package com.railcast.api.repository;

import com.railcast.api.model.TrainEvent;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TrainEventRepository extends JpaRepository<TrainEvent, Long> {
}
