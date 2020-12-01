import json

class Contacts:

   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email
 		
   
   def getPhone(self):
     return self.phone

   def getEmail(self):
     return self.email   




class Leads:

   def __init__(self, name, phone,email):
      self.name = name
      self.phone = phone
      self.email = email
 		
   
   def getPhone(self):
     return self.phone

   def getEmail(self):
     return self.email






registration_list =  ['{"registrant": {"name": "Lucy Liu","email": "lucy@liu.com","phone": "None"} }','{"registrant": {"name": "Doug","email": "doug@emmy.com","phone": "4564445556"} }','{"registrant": {"name": "Uma Thurman","email": "uma@thurs.com","phone": "None"} }']

ContactsList=[];
LeadsList=[];

one=Contacts("Alice Brown","1231112223","None");
ContactsList.append(one);
two=Contacts("Bob Crown","None","bob@crowns.com");
ContactsList.append(two);
three=Contacts("Carlos Drew ","3453334445","carl@drewess.com");
ContactsList.append(three);
four=Contacts("Doug Emerty","4564445556","None");
ContactsList.append(four);
five=Contacts("Egan Fair","5675556667","eg@fairness.com");
ContactsList.append(five);





six=Leads("None","None","kevin@keith.com");
LeadsList.append(six);
seven=Leads("Lucy","3210001112","lucy@liu.com");
LeadsList.append(seven);
eigth=Leads("Mary Middle","3331112223","mary@middle.com");
LeadsList.append(eigth);
nine=Leads("None","4442223334","None");
LeadsList.append(nine);
ten=Leads("None","None","ole@olson.com");
LeadsList.append(ten);




for i in registration_list:
	individualRegList = json.loads(i)
	flag=0;
	check_lead=0;
	for j in ContactsList:
		if((individualRegList["registrant"]['email']==j.getEmail() or individualRegList["registrant"]['phone']==j.getPhone()) and individualRegList["registrant"]['email'] !="None" and  individualRegList["registrant"]['phone'] !="None") :
			flag=1
			break;
	if(flag==0):
		for j in LeadsList:
			if(individualRegList["registrant"]['email']==j.getEmail() or individualRegList["registrant"]['phone']==j.getPhone() and individualRegList["registrant"]['email'] !="None" and  individualRegList["registrant"]['phone'] !="None"):
				vl=Contacts(individualRegList["registrant"]['name'],individualRegList["registrant"]['phone'],individualRegList["registrant"]['email'])
				ContactsList.append(vl);
				check_lead=1
				LeadsList.remove(j);

	if(flag==0 and check_lead==0):
		vl=Contacts(individualRegList["registrant"]['name'],individualRegList["registrant"]['phone'],individualRegList["registrant"]['email'])
		ContactsList.append(vl);



