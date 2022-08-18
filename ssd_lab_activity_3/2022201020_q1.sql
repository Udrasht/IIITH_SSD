with exp1 as (select concat(e.Fname,e.Minit,e.Lname) as Fullname,e.Ssn,e.Dno,d.Dname from EMPLOYEE as e, WORKS_ON as w,PROJECT as p, DE
PARTMENT as d where w.pno=p.Pnumber and w.Hours<40 and p.Dnum=d.Dnumber and e.Ssn=d.Mgr_ssn) select distinct * from exp1;

