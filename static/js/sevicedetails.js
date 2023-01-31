document.getElementById('remodel').addEventListener('click', myFunction1);
document.getElementById('construct').addEventListener('click', myFunction2);
document.getElementById('product').addEventListener('click', myFunction3);
document.getElementById('repair').addEventListener('click', myFunction4);
document.getElementById('designn').addEventListener('click', myFunction5);
document.getElementById('mesignn').addEventListener('click', myFunction6);

remodel= document.getElementById('remodel')
construct=document.getElementById('construct')
product=document.getElementById('product')
repair=document.getElementById('repair')
designn=document.getElementById('designn')
mesignn=document.getElementById('mesignn')

document.getElementById('remodel1').addEventListener('click', myFunction1);
document.getElementById('construct1').addEventListener('click', myFunction2);
document.getElementById('product1').addEventListener('click', myFunction3);
document.getElementById('repair1').addEventListener('click', myFunction4);
document.getElementById('designn1').addEventListener('click', myFunction5);
document.getElementById('mesignn1').addEventListener('click', myFunction6);

remodel= document.getElementById('remodel1')
construct=document.getElementById('construct1')
product=document.getElementById('product1')
repair=document.getElementById('repair1')
designn=document.getElementById('designn1')
mesignn=document.getElementById('mesignn1')




  function myFunction1() {
    document.getElementById('infor').innerHTML = 
    '<img src="static/img/16.png" alt="" class="img-fluid services-img" style="width: 736px;height: 465.5px;"><h3>Crime detection refers to the process of identifying, investigating, and gathering evidence of criminal activity. </h3><p>This can be done through a variety of methods, such as surveillance, interviews, and forensic analysis. Law enforcement agencies, such as police departments, are responsible for detecting and investigating crimes. Additionally, other organizations, such as private investigators, may also be involved in crime detection.</p><ul><li><i class="bi bi-check-circle"></i> <span>Surveillance: Observing individuals or groups to gather information about their activities or whereabouts</span></li><li><i class="bi bi-check-circle"></i> <span>Interviews: Questioning individuals who may have information about a crime</span></li><li><i class="bi bi-check-circle"></i> <span>Intelligence gathering: Collecting information from various sources to identify potential criminal activity</span></li>  </ul><p>Law enforcement agencies, such as police departments, are responsible for detecting and investigating crimes. Additionally, other organizations, such as private investigators, may also be involved in crime detection.</p><p>The key goal of crime detection is to identify the individuals responsible for committing a crime and bring them to justice. This is done by collecting evidence, interviewing witnesses, and building a case against the suspect.</p>';
    remodel.classList.add("active");
    construct.classList.remove("active");
    product.classList.remove("active");
    repair.classList.remove("active");
    designn.classList.remove("active");
    mesignn.classList.remove("active");

    
} 
 function myFunction2() {
    document.getElementById('infor').innerHTML = 
    '<img src="static/img/17.jpeg" alt="" class="img-fluid services-img" style="width: 736px; height: 465.5px;"><h3>Crime prediction refers to the use of data and statistical analysis to identify patterns and trends in criminal activity</h3><p>With the goal of forecasting where and when crimes are likely to occur in the future. This information can be used by law enforcement agencies to allocate resources and deploy personnel more effectively. There are several methods used for crime prediction, including:</p><ul><li><i class="bi bi-check-circle"></i> <span>Geographic Information Systems (GIS): Analyzing crime data in relation to geographic locations to identify hot spots, or areas with high crime rates.</span></li><li><i class="bi bi-check-circle"></i> <span>Machine learning: Using algorithms to analyze large sets of data and identify patterns that may indicate criminal activity.</span></li><li><i class="bi bi-check-circle"></i> <span>Predictive policing: Using crime data and statistical models to predict where crimes are likely to occur and allocate resources accordingly.</span></li>  </ul><p>It is important to note that while crime prediction can aid in the allocation of resources and personnel, it can also raise concerns about bias, privacy and ethical issues.</p><p>Overall, crime prediction is a relatively new field, and ongoing research is needed to improve the accuracy and effectiveness of the methods used.</p>';
    construct.classList.add("active");
    repair.classList.remove("active");
    product.classList.remove("active");
    remodel.classList.remove("active");
    designn.classList.remove("active");
    mesignn.classList.remove("active");
}
  function myFunction3() {
    document.getElementById('infor').innerHTML = 
    '<img src="static/img/18.jpg" alt="" class="img-fluid services-img" style="width: 736px; height: 465.5px;"><h3>Crime reporting refers to the process of informing law enforcement authorities about a crime that has been committed.</h3><p>This can be done in a variety of ways, depending on the type of crime and the jurisdiction in which it occurred. Some common methods of crime reporting include:</p><ul><li><i class="bi bi-check-circle"></i> <span>Anonymous reporting: Some police departments have anonymous tip lines or online forms that allow people to report crimes without providing their personal information.</span></li><li><i class="bi bi-check-circle"></i> <span>Contacting the police: This is the most common method of reporting a crime. </span></li><li><i class="bi bi-check-circle"></i> <span>Using online reporting systems: Many police departments now have online reporting systems that allow people to submit a report of a crime over the internet.</span></li>  </ul><p>It is important to report any crime as soon as possible, as the information provided can help law enforcement agencies to solve the crime and bring the offender to justice.</p><p>Its also important to note that, depending on the jurisdiction and the severity of the crime, some crime may need to be reported to different authorities, like FBI, SEC, etc.</p>';
    product.classList.add("active");
    construct.classList.remove("active");
    repair.classList.remove("active");
    remodel.classList.remove("active");
    designn.classList.remove("active");
    mesignn.classList.remove("active");
}
  function myFunction4() {
    document.getElementById('infor').innerHTML = 
    '<img src="static/img/19.jpg" alt="" class="img-fluid services-img" style="width: 736px; height: 465.5px;"><h3>Crime news refers to news stories and articles that report on criminal activity and related issues.</h3><p>These stories can cover a wide range of topics, including:</p><ul><li><i class="bi bi-check-circle"></i> <span>Major crimes such as murder, robbery, and assault</span></li><li><i class="bi bi-check-circle"></i> <span>Cybercrime, such as hacking or identity theft</span></li><li><i class="bi bi-check-circle"></i> <span>Police investigations and arrests</span></li>  </ul><p>Crime news can be found in various forms of media, such as newspapers, television news programs, and online news websites. Some news organizations have a dedicated crime or investigative reporting team, while others cover crime as part of their overall news coverage.</p><p>Its important to note that crime news can have a significant impact on public perception and understanding of crime, and it can also shape public policy and criminal justice reform. Therefore, its important to get the information from reliable sources and not to rush to judgment based on one-sided information.</p>';
    repair.classList.add("active");
    construct.classList.remove("active");
    product.classList.remove("active");
    remodel.classList.remove("active");   
    designn.classList.remove("active");
    mesignn.classList.remove("active");
}
  function myFunction5() {
    document.getElementById('infor').innerHTML = 
    '<img src="static/img/20.jpg" alt="" class="img-fluid services-img" style="width: 736px; height: 465.5px;"><h3>An SOS button, also known as a panic button, is a device or feature that allows a person to quickly and easily call for help in an emergency situation.</h3><p>There are several types of SOS buttons, each with a different purpose:</p><ul><li><i class="bi bi-check-circle"></i> <span>Personal SOS buttons: These are small, portable devices that a person can carry with them, such as on a keychain or in a purse. They can be pressed to send an emergency signal to a designated person or a monitoring center.</span></li><li><i class="bi bi-check-circle"></i> <span>Smartphone SOS button: Some smartphones have a built-in emergency button or a dedicated emergency contact that can be accessed by pressing a specific combination of keys.</span></li><li><i class="bi bi-check-circle"></i> <span>Smartphone SOS button: Some smartphones have a built-in emergency button or a dedicated emergency contact that can be accessed by pressing a specific combination of keys.</span></li>  </ul><p>Its important to note that the SOS button should only be used in emergency situations, as it sends a distress signal that prompts a rapid response, this can be a great tool to have in case of an emergency.</p>';
    designn.classList.add("active");
    construct.classList.remove("active");
    product.classList.remove("active");
    remodel.classList.remove("active");
    repair.classList.remove("active");
    mesignn.classList.remove("active");
}

