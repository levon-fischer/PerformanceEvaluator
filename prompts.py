##################
# Prep Constants #
##################

SYSTEM = \
"""
You are a panel member for an Air Force awards board. Your job is to grade each performance statement
in an award nomination using the user's grading criteria and priorities.
"""

OVERVIEW = \
"""
Performance Statements are efficient, increase clarity, and improve the ability to understand an
airman’s performance correctly and equitably.
Performance Statements: Guidance for writing Performance Statements is deliberately not overly
prescriptive to enable flexibility and freedom when capturing performance. There are two basic
principles:
    - Standalone. Each Performance Statement is a standalone sentence and includes.
        o 1) action and
        o 2) at least one of the following: impact or results/outcome.
    - Readability. Performance Statements are plain language and avoid using uncommon
acronyms and abbreviations. If using acronyms and abbreviations, only utilize those
identified on the approved Air Force Acronym and Abbreviation List, unless noted by an
approved category.
"""

PERFORMANCE_LEVELS = \
"""
Membership
Membership-level performance infers tactical-level activities on a small scale. These actions are the
building blocks toward larger accomplishments. These efforts depict contributions of a junior Airman, an
apprentice, or the expected daily tasking of someone higher ranked:
    - Job performance in your primary duty includes helping, assisting, participating, and
supporting.
    - Self-improvement describes short training courses, college classes, exams like the College-
Level Examination Program (CLEP)—things that would be considered the building blocks toward
more significant educational accomplishments.
    - Base and community involvement includes helping, assisting, participating, and supporting.
    - Mentoring includes your impact on the people in your charge. Supervisory Supervisory-level
performance is tactical or operational in nature. These efforts depict actions normally
accomplished by NCOs or journeymen.
    - Job performance includes oversight or supervision of a small group, small team, or small
program and taking charge of tactical activities.
    - Self-improvement describes short in-residence or correspondence courses or certifications
and completion of career development courses, and completion of the Community College of
the Air Force (CCAF) degree.
    - Base and community involvement includes oversight or supervision of small groups or small
teams and organizing/leading small-scale base and community activities.
    - Mentoring includes impact on the Airmen in your charge and expansion to those around you.

Management
Management-level is more operational in nature. These efforts depict activities normally accomplished
by senior NCOs or craftsmen:
    - Job performance includes leading multiple teams, multiple programs, and/or large populations
and organizing, directing, planning, and controlling large-scale projects.
    - Self-improvement efforts describe significant educational and training milestones, long in-
residence or correspondence courses, career development course completion with outstanding
grades and distinction, and completion of undergraduate degrees.
    - Base and community involvement includes leading multiple teams, multiple programs, and/or
large populations and organizing, directing, planning, and controlling large-scale projects.
    - Mentoring at the management level depicts activities with influence over large groups of
Airmen inside and outside the organization and significant involvement in professional
development.

Leadership
Leadership-level performance depicts strategic involvement. These are functions expected from a
leader. Remember, anyone has the potential to perform at the leadership level:
    - Job performance verbiage includes organizing, directing, planning, and supervising large
programs and/or vast populations and assuming responsibility over major operations.
    - Self-improvement describes higher-level educational achievements and/or significant in-
residence courses and completion of graduate degrees.
    - Base and community involvement includes organizing, directing, planning, and supervising
large base and community programs, overseeing vast operations, and assuming responsibility
over vast populations.
    - Mentoring in this category demonstrates influence over hundreds of Airmen throughout the
base and involvement organizing professional development panels and seminars. These leaders
offer comments at graduations and other professional development venues.
"""

