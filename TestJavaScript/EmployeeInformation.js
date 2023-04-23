import fs from 'fs';

class Employee {
  constructor(name,hourlyRate,hours,startMonth,startYear) {
    this.name= name;
    this.hourlyRate= hourlyRate;
    this.hours=hours;
    this.startMonth=startMonth;
    this.startYear=startYear;
  }


  get getStartMonth(){
    return this.startMonth;
  }


  get calculateSalary(){
     var salary= this.hourlyRate*this.hours;
    return salary;
  }

  toString(){
    console.log(this.name+":");
    console.log("\t Started: "+this.startYear+","+this.getStartMonth);
    console.log("\t Hourly Rate: $"+this.hourlyRate);
    console.log("\t"+this.hours+" Hours per week");
    console.log("\t Annual Earnings: $"+this.calculateSalary);


  }

}

let emp1= new Employee("Roger",25,10,"Jan1","2023");
emp1.toString();




fs.readFile('EmployeeInformation.txt', (err, data) => {
    if (err) throw err;

    var info= data.toString();
    var startMonth=[];
    console.log(info);

    for(let i=0; i>info.length; i++){
      while(info[i]!=" "){
        startMonth[i]=info[i];
      }

    }

})
