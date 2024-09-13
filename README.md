# IOTify-DESE-Workshop
This repository contains ReadMe and Code Files for the Project IOTify DESE Workshop submitted as mini-project under the coursework Design for IOT at IISc




<!-- PROJECT LOGO -->
<br />

  <h3 align="center">IOTify-DESE-Workshop</h3>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#Procedure Overview">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

    IOTify DESE workshop Project aims to be able to establish a prototype for monitoring industrial equipments by collecting sensor data, analysing it and transfer the data to a user interpretable dashboard.


### Built With

* [MQTT]
* [Nordic Development Board - NRF52840]
* [Sensors - Hall Sensor,MPU6050,Nicla Voice]


<!-- ROADMAP -->
## Procedural Overview

1. FFT of Vibrational Data to recognize motor Fault:
   We use FFT to map the occurence of a particular motor fault to the FFT component appearing at a particular frequency.
2.Air Lock condition recognition using Nicla voice
   Nicla voice is an NDP aided development board used to run edge AI based models to recognize voices.
   We have trained and generated a model with sounds during pumping action with and without airlock.
  Further we run the build model along with our custom code to spot the two scenarios.
3. Stall current recognition through use of Hall-sensor
   Stall current is generated when motor jam occurs where it draws current with performing the required rotary action hence causing all current to get dissipated     as heat burning the rotor windings.
4.All the analysed data are transferred over to a custom Dashboard using MQTT that can indicate different fault scenarios.


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Basati Sivakrishna ]()
* [Professor : T V Prabhakar ]()
* []()