ALQ = \
"""
Airman Leadership Qualities (ALQ)

The major performance areas (MPA) and Airman leadership qualities (ALQ) are:

(MPA) Executing the Mission
• (ALQ) Job Proficiency: Demonstrates knowledge and professional skill in assigned duties, achieving
positive results and impact in support of the mission.
• (ALQ) Initiative: Assesses and takes independent or directed action to complete a task or mission
that influences the mission or organization.
• (ALQ) Adaptability: Adjusts to changing conditions, to include plans, information, processes,
requirements and obstacles in accomplishing the mission.

(MPA) Leading People
• (ALQ) Inclusion and Teamwork: Collaborates effectively with others to achieve an inclusive climate in
pursuit of a common goal or to complete a task or mission.
• (ALQ) Emotional Intelligence: Exercises self-awareness, manages their own emotions effectively;
demonstrates an understanding of others’ emotions, and appropriately manages relationships.
• (ALQ) Communication: Articulates information in a clear and timely manner, both verbally and non-
verbally, through active listening and messaging tailored to the appropriate audience.

(MPA) Managing Resources
• (ALQ) Stewardship: Demonstrates responsible management of assigned resources, which may include
time, equipment, people, funds and/or facilities.
• (ALQ) Accountability: Takes responsibility for the actions and behaviors of self and/or team;
demonstrates reliability and transparency.

(MPA) Improving the Unit
• (ALQ) Decision Making: Makes well-informed, effective and timely decisions under one’s control that
weigh constraints, risks, and benefits.
• (ALQ) Innovation: Thinks creatively about different ways to solve problems, implements
improvements and demonstrates calculated risk-taking.

Each Airman leadership quality is assessed on a five-point scale of proficiency levels:
1) does not meet expectations
2) developing
3) proficient
4) highly proficient
5) outstanding.

They are currently grade independent, understanding raters will account for the relative expectation
based on rank and Air Force specialty code.
"""

########
# Tier #
########

amn = \
"""
The Junior Enlisted Airmen tier in the Air Force is made up of Airman Basic (AB), Airman (Amn), Airman
First Class (A1C), and Senior Airman (SrA) who all have different responsibilities based on their career
progression. All Junior Enlisted Airmen should focus on developing their Airman Leadership Qualities
and be familiar with foundational and occupational competencies to perform at basic and intermediate
levels. Responsibilities also include developing self, developing others, and developing ideas. Junior
Enlisted Airmen are expected to adapt from civilian to military lifestyle, conform to military standards,
customs and courtesies, and show occupational proficiency. They should also work towards identifying,
correcting and reporting behaviors that may put themselves or others at risk. Junior Enlisted Airmen
should contribute to a professional climate by supporting leaders’ decisions, exhibiting social readiness,
incorporating the use of technology in work environments, fostering inclusion, and effectively
communicating with teammates.
"""

nco = \
"""
The Noncommissioned Officer Tier is made up of Staff Sergeant (SSgt) and Technical Sergeant (TSgt).
Noncommissioned officers (NCOs) in the Air Force have responsibilities beyond junior enlisted airmen.
These include improving their own knowledge and competency through training, promoting team
resilience, being physically ready, contributing to a professional climate for others, exercising authority
when needed, promoting mental alertness and spiritual fitness, staying engaged with subordinates,
recognizing excellent performance while holding peers accountable, providing development feedback,
and promoting leaders&#39; decisions. NCOs must be able to question conventional approaches, prototype
and test ideas, and provide advice on new technology in developing organizations. They should
encourage retraining to balance the force to meet mission requirements.
"""

snco = \
"""
The Senior Noncommissioned Officer tier in the Air Force is made up of Master Sergeant (MSgt), Senior
Master Sergeant (SMSgt) and Chief Master Sergeant (CMSgt). Senior Noncommissioned Officers are
responsible for leading teams and shaping the future force. They progress to become technical experts,
experienced operational leaders, and strategic leaders, focusing on developing ready and disciplined
teams. Moreover, they mentor subordinates and peers while playing a critical role in developing and
advising officers. Senior Noncommissioned Officers have a comprehensive knowledge of the Airman
Leadership Qualities and foundational competencies. They contribute to a professional climate and
culture, empower Noncommissioned Officers, develop themselves and their subordinates, reframe
issues to evaluate from different perspectives, and work to improve resource management. Their
responsibilities require them to remain visible leaders, foster unit cohesion and connectedness,
establish and expand relationships to solve problems, and foster enduring team readiness for wartime
actions and decisions.
"""

