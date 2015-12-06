import re
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import os
import httplib2
from datetime import datetime
c=0

def make_soup(s):
   match=re.compile('https://|http://|www.|.com|.in|.org|gov.in')
   if re.search(match,s):
     http = httplib2.Http()
     status, response = http.request(s)
     page = BeautifulSoup(response,"html.parser",parse_only=SoupStrainer('div'))#,parse_only=SoupStrainer('div')
     return page
   else:
     return None
def test_internet():
   while(True):
      try:
         test_in=make_soup("https://www.google.com")
         break
      except:
            continue
def parse1(s):
   global c
   temp_set=set()
   soup=make_soup(s)
   if(soup!=None):
      for div in soup.find_all('div',class_=[ "thing" , "id-t3_3ua12m" ,"linkflair" , "linkflair-normal" , "odd" ,  "link"]):
       try:
         if(div.p!=None and div.p.next_sibling!=None and div.p.next_sibling.next_sibling!=None):
          x=div.p.next_sibling.next_sibling.next_sibling['class']
          #print(x)
          if(x[0]=='entry'):
            element='\nPROMPT '+str(c+1)+'\n'
            if(div.p.next_sibling.next_sibling.next_sibling!=None and div.p.next_sibling.next_sibling.next_sibling.p!=None and div.p.next_sibling.next_sibling.next_sibling.p.a!=None):
               element=element+div.p.next_sibling.next_sibling.next_sibling.p.a.string+'\n'
               element=element+div.p.next_sibling.next_sibling.next_sibling.p.a['href']+'\n'
            if(div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'})!=None and div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).time!=None):
                  element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).time['datetime']+'\t'
                  element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).time['title']+'\t'
                  element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).time.string+'\n'
            if(div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'})!=None and div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).a!=None):
               element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).a.string+'\n'
               element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).text+'\n'
            if(div.div.find('div',{'class':'score likes'})!=None):
               element=element+'score likes '+div.div.find('div',{'class':'score likes'}).string+'\t'
               element=element+'score dislikes '+div.div.find('div',{'class':'score dislikes'}).string+'\t'
               element=element+'score unvoted '+div.div.find('div',{'class':'score unvoted'}).string+'\n\n'
            f.write(element)
            c=c+1
          elif(x[0]=='thumbnail'):
            element='\nPROMPT '+str(c+1)+'\n'
            if(div.find('div',{'class':'entry unvoted'})!=None and div.find('div',{'class':'entry unvoted'}).p!=None and div.find('div',{'class':'entry unvoted'}).p.a!=None and div.find('div',{'class':'entry unvoted'}).p.a.string!=None):
               element=element+div.find('div',{'class':'entry unvoted'}).p.a.string+'\n'
               element=element+div.find('div',{'class':'entry unvoted'}).p.a['href']+'\n'
               if(div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'})!=None and div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).time != None):
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).time['datetime']+'\t'
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).time['title']+'\t'
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).time.string+'\n'
               if(div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).a!=None):
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).a.string+'\n'
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).text+'\n'
               if(div.p.next_sibling.next_sibling.find('div',{'class':'score likes'})!=None and div.p.next_sibling.next_sibling.find('div',{'class':'score dislikes'})!=None and div.p.next_sibling.next_sibling.find('div',{'class':'score unvoted'})!=None):
                  element=element+'score likes '+div.p.next_sibling.next_sibling.find('div',{'class':'score likes'}).string+'\t\t'
                  element=element+'score dislikes '+div.p.next_sibling.next_sibling.find('div',{'class':'score dislikes'}).string+'\t\t'
                  element=element+'score unvoted '+div.p.next_sibling.next_sibling.find('div',{'class':'score unvoted'}).string+'\n'
            f.write(element)
            c=c+1
       except:
            print('ERROR')
            continue
def count_next_of_current(s,m):
    test_internet()
    soup=make_soup(s)
    y='https://www.reddit.com/r/'+m+'/'+select_tab+'/?count='
    match=re.compile(y)
    for link in soup.find_all('a',{'rel':['next']}):
        href=link['href']
        return href
