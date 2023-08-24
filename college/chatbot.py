from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>CRCE BOT</b>')

# nlp = spacy.load("en_core_web_sm")
custom_logger = logging.getLogger(__name__)
chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            # 'default_response': "Hi there, Welcome to Fr. CRCE! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'default_response':'I am sorry, but i do not understand. I am still learning.<br>If you find this as more relevant question and if bot has not responded after multiple attempts please add it in the suggestion box above',
            'maximum_similarity_threshold':0.50
        }
    ],
    logger=custom_logger
)
trainer = ListTrainer(chatbot)
# trainer1 = ChatterBotCorpusTrainer(chatbot)

# trainer1.train('chatterbot.corpus.custom.general')

conversation = [
    "Hi",
    "Helloo!",

    "How are you?",
    "I'm good.</br> <br>Go ahead and write your query. 😃✨ ",

    "Great",
    "Go ahead and write your query. 😃✨ ",

    "good",
    "Go ahead and write your query. 😃✨ ",

    "fine",
    "Go ahead and write the number of any query. 😃✨ ",

    "Thank You",
    "Your Welcome 😄",

    "Thanks",
    "Your Welcome 😄",

    "Bye",
    "Thank You for visiting!..",

    "What do you do?",
    "I am made to give Information about BVRIT college.",

    "How many Programs are there?",
    "There are a total of 4 programs for Undergraduate and Postgraduate: 1.Bachelors of Technology 2.Masters of business administration 3.Masters of Technology 4.Pharmacy",

    "undergraduate programs?",
    "They are: Artificial intelligence and Data Science(AIDS), Biomedical engineering(BME), Chemical Engineering(CHE), Civil ENgineering(Civil), Computer Science and ENgineering(CSE), CSE-Artificial Intelligence and Machine Learning(CSE-AI & ML), Computer Science and ENgineering-Data Science(CSE-DS), Computer Science and Business Systems(CSBS), ELectrical and ELectronics Engineering(EEE), Electronics and Communication ENgineering(ECE), Information Technology(INF), MEchanical Engineering(Mech), Pharmaceutical Engineering(PHE).",

    "UG programs bvrit offers?",
    "It provides various UG programs Artificial intelligence and Data Science(AIDS), Biomedical engineering(BME), Chemical Engineering(CHE), Civil ENgineering(Civil), Computer Science and ENgineering(CSE), CSE-Artificial Intelligence and Machine Learning(CSE-AI & ML), Computer Science and ENgineering-Data Science(CSE-DS), Computer Science and Business Systems(CSBS), ELectrical and ELectronics Engineering(EEE), Electronics and Communication ENgineering(ECE), Information Technology(INF), MEchanical Engineering(Mech), Pharmaceutical Engineering(PHE) etc.,.<br>for more information 👉<a href = "'https://www.bvrit.ac.in/study/under-graduate'"> click here</a>",

    "postgraduate programs?",
    "It provides various PG programs Engineering Design,VLSI SYstem Design,Masters of Business Administration(MBA),Defence Technology(DT), EMbedded Systems, Electric Vehicle Technology etc.,for more information 👉 <a href = "'https://www.bvrit.ac.in/study/post-graduate'"> click here</a>",

    "PG programs?",
    "It provides various PG programs Engineering Design,VLSI SYstem Design,Masters of Business Administration(MBA),Defence Technology(DT), EMbedded Systems, Electric Vehicle Technology etc.,for more information 👉 <a href = "'https://www.bvrit.ac.in/study/post-graduate'"> click here</a>",

    "admission process for B.tech?",
    "70 % of the seats are allotted based on merit in the EAMCET conducted by Govt. of Telangana.<br>30 % of the seats are earmarked for Management / NRI candidates.<br>In addition to the above, Diploma holders are admitted in the second year of B.Tech <br> for more information 👉<a href = "'https://www.bvrit.ac.in/study/admission-process'"> click here</a>",

    "admission process for M.Tech?",
    "70 % of the seats are allotted based on merit in the Integrated Common Entrance Test (PGECET)<br> 30 % of the seats are earmarked for Management candidates.<br> for more information 👉 <a href = "'https://www.bvrit.ac.in/study/admission-process'"> click here</a>",

    "admission process for MBA?",
    "70 % of the seats are allotted based on merit in the ICET conducted by Govt. of Telangana.<br> 30 % of the seats are earmarked for Management candidates. <br> for more information 👉 <a href = "'https://www.bvrit.ac.in/study/admission-process'"> click here</a>",

    "How many seats are available in different departments in BVRIT?",
    "BVRIT has total intake of Seats differ with department<br> Computer Science & Engineering/CSE (300 seats), Information Technology/IT (120 seats), CSE-AI-ML (60 seats), CSE-Data science (60 seats), CSE-Business Systems(60 Seats), AI-DS (60 seats), MTech (CSE) (18 seats)<br> Information Technology(IT) (120 seats) <br> mechanical(MECH)(60 seats) <br> ECE (240 seats) <br> EEE (60 seats) <br> CIVIL Engineering (120 seats) <br>  for more information click here 👉<a href = "'https://www.bvrit.ac.in/study/departments'">seats in each department</a>",

    "How many seats are available in each department",
    "BVRIT has total intake of Seats differ with department<br> Computer Science & Engineering/CSE (300 seats), Information Technology/IT (120 seats), CSE-AI-ML (60 seats), CSE-Data science (60 seats), CSE-Business Systems(60 Seats), AI-DS (60 seats), MTech (CSE) (18 seats)<br> Information Technology(IT) (120 seats) <br> mechanical(MECH)(60 seats) <br> ECE (240 seats) <br> EEE (60 seats) <br> CIVIL Engineering (120 seats) <br>  for more information click here 👉<a href = "'https://www.bvrit.ac.in/study/departments'">seats in each department</a>",

    "Clear information of all undergraduate programs in BVRIT?",
    "You can get the clear information and intake percentage 👉<a  href="'https://bvrit.ac.in/study/under-graduate'">HERE</a>",

    "Clear information about the postgraduation programs at BVRIT?",
    "You can get the clear information and intake percentage about the PG programs👉<a href="'https://bvrit.ac.in/study/post-graduate'">HERE</a>",

    "how many seats available in CSE?",
    "seats availability differ for each department details of each department are as follows <br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSE</a>--300 seats<br>👉<a href = "'https://www.bvrit.ac.in/it-overview'"> IT</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSDS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSBS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> AIML</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/civil-overview'"> CIVIL</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/mech-overview'"> MECHANICAL</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/ece-overview'"> ECE</a>--240 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'"> EEE</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'">CHEMICAL</a>--60 seats<br>for more information about each department click on department name",

    "how many seats available in ECE?",
    "seats availability differ for each department details of each department are as follows <br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSE</a>--300 seats<br>👉<a href = "'https://www.bvrit.ac.in/it-overview'"> IT</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSDS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSBS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> AIML</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/civil-overview'"> CIVIL</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/mech-overview'"> MECHANICAL</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/ece-overview'"> ECE</a>--240 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'"> EEE</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'">CHEMICAL</a>--60 seats<br>for more information about each department click on department name",

    "how many seats available in EEE?",
    "seats availability differ for each department details of each department are as follows <br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSE</a>--300 seats<br>👉<a href = "'https://www.bvrit.ac.in/it-overview'"> IT</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSDS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSBS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> AIML</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/civil-overview'"> CIVIL</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/mech-overview'"> MECHANICAL</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/ece-overview'"> ECE</a>--240 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'"> EEE</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'">CHEMICAL</a>--60 seats<br>for more information about each department click on department name",

    "how many seats available in mechanical?",
    "seats availability differ for each department details of each department are as follows <br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSE</a>--300 seats<br>👉<a href = "'https://www.bvrit.ac.in/it-overview'"> IT</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSDS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSBS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> AIML</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/civil-overview'"> CIVIL</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/mech-overview'"> MECHANICAL</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/ece-overview'"> ECE</a>--240 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'"> EEE</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'">CHEMICAL</a>--60 seats<br>for more information about each department click on department name",

    "how many seats available in Civil?",
    "seats availability differ for each department details of each department are as follows <br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSE</a>--300 seats<br>👉<a href = "'https://www.bvrit.ac.in/it-overview'"> IT</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSDS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSBS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> AIML</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/civil-overview'"> CIVIL</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/mech-overview'"> MECHANICAL</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/ece-overview'"> ECE</a>--240 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'"> EEE</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'">CHEMICAL</a>--60 seats<br>for more information about each department click on department name",

    "how many seats available in Chemical?",
    "seats availability differ for each department details of each department are as follows <br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSE</a>--300 seats<br>👉<a href = "'https://www.bvrit.ac.in/it-overview'"> IT</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSDS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSBS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> AIML</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/civil-overview'"> CIVIL</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/mech-overview'"> MECHANICAL</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/ece-overview'"> ECE</a>--240 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'"> EEE</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'">CHEMICAL</a>--60 seats<br>for more information about each department click on department name",

    "how many seats available in CSDS?",
    "seats availability differ for each department details of each department are as follows <br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSE</a>--300 seats<br>👉<a href = "'https://www.bvrit.ac.in/it-overview'"> IT</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSDS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSBS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> AIML</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/civil-overview'"> CIVIL</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/mech-overview'"> MECHANICAL</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/ece-overview'"> ECE</a>--240 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'"> EEE</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'">CHEMICAL</a>--60 seats<br>for more information about each department click on department name",

    "how many seats available in CSBS?",
    "seats availability differ for each department details of each department are as follows <br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSE</a>--300 seats<br>👉<a href = "'https://www.bvrit.ac.in/it-overview'"> IT</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSDS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSBS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> AIML</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/civil-overview'"> CIVIL</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/mech-overview'"> MECHANICAL</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/ece-overview'"> ECE</a>--240 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'"> EEE</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'">CHEMICAL</a>--60 seats<br>for more information about each department click on department name",

    "how many seats available in AIML?",
    "seats availability differ for each department details of each department are as follows <br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSE</a>--300 seats<br>👉<a href = "'https://www.bvrit.ac.in/it-overview'"> IT</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSDS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> CSBS</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/cse-overview'"> AIML</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/civil-overview'"> CIVIL</a>--120 seats<br>👉<a href = "'https://www.bvrit.ac.in/mech-overview'"> MECHANICAL</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/ece-overview'"> ECE</a>--240 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'"> EEE</a>--60 seats<br>👉<a href = "'https://www.bvrit.ac.in/eee-overview'">CHEMICAL</a>--60 seats<br>for more information about each department click on department name",

    "is pharmaceutical engineering there in bvrit?",
    "yes bvrit has pharmaceutical engineering",

    "is chemical engineering there in bvrit?",
    "yes bvrit has chemical engineering",

    "Is Student's Care a facility in hostel?",
    "Yes, Facilities for medical emergencies, resident rector and warden look after the girl students staying in the hostels.<br> for all details of the facilities available can be found 👉<a href="'https://www.bvrit.ac.in/discover/students-life'"> here </a>",

    "Is there transportation facility?",
    "BVRIT has a very good transportation facility providing transport from all over the city in a reasonable price.",

    "Is there any free food facility in the college?",
    "BVRIT provides free breakfast for the students who travel from distance daily in the morningfrom 9AM to 10AM, also tea is provided in the tea break and healthy snacks are provided while travelling back home in the evening .<br>There is no special charge taken for this facility.<br> for all details of the facilities available can be found 👉<a href="'https://www.bvrit.ac.in/discover/students-life'"> here </a> ",

    "How many blocks are there in BVRIT?",
    "There are different blocks namely AbdulKalam block(Freshman), Aryabhatta block(cse), Vishweshwaraiah block(eee), Bhaskara block(it) etc., each for the different department.",

    "How are the faculty at BVRIT?",
    "Every teacher at BVRIT will have scored first class marks in their PostGraduation and encouraging in every aspect and provides with best knowledge as possible",

    "What is the address of bvrit?",
    "B V Raju Institute of Technology, Vishnupur, Narsapur, Medak Dist, 502313",

    "location of bvrit?",
    "B V Raju Institute of Technology, Vishnupur, Narsapur, Medak Dist, 502313",

    "BVRIT Contact No.?",
    "Contact No.-08458 - 222000 and Email id for contact is info@bvrit.ac.in.<br> or you can find any contact information related to your issue 👉<a href="'https://www.bvrit.ac.in/contactus'">HERE</a>",

    "contact details for any issues?",
    "you can find any contact information related to your issue 👉 <a href="'https://www.bvrit.ac.in/contactus'">HERE</a>",

    "Contact details for accounts and general queries?",
    "you can find any contact information related to accounts 👉 <a href="'https://www.bvrit.ac.in/contactus'">HERE</a>",

    "Contact details for administration queries?",
    "you can find any contact information related to administration 👉 <a href="'https://www.bvrit.ac.in/contactus'">HERE</a>",

    "does the college has transport facilities?",
    "It has bus transport facilities find the details 👉<a href="'https://www.bvrit.ac.in/transportlink'"> HERE </a>",

    "where can i find the details of the bus routes available?",
    "you can find all bus route details in this document 👉 <a href="'https://drive.google.com/file/d/14yW6L0ewXpLIrHV6_OuQdn1OxBCLpWed/view'">Here</a>",

    "Where can I find more information about BVRIT college?",
    "For more information on BVRIT is <a href="'https://www.bvrit.ac.in/'">here</a> Click on link.",

    "Is there any Hospital facility?",
    "Yes, In BVRIT Hospital facility is available.you can find in detail👉 <a href="'https://www.bvrit.ac.in/differentiators/centennial-health-centre'"> Here </a>",

    "what is the EAMCET code?",
    "The code for EAMCET/ECET/ICET is \"BVRI\" <br> and for PGCET is \"BVRI1\" ",

    "what is the ECET code?",
    "The code for EAMCET/ECET/ICET is \"BVRI\" <br> and for PGCET is \"BVRI1\" ",

    "what is the ICET code?",
    "The code for EAMCET/ECET/ICET is \"BVRI\" <br> and for PGCET is \"BVRI1\" ",

    "what is the PGCET code?",
    "The code for EAMCET/ECET/ICET is \"BVRI\" <br> and for PGCET is \"BVRI1\" ",

    "where can i find the complete details of placements",
    "for complete details 👉< a href=" 'https://www.bvrit.ac.in/placements/placement-details' " > Click Here < / a >",

    "Is hostel facility available in bvrit?",
    "Yes , BVRIT campus has 2 Girls hostels and 6 Boys hostel.",

    "strength of Employees and Students in bvrit?",
    "An employee strength of 550+, student strength of more than 7500.",

    "Principal of BVRIT?",
    "Dr. K.Lakshmi Prasad is the principal of BVRIT.",

    "What is the capacity of Hostels for girls?",
    "The hostels have a housing capacity for 500-600 girls.",

    "What are the facilities in hostel?",
    "Gymnasium, Badminton and Volleyball Courts, Indoor sport like Table Tennis, Chess and Carom, separate facilities for viewing TV and reading newspapers and magazines and facilitation for celebration of various days/festivals by the hostel residents.<br> Wholesome, nutritious food is available in the mess.Internet and Wi-Fi facility with computers, Housekeeping service and Security is also there.<br> for all details of the facilities available can be found 👉<a href="'https://www.bvrit.ac.in/discover/students-life'"> here </a> ",

    "How is research and development at BVRIT?",
    "BVRIT is a premier institute having highly committed faculty with admirable academic and research background and strong inclination towards research and development of innovative technologies.",

    "What is the fee structure at BVRIT?",
    "The tuition fee for B.tech course is 1,35,000/- all the supplementary fee will be shown in Ecap.",

    "How can parents keep track of their child at BVRIT?",
    "Each parent and his ward will be having access to their Ecap accounts where they can check their daily attendance , fee details and marks secured and also pending library books and backlogs.",

    "Where do I find the photo gallery of BVRIT?",
    "You can find the photo gallery here:  <a href="'https://bvrit.ac.in/index.php/gallery/photo-gallery'">CLICK HERE</a>",

    "Where do I find all the news of BVRIT?",
    "YOu can find all the news articles related to BVRIT here: <a href="'https://bvrit.ac.in/gallery/news-gallery'">Click here</a>",

    "What are the cultural events that take place at BVRIT?",
    "There are many events taking place at BVRIT every 2 or 3 months ..some of those are: cultural day,Athenes, Amogha,Kalos-Hours , Zealotz, Promethean.",

    "What are the clubs at BVRIT?",
    "There are many clubs at BVRIT to join and enhance your skills. Few of the clubs like CBB(coding club),cultural club, student clubs etc.,info of few clubs can be found<a href="'https://www.bvrit.ac.in/differentiators/club-inquizitive'">Here</a>",

    "Name few clubs at BVRIT?",
    "Cultural club BVRIT, Photography club(My BVRIT), Coding Brigade BVRIT etc.,info of few clubs can be found<a href="'https://www.bvrit.ac.in/differentiators/club-inquizitive'">Here</a>",

    "How is the Library facility at BVRIT?",
    "BVRIT has excellent books available to help all the students crack many competitive exams like gate and also useful for higher studies.",

    "Clear information of all undergraduate programs in BVRIT?",
    "You can get the clear information and intake percrntage here: https://bvrit.ac.in/study/under-graduate",

    "Clear information about the postgraduation programs at BVRIT?",
    "You can get the clear information and intake percentage about the PG programs here: https://bvrit.ac.in/study/post-graduate",

    "How are the lab equipments at bvrit?",
    "BVRIT is well known for all its infrastructure among the top colleges in Telangana.",

    "Where can I find all the transportation details of bvrit?",
    "you can find all those here<a href="'https://bvrit.ac.in/transportlink/'">transport details</a> ",

    "What are the companies  that come for placement?",
    "Many companies like Amazon, Micron, Optum, Hcl, TCS, Cognizant, Capgemini, Adobe, Providence, LTI, Accenture, Oracle, Virtusa etc., visit the campus for the placements.<br> for complete details refer👉<a href=" 'https://www.bvrit.ac.in/placements/placement-details' ">Here</a>",

    "What are the companies  that visit bvrit for placements?",
    "Many companies like Amazon, Micron, Optum, Hcl, TCS, Cognizant, Capgemini, Adobe, Providence, LTI, Accenture, Oracle, Virtusa etc., visit the campus for the placements.<br> for complete details refer👉<a href=" 'https://www.bvrit.ac.in/placements/placement-details' ">Here</a>",

    "How many percentage students get placed in BVRIT?",
    "80-90% students take placements.<br> for complete details refer 👉<a href=" 'https://www.bvrit.ac.in/placements/placement-details' ">Here</a>",

    "What is the highest package offered at BVRIT till date?",
    "The highest package till date is 44LPA",

    "What is the academic calender for Btech 8th semester?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 7th semester?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 6th semester?",
    "detailed and updated academic calender can be found👉 <a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 5th semester?",
    "detailed and updated academic calender can be found👉 <a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 4th semester?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 3rd semester?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 2nd semester?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 1st semester?",
    "detailed and updated academic calender can be found👉 <a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 8th sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 7th sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 6th sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 5th sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 4th sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 3rd sem?",
    "detailed and updated academic calender can be found👉 <a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 2nd sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Btech 1st sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for MBA 1st sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for MBA 2nd sem?",
    "detailed and updated academic calender can be found👉 <a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for MBA 3rd sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for MBA 4th sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Mtech 4th sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Mtech 3rd sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Mtech 2nd sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "What is the academic calender for Mtech 1st sem?",
    "detailed and updated academic calender can be found 👉<a href="'https://www.bvrit.ac.in/study/academic-calendars'">HERE</a>",

    "what is cse syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is ece syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is eee syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is IT syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is mechanical syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is civil syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is csbs syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is csds syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is aiml syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is MBA syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "what is MTECH syllabus",
    "Syllabus book is provided for each student based on their department where as Detailed information can be found for each department here as follows<br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSE</a> <br>👉 <a href="'https://www.bvrit.ac.in/it-curriculum'">IT</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">EEE</a><br>👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">MTECH in CSE</a><br> 👉 <a href="'https://www.bvrit.ac.in/eee-curriculum'">MTECH in EEE</a><br> 👉 <a href="'https://www.bvrit.ac.in/ece-curriculum'">MTECH in ECE</a><br>👉 <a href="'https://www.bvrit.ac.in/mba-curriculum'">MBA</a><br>👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSDS</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">AIML</a><br> 👉 <a href="'https://www.bvrit.ac.in/cse-curriculum'">CSBS</a><br> 👉 <a href="'https://www.bvrit.ac.in/civil-curriculum'">CIVIL</a><br> 👉 <a href="'https://www.bvrit.ac.in/mech-curriculum'">MECHANICAL</a><br> 👉 <a href="'https://www.bvrit.ac.in/chemical-curriculum'">CHEMICAL</a>",

    "Where can i find the sem results?",
    "results will be displayed in bvrit ecap where you can access them by entering your username and password<br> the corresponding link is 👉<a href="'https://bvrit.edu.in/StudentMaster.aspx'">here</a>",

    "Where can i find my personal details?",
    "you can find your personal details in bvrit ecap which you can access by entering your username and password <br> the corresponding link is 👉<a href="'https://bvrit.edu.in/StudentMaster.aspx'">here</a>",

    "Whether i can change my personal details in ecap?",
    "You can find your personal details in bvrit ecap portal but you cannot edit those details. If you want any changes to the details please contact admin.",

    "what is the current fee for btech?",
    "current fee for Btech is 1,35,000 which will change for every 3 years.",

    "what are the documents needed to submitted for epass scholarship renewal in college?",
    "The student has to submit the necessary documents in the admin section in abdul kalam block before the last date.<br> some of the documents are:<br>1)bonafide for past 7 years and recent year given by the college<br> 2)memos for last two sems <br> 3)income and residence proof etc..<br> detailed documents list can be found in the document 👉<a href="'epass documents for college.pdf'">here</a>",

    "what are the documents for epass scholarship renewal in college?",
    "The student has to submit the necessary documents in the admin section in abdul kalam block before the last date.<br> some of the documents are:<br>1)bonafide for past 7 years and recent year given by the college<br> 2)memos for last two sems <br> 3)income and residence proof etc..<br> detailed documents list can be found in the document 👉<a href="'epass documents for college.pdf'">here</a>",

    "where can i get the bonafide for scholarship?",
    "You can get the bonafide in scholarship section in IT department(Bhaskara Block).",

    "Where is exam branch in college?",
    "Exam branch is in IT department block(Bhaskara Block).Contact details can be found 👉<a href="'https://www.bvrit.ac.in/examinations-staff'">Here</a>",

    "where can i pay the fee online?",
    "you can pay the fee online in ecap by entering your details here is the webiste link👉 <a href="'https://bvrit.edu.in/StudentMaster.aspx'"> pay here </a>",

    "how can i pay the fee online?",
    "First the student/parent need to login through bvrit ecap then these were the steps need to be performed <br>1) Go for online payment option <br> 2)then choose the fee needed to be paid<br> Then it will show the payment options <br> 3) enter your details correctly and click on proceed<br> 4) After successful completion you can download the reciept in ecap from online reciepts option.<br> You can 👉<a href="'https://bvrit.edu.in/StudentMaster.aspx'"> pay here </a> by following above steps",

    "where can i track my attendance?",
    "In ecap there is an option called attendance where you can see the attendance details <a href="'https://bvrit.edu.in/StudentMaster.aspx'"> check attendance here </a>",
]

trainer.train(conversation)
