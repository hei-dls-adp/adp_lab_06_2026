
<b style='color:red;'>Do not read this file</b>

### What is annex 11 ?

Annex 11 provides GMP guidance for the use, validation, and lifecycle management of computerized systems in pharmaceutical manufacturing.

:bulb: In short, if Node-RED is used in a GMP context, which is generally the case for most products related to the pharmaceutical industry, the annex must be complied with to deliver a product. This applies not only to the final testing phase, but throughout the entire product development process, including the development phase.

#### Scope and Purpose

Annex 11 applies to all forms of computerized systems used in GMP-regulated activities, including software and hardware components that fulfill specific functionalities. Its purpose is to ensure that when a computerized system replaces a manual operation, there is no decrease in product quality, process control, or quality assurance, and no increase in overall process risk. The guidance aligns with EU GMP principles and has been adopted by Health Canada with terminology adjustments for Canadian regulations. 

#### Validation and IT Infrastructure
Computerized systems must be validated, and the supporting IT infrastructure must be qualified. Validation ensures that the system consistently performs as intended, while qualification confirms that the hardware and network environment meet operational requirements. Decisions on the extent of validation and data integrity controls should be based on a documented risk assessmentof the system. 

#### Risk Management
Risk management is a central principle in Annex 11. It should be applied throughout the lifecycle of the computerized system, considering patient safety, data integrity, and product quality. This includes assessing risks during system design, implementation, operation, and retirement, and implementing controls proportionate to the identified risks. 

#### Personnel Responsibilities
Annex 11 emphasizes close cooperation among all relevant personnel, including Process Owners, System Owners, Qualified Persons, and IT staff. Each individual should have appropriate qualifications, defined responsibilities, and access levels to perform their duties effectively. Proper training and documentation of responsibilities are essential for compliance. 

#### Lifecycle Considerations
The guidance covers both project and operational phases of computerized systems. This includes system specification, development, testing, deployment, maintenance, and eventual decommissioning. Annex 11 encourages flexibility in approach, allowing organizations to adopt alternative methods if scientifically justified, while maintaining compliance with GMP requirements. 

#### Key Takeaways
•	Annex 11 ensures safe, reliable, and compliant use of computerized systemsin pharmaceutical manufacturing.
•	Validation, qualification, and risk management are mandatory throughout the system lifecycle.
•	Personnel roles and responsibilities must be clearly defined and documented.
•	The guidance allows flexibility for new technologies and alternative approaches, provided they maintain product quality and regulatory compliance. 



### IQ OQ PQ
In a GMP, **Good Manufacturing Practice**, context, validation and qualification are closely related but not interchangeable. The distinction is important because regulators like the European Medicines Agency and U.S. Food and Drug Administration expect both to be properly defined and documented.

#### Qualification, Equipment, Facilities, Utilities.
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

#### Validation (Processes, Methods, Systems)
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

---

# La question à deux balles.

### Are there any certified devices?
No, a device, such as an O₂ analyzer, is not, in itself, GMP certified.

#### Pourquoi ?
Les GMP, Good Manufacturing Practice, — définies notamment par European Medicines Agency et U.S. Food and Drug Administration — ne certifient pas des équipements individuels.

Elles évaluent un système qualité global, site, processus, organisation.
•	❌ Pas de, certificat GMP, pour un capteur O₂
•	✅ Mais utilisation conforme aux GMP possible (et exigée)

🧪 Ce qu’on exige réellement pour un appareil (ex: mesure O₂)
Pour qu’un appareil soit acceptable en environnement GMP, il doit être :
1.  Qualifié
    •	IQ / OQ / PQ réalisés
    •	Installation correcte, fonctionnement vérifié, performance démontrée
2.  Étalonné (calibré)
    •   Avec des standards traçables (souvent ISO/NIST)
    •   À fréquence définie
3.  Maintenu
    •	Plan de maintenance documenté
    •	Gestion des pannes et dérives
4.  Adapté à l’usage (fit for purpose)
    •	Précision suffisante pour le process
    •  	Plage de mesure appropriée
5.  Intégré dans le système qualité
    •	Procédures (SOP)
    •	Enregistrements (logs, audits)
    •	Formation des opérateurs