def read_reddit_images(change_file_number,m,x):
    test_internet()
    global f
    global select_tab
    select_tab=x
    #x=m+'_'+select_tab+str(change_file_number)+'.txt'
    x=m+'_'+select_tab+'.txt'
    f=open(x,'a',encoding='utf-8')
    FORMAT = '%d-%m-%Y %H:%M:%S'
    f.write('\n\n\n\niteration number '+str(change_file_number)+' '+datetime.now().strftime(FORMAT)+'\n\n')
    maximum_number_of_next_pages=7
    s='https://www.reddit.com/r/'+m+'/'+select_tab
    soup=make_soup(s)
    parse1(s)
    count=0
    print('for '+m+' '+select_tab+' current page number is'+'\n'+str(count))
    while(count<maximum_number_of_next_pages):
        test_internet()
        s=count_next_of_current(s,m)
        if(s!=None):
            parse1(s)
            count=count+1
            print(count)
        else:
            break
    f.write('\n\niteration number '+str(change_file_number)+' '+datetime.now().strftime(FORMAT)+'\n\n') 
    f.close()

def maincall(m,i):
   read_reddit_images(i,m,'hot')
   read_reddit_images(i,m,'new')
   read_reddit_images(i,m,'top')
   read_reddit_images(i,m,'rising')
   read_reddit_images(i,m,'controversial')
   read_reddit_images(i,m,'gilded')
def subs(b):
   test_internet()
   t=open('mytext.txt','r')
   i=t.read()
   temp=int(i)
   temp=temp+1
   t.close()
   t=open('mytext.txt','w')
   t.write(str(temp))
   t.close()
   for k in b:
        test_internet()
        maincall(k,i)
