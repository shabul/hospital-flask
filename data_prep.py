import pandas as pd
from datetime import datetime
import pickle

import random

def gen_dob(count):
    op = []
    for c in range(count):
        x = datetime.strptime(str( random.choice(range(1,27))) +"/"+ str( random.choice(range(1,12))) + "/" + str( random.choice(range(1973,2022))) , '%d/%m/%Y').date()
        op.append(x)
    return op


def gen_app_date(count):
    op = []
    for c in range(count):
        x = datetime.strptime(str( random.choice(range(1,27))) +"/"+ str( random.choice(range(1,12))) + "/" + str( random.choice(range(2020,2022))) , '%d/%m/%Y').date()
        op.append(x)
    return op


def gen_app_time(count):
    op = []
    for c in range(count):
        x = datetime.strptime(str( random.choice(range(0,23))) +":"+ str( random.choice(range(0,59)))  , '%H:%M').time()
        op.append(x)
    return op



def gen_room_type(count):
    return [random.choice(['AC','Non AC','ICU',"General"]) for c in range(count)]



def gen_ins_type(count):
    return [random.choice([True,False]) for c in range(count)]




def gen_minor(count):
    return [random.choice([True,False]) for c in range(count)]




def gen_accident(count):
    return [random.choice([True,False]) for c in range(count)]


def gen_gender(count):
    return [random.choice(['Male','Female']) for c in range(count)]


def gen_emp_type(count):
    return [random.choice(['Business','Private Employee','Govt Employee']) for c in range(count)]



def gen_phone(count):
    return [random.choice(range(9000000000,9999999999)) for c in range(count)]


def gen_age(count):
    return [random.choice(range(1,80)) for c in range(count)]


def gen_height(count):
    return [random.choice(range(145,188)) for c in range(count)]


def gen_weight(count):
    return [random.choice(range(12,120)) for c in range(count)]


def gen_med_comp(count):
    l = ["Diabetes","Blood Pressure","Thyroid","Asthma","Cancer","Heart Disease"]
    
    return [",".join(random.sample(l, random.choice([1,2,3,4,5])))  for c in range(count)]

def gen_dr(count):
    drs = ['Dr.Ravi Kumar',
            'Dr.Shobhana',
            'Dr.Subramanian',
            'Dr.Vijaya',
            'Dr.Sonia Thomas',
            'Dr.Vaseem Akram']
    return [random.choice(drs) for c in range(count)]


names =['Nicol', 'Cindy', 'Betsy', 'Oren', 'Giovanna', 'Eloy', 'Kelsy',
       'Willie', 'Daria', 'Lyla', 'Linwood', 'Shira', 'Catherine', 'Eva',
       'Kierra', 'Marjorie', 'Katie', 'Arianne', 'Tyrek', 'Stefanie',
       'Noah', 'June', 'Chandra', 'Brendon', 'Amani', 'Bree', 'Marissa',
       'Rogelio', 'Mykel', 'Ray', 'Gabe', 'Erwin', 'Louise', 'Luigi',
       'Guillermo', 'Milton', 'James', 'Marjorie', 'Michele', 'Brandi',
       'Emilio', 'Carroll', 'Liza', 'Melva', 'Pauline', 'Cindi', 'Lotus',
       'Jaimie', 'Pauline', 'Carolyn', 'Hazel', 'Ralph', 'Danielle',
       'Kristen', 'Haven', 'Kelsi', 'Daniel', 'Rae', 'Kory', 'Rocky',
       'Gladys', 'Cleo', 'Marva', 'Axel', 'Rodger', 'Daniel', 'Roscoe',
       'Deasia', 'Amberley', 'Bud', 'Gale', 'Jacqueline', 'Marian',
       'Josh', 'Carrie', 'Amelia', 'Gina', 'Ben', 'Jennah', 'Marina',
       'Heidi', 'Lindsay', 'Timoteo', 'Sabrina', 'Malvina', 'Kathi',
       'Taylor', 'Rhoda', 'Jess', 'Joey', 'Phillip', 'Christy', 'Moriah',
       'Patrick', 'Jared', 'Karson', 'Jubilee', 'Bonita', 'Maggie',
       'Luther']