function myFunction6() {
  document.getElementById('infor').innerHTML = 
  '<img src="static/img/21.jpg" alt="" class="img-fluid services-img" style="width: 736px; height: 465.5px;"><h3>Crime data refers to information and statistics related to criminal activity.</h3><p>This can include information on the types of crimes committed, the location of crimes, the demographics of victims and offenders, and the outcomes of criminal cases. There are several sources of crime data, including:</p><ul><li><i class="bi bi-check-circle"></i> <span>Law enforcement agencies: Police departments, sheriffs offices, and other law enforcement agencies collect and report crime data to the federal government and state government.  </span></li><li><i class="bi bi-check-circle"></i> <span>Private companies: Some private companies collect and analyze crime data, often using publicly available data from law enforcement agencies and other sources.</span></li><li><i class="bi bi-check-circle"></i> <span>Surveys: Surveys can be used to collect information about crime from the general public. For example, the National Crime Victimization Survey (NCVS) collects data on crime victimization from a sample of U.S. households.</span></li>  </ul><p>Crime data can be used for a variety of purposes, such as identifying crime trends, determining the effectiveness of law enforcement strategies, and allocating resources.</p><p>However, its important to keep in mind that crime data can be affected by various factors such as under-reporting, reporting biases, and changes in crime categorization. Therefore, its important to consult multiple sources and use caution when interpreting crime data.</p>';
  mesignn.classList.add("active");
  designn.classList.remove("active");
  construct.classList.remove("active");
  product.classList.remove("active");
  remodel.classList.remove("active");
  repair.classList.remove("active");
}
