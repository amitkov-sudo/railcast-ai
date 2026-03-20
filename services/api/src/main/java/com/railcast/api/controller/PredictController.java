package com.railcast.api.controller;

import com.railcast.api.dto.PredictResponse;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PredictController {

    @GetMapping("/predict")
    public PredictResponse predict() {
        return new PredictResponse(
                "Prediction endpoint placeholder",
                "Will integrate with ml-inference service."
        );
    }
}