contact_person = ['Denise', 'Saphira', 'Jessie', 'Eugenia', 'Jalon', 'Brett',
       'Kimberly', 'Kara', 'Valerie', 'Braden', 'Yvonne', 'Maxine',
       'Nathan', 'Summer', 'Lacey', 'Seth', 'Johannes', 'Adison',
       'Xander', 'Wanda', 'Jeramy', 'Nanci', 'Josephine', 'Breana',
       'Anne', 'Jeraldine', 'Blair', 'Maliya', 'Jonathan', 'Marquis',
       'Dan', 'Sheree', 'Marla', 'Gay', 'Leonor', 'Aidyn', 'Ruth',
       'Cherie', 'Rhonda', 'Tony', 'Mary', 'Dante', 'Jeffry', 'Garry',
       'Robert', 'Ben', 'Jaidyn', 'Rojelio', 'Ami', 'Daphne', 'Julian',
       'Jonathan', 'Kaila', 'Kai', 'Wesley', 'Myra', 'Karyme', 'Anais',
       'Rex', 'Elouise', 'Leland', 'Tamarra', 'Vance', 'Sharon', 'Kevon',
       'Penny', 'Alfred', 'Serenity', 'Winifred', 'Loretta', 'Magdalena',
       'Carolyn', 'Nathaniel', 'Natasha', 'Carolyn', 'Cheri', 'Marilyn',
       'Armando', 'Jayton', 'Aileen', 'Enrique', 'Colt', 'Harold',
       'Billie', 'Luiz', 'Maddison', 'Calvin', 'Geraldine', 'Latoria',
       'Hagen', 'Chantel', 'Willard', 'Rose', 'Alana', 'Omid', 'Aaliyah',
       'Skyler', 'Carson', 'Hannah', 'Libby']