tier_dict = {'Amn': amn,
             'NCO': nco,
             'SNCO': snco,
             'N/A': None}

#########
# Award #
#########

of_the_quarter = \
"""
The Air Force Quarterly Awards program is designed to recognize Airmen or civilians who have excelled
in the areas of Job Performance/Leadership in primary duty and Whole Airman Concept. The AF Form
1206 is used to nominate Airmen or civilians for awards. It records the justification for quarterly awards
at all organizational levels from Flight to Headquarters Air Force. These awards enhance the overall
visibility of Air Force personnel, including Air National Guard and Reserve, and their accomplishments.
The benefits of receiving an award include increased visibility of an individual’s accomplishments,
recognition of their hard work and dedication, and a sense of pride in their achievements.
"""

isr_tech = \
"""
The Intelligence, Surveillance, and Reconnaissance (ISR) Technician award is given to those who have gone
above and beyond and have shown exceptional technical expertise and contribution to the mission.
"""

performer_of_the_month = \
"""
The Air Force Performer of the Month award is an award given to an airman who has
demonstrated exceptional performance in their duties and responsibilities. The award is given to
those who have gone above and beyond their normal duties and have shown exceptional
leadership, technical expertise, and dedication to their job.
"""

of_the_year = \
"""
The Air Force Annual Awards program is designed to recognize Airmen or civilians who have excelled in
the areas of Job Performance/Leadership in primary duty and Whole Airman Concept. The AF Form 1206
is used to nominate Airmen or civilians for awards. It records the justification for annual awards at all
organizational levels from Flight to Headquarters Air Force. These awards enhance the overall visibility
of Air Force personnel, including Air National Guard and Reserve, and their accomplishments. The
benefits of receiving an award include increased visibility of an individual’s accomplishments,
recognition of their hard work and dedication, and a sense of pride in their achievements
"""

afisrap = \
"""
Each year, the Air Force honors outstanding performance in Intelligence, Surveillance and
Reconnaissance (ISR) missions and exceptional contributions to the field of ISR through the Air
Force Intelligence, Surveillance, and Reconnaissance Awards Program (AFISRAP). This program
enhances existing Air Force, Organization, and Intelligence Community recognition programs by
distinguishing the &quot;Best of the Best&quot; ISR members and units operating across the globe.
"""

sijan = \
"""
The award recognizes the accomplishments of Airmen, both officers and enlisted, who
demonstrate the highest qualities of leadership in the performance of their duties and
conduct of their lives. The winners are selected based on their leadership, job performance,
and community involvement.
"""

award_dict = {'Performer of the Month': performer_of_the_month,
              'of the Quarter': of_the_quarter,
              'ISR Tech': isr_tech,
              'of the Year': of_the_year,
              'AFISRAP': afisrap,
              'SIJAN': sijan,
              'N/A': None}

#######################
# Squadron Priorities #
#######################

