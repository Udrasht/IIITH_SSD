 select d.Mgr_ssn as Menegar_ssn,count(*) as Numberofproject from PROJECT as p,PROJECT as q,DEPARTMENT as d where p.Dnum=q.Dnum and p.Pname='ProductY'and d.Dnumber=p.Dnum;