address_data = ['No.14,Geil St.,Muthialpet,Ch.1',
       'Kalidass St,Jeyaram Nagar, Kolathur, Ch-99',
       'L-10. SIDCO 1st Main Road, Kaviyarasu Kannadasan Nagar, Ch-118',
       'No.105, Theagaraya Road, Chennai-17',
       'No.40,Thiruvenkatasamy St., Pulianthope, Ch-12.',
       'No.10 Solai St, Chennai-23',
       'No.1, Kabaleeswarar Nagar,ECR,Neelangarai, Chennai-115',
       '101, Gangai Amman Koil Street, Karapakkam Ch-97',
       '4th Main Road,M.K.B Nagar Pumping Station, Chennai-39',
       'No.48, Subbarayan 2nd st, Otteri, Chennai12',
       'No.31, C.P.Ramasamy Road,Alwarpet, Chennai-18',
       '48A, Pammal Nallathambi St,M.G.R. Nagar, Chennai-83',
       '29th St., Nanganallur Over Head Tank, Nanganallur, Chennai-61',
       'Kathivakkam Municipality Office,Chennai-57',
       'No.2/336, M.G Road, Manapakkam, Chennai-89',
       '7, 5th Cross St., U.I.Colony, Ch-24',
       'No.1, CYS Road, Ekangipuram Pumping Station, Mangalapuram, Chennai-11',
       'Porur Head Works, Senthil Nagar School Road, Porur, Ch-116',
       'No.50, S.N.Chetty Street, Ch-13',
       'Pilliar Koil St., Library Room, Kallikuppam, Ambattur, Chennai-53',
       'No.102, Bajanai Koil Street, Nandambakkam, Chennai-89',
       'Over Head Tank, Balaji Nagar main Road, Adambakkam, Chennai-88.',
       'No.54, Venkatadri St., ch-7',
       'No.2, Memorial Hall Road, Park Town,Chennai-3',
       'No.153A, Sundaram Pillai Nagar Main Street, Tondiarpet Chennai-81',
       'Thiyagarayapuram, Near Over Head Tank, Thiruvottiyur,Ch-19',
       'Kalidass St,Jeyaram Nagar, Kolathur, Ch-99',
       'No.63, Perambalu Chetty St, Ch - 600 021',
       'Annai Sivagami Nagar, 10th Street, (Old pump House)',
       'Thiyagarayapuram, Near Over Head Tank, Thiruvottiyur,Ch-19',
       'T.H.Road, Near Over Head Tank, Thiruvottiyur, Chennai-19',
       '69th Street,R.V.Nagar,Jafferkhanpet, Ch-83.',
       'New Street, Alandur OHT, Alandur, Chennai-16',
       'Otteri Salai Puzhuthivakkam, Ch-91',
       'No.1/330, Padasalai St. Mugalivakkam, Chennai-125.',
       'MTH Road, Opp TI Cycles, Ambattur,Chennai-53',
       'East Coast Road, Srinivasapuram, Kottivakkam, Chennai-41',
       'No.11, Conronsmith Road,Gopalapuram, Ch-86',
       'No.238, Papers Mills Road,Perambur Ch.11',
       'Puzhal Town Panchayat Office, Puzhal, Chennai-66',
       'No.11A, Alagirisamy Road,K.K.Nagar,Chennai-78',
       'Gengu Reddy Road, Chennai-8', 'Balaji Nagar, Chennai-97',
       'Mathur Panchayat Office, Mathur MMDA, Chennai-68',
       'K.K. Nagar Double Tank, R.K Shanmugam Salai, Ch-78',
       'No.1, New Avadi Road, Shaft Road, Kilpauk, Chennai-10',
       'Old No.182, New No.302, Thambu Chetty Street, Chennai-1',
       'K.R.Ramasamy Nagar, Near Over Head Tank, Therady,Thiruvottiyur,Ch-19.',
       'Vivek Nagar,Venkatapuram, Ambattur, Chennai-53',
       'No.54, Kothandaraman `St., Ch-13',
       'Masthan Gory St.,Adambakkam, Chennai-88',
       'No.76/3, 3rd, Avenue Besant Nagar OHT., Chenai-90.',
       'H-7,11 Block,2nd st,Anna Nagar, Chennai-40',
       'Lattangs Road, Chennai-84',
       'A1,Block 139, Ist Street, Naduvankarai, Chennai-40',
       'No.53, North Mada St., Thiruvanmiyur, Chennai-41',
       'No.11, Subarayan Street,Chennai-29', 'No.59,M.S.Koil St., Ch-13',
       '1630,J Block, V Street,Anna Nagar West, Chennai-40',
       'No.136/111, Choolaimedu High Road, Chennai-94',
       'Thanikachalam Nagar, Filling Point, Ponniammanmedu, Chennai-110',
       'Vivekanandar St., Over Head Tank, Lakishmipuram, Chennai-99',
       'No.12, Kathpada Pumping Station, Chennai-21',
       'No.12B, 1st Avenue, Ashok Nagar, Chennai-83',
       'No.1, T.S.Krishna Nagar main road,Mogappair, Ch-101',
       'Chunnambu Kolthur Road, Pallikaranai, Chennai-100',
       'Temple Street, Chennai-10',
       'Alapakkam Filling station, Gengai Amman Koil Street, Maduraval, Chennai-95.',
       '383,Anna Salai, Chennai-25',
       'No.31, Perambur High Road, Chennai-11',
       'Sewage Pumping station, Kambar Street,R.K.kambar Street, Valasaravakkam, Ch-87',
       'Anna Park, Thiruvalluvar Salai,Alwarpet, Ch-18',
       'Nerkundram, Panchayat Office, 6, Karunnigar Street, Nerkundram, ch-107',
       'No.24,Brindavan St.,Mylapore,ch-4.',
       '181, Perambur Barrex Road, Chennai-12',
       'No.41, Mundakanniamman Koil St., Chennai-4',
       'No.1 Dr. Thomas Road,T Nagar, Chennai-17',
       'No.17, Jani John Khan St,Royapettah, Chennai-14',
       'Park Road, Anna Nagar West, Chennai-101',
       '1st Main Road, Kottur Garden Chennai-85',
       'No.45, Veerabadran St.,Pudupet, Ch-2',
       'No.6, Amman Koil 1st Lane, George Town, Chennai-79',
       'No.112, Ambedkar Street, Manali, Chennai-68',
       'Pandian St., Prakash Nagar, Ambattur, Chennai-53',
       'No.112, Ambedkar Street, Manali, Chennai-68',
       'Ramapuram Panchyat Office, Bajanai Koil St, Ramapuram,Ch-89',
       '4th Main Road, M.K.B Nagar Pumping Station, Chennai-39',
       'No.112, Ambedkar Street, Manali, Chennai-68',
       'No.1,Kaviyarasu Kannadasan Nagar 1st Main Road, Kannadasan Nagar Ch-118',
       'Nerkundram, Panchayat Office, 6, Karunnigar Street, Nerkundram, Ch-107',
       'No.48, Govindappan St.,Ch-79',
       'East coast Road, Near Govt. Peripheral Hospital, Injambakkam, Ch-115',
       'No.28, Prof.Sanjeevi St,Mylapore, Chennai-4',
       'Otteri Salai Puzhuthivakkam, Ch-91.',
       'No.53,North Mada St., Thiruvanmiyur, Chennai-41.',
       'T.H.Road, Near Over Head Tank, Thiruvottiyur, Chennai-19',
       'Justice Radhakrishnan Salai, TNHB, Periyar nagar Ch-42',
       'No.238, Papers Mills Road,Perambur Ch.11',
       'No.1,Whannels Road,Egmore,Chennai-8',
       '24,Ramanujam Road, Old Washermenpet Ch.21']