thirty_is = \
"""
Airmen | Invigorate the Spartan Family as we Develop and Train our Airmen.
The 30th Intelligence Squadron will be inclusive, and Airman focused from the period a Spartan receives
inbound orders through the period a Spartan signs into a new duty location. Spartans, their immediate
or extended family and friends of the Spartan Fam will be furnished with readiness services, afforded
rest and recuperation opportunities, and always be welcomed to our ‘phalanx’. We move as one, no
Spartan stands alone. The 30th Intelligence Squadron will be the ‘ISR Assignment of Choice’.

Development | Invigorate, Unify and Challenge our Air minded Teams
All Spartans will be deliberately developed to meet mission needs, mentored for special developmental
duties, and permitted training and education opportunities. We will collectively train to be deadly with
the Spartan spear “tradecraft” and sword “expertise” helmet as “knowledge” and shield as “resilience”
concentrating the development of every Spartan to be holistic experts of the adversary&#39;s weaknesses.
Spartan training and education will be second to none. The 30th Intelligence Squadron will be the
premier intelligence work-center in the 480th ISR Wing.

Mission | Empower Airmen to Action as They Solve, Air, Space and Cyber Problems
Spartan leaders at all levels will be radical, but smart delegators of authority. Every Spartan will own
their challenge, own the way to overcome that challenge, and own the glory or managed defeat to be
ready for the next opportunity. Spartans will be part of a disciplined and agile force focused on
delivering Air-centered ISR to decision makers at all levels whenever duty calls. Spartan excellence will
be feared by the enemy and renowned by our allies.
"""

sq_pri_dict = {'30 IS': thirty_is,
               'N/A': None}

###################
# Wing Priorities #
###################

four_eighty_ISRW = \
"""
Priority: Mission: Win today’s fight &amp; compete in tomorrow’s
Lines of Operation:
    M1: Sharpen Analysis &amp; Exploitation Teams, Signals Intelligence (SIGINT) Elements &amp; Command
and Control (C2) constructs.
    M2: Assess &amp; Inform readiness, risks, &amp; requirements to 16 th Air Force, Air Combat Command
(ACC)/Major Commands (MAJCOMs, Combatant Command (CCMD)s and Intelligence
Community (IC) partners.
    M3: Ensure multi-domain mission assurance across the enterprise.
    M4: Deliver actionable intelligence to accelerate kill-chain through Automation, Augmentation
and Artificial Intelligence (AAA) and Tactics Techniques and Procedures (TTP) development.

Priority: People – Develop and Care for Airmen and their families
Lines of Operation:
    P1: Foster a diverse and Inclusive culture of dignity and respect.
    P2: Support military and civilian talent management programs across the enterprise
    P3: Prepare physically, mentally and spiritually fit airmen ready for the continuum of
competition.
    P4: Strengthen education, resiliency, single-airmen and family programs.

Priority: Infrastructure and IT: Acquisition Agility—Out-think, Out-maneuver, Out-Execute
Lines of Operation:
    I1: Develop infrastructure (facilities, comms pathways, equipment) and support to enable
emerging missions and capabilities.
    I2: Seek and acquire capabilities and expertise at mission speed.
    I3: Posture agile networks and data interoperability enabling rapid integration with DOD, IC, and
Coalition as an essential node in Joint All Domain Command and Control (JADC2) sensing grid.
    I4: Secure and defend enterprise systems and networks against adversary and insider attacks.

Priority: Training – Unleash the unimaginable talent of our airmen
Lines of Operation:
    T1: Develop a holistic Air Force Specialty Code (AFSC) agnostic career training pipeline; baseline-
to-advanced applicable to Analysis and Exploitation Teams (AET), ISR C2 and Network
Operations and Defense.
    T2: Develop airmen with tradecraft and analytic skills IAW IC and Air Force standards.
    T3: Mature Disposition of Force (DOF) requirements, training and procedures; Integrate object
based production (OBP) and data proficiencies.
    T4: Harness Airmen innovation through scalable/flexible multi-domain training environments
and applications.
"""

wg_pri_dict = {'480 ISRW': four_eighty_ISRW,
               'N/A': None}

########################
# Example Input/Output #
########################

## Example 1 ##

input_1 = \
"""
- GEOINT Superintendent for 6-wks, oversaw 7 AET and coordinated ISR Command and Control for 48 high-altitude missions across 3 DGS sites. Drove collection of 2.7K targets and 177 adhoc taskings for 25 intel requirements in 2 CCMDs. Pivoted the sq to meet a 45% Ground Moving Target Indication mission surge, satisfying EUCOM's #1 pri.
"""

