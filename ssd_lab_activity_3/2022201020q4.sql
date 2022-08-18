select e.Dno,count(*) as count,e.Sex from EMPLOYEE as e group by e.Dno,e.Sex having count(Sex)>=2 and e.Sex='F';