inp_data = pd.DataFrame()
count = 100

inp_data['patient_name'] = names

inp_data['gender'] = gen_gender(count)

inp_data['dob'] = gen_dob(count)

inp_data.dob.iloc[1]

inp_data['room_type'] = gen_room_type(count)
inp_data['insurance'] = gen_ins_type(count)
inp_data['emp_type'] = gen_emp_type(count)

inp_data['contact_person'] = contact_person



inp_data['phone_number']  =gen_phone(count)

inp_data['dr_name'] = gen_dr(count)

inp_data['admit_date'] = gen_app_date(count)
inp_data['admit_time'] = gen_app_time(count)



inp_data['minor'] = gen_minor(count)

inp_data['accident'] = gen_accident(count)









## Insert into DB\

from utils.models import db, Users,InPatientsData,AppointmentsData



    


app_data = pd.DataFrame()
count = 100

app_data['patient_name'] = names

app_data['gender'] = gen_gender(count)

app_data['age'] = gen_age(count)

app_data['med_comp'] = gen_med_comp(count)
app_data['address'] = address_data

app_data['height'] = gen_height(count)
app_data['weight'] = gen_weight(count)


app_data['dr_name'] = gen_dr(count)

app_data['app_date'] = gen_app_date(count)
app_data['app_time'] = gen_app_time(count)


def app_data_ingestion():
    for i in app_data.to_dict(orient=('records')):
        rec =AppointmentsData(
                    patient_name=i['patient_name'],
                    age=i['age'],
                    gender  =i[ 'gender'],
                    med_comp =i[ 'med_comp'],
                    address =i['address'],
                    height =i['height'],
                    weight =i['weight'],
                    dr_name=i['dr_name'],
                    app_date =i['app_date'],
                    app_time =i['app_time']
                )



        db.session.add(rec)
        db.session.commit()
        
    return "Added data to Appointments DB"
    
    
def inp_data_ingestion():
    for i in inp_data.to_dict(orient='records'):
        rec = InPatientsData(
                    patient_name  =i['patient_name']     ,
                    dob  = i['dob']    ,
                    gender  = i['gender']    ,
                    room_type  = i['room_type']    ,
                    insurance  =    i['insurance'] ,
                    emp_type  =    i['emp_type'] ,
                    contact_person  = i['contact_person']    ,
                    phone_number  =     i['phone_number'],
                    dr_name  =  i['dr_name']   ,
                    admit_date  =   i['admit_date']  ,
                    admit_time  = i['admit_time']    ,
                    minor  =    i['minor'] ,
                    accident  =  i['accident']   ,
                )
        
        db.session.add(rec)
        db.session.commit()
    
    return "Added data to InpatientDat DB"