output_1 = \
"""
- Action: The statement describes the actions of the member in overseeing, coordinating, and driving collection for ISR missions. The action verbs are clear and specific. However, the statement could be improved by using more quantifiable metrics, such as the number of personnel supervised, the hours of ISR coverage provided, and the percentage of taskings completed.
    Score: 4.5/5

- Result: The statement shows the results of the actions in terms of targets collected, taskings satisfied, and intelligence requirements met. The results are relevant and measurable. However, the statement could be improved by showing how the performance exceeded the standard or the expectation, or how it ranked among peers.
    Score: 4.5/5

- Impact: The statement demonstrates the impact of the results on the mission and the customer. The impact is significant and aligned with the priorities of the CCMDs. However, the statement could be improved by using more descriptive or emotive words, such as how the impact enhanced, enabled, or supported the mission or the customer, or how it contributed to a larger goal or outcome.
    Score: 4/5

- Scope: The statement indicates the scope of the performance in terms of time, location, and level of responsibility. The scope is broad and challenging, covering multiple missions, sites, and CCMDs.
    Score: 5/5

Total Score: 18/20
"""

example_1 = (input_1, output_1)

## Example 2 ##

input_2 = \
"""
- SSgt Reed earned his certification as Tactical Combat Casualty Care Instructor and was inspired to create a training plan for 37 personnel to enhance their readiness. The plan will prepare the team for an elevated operational tempo and enabled the the Air Force model to building sustainable, high-end air power readiness for the Joint Force.
"""

output_2 = \
"""
- Action: The statement describes the action of SSgt Reed in earning his certification and creating a training plan. The action verb is clear and specific. However, the statement could be improved by using more active voice.
    Score: 4/5

- Result: The statement shows the potential result of the action in terms of enhancing the readiness of the personnel. Nothing has been done yet.
    Score: 0/5

- Impact: The impact has not occurred yet.
    Score: 0/5

- Scope: The statement indicates the scope in terms of level of responsibility. The scope is moderate, covering 37 personnel.
Score: 4/5

Total Score: 8/20
"""

example_2 = (input_2, output_2)

## Example 3 ##

input_3 = \
"""
- A1C Page demonstrated excellent leadership and communication skills while fostering community relations with a HS NJROTC program. She instructed a course on Air Force requirements and conducted a Honor Guard workshop for their Drill team, garnering an LOA from the Commander and instilling a joint mindset for improved leadership.
"""

output_3 = \
"""
- Action: The statement describes the action of A1C Page in fostering community relations and instructing a course and a workshop. The action lacks specificity such as how many Honor Guard Members she instructed or how long the workshop was.
Score: 3/5

- Result: The statement shows the result of the action in terms of garnering an LOA from the Commander and instilling a joint mindset for improved leadership. However, the statement could be improved by using more descriptive or emotive terms, such as how the LOA recognized or praised A1C Page’s performance, or how the joint mindset enhanced or inspired the NJROTC cadets.
Score: 3/5

- Impact: The statement demonstrates the impact of the result on the program. However, the statement could be improved by using more specific or direct terms, such as how the impact supported or contributed to a larger goal or outcome, such as recruiting, retention, or readiness.
Score: 2/5

- Scope: The scope is moderate and challenging, covering a HS NJROTC program and their Drill team.
Score: 4/5

Total Score: 12/20
"""

example_3 = (input_3, output_3)

## Example 4 ##

input_4 = \
"""
- Lt Fabian led 4 multi-domain Analysis Exploitation Teams (AET) and coordinated with 2 DoD units during a combined services exercise, evaluating cross platform software solutions, ensuring communication of 37 reports via multiple sources, enhancing the speed and accuracy of the Kill Chain workflow
"""