⚠️ Ce qui peut prêter à confusion
Certains fournisseurs disent :
•	“GMP compliant”
•	“Designed for GMP environments”
👉 Cela signifie généralement :
•	matériaux compatibles (ex: inox, cleanroom)
•	documentation fournie pour qualification
•	conformité à certaines normes (ex: ISO)
Mais ce n’est pas une certification GMP officielle.

🧩 En résumé
•	Les entreprises/sites peuvent être certifiés GMP
•	Les appareils ne le sont pas
•	Mais ils doivent être :
👉 qualifiés + calibrés + contrôlés pour être utilisés en GMP


### Qualification
Oui — prenons un cas très concret en GMP avec un capteur O₂ de chez Hamilton Company, typiquement utilisé en bioprocédés (fermentation, production biotech).

🧪 Exemple réel : capteur O₂ Hamilton en bioproduction GMP
🔧 Le matériel
Un exemple typique est un capteur de type VisiFerm ou OxyFerm :
•	Capteur d’oxygène dissous (DO) installé sur un bioréacteur
•	Mesure en continu l’O₂ pendant la culture cellulaire
•	Compatible CIP/SIP, autoclavable, inox pharma  
👉 Typiquement utilisé dans :
•	production de vaccins
•	anticorps monoclonaux
•	fermentation microbienne

⚙️ Étape 1 — Qualification, selon GMP
Avant toute utilisation, le capteur est qualifié dans son environnement :
IQ (Installation)
•	Vérification du montage sur le bioréacteur (port PG13.5, étanchéité, matériaux)
•	Vérification documentation fournisseur (certificats matériaux, numéro de série)
OQ (Fonctionnement)
•	Test de réponse du capteur (air = 100% sat, azote = 0%)
•	Vérification plage (ex: 0–100% saturation ou ppm)  
PQ (Performance)
•	Test en conditions réelles (culture)
•	Vérifier que la mesure est stable et cohérente avec le procédé

👉 À ce stade, on ne valide pas encore le process — uniquement que le capteur fonctionne correctement dans ce système particulier-.

🧪 Étape 2 — Calibration / étalonnage
Très concret :
•	Calibration 2 points :
o	0% O₂ (azote)
o	100% O₂ (air ou gaz étalon)
•	Fréquence définie (avant batch ou périodique)
•	Traçabilité des gaz utilisés
👉 Exemple similaire en médical : les capteurs O₂ doivent être calibrés régulièrement et stabilisés avant usage  

🧬 Étape 3 — Validation du procédé
Une fois le capteur qualifié :
👉 Il devient critique dans la validation process
Exemple :
•	Spécification : DO doit rester à 40% ± 5%
•	Le capteur fournit la donnée utilisée pour :
o	réguler l’aération
o	déclencher des actions automatiques
Donc lors de la process validation :
•	tu démontres que :
o	le procédé maintient le DO dans les specs
o	ET que la mesure est fiable (car capteur qualifié)

📁 Documentation GMP typique
Pour un audit, tu dois avoir :
•	Certificats fournisseur (matériaux, parfois FDA compliance)
•	Dossier de qualification (IQ/OQ/PQ)
•	SOP de calibration
•	Historique des calibrations
•	Gestion des dérives / déviations
👉 Les capteurs Hamilton ont souvent :
•	numéro de série
•	certificats de test usine
•	conformité matériaux (ex: acier poli Ra < 0.4 µm)  

⚠️ Point clé (très important en audit)
Même si le capteur :
•	est haut de gamme
•	a des certificats (CE, parfois FDA, ATEX)
👉 Ce n’est toujours PAS un “capteur GMP certifié”
Mais :
•	✔️ il est GMP compatible
•	✔️ il est qualifiable
•	✔️ il fournit la base pour la validation

🧩 Résumé ultra concret
Dans ton exemple Hamilton :
1.	Tu achètes un capteur O₂ (ex: VisiFerm)
2.	Tu fais IQ/OQ/PQ → qualification
3.	Tu le calibres régulièrement
4.	Tu l’utilises dans ton process
5.	Tu valides ton procédé → validation
👉 Donc :
le capteur n’est pas GMP → ton utilisation du capteur l’est


