import json
import Reg_exp_Emp_fields
import unittest
import logging


class Testclass(unittest.TestCase):

    logging.basicConfig(filename='success.log', filemode='w', format='%(asctime)s--%(levelname)s:--%(message)s',
                        level=logging.DEBUG)

    def test_sample_json_file(self):
        """Test all sample json files in the testdata directory."""
        json_file = "Employees.json"
        json_fp = open(json_file, 'r')
        json_content = json_fp.read()
        json_fp.seek(0)
        json_data = json.load(json_fp)
        json_fp.close()
        '''
            json.load(file_pointer) where file_pointer open json file in read mode. This method creates and returns a dictionary
            from JSON file
            json.loads(file_pointer(read)) where file_pointer.read() is a string and rest is same as json.load(). But, we need
            to use pprint() to print the dictionary
        '''
        for elements in json_data:                           # Each elements is a tag under json_data
            # print "Details of ", elements                  # description of elements
            # print json_data[elements]                      # Each elements is a list of dictionaries
            for entry in range(len(json_data[elements])):    # entry stands for a dictionary from a list of dictionaries for elements
                email_id = json_data[elements][entry]['emailAddress']
                fname = json_data[elements][entry]['firstName']
                uid = json_data[elements][entry]['userId']
                reg = json_data[elements][entry]['region']
                flname = json_data[elements][entry]['preferredFullName']
                job_roll = json_data[elements][entry]['jobTitleName']
                lname = json_data[elements][entry]['lastName']
                contact = json_data[elements][entry]['phoneNumber']
                ecode = json_data[elements][entry]['employeeCode']

                # Here elements stands for Employees of an organisation and each entry stands for details of an Employee

                for item in json_data[elements][entry]:
                    if item == 'userId':
                        uid_value = Reg_exp_Emp_fields.check_userID(uid)
                        if self.assertIs(uid_value, True):
                            logging.info("Employee user ID is valid")
                        else:
                            #print type(self.failIf(uid_value))
                            logging.error("Employee user ID is not valid")


                        '''if self.assertEqual(uid_value, True):
                            logging.info("Employee user ID is valid")
                        if not self.assertEqual(uid_value, True):
                            logging.error("Employee user ID is not valid")'''
                        #self.assertEqual(uid_value, True, msg=logging.error("Employee user ID is not valid"))

                    if item == 'jobTitleName':
                        job_roll_value = Reg_exp_Emp_fields.check_jobTitleName(job_roll)
                        #self.assertEqual(job_roll_value, True, msg="Employee Job title is not valid")
                        self.assertEqual(job_roll_value, True, msg=logging.error("Employee Job title is not valid"))
                        #self.assertFalse(job_roll_value, msg=logging.error("Employee Job title is not valid"))

                    if item == 'firstName':
                        fname_value = Reg_exp_Emp_fields.check_firstName(fname)
                        #self.assertEqual(fname_value, True, msg="Employee first name is not valid")
                        self.assertEqual(fname_value, True, msg=logging.error("Employee first name is not valid"))
                        #self.assertFalse(fname_value, msg=logging.error("Employee first name is not valid"))

                    if item == 'lastName':
                        lname_value = Reg_exp_Emp_fields.check_lastName(lname)
                        #self.assertEqual(lname_value, True, msg="Employee last name is not valid")
                        self.assertEqual(lname_value, True, msg=logging.error("Employee last name is not valid"))
                        #self.assertFalse(lname_value, msg=logging.error("Employee last name is not valid"))

                    if item == 'preferredFullName':
                        flname_value = Reg_exp_Emp_fields.check_preferredFullName(flname)
                        #self.assertEqual(flname_value, True, msg="Employee Preferred full name is not valid")
                        self.assertEqual(flname_value, True, msg=logging.error("Employee full name is not valid"))
                        #self.assertFalse(flname_value, msg=logging.error("Employee full name is not valid"))

                    if item == 'employeeCode':
                        ecode_value = Reg_exp_Emp_fields.check_employeeCode(ecode)
                        #self.assertEqual(ecode_value, True, msg="Employee code is not valid")
                        self.assertEqual(ecode_value, True, msg=logging.error("Employee code is not valid"))
                        #self.assertFalse(ecode_value, msg=logging.error("Employee code is not valid"))

                    if item == 'region':
                        reg_value = Reg_exp_Emp_fields.check_region(reg)
                        #self.assertEqual(reg_value, True, msg="Working region is not valid")
                        self.assertEqual(reg_value, True, msg=logging.error("Employee Working region is not valid"))
                        #self.assertFalse(reg_value, msg=logging.error("Employee Working region is not valid"))

                    if item == 'phoneNumber':
                        contact_value = Reg_exp_Emp_fields.check_phoneNumber(contact)
                        #self.assertEqual(contact_value, True, msg="Contact number is not valid")
                        self.assertEqual(contact_value, True, msg=logging.error("Employee contact number is not valid"))
                        #self.assertFalse(contact_value, msg=logging.error("Employee contact number is not valid"))

                    if item == 'emailAddress':
                        email_id_value = Reg_exp_Emp_fields.check_emailAddress(email_id)
                        #self.assertEqual(email_id_value, True, msg="Email ID is not valid")
                        self.assertEqual(email_id_value, True, msg=logging.error("Employee Email_ID is not valid"))
                        #self.assertFalse(email_id_value, msg=logging.error("Employee Email_ID is not valid"))


if __name__ == '__main__':
    unittest.main()