def main():
   test_internet()
   b=[]
   b=['24hoursupport','3amjokes','ADHD','AMA','AcademicPhilosophy','AcademicPsychology','Aerospace','Android','AndroidQuestions','Anger','Anxiety',
      'AskAnthropology','AskComputerScience','AskElectronics','AskEngineers','AskHR','AskHistorians','AskMen','AskPhysics','AskReddit','AskScienceDiscussion',
      'AskScienceFiction','AskSocialScience','AskWomen','Ask_Politics','Bash','BehavioralEconomics','BigDataJobs','BipolarReddit','CAD','C_Programming',
      'ComputerScience','Confession','CoverTheWorld','Cplusplus','CppForbeginners','CrappyDesign','CrazyIdeas','DIY','DIYCompSci','DailyProgrammer','DeadBedrooms',
      'DebateReligion','DecidingToBeBetter','DigitalNomad','DoesNotTranslate','ECE','Economics','EngineeringStudents','Entrepreneur','ExNoContact','FEA','FE_Exam',
      'Feminism','FluidMechanics','Foodforthought','FoundWords','Freethought','GetMotivated','GetStudying','GraphicsProgramming','HITsWorthTurkingFor','HTMLBattles',
      'HomeworkHelp','HowsYourJob','IAmA','IOPsychology','InternetIsBeautiful','LaTeX','LanguageLearning','LearnANewLanguage','LearnJava','LearnJavaScript',
      'LifeProTips','LinguisticsHumor','LongDistance','MachineLearning','Manufacturing','MathHelp','Meditation','NetworkingJobs','Neuropsychology','NoStupidQuestions',
      'ObjectiveC','PCMasterRace','PLC','PhilosophyofScience','PhsychologicalTricks','PoliticalDiscussion','Polyamory','PrintedCircuitBoard','Progether',
      'ProgrammerHumor','Proofreading','Python','RapeCounseling','RetailManagement','STEMdents','SWORDS','SWResources','SampleSize','SanctionedSuicide','Seduction',
      'SiblingSupport','Statistics','SuicideWatch','Swift','SysadminJobs','TechNews','ThermalPerformance','Tinder','TinyCode','TowerOfBabel','TrueAskReddit',
      'TrueReddit','Unix','VentureBiotech','WeMetOnline','Web_Development','WhatsTheWord','YoungJobs','academicpsychology','academicpublishing','accounting','advice',
      'androiddev','translator','answers','asklinguistics','askmath','askphotography','askreddit','askscience','assistance','astronomy','audiology','autism','badcode',
      'badlinguistics','beermoney','behavioralmedicine','behaviortherapy','bestof','bestofTLDR','bioengineering','biology','biotech','bodybuilding','bookquotes',
      'books','breadboard','bugs','buildapc','business','careerguidance','cfd','changemyview','chemicalengineering','chipdesign','civilengineering','cloudcomputing',
      'coding','coffeescript','cogneuro','cogneurocogsci','cognitivelinguistics','cogsci','compilers','complexsystems','compling','compression','compsci',
      'computerforensics','computers','computerscience','conlangs','conspiracy','construction','cosmology','coursearea','cpp','cpp_questions','crypto','cryptography',
      'cs50','csbooks','cscareerquestions','csharp','css','dae','dailyprogrammer','dailyscripts','darkinternet','dataisbeautiful','datamining','dementia','depression',
      'diy','documentaries','dotnet','downsyndrome','dyslexia','economics','education','eebooks','electricalengineering','electronics','engineering',
      'engineeringtechnology','entrepreneur','epidemiology','etymology','eurodiversity','everythingscience','evolution','evopsych','explainlikeimfive','favors',
      'finance','financialindependence','findareddit','forhire','forth','freelance','freelanceUK','freelanceWriters','funny','gadgets','genetics','getdisciplined',
      'getemployed','getmotivated','getting_over_it','goldredditsays','grammar','grammarwriting','graphic_design','hacking','hardware','history','holdmybeer',
      'homeworkhelp','html','htmlbasics','humanism','hwstartups','hypotheticalsituation','iWantToLearn','ideasfortheadmins','illegaltorrents','improvevocab','india',
      'ineedafavor','intel','intelligence','interview','inventions','iwantoutjobs','java','javaTIL','javacodegeeks','javahelp','javascript','jobbit','jobsearchhacks',
      'jokes','jquery','languagetechnology','learnjava','learnjavascript','learnmath','learnprogramming','learnpython','lectures','lifehacks','linguistics','linux',
      'linux4noobs','linuxquestions','literature','logic','machinelearning','marketing','masculism','math','mathbooks','mathematics','mathpsych','matlab',
      'mechanicalengineering','medicine','meditation','mentalhealth','mentors','metalworking','microsoft','mmfb','motivation','movies','music','mysql','needadvice',
      'networking','neuro','neurodiversity','neurophilosophy','neuropsychology','newproducts','news','newtoreddit','nonprofit_jobs','nootropics','obvious',
      'occupationaltherapy','ocd','offmychest','opengl','osdev','parkrangers','perl','philosophy','philosophyofScience','philosophyofscience','php','physics','pics',
      'politics','privacy','product_design','productivity','programbattles','programming','programmingbuddies','programmingchallenges','psychiatry','psychology',
      'psychopharmacology','psychotherapy','psychscience','puzzles','python','quotes','rage','rational','reasonstolive','rehabtherapy','relationship_advice',
      'relationships','resumes','riddles','robotics','ruby','saneorpsycho','schizophrenia','science','scientificresearch','self','selfhelp','selfimprovement','sex',
      'shittyaskscience','shittyideas','shittyprogramming','showerthoughts','simpleliving','slp','socialism','socialmedia','socialskills','sociology','software',
      'softwarearchitecture','softwaredevelopment','softwaregore','solotravel','space','specialed','startups','stopselfharm','suicidology','sysadmin','systems',
      'talesfromtechsupport','technology','techsupport','teenagers','testimonials','themixednuts','thisismyjob','tipofmytongue','todayilearned','tr',
      'translationstudies','travel','tutor','ultralight','undelete','undeleteShadow','undergraduateresearch','uniqueminds','visualbasic','web_programming','webdev',
      'whatisthis','whatstheword','windows','windowsazure','womenEngineers','words','work','workonline','worldnews','writingprompts']
   l=set()
   for k in b:
      l.add(k)
   b=[]
   for k in l:
      b.append(k)
   b.sort()
   subs(b)
if __name__ == '__main__':
   main()