### Audi GMP from ChatGPT
Oui — il y a plusieurs pièges très fréquents en audit GMP autour des capteurs O₂ (comme ceux de Hamilton). Les inspecteurs ne testent pas le capteur lui-même, mais la manière dont tu le maîtrises dans ton système qualité.
Voici les plus classiques 👇

⚠️ Pièges fréquents en audit GMP (capteur O₂)
1. ❌ “Le capteur est qualifié” mais pas le système complet
Très courant :
•	IQ/OQ faits sur le capteur seul
•	mais pas sur :
o	la boucle de régulation (capteur → automate → vanne → process)
o	le bioréacteur entier
👉 Problème GMP :
On ne qualifie pas un instrument isolé, mais un système d’usage
✔️ Attendu :
qualification du process control loop complet

2. ❌ Calibration non tracée ou incomplète
Exemples de non-conformités :
•	pas de certificat des gaz étalons
•	pas de traçabilité métrologique (ISO/NIST)
•	fréquence de calibration “historique mais non justifiée”
👉 En audit, c’est un classique critique
✔️ Attendu :
•	standards traçables
•	SOP claire
•	justification de la fréquence

3. ❌ “As found / as left” absent
Les inspecteurs aiment ce point :
•	tu calibres le capteur
•	mais tu ne documentes pas :
o	état AVANT calibration (as found)
o	état APRÈS calibration (as left)
👉 Risque :
tu ne peux pas détecter une dérive progressive
✔️ GMP attendu :
preuve de dérive et impact potentiel sur lots produits

4. ❌ Alarmes process non justifiées
Exemple :
•	DO doit rester à 40%
•	mais alarmes réglées “empiriquement”
👉 problème :
pas de justification scientifique (no lifecycle approach)
✔️ attendu :
•	justification basée sur développement process (DoE / validation)

5. ❌ Mauvaise gestion des sondes en place (drift ignoré)
Cas typique avec capteurs O₂ :
•	la sonde dérive lentement
•	mais est recalibrée uniquement “périodiquement”
•	sans trend analysis
👉 problème GMP :
absence de continuous monitoring of performance
✔️ attendu :
•	trending des calibrations
•	détection dérive avant impact produit

6. ❌ Remplacement de sonde sans requalification
Très fréquent en production :
•	changement de capteur Hamilton (même modèle)
•	mais pas de re-OQ / impact assessment
👉 erreur classique :
“same model = same performance”
✔️ attendu :
•	évaluation d’impact
•	parfois re-OQ partielle

7. ❌ Données électroniques non maîtrisées (CSV)
Les capteurs sont souvent connectés à SCADA/DCS.
Problèmes fréquents :
•	accès utilisateurs non contrôlé
•	modifications de paramètres sans audit trail
•	données brutes non sécurisées
👉 domaine critique :
Computer System Validation
✔️ attendu :
•	audit trail actif
•	gestion des droits
•	intégrité des données (ALCOA+)

🧠 Le piège global le plus important
👉 Beaucoup de sites pensent :
“Le capteur est bon, donc la mesure est GMP”
❌ Faux en GMP
✔️ Réalité :
La GMP ne valide pas l’instrument — elle valide la fiabilité de la décision basée sur l’instrument

🧩 Résumé simple
Les inspecteurs cherchent surtout :
•	qualification système complète (pas isolée)
•	calibration traçable et justifiée
•	contrôle du drift (pas juste calibration périodique)
•	intégrité des données (CSV)
•	impact process toujours évalué


### URS - PQ
-   I test if the sensor returns the correct information.
-   I test if the robot allows me to return the correct information.
-   I test if I can correctly record the positions of the robot and the sensor.
-   I test if I can read the information into Excel.
-   I check the sensor type and its serial number.
-   I test on two different nests if the sensor and axis information is consistent with Excel.
-   I take two test specimens and check if they are properly supported before being placed.
-   I record the times and nest numbers.
End of URS


### Bonus OPC UA
Read OPC UA @ 192.168.0.33
[OPC UA Tutorial: Connect and Exchange Data with Industrial Equipmen](https://flowfuse.com/blog/2025/07/reading-and-writing-plc-data-using-opc-ua/)
La température de l’air? En plus du temps.
À montrer en démo via OPC ua.
