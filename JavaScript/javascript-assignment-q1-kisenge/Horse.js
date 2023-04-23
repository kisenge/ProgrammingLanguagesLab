import{Saddle} from './Saddle.js';

export class Horse {
  constructor(name,age,costToRent,saddle) {
    this.name= name;
    this.age= age;
    this.costToRent=costToRent;
    this.saddle=saddle;
  }


  get getName(){
    return this.name;
  }


  get getAge(){
    return this.age;
  }


  get getCostToRent(){
    return this.costToRent;
  }


  get getSaddle(){
    return this.saddle;
  }

  set changeName(newName){
    this.name=newName;
  }

  set changeAge(newAge){
    this.name=newName;
  }

  set changeCostToRent(newCost){
    this.costToRent=newCost;s
  }

  set changeSaddle(newSaddle){
    this.saddle= newSaddle;
  }

  get getHorseInfo(){
    console.log("\n\n\n\nLesson with: "+this.name+" (age: "+this.age+")");
    console.log("\n\tSaddle: "+this.saddle.getMaterial+" (width: "+this.saddle.getWidth+"cm)");
  }

  get getLessonCost(){
    let cost= this.saddle.getRentCost;
    cost= cost+this.costToRent;
    console.log("\nCost of a lesson: $"+cost);
  }

  
}
