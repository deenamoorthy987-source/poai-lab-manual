/*Develop a Prolog knowledge base unsing facts and rules for the "like" relationship. Show how infrerece is perfomed using Prolog queries.*/

/*Facts*/
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

/*Rule 1: John likes anything mary likes*/
likes(john,X):-likes(mary,X).

/*Rule 2 : Johan likes anwyon who likes wine*/
likes(john, X):- likes(X,wine).

/*John likes anyoun who like themselves*/
likes(john,X):-likes(X,X).

/*Write a Prolog program to determine whether a student is eligible for campus placement based on the following rules. CONDITIONS: CGPA>=7.5 No active arrears Good communication skills A student is eligible only if all three condition are satisfied.*/

/*Facts*/

cgpa(ash,8.5).
cgpa(rahul,7.2).
cgpa(priya,9.1).
arrears(ash,0).
arrears(rahul,1).
arrears(priya,0).
communction(ash,good).
communction(rahul,good).
communction(priya,average).

/*Rules*/

eligible(Student):-cgpa(Student,C),c>=7.5,arrears(Student,C),communication(Student,good).

/*Write a Prolog program for a smart home autimation system that decides actions based on environmental conditions. CONDITIONS If temperatur is high and someone is at home, turn on AC if it is dark and comeone is at home, turn on lights, If nobody is at home, active security alarm.*/

/*Facts*/

temperature(high).
light(dark).
home(yes).

/*RULES*/

action(turn_on_ac):-temperature(high),home(yes).
action(turn_on_lights):-light(dark),home(yes).


/*Develop a Prolog Expert System for library Management S student can borrow a book only if: The student is registed The student has no ovedue books The requested book is available.*/

/*Facts*/

registered(ash).
registered(priya).
registered(rahul).

overdue(ash,no).
overdue(priya,no).
overdue(rahul,no).

request(ash,book).
request(priya,book).
request(rahul,book).
available(book).

/*Rule*/

can_borrow(Student,Book):-registered(Student),overdue(Student,no),request(Student,Book),available(Book).


/*Deveop a Prolog program to recommen elective courses based on student interest.*/

/*Facts*/

interest(ash,ai).
interest(ash,python).

interest(priya,data_science).
interest(rahul,cyber_security).

/*Rules*/

recommed(student,machine_learning):-interest(student,ai).
recommed(student,machine_learning):-interest(student,python).
recommed(student,data_analytic):-interest(student,data_science).
recommend(student,ethical_hacking):-interest(student,cyber_security).

/*write a prolog program to represent a famil tree and determine gradparent,sibling and ancestor relationships.*/

/*facts*/

parent(ram,sita).
parent(ram,raja).

parent(sita,anu).
parent(raja,deepa).

/*Rules*/

grandparent(X,Y):-parent(X,Y),parent(Z,Y).
sibling(X,Y):-parent(Z,Y),X/=Y.
ancestor(X,Y):-parent(X,Y).
ancestor(X,Y):-parent(X,Z),ancestor(Z,Y).




