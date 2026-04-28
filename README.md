<h1>
  <img src="./img/hei-en.png" alt="HEI-Vs Logo" width="350">
  <br> Automation in development and production
    <h2>Interfaces</h2>
  <br>
</h1>

Author: [Cédric Lenoir](mailto:cedric.lenoir@hevs.ch)

# adp_lab_06_2026, annex 11

This final module is divided into three parts:
- The first, theoretical part, lasts 2 x 45 minutes.
- Then two practical modules, each lasting 4 x 45 minutes.
- 
Between the two practical modules, there will be a module on Grafana and InfluxDB. Practical work guidelines, including the URS for the practical part, will be provided in advance so that you can prepare it. [Here is a short exemple](Modules_8_10_11.md).

---

## What is annex 11 ?

Annex 11 provides GMP guidance for the use, validation, and lifecycle management of computerized systems in pharmaceutical manufacturing.

:bulb: In short, if Node-RED is used in a GMP context, which is generally the case for most products related to the pharmaceutical industry, the annex must be complied with to deliver a product. This applies not only to the final testing phase, but throughout the entire product development process, including the development phase.

### Scope and Purpose

Annex 11 applies to all forms of computerized systems used in GMP-regulated activities, including software and hardware components that fulfill specific functionalities. Its purpose is to ensure that when a computerized system replaces a manual operation, there is no decrease in product quality, process control, or quality assurance, and no increase in overall process risk. The guidance aligns with EU GMP principles and has been adopted by Health Canada with terminology adjustments for Canadian regulations. 

### Validation and IT Infrastructure
Computerized systems must be validated, and the supporting IT infrastructure must be qualified. Validation ensures that the system consistently performs as intended, while qualification confirms that the hardware and network environment meet operational requirements. Decisions on the extent of validation and data integrity controls should be based on a documented risk assessmentof the system. 

### Risk Management
Risk management is a central principle in Annex 11. It should be applied throughout the lifecycle of the computerized system, considering patient safety, data integrity, and product quality. This includes assessing risks during system design, implementation, operation, and retirement, and implementing controls proportionate to the identified risks. 

### Personnel Responsibilities
Annex 11 emphasizes close cooperation among all relevant personnel, including Process Owners, System Owners, Qualified Persons, and IT staff. Each individual should have appropriate qualifications, defined responsibilities, and access levels to perform their duties effectively. Proper training and documentation of responsibilities are essential for compliance. 

### Lifecycle Considerations
The guidance covers both project and operational phases of computerized systems. This includes system specification, development, testing, deployment, maintenance, and eventual decommissioning. Annex 11 encourages flexibility in approach, allowing organizations to adopt alternative methods if scientifically justified, while maintaining compliance with GMP requirements. 

### Key Takeaways
•	Annex 11 ensures safe, reliable, and compliant use of computerized systemsin pharmaceutical manufacturing.
•	Validation, qualification, and risk management are mandatory throughout the system lifecycle.
•	Personnel roles and responsibilities must be clearly defined and documented.
•	The guidance allows flexibility for new technologies and alternative approaches, provided they maintain product quality and regulatory compliance. 



## IQ OQ PQ
In a GMP, **Good Manufacturing Practice**, context, validation and qualification are closely related but not interchangeable. The distinction is important because regulators like the European Medicines Agency and U.S. Food and Drug Administration expect both to be properly defined and documented.

### Qualification, Equipment, Facilities, Utilities.
Qualification is about proving that equipment, systems, or facilities are installed and operate correctly.
It answers: **Is this system fit for use?**
Typical stages:
•	IQ, **Installation Qualification**.
Verifies equipment is installed according to specifications.
•	OQ, **Operational Qualification**
Confirms the system operates as intended under controlled conditions.
•	PQ, **Performance Qualification**
Demonstrates consistent performance in real-world conditions.
Examples:
•	HVAC system in a cleanroom
•	Water purification system
•	Manufacturing equipment (e.g., tablet press)

### Validation (Processes, Methods, Systems)
Validation ensures that a process or method consistently produces results meeting predetermined quality criteria.
It answers: “Does this process reliably produce the correct outcome?”
Types of validation:
•	Process Validation – manufacturing processes
•	Analytical Method Validation – lab testing methods
•	Cleaning Validation – ensures no cross-contamination
•	Computer System Validation (CSV) – software systems
Example:
•	Tablet manufacturing process consistently producing correct dosage and quality

### Key Difference
•	Qualification = “The **tool** works”
•	Validation = “The **process** using the tool works”

#### How They Fit Together
Qualification is actually a subset of validation:
1.	You qualify equipment and systems first
2.	Then you validate the processes that use them

Without proper qualification, process validation is not reliable.

**Quick Comparison**

|Aspect	|Qualification	|Validation|
|-------|---------------|----------|
|Focus	|Equipment, facilities, utilities|	Processes, methods, systems|
|Purpose|Ensure system works correctly	|Ensure consistent output quality
|Scope	|Narrower	|Broader
|Examples	|HVAC, water system, machines	|Manufacturing process, test method
|Relationship	|Part of validation lifecycle	|Encompasses qualification|

[More details on GMP on the next page](GMP.md).

<!-- end of file -->