"""
Program:IvyVisit Planner
Author: Alison Garrett
Last Date Modified: 3/13/2022

The purpose of this program is to allow a user to plan a visit to
Ivy Tech for one of the scheduled IvyVisit Fridays.

"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
import re


"""Demographic Info"""
class Page1(EasyFrame):
    name = "" # empty variable is delcared to share name value with other classes
    
    def __init__(self):
        """sets up window and widgets for demographic information"""
        EasyFrame.__init__(self, width = 350, height = 300, title = "Ivy Visit Planner")
        #Ivy Logo
        ivyLogo = self.addLabel(text = "", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "green")
        self.image = PhotoImage(file = "ivylogo.gif")
        ivyLogo["image"] = self.image
        #General Settings
        self["background"] = "green"
        self.addLabel(text = "Welcome to Ivy Visit Planner!", row = 1, column =0, columnspan = 2, sticky = "NSEW")
        self.addLabel(text = "Please start customizing your visit", row = 2, column = 0, columnspan =2, sticky = "NSEW")
        #Enter First and Last Name
        self.addLabel(text = "First Name", row = 3, column = 0)
        self.firstName = self.addTextField(text = "", row = 3, column = 1)
        self.addLabel(text = "Last Name", row = 4, column = 0)
        self.lastName = self.addTextField(text = "", row = 4, column = 1)
        
        #Date of Birth
        self.addLabel(text = "Date of Birth (MM/DD/YYYY)", row = 5, column = 0)
        self.birthday = self.addTextField(text = "", row = 5, column = 1)
        
        #Phone Number
        self.addLabel(text = "Phone Number (111-222-3333)", row = 6, column = 0)
        self.phoneNum = self.addTextField(text = "", row = 6, column = 1)
        
        #Email
        self.addLabel(text = "Email", row = 7, column = 0)
        self.email = self.addTextField(text = "", row = 7, column = 1)

        #NextButton
        self.nextBtn = self.addButton(text = "Next Page", row = 8, column = 0, columnspan = 2, command = self.inputValidation)

    def inputValidation(self):
        """Validates input for first name, last name, birthday, phone number, and email to make sure a
            value is enterted correctly"""
        Page1.name = self.firstName.getText() #variable is declared for first name
        Page1.lastname = self.lastName.getText() #variable is declared for last name
        Page1.birthday = self.birthday.getText() #variable is delcared for birthday
        Page1.phoneNum = self.phoneNum.getText() #variable is delcared for phone number
        Page1.email = self.email.getText() #variable is declared for email
        emailPattern = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #variable is declared for format of email
        #first and last name are validated to make sure they are not empty
        if Page1.name == "":
            self.messageBox(title = "ERROR", message = "First name is a required field.")
        elif Page1.lastname == "":
            self.messageBox(title = "ERROR", message = "Last name is a required field.")
        #birthday is validated to make sure it is at least 10 characters long
        elif len(Page1.birthday) != 10:
            self.messageBox(title = "ERROR", message = "Enter your birthday in the correct format.")
        #phone number is validated to make sure it is at least 12 characters long
        elif len(Page1.phoneNum) != 12:
            self.messageBox(title = "ERROR", message = "Enter your phone number in the correct format.")
        #email is validated to make sure it matches the emailPattern format declared above. If it matches self.close() is called
        elif re.match(emailPattern, Page1.email):
            self.close()
        else:
            self.messageBox(title = "ERROR", message = "Please enter a valid email.")

    def close(self):
        """returns the first name value to the class, and closes the current window"""
        Page1.name = self.firstName.getText()
        self.master.destroy()

"""Date/Time selection"""
class Page2(EasyFrame):
    date = "" # empty variable is delcared to share date value with other classes
    time = "" # empty variable is delcared to share time value with other classes
    
    def __init__(self):
        """sets up window and widgets for selecting date/time of visit"""
        EasyFrame.__init__(self, width = 350, height = 200, title = "Ivy Visit Planner")
        self["background"] = "green"
        self.addLabel(text = "When would you like to visit?", row = 0, column =0, columnspan = 2, sticky = "NSEW")
        
        #Date Radiobuttons
        self.addLabel(text = "Date", row = 1, column = 0)
        self.dateGroup = self.addRadiobuttonGroup(row = 2, column = 0)
        defaultRB = self.dateGroup.addRadiobutton(text = "April 1, 2022")
        self.dateGroup.addRadiobutton(text = "May 6, 2022")
        self.dateGroup.addRadiobutton(text = "June 3, 2022")
        self.dateGroup.setSelectedButton(defaultRB)
    
        #Time Radiobuttons
        self.addLabel(text = "Time", row = 1, column = 1)
        self.timeGroup = self.addRadiobuttonGroup(row = 2, column = 1)
        defaultRB = self.timeGroup.addRadiobutton(text = "10am-12pm")
        self.timeGroup.addRadiobutton(text = "12pm-2pm")
        self.timeGroup.addRadiobutton(text = "2pm-4pm")
        self.timeGroup.setSelectedButton(defaultRB)

        #NextButton
        self.nextBtn = self.addButton(text = "Next Page", row = 7, column = 0, columnspan = 2, command = self.close)
    
    def close(self):
        """returns date and time variables back to class, and closes current window"""
        Page2.date = self.dateGroup.getSelectedButton()["text"]
        Page2.time = self.timeGroup.getSelectedButton()["text"]
        self.master.destroy()

"""Program Selection"""
class Page3(EasyFrame):
    program = "" # empty variable is delcared to share program value with other classes
    
    def __init__(self):
        """sets up window and widgets"""
        EasyFrame.__init__(self, width = 350, height = 300, title = "Ivy Visit Planner")
        self["background"] = "green"
        self.addLabel(text = "What program areas are you interested in?", row = 0, column =0, columnspan = 2, sticky = "NSEW")
        self.listBox = self.addListbox(row = 2, column = 0, rowspan = 2)
        #Listbox Program Items
        self.listBox.insert(0, "Arts and Communication")
        self.listBox.insert(1, "Business")
        self.listBox.insert(2, "Automotive")
        self.listBox.insert(3, "Education")
        self.listBox.insert(4, "General Studies")
        self.listBox.insert(5, "Health Science")
        self.listBox.insert(6, "Information Technology")
        self.listBox.insert(7, "Hospitality/Culinary")
        self.listBox.insert(8, "Manufacturing")
        self.listBox.insert(9, "Public and Human Services")
        self.listBox.insert(10, "Public Safety")
        self.listBox.insert(11, "Transportation/Logistics")
        self.listBox.insert(12, "Undecided")
        self.listBox.setSelectedIndex(0)

        #NextButton
        self.nextBtn = self.addButton(text = "Next Page", row = 8, column = 0, columnspan = 2, command = self.close)

    def close(self):
        """returns program variable back to class, and closes current window"""
        Page3.program = self.listBox.getSelectedItem()
        self.master.destroy()

"""Building tour"""
class Page4(EasyFrame):
    building = "" # empty variable is delcared to share building tour value with other classes
    
    def __init__(self):
        """sets up window and widgets for building tour selection"""
        EasyFrame.__init__(self, width = 950, height = 500, title = "Ivy Visit Planner")
        self["background"] = "green"
        self.addLabel(text = "What Building would you like to tour?", row = 0, column =0, columnspan = 19, sticky = "NSEW")
        #Campus Image and Label
        mainCampus = self.addLabel(text = "Main Campus", row = 2, column = 0, columnspan = 3)
        self.image = PhotoImage(file = "main.gif")
        mainCampus["image"] = self.image
        self.addLabel(text = "Main Campus", row = 1, column =0, sticky = "NSEW")
        #Nursing Image and Label
        nursing = self.addLabel(text = "Nursing", row = 2, column = 5, columnspan = 3)
        self.image2 = PhotoImage(file = "nursing.gif")
        nursing["image"] = self.image2
        self.addLabel(text = "Nursing", row = 1, column =5, sticky = "NSEW")
        #ICLS Image and Label
        icls = self.addLabel(text = "Indiana Center For Life Sciences", row = 2, column = 8, columnspan = 3)
        self.image3 = PhotoImage(file = "icls.gif")
        icls["image"] = self.image3
        self.addLabel(text = "Indiana Center For Life Sciences", row = 1, column =8, sticky = "NSEW")

        #Radio Buttons to select building
        self.buildingGroup = self.addRadiobuttonGroup(row = 3, column = 5, columnspan = 2)
        defaultRB = self.buildingGroup.addRadiobutton(text = "Main Campus")
        self.buildingGroup.addRadiobutton(text = "Nursing")
        self.buildingGroup.addRadiobutton(text = "Indiana Center for Life Sciences")
        self.buildingGroup.setSelectedButton(defaultRB)

        #NextButton
        self.nextBtn = self.addButton(text = "Next Page", row = 4, column = 5, columnspan = 2, command = self.close)

    def close(self):
        """returns building variable back to class, and closes current window"""
        Page4.building = self.buildingGroup.getSelectedButton()["text"]
        self.master.destroy()

"""Enrollment Meeting"""
class Page5(EasyFrame):
    department = "" #empty variable is declared to share department value with other classes
    finAid = False #boolean variable is declared to collect if student does/does not need to meet with Financial Aid
    
    def __init__(self):
        """sets up window and widgets for who appointment should be scheduled with"""
        EasyFrame.__init__(self, width = 500, height = 500, title = "Ivy Visit Planner")
        self["background"] = "green"
        self.addLabel(text = "Check all of the enrollment steps you have completed: ", row = 0, column =0, columnspan = 3, sticky = "NSEW")
        #Checkboxes for enrollment steps
        self.appBtn = self.addCheckbutton(text = "Admissions Application", row = 1, column = 0)
        self.myivyBtn = self.addCheckbutton(text = "Setup MyIvy Account", row = 2, column = 0)
        self.assmtBtn = self.addCheckbutton(text = "Knowledge Assessment", row = 3, column = 0)
        self.fafsaBtn = self.addCheckbutton(text = "Filed my FAFSA", row = 4, column = 0)

        #NextButton
        self.nextBtn = self.addButton(text = "Next Page", row = 5, column = 0, columnspan = 2, command = self.close)

    def close(self):
        """Checks which boxes were selected and determines what department(s) student should meet with. Closes window when done."""
        # If enrollment steps are completed, student meets with Enrollment Specialist. Otherwise, they meet with admissions.
        if self.appBtn.isChecked() and self.myivyBtn.isChecked() and self.assmtBtn.isChecked():
            Page5.department = "Enrollment Specialist"
        else:
            Page5.department = "Admissions Counselor"
        # If a student does not have the FAFSA completed, they will meet with FA and boolean variable will be made true.
        if self.fafsaBtn.isChecked():
            Page5.finAid = False
        else:
            Page5.finAid = True
        self.master.destroy()

"""Summary Page"""
class PageEnd(EasyFrame):
    def __init__(self):
        """sets up window and widgets for summary of visit"""
        EasyFrame.__init__(self, width = 400, height = 300, title = "Ivy Visit Planner")
        self["background"] = "green"
        #Ivy Logo
        ivyLogo = self.addLabel(text = "", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "green")
        self.image = PhotoImage(file = "ivylogo.gif")
        ivyLogo["image"] = self.image
        #Visit Summary
        self.addLabel(text = 'Thanks for registering, ' + Page1.name + '!\n'
                          'Here is a summary of your visit:', row = 1, column = 0, columnspan = 2, sticky = "NSEW")
        #If the student needs to meet with Financial Aid, they will get the first summary, otherwise they will receive the second.
        if Page5.finAid == True:
            self.addLabel(text = 'Date: \n'
                          'Time: \n'
                          'Program: \n'
                          'Tour: \n'
                          'Appointment: \n'
                          'FAFSA Help: \n'
                          , row = 2, column = 0, sticky = "NSEW")
            self.addLabel(text = Page2.date + '\n'
                          + Page2.time + '\n'
                          + Page3.program + '\n'
                          + Page4.building + '\n'
                          + Page5.department + '\n'
                          'Yes'
                          , row = 2, column = 1, sticky = "NSEW")
        else:
            self.addLabel(text = 'Date: \n'
                          'Time: \n'
                          'Program: \n'
                          'Tour: \n'
                          'Appointment: \n'
                          , row = 2, column = 0, sticky = "NSEW")
            self.addLabel(text = Page2.date + '\n'
                          + Page2.time + '\n'
                          + Page3.program + '\n'
                          + Page4.building + '\n'
                          + Page5.department
                          , row = 2, column = 1, sticky = "NSEW")

         #End Button
        self.endBtn = self.addButton(text = "See you soon!", row = 7, column = 0, columnspan = 2, command = self.close)

    def close(self):
        """Closes window and program"""
        self.master.destroy()
    
    
def main():
    """runs each window/page of the visit planner"""
    Page1().mainloop()
    Page2().mainloop()
    Page3().mainloop()
    Page4().mainloop()
    Page5().mainloop()
    PageEnd().mainloop()

if __name__ == "__main__":
    main()