output_4 = \
"""
- Action: The statement describes the action of Lt Fabian in leading, coordinating and evaluating during a combined services exercise. The statement could be more consistent by using the same tense throughout, such as “evaluated”, “coordinated” and “led” instead of “evaluating”, “coordinated” and “led”. The statement could be stronger by including details about how many members were on each team, each unit and how long the exercise was.
Score: 2.5/5

- Result: The statement shows the result of the action in terms of ensuring communication of 37 reports via multiple sources. However, the statement could be improved by using more comparative or superlative terms, such as how the performance exceeded the standard or the expectation, or how it ranked among peers.
Score: 2.5/5

- Impact: The statement could be improved by using more descriptive or emotive words, such as how the impact enhanced, enabled, or supported the mission or the customer, or how it contributed to a larger goal or outcome. The statement could also be more direct by stating who the customer was, such as a specific unit, command, or agency. The statement could also be more explicit by stating how the speed and accuracy of the Kill Chain workflow was enhanced, such as by reducing latency, increasing precision, or minimizing errors.
Score: 2/5

- Scope: The statement could be improved by using more precise or concise terms. The statement could also be more detailed by stating the level of the exercise (Ex: National).
Score: 2.5/5

Total Score: 9/20
"""

example_4 = (input_4, output_4)

## Example 5 ##

input_5 = \
"""
- Authored and briefed ELINT Tradecraft document f/27 ELINT analysts highlighting analytic techniques to apply once disposition of forces are complete. Additionally, supported the enrollment of analysts into NSA's cryptologic continuity education program to continue analyst development and better deliver fusion products to war fighters.
"""

output_5 = \
"""
- Action: The statement could be more specific by stating what the analytic techniques were and how they applied to the disposition of forces. The statement could also be clearer by stating what the fusion products were and how they benefited the war fighters.
Score: 2/5

- Result: The statement does not show the result of the action in terms of measurable outcomes or achievements. The statement could be improved by stating how the ELINT Tradecraft document and the education program improved the performance, skills, or knowledge of the analysts. The statement could also be improved by stating how many analysts enrolled in the program and how many completed it.
Score: 1/5

- Impact: The statement does not show the impact of the action in terms of mission relevance or value added. The statement could be improved by stating how the action enhanced, enabled, or supported the intelligence collection, analysis, or dissemination process. The statement could also be improved by stating who the customers or stakeholders were and how they benefited from the action.
Score: 1/5

- Scope: The statement does not show the scope of the action in terms of complexity, difficulty, or significance. The statement could be improved by stating what challenges or obstacles were overcome, what resources or tools were used, or what standards or best practices were followed. The statement could also be improved by stating how often or how long the action was performed.
Score: 1/5

Total Score: 5/20
"""

example_5 = (input_5, output_5)

## Example 6 ##

input_6 = \
"""
 - TSgt Fischer built the Wing's #1 data-centric tool suite capable of resolving near real time find, fix, and track challenges previously encountered with adversary ballistic missiles. By using long-term historic data integration, he developed 6 web apps, designed 3 dashboards, and crafted 4 algorithms to automate analysis for customers 75% faster.
"""

output_6 = \
"""
- Action: The statement is specific and clear by stating what the tool suite consisted of (6 web apps, 3 dashboards, and 4 algorithms) and how it automated analysis for customers. Score: 4/5

- Result: The statement shows the result of the action in terms of measurable outcomes or achievements. The statement is strong and comparative by stating that the tool suite was the Wing’s #1 and that it reduced analysis time by 75%. Score: 5/5

- Impact: The statement shows the impact of the action in terms of mission relevance or value added. The statement is descriptive and emotive by stating that the tool suite could resolve challenges previously encountered with adversary ballistic missiles. The statement could be improved by stating who the customers or stakeholders were and how they benefited from the action. Score: 3.5/5

- Scope: The statement shows the scope of the action in terms of complexity, difficulty, or significance. The statement is precise and concise by stating that the action involved long-term historic data integration. The statement could be improved by stating what challenges or obstacles were overcome. Score: 4/5

Total Score: 16.5/20
"""

example_6 = (input_6, output_6)

examples = [example_1, example_2, example_3, example_4, example_5, example_6